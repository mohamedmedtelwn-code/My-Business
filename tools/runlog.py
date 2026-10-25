#!/usr/bin/env python3
"""Run logger for the five teams.

Every team calls ``start`` at the beginning of a run and ``end`` at the end.
Events are appended to ``management/runs.jsonl`` (one JSON object per line):

  {"event":"start","run_id":"research-20261101-0600-ab12","team":"research","ts":"...","note":"..."}
  {"event":"end","run_id":...,"team":...,"start":...,"end":...,"outcome":"ok|warn|bad|limit|crashed",
   "summary":"one line","files_touched":{"added":[],"modified":[],"deleted":[]},"tickets_raised":[],
   "duration_s":123,"business":"<slug or null>"}
  {"event":"reset","team":"work","ts":"..."}

What ``start`` does:
  1. sweeps crashed runs (a start older than ``run_stale_hours`` with no end gets an ``end``
     with outcome ``crashed``);
  2. refuses if the team's circuit breaker is open (``breaker_failures`` consecutive bad,
     limit or crashed outcomes) until ``runlog.py reset --team X``;
  3. takes the team lock ``management/.lock-<team>`` (one run per team at a time; a stale lock
     is cleared);
  4. snapshots the file tree so ``end`` can list the files the run touched.

Usage:
  python tools/runlog.py start --team research [--note "..."] [--business slug]
  python tools/runlog.py end --id <run_id> --outcome ok|warn|bad|limit --summary "..." [--tickets a,b] [--commit]
  python tools/runlog.py status [--json]
  python tools/runlog.py reset --team work
Exit codes: 0 ok, 2 refused (locked / breaker open / unknown run), 1 other error.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import secrets
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import studio  # noqa: E402

OUTCOMES = ("ok", "warn", "bad", "limit")
FAILURES = ("bad", "limit", "crashed")
IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache"}


class RunlogError(Exception):
    def __init__(self, msg: str, code: int = 2):
        super().__init__(msg)
        self.code = code


# -- paths -----------------------------------------------------------------
def log_path(root: Path) -> Path:
    return Path(root) / "management" / "runs.jsonl"


def lock_path(root: Path, team: str) -> Path:
    return Path(root) / "management" / f".lock-{team}"


def snap_path(root: Path, run_id: str) -> Path:
    return Path(root) / "management" / f".run-{run_id}.json"


# -- events ----------------------------------------------------------------
def read_events(root: Path) -> list[dict]:
    p = log_path(root)
    if not p.exists():
        return []
    out = []
    for line in studio.read_text(p).splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue  # a torn line never blocks the pipeline
    return out


def append_event(root: Path, obj: dict) -> None:
    studio.append_text(log_path(root), json.dumps(obj, ensure_ascii=False) + "\n")


def _parse_ts(s: str) -> _dt.datetime:
    return _dt.datetime.fromisoformat(s)


def open_runs(events: list[dict]) -> dict[str, dict]:
    """run_id -> start event for runs that have a start but no end."""
    starts = {e["run_id"]: e for e in events if e.get("event") == "start"}
    for e in events:
        if e.get("event") == "end":
            starts.pop(e.get("run_id"), None)
    return starts


def sweep_crashed(root: Path, cfg: dict) -> list[str]:
    """Mark stale open runs as crashed. Returns the run ids marked."""
    events = read_events(root)
    stale_after = _dt.timedelta(hours=float(cfg.get("run_stale_hours", 3)))
    now = _dt.datetime.now()
    marked = []
    for run_id, st in open_runs(events).items():
        try:
            started = _parse_ts(st["ts"])
        except (KeyError, ValueError):
            continue
        if now - started > stale_after:
            append_event(root, {
                "event": "end", "run_id": run_id, "team": st.get("team"), "business": st.get("business"),
                "start": st["ts"], "end": studio.now_iso(), "outcome": "crashed",
                "summary": f"start without end after {cfg.get('run_stale_hours', 3)} h; marked crashed by the next run",
                "files_touched": {"added": [], "modified": [], "deleted": []}, "tickets_raised": [],
                "duration_s": int((now - started).total_seconds()),
            })
            sp = snap_path(root, run_id)
            if sp.exists():
                sp.unlink()
            marked.append(run_id)
    return marked


def consecutive_failures(events: list[dict], team: str) -> int:
    n = 0
    for e in events:
        if e.get("team") != team:
            continue
        if e.get("event") == "reset":
            n = 0
        elif e.get("event") == "end":
            n = n + 1 if e.get("outcome") in FAILURES else 0
    return n


def breaker_open(events: list[dict], team: str, cfg: dict) -> bool:
    return consecutive_failures(events, team) >= int(cfg.get("breaker_failures", 3))


# -- snapshot ---------------------------------------------------------------
def snapshot(root: Path) -> dict[str, list]:
    root = Path(root)
    snap = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        for fn in filenames:
            p = Path(dirpath) / fn
            rel = p.relative_to(root).as_posix()
            if rel == "management/runs.jsonl" or fn.startswith(".run-") or fn.startswith(".lock-") \
                    or fn.endswith("-journal") or fn.startswith(".tmp-"):
                continue
            try:
                st = p.stat()
            except OSError:
                continue
            snap[rel] = [st.st_mtime_ns, st.st_size]
    return snap


def diff_snapshots(before: dict, after: dict) -> dict:
    added = sorted(k for k in after if k not in before)
    deleted = sorted(k for k in before if k not in after)
    modified = sorted(k for k in after if k in before and after[k] != before[k])
    return {"added": added, "modified": modified, "deleted": deleted}


# -- lock -------------------------------------------------------------------
def acquire_lock(root: Path, team: str, run_id: str, cfg: dict) -> None:
    lp = lock_path(root, team)
    payload = json.dumps({"run_id": run_id, "team": team, "start": studio.now_iso(), "pid": os.getpid()})
    for attempt in (1, 2):
        try:
            fd = os.open(str(lp), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            # Stale lock? Compare its start time with run_stale_hours.
            try:
                held = json.loads(studio.read_text(lp))
                started = _parse_ts(held["start"])
            except Exception:
                started = None
            stale_after = _dt.timedelta(hours=float(cfg.get("run_stale_hours", 3)))
            if started is None or _dt.datetime.now() - started > stale_after:
                try:
                    lp.unlink()
                except OSError:
                    pass
                continue  # retry once after clearing a stale lock
            raise RunlogError(
                f"Team '{team}' is already running (run {held.get('run_id')} since {held.get('start')}). "
                f"If that run died, wait until it is {cfg.get('run_stale_hours', 3)} h old or run: runlog.py reset --team {team}")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(payload)
        return
    raise RunlogError(f"Could not take the lock for team '{team}'.")


def release_lock(root: Path, team: str, run_id: str | None = None) -> None:
    lp = lock_path(root, team)
    if not lp.exists():
        return
    if run_id is not None:
        try:
            held = json.loads(studio.read_text(lp))
            if held.get("run_id") not in (None, run_id):
                return  # someone else's lock
        except Exception:
            pass
    try:
        lp.unlink()
    except OSError:
        pass


# -- public API --------------------------------------------------------------
def start(root: Path, team: str, note: str = "", business: str | None = None, force: bool = False) -> dict:
    root = Path(root)
    if team not in studio.TEAMS:
        raise RunlogError(f"Unknown team '{team}'. Teams: {', '.join(studio.TEAMS)}", code=1)
    cfg = studio.load_config(root)
    crashed = sweep_crashed(root, cfg)
    events = read_events(root)
    if breaker_open(events, team, cfg) and not force:
        raise RunlogError(
            f"Circuit breaker open for team '{team}': {consecutive_failures(events, team)} failed runs in a row. "
            f"The owner reviews the last runs, fixes the cause, then runs: runlog.py reset --team {team}")
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M")
    run_id = f"{team}-{stamp}-{secrets.token_hex(2)}"
    acquire_lock(root, team, run_id, cfg)
    snap = snapshot(root)
    studio.write_text(snap_path(root, run_id), json.dumps({"team": team, "business": business, "start": studio.now_iso(), "snapshot": snap}))
    append_event(root, {"event": "start", "run_id": run_id, "team": team, "business": business, "ts": studio.now_iso(), "note": note})
    return {"run_id": run_id, "team": team, "business": business, "crashed_marked": crashed, "start": studio.now_iso()}


def end(root: Path, run_id: str, outcome: str, summary: str, tickets: list[str] | tuple[str, ...] = (),
        commit: bool = False) -> dict:
    root = Path(root)
    if outcome not in OUTCOMES:
        raise RunlogError(f"Outcome must be one of {', '.join(OUTCOMES)}; got '{outcome}'.", code=1)
    sp = snap_path(root, run_id)
    events = read_events(root)
    start_ev = next((e for e in events if e.get("event") == "start" and e.get("run_id") == run_id), None)
    if start_ev is None:
        raise RunlogError(f"Unknown run id '{run_id}' (no start event). Did you call runlog.py start?")
    if any(e.get("event") == "end" and e.get("run_id") == run_id for e in events):
        raise RunlogError(f"Run '{run_id}' already has an end event.")
    team = start_ev.get("team")
    business = start_ev.get("business")
    before = {}
    if sp.exists():
        try:
            before = json.loads(studio.read_text(sp)).get("snapshot", {})
        except Exception:
            before = {}
    touched = diff_snapshots(before, snapshot(root))
    open_dir = studio.STAGES["tickets_open"]
    auto_tickets = [Path(p).stem for p in touched["added"] if p.startswith(open_dir + "/") and p.endswith(".md")]
    all_tickets = sorted(set(list(tickets) + auto_tickets))
    now = _dt.datetime.now()
    try:
        duration = int((now - _parse_ts(start_ev["ts"])).total_seconds())
    except Exception:
        duration = None
    rec = {
        "event": "end", "run_id": run_id, "team": team, "business": business,
        "start": start_ev.get("ts"), "end": studio.now_iso(), "outcome": outcome, "summary": summary.strip(),
        "files_touched": touched, "tickets_raised": all_tickets, "duration_s": duration,
    }
    append_event(root, rec)
    if sp.exists():
        sp.unlink()
    release_lock(root, team, run_id)
    if commit:
        rec["commit"] = git_commit(root, team, run_id, outcome, touched)
    return rec


def git_commit(root: Path, team: str, run_id: str, outcome: str, touched: dict) -> str | None:
    """Commit the run's changes if the folder is a git repo. Never raises."""
    if not (Path(root) / ".git").exists():
        return None
    n_in = len(touched.get("added", [])) + len(touched.get("modified", []))
    msg = f"run({team}): {run_id} {outcome} touched={n_in} deleted={len(touched.get('deleted', []))}"
    try:
        subprocess.run(["git", "add", "-A"], cwd=str(root), check=True, capture_output=True)
        r = subprocess.run(["git", "-c", "user.email=studio@local", "-c", "user.name=venture-studio",
                            "commit", "-q", "-m", msg], cwd=str(root), capture_output=True, text=True)
        if r.returncode != 0:
            return None  # nothing to commit, or git unavailable: not a run failure
        return msg
    except Exception:
        return None


def status(root: Path) -> dict:
    root = Path(root)
    cfg = studio.load_config(root)
    events = read_events(root)
    out = {}
    opens = open_runs(events)
    for team in studio.TEAMS:
        ends = [e for e in events if e.get("event") == "end" and e.get("team") == team]
        last = ends[-1] if ends else None
        out[team] = {
            "last_run": last.get("end") if last else None,
            "last_outcome": last.get("outcome") if last else None,
            "last_summary": last.get("summary") if last else None,
            "runs": len(ends),
            "consecutive_failures": consecutive_failures(events, team),
            "breaker_open": breaker_open(events, team, cfg),
            "running": [r for r, e in opens.items() if e.get("team") == team],
            "locked": lock_path(root, team).exists(),
        }
    return out


def reset(root: Path, team: str) -> None:
    root = Path(root)
    if team not in studio.TEAMS:
        raise RunlogError(f"Unknown team '{team}'.", code=1)
    append_event(root, {"event": "reset", "team": team, "ts": studio.now_iso()})
    release_lock(root, team)


# -- CLI --------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="runlog.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("start")
    s.add_argument("--team", required=True, choices=studio.TEAMS)
    s.add_argument("--note", default="")
    s.add_argument("--business")
    s.add_argument("--force", action="store_true", help="start even if the circuit breaker is open")
    e = sub.add_parser("end")
    e.add_argument("--id", required=True)
    e.add_argument("--outcome", required=True, choices=OUTCOMES)
    e.add_argument("--summary", required=True)
    e.add_argument("--tickets", default="", help="comma-separated ticket ids raised (new files in tickets/open are detected anyway)")
    e.add_argument("--commit", action="store_true", help="git commit the run's changes")
    st = sub.add_parser("status")
    st.add_argument("--json", action="store_true")
    r = sub.add_parser("reset")
    r.add_argument("--team", required=True, choices=studio.TEAMS)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = Path(args.root) if args.root else studio.find_root(Path.cwd())
    except FileNotFoundError as ex:
        print(f"ERROR: {ex}")
        return 1
    try:
        if args.cmd == "start":
            info = start(root, args.team, note=args.note, business=args.business, force=args.force)
            if info["crashed_marked"]:
                print(f"NOTE: marked crashed: {', '.join(info['crashed_marked'])}")
            print(f"RUN_ID {info['run_id']}")
            print(f"Started {args.team} at {info['start']}. End with: python tools/runlog.py end --id {info['run_id']} --outcome ok --summary \"...\"")
        elif args.cmd == "end":
            tickets = [t.strip() for t in args.tickets.split(",") if t.strip()]
            rec = end(root, args.id, args.outcome, args.summary, tickets=tickets, commit=args.commit)
            t = rec["files_touched"]
            print(f"Ended {rec['run_id']} outcome={rec['outcome']} duration={rec['duration_s']}s "
                  f"files added={len(t['added'])} modified={len(t['modified'])} deleted={len(t['deleted'])} "
                  f"tickets={','.join(rec['tickets_raised']) or '-'}" + (f" commit=\"{rec['commit']}\"" if rec.get("commit") else ""))
        elif args.cmd == "status":
            st = status(root)
            if args.json:
                print(json.dumps(st, indent=2))
            else:
                for team, v in st.items():
                    flag = "BREAKER OPEN" if v["breaker_open"] else ("running" if v["running"] else "")
                    print(f"{team:<12} last={v['last_run'] or '-':<20} outcome={v['last_outcome'] or '-':<8} "
                          f"fails={v['consecutive_failures']} {flag}  {v['last_summary'] or ''}")
        elif args.cmd == "reset":
            reset(root, args.team)
            print(f"Reset team '{args.team}': breaker closed, lock cleared.")
        return 0
    except RunlogError as ex:
        print(f"REFUSED: {ex}")
        return ex.code


if __name__ == "__main__":
    sys.exit(main())
