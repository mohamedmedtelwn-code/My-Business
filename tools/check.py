#!/usr/bin/env python3
"""Pipeline checker: validates the state of the studio folder.

Every team runs it at the start and the end of a run. It reads files only.

ERROR (exit 1) means the folder is in a state the rules forbid and the team
must fix it before doing anything else:
  - a stage folder is missing
  - a file sits in the wrong stage (scored brief in the inbox, unscored brief in
    approved/, approved score below the threshold, plan without a status,
    validation with a final verdict still in 15-validating/, decided ticket still
    in open/, closed ticket without an owner decision)
  - a business is live with an open blocking Preparation ticket
  - more live businesses than the Phase cap allows
  - a business folder without plan.md or WORK.md
  - the studio ledger and a business ledger disagree

WARN (exit 0, or 1 with --strict) means attention is needed:
  - validation past its deadline (Planning must close it)
  - open ticket older than ticket_stale_days; older than ticket_pause_days means
    the business should be paused
  - more than open_ticket_cap tickets open at once
  - a metrics row without a Source cell ("no number without a source")
  - research/platform-rules.md older than platform_rules_max_age_days
  - payout route not verified while a business is live
  - a run that started and never ended (crash), or a team's circuit breaker open
  - FLAG.md present in a business (Management must act)

Usage:
  python tools/check.py [--json] [--strict]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import studio  # noqa: E402

FINAL_VERDICTS = ("PASSED", "PARKED")
TOTAL_RE = re.compile(r"\*\*Total:\*\*\s*(\d+(?:\.\d+)?)\s*/\s*100")
VERDICT_RE = re.compile(r"\*\*Verdict:\*\*\s*([A-Z]+)")


class Report:
    def __init__(self):
        self.findings: list[dict] = []
        self.summary: dict = {}

    def error(self, where: str, msg: str):
        self.findings.append({"level": "ERROR", "where": where, "message": msg})

    def warn(self, where: str, msg: str):
        self.findings.append({"level": "WARN", "where": where, "message": msg})

    def info(self, where: str, msg: str):
        self.findings.append({"level": "INFO", "where": where, "message": msg})

    @property
    def ok(self) -> bool:
        return not any(f["level"] == "ERROR" for f in self.findings)

    def as_dict(self) -> dict:
        return {"ok": self.ok, "findings": self.findings, "summary": self.summary,
                "errors": sum(f["level"] == "ERROR" for f in self.findings),
                "warnings": sum(f["level"] == "WARN" for f in self.findings)}


def _read(p: Path) -> str:
    try:
        return studio.read_text(p)
    except Exception:
        return ""


def _total(text: str):
    m = TOTAL_RE.search(text)
    return float(m.group(1)) if m else None


def _verdict(text: str):
    m = VERDICT_RE.search(text)
    return m.group(1) if m else None


def _rel(root: Path, p: Path) -> str:
    return studio.rel(root, p)


# ---------------------------------------------------------------------------
def check_structure(root: Path, rep: Report) -> bool:
    ok = True
    for key, relp in studio.STAGES.items():
        if not (root / relp).is_dir():
            rep.error(relp, f"Stage folder missing: {relp}")
            ok = False
    cfg_path = root / "management" / "config.json"
    if not cfg_path.exists():
        rep.warn("management/config.json", "No config.json; defaults in tools/studio.py apply. Create it from the README.")
    else:
        try:
            cfg = json.loads(_read(cfg_path))
        except json.JSONDecodeError as e:
            rep.error("management/config.json", f"config.json is not valid JSON: {e}")
            return False
        if not cfg.get("studio_start"):
            rep.warn("management/config.json", "studio_start is not set: Phase 1 never ends. Set it to the first run's date (README step 2).")
    return ok


def check_inbox(root: Path, rep: Report, cfg: dict) -> int:
    files = studio.list_md(root / studio.STAGES["inbox"])
    for p in files:
        where = _rel(root, p)
        if not studio.ID_RE.match(p.stem):
            rep.warn(where, f"File name should be YYYYMMDD-<slug>.md: {p.name}")
        text = _read(p)
        if "## Score" in text:
            rep.error(where, "Scored brief still in the inbox: Planning must move it to 10-assessed/approved or rejected (## Score present).")
        if "**id:**" not in text.lower():
            rep.warn(where, "Brief has no **Id:** line (templates/idea-brief.md).")
    return len(files)


def check_assessed(root: Path, rep: Report, cfg: dict) -> int:
    thr = float(cfg.get("rubric_threshold", 70))
    n = 0
    for p in studio.list_md(root / studio.STAGES["approved"]):
        n += 1
        where = _rel(root, p)
        text = _read(p)
        if "## Score" not in text:
            rep.error(where, "Brief in approved/ without a ## Score section.")
            continue
        if "## Rejected" in text:
            rep.error(where, "Brief in approved/ carries a ## Rejected section.")
        total = _total(text)
        if total is None:
            rep.warn(where, "## Score has no '**Total:** NN/100' line; tools cannot read the score.")
        elif total < thr:
            rep.error(where, f"Approved brief scores {total:g}, below the threshold of {thr:g}.")
    for p in studio.list_md(root / studio.STAGES["rejected"]):
        n += 1
        where = _rel(root, p)
        text = _read(p)
        if "## Rejected" not in text and "## Score" not in text and "## Status: blocked" not in text:
            rep.error(where, "Brief in rejected/ without a ## Rejected reason or a ## Score.")
    return n


def check_validating(root: Path, rep: Report, cfg: dict) -> dict:
    today = studio.today()
    counts = {"running": 0, "passed": 0, "parked": 0}
    for p in studio.list_md(root / studio.STAGES["validating"]):
        counts["running"] += 1
        where = _rel(root, p)
        text = _read(p)
        f = studio.parse_fields(text)
        if not p.stem.endswith("-validate"):
            rep.warn(where, "Validation file should be named <id>-validate.md")
        deadline = studio.first_date(f.get("deadline"))
        if not deadline:
            rep.error(where, "Validation brief has no **Deadline:** date.")
        v = _verdict(text)
        if v in FINAL_VERDICTS:
            rep.error(where, f"Verdict {v} reached but the file is still in 15-validating/: move it to {v.lower()}/ (and write the plan if PASSED).")
        elif deadline and deadline < today:
            rep.warn(where, f"Validation past its deadline ({deadline}): Planning must count signals (tools/signals.py) and close it.")
    for p in studio.list_md(root / studio.STAGES["passed"]):
        counts["passed"] += 1
        v = _verdict(_read(p))
        if v != "PASSED":
            rep.warn(_rel(root, p), f"File in passed/ has verdict {v or 'none'}; expected PASSED.")
    for p in studio.list_md(root / studio.STAGES["parked"]):
        counts["parked"] += 1
        v = _verdict(_read(p))
        if v == "PASSED":
            rep.warn(_rel(root, p), "File in parked/ has verdict PASSED.")
    return counts


def check_planned(root: Path, rep: Report) -> int:
    files = studio.list_md(root / studio.STAGES["planned"])
    for p in files:
        where = _rel(root, p)
        text = _read(p)
        if not p.stem.endswith("-plan"):
            rep.warn(where, "Plan file should be named <id>-plan.md")
        if "status" not in studio.parse_fields(text):
            rep.error(where, "Plan has no **Status:** line (templates/execution-plan.md).")
    return len(files)


def read_tickets(root: Path, folder_key: str) -> list[dict]:
    out = []
    for p in studio.list_md(root / studio.STAGES[folder_key]):
        text = _read(p)
        f = studio.parse_fields(text)
        raised = f.get("raised", "")
        out.append({
            "path": p, "id": f.get("ticket") or p.stem, "business": (f.get("business") or "").strip().strip("<>"),
            "raised": studio.first_date(raised), "by": raised.split(" by ")[-1].strip().lower() if " by " in raised else "",
            "blocks": (f.get("blocks") or "").strip(), "decision": studio.owner_decision(text),
            "type": "investment" if "investment ticket" in text.lower()[:200] else "approval",
            "amount": f.get("amount requested", ""), "title": next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), p.stem),
        })
    return out


def check_tickets(root: Path, rep: Report, cfg: dict, live: dict) -> dict:
    today = studio.today()
    stale = int(cfg.get("ticket_stale_days", 3))
    pause = int(cfg.get("ticket_pause_days", 7))
    cap = int(cfg.get("open_ticket_cap", 10))
    opened = read_tickets(root, "tickets_open")
    closed = read_tickets(root, "tickets_closed")
    for t in opened:
        where = _rel(root, t["path"])
        if t["decision"]:
            rep.error(where, f"Ticket has owner decision {t['decision']} but is still in open/: move it to closed/ and act on it.")
        if not t["raised"]:
            rep.error(where, "Ticket has no **Raised:** date.")
            continue
        age = studio.days_between(t["raised"], today)
        if age > pause and t["business"] in live:
            rep.warn(where, f"Ticket open {age} days (older than {pause}): pause business '{t['business']}' until the owner acts.")
        elif age > stale:
            rep.warn(where, f"Ticket open {age} days, older than {stale} days: the owner has not acted yet.")
        if t["business"] in live and t["by"] == "preparation" and t["blocks"].lower() not in ("", "none", "nothing", "-"):
            rep.error(where, f"Business '{t['business']}' is live with an open blocking Preparation ticket ({t['id']}: blocks {t['blocks']}).")
    if len(opened) > cap:
        rep.warn(studio.STAGES["tickets_open"], f"{len(opened)} open tickets, above the cap of {cap}: no new tickets until the owner clears the queue.")
    for t in closed:
        if not t["decision"]:
            rep.error(_rel(root, t["path"]), "Closed ticket has no owner decision (APPROVED / REJECTED / DONE).")
    return {"open": len(opened), "closed": len(closed), "open_list": opened}


def read_businesses(root: Path) -> dict:
    out = {}
    biz_root = root / studio.STAGES["businesses"]
    if not biz_root.is_dir():
        return out
    for folder in sorted(p for p in biz_root.iterdir() if p.is_dir()):
        plan = folder / "plan.md"
        text = _read(plan) if plan.exists() else ""
        f = studio.parse_fields(text)
        status = (f.get("status") or "live").strip().lower()
        if status not in ("live", "paused", "stopped"):
            status = "live"
        out[folder.name] = {"path": folder, "status": status, "launched": studio.first_date(f.get("launched")),
                            "has_plan": plan.exists(), "fields": f, "title": next((l.replace("# Execution Plan:", "").strip() for l in text.splitlines() if l.startswith("# ")), folder.name)}
    return out


def check_businesses(root: Path, rep: Report, cfg: dict) -> dict:
    biz = read_businesses(root)
    for slug, b in biz.items():
        where = f"businesses/{slug}"
        if not b["has_plan"]:
            rep.error(where, "Business folder without plan.md.")
        if not (b["path"] / "WORK.md").exists():
            rep.error(where, "Business folder without WORK.md (the Work agent's standing instruction).")
        for name in ("logbook.md", "metrics.md", "ledger.md"):
            if not (b["path"] / name).exists():
                rep.warn(where, f"Missing {name}.")
        if (b["path"] / "FLAG.md").exists():
            rep.warn(where, "FLAG.md present: a kill or scale threshold was crossed; Management must recommend and the owner sign.")
        m = b["path"] / "metrics.md"
        if m.exists():
            for i, line in enumerate(_read(m).splitlines()):
                if not line.strip().startswith("|"):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) < 5 or cells[0].lower() == "date" or set(cells[0]) <= set("-: "):
                    continue
                if not cells[4]:
                    rep.warn(f"{where}/metrics.md:{i + 1}", "Metrics row without a Source cell: no number without a source.")
    live = {s: b for s, b in biz.items() if b["status"] == "live"}
    phase = studio.phase(cfg)
    cap = studio.live_cap(cfg)
    if len(live) > cap:
        rep.error("businesses/", f"{len(live)} live businesses, above the Phase {phase} cap of {cap}. Management must propose stops; Preparation must hold launches.")
    if live and not cfg.get("payout_route_verified", False):
        rep.warn("management/payments.md", "Payout route not verified (config payout_route_verified=false) while a business is live: no business may accept money until the owner verifies a route.")
    return {"all": biz, "live": live, "phase": phase, "cap": cap}


def check_platform_rules(root: Path, rep: Report, cfg: dict) -> None:
    p = root / "research" / "platform-rules.md"
    max_age = int(cfg.get("platform_rules_max_age_days", 30))
    if not p.exists():
        rep.warn("research/platform-rules.md", "Missing: Work agents need current platform rules.")
        return
    checked = studio.first_date(studio.parse_fields(_read(p)).get("checked"))
    if not checked:
        rep.warn("research/platform-rules.md", "No **Checked:** date.")
    elif studio.days_between(checked, studio.today()) > max_age:
        rep.warn("research/platform-rules.md", f"platform-rules.md last checked {checked}, older than {max_age} days: Research re-checks it this cycle.")


def check_runs(root: Path, rep: Report, cfg: dict) -> None:
    try:
        import runlog
    except ImportError:
        return
    events = runlog.read_events(root)
    if not events:
        return
    import datetime as dt
    stale_after = dt.timedelta(hours=float(cfg.get("run_stale_hours", 3)))
    now = dt.datetime.now()
    for run_id, st in runlog.open_runs(events).items():
        try:
            started = dt.datetime.fromisoformat(st["ts"])
        except Exception:
            continue
        if now - started > stale_after:
            rep.warn("management/runs.jsonl", f"Run {run_id} ({st.get('team')}) started {st['ts']} and has no end: crashed. The next runlog start marks it.")
    for team in studio.TEAMS:
        if runlog.breaker_open(events, team, cfg):
            rep.warn("management/runs.jsonl", f"Circuit breaker open for team '{team}' ({runlog.consecutive_failures(events, team)} failed runs in a row): fix the cause, then runlog.py reset --team {team}.")


def check_ledger(root: Path, rep: Report) -> None:
    db = root / "management" / "ledger.sqlite"
    if not db.exists():
        return
    try:
        import ledger
        led = ledger.Ledger(root)
        try:
            ok, issues = led.reconcile()
        finally:
            led.close()
    except Exception as e:  # never let a tool bug hide the folder state
        rep.warn("management/ledger.sqlite", f"Could not reconcile the ledger: {e}")
        return
    for i in issues:
        rep.error("management/ledger.md", f"Ledger mismatch: {i}")


# ---------------------------------------------------------------------------
def run(root: Path) -> dict:
    root = Path(root)
    rep = Report()
    cfg = studio.load_config(root)
    if not check_structure(root, rep):
        rep.summary = {"phase": studio.phase(cfg)}
        return rep.as_dict()
    inbox = check_inbox(root, rep, cfg)
    assessed = check_assessed(root, rep, cfg)
    val = check_validating(root, rep, cfg)
    planned = check_planned(root, rep)
    biz = check_businesses(root, rep, cfg)
    tickets = check_tickets(root, rep, cfg, biz["live"])
    check_platform_rules(root, rep, cfg)
    check_runs(root, rep, cfg)
    check_ledger(root, rep)
    statuses = {}
    for b in biz["all"].values():
        statuses[b["status"]] = statuses.get(b["status"], 0) + 1
    rep.summary = {
        "date": studio.today(), "phase": biz["phase"], "live_cap": biz["cap"],
        "inbox": inbox, "assessed": assessed, "validating": val["running"], "passed": val["passed"], "parked": val["parked"],
        "planned": planned, "tickets_open": tickets["open"], "tickets_closed": tickets["closed"],
        "live": statuses.get("live", 0), "paused": statuses.get("paused", 0), "stopped": statuses.get("stopped", 0),
    }
    return rep.as_dict()


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="check.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root")
    p.add_argument("--json", action="store_true")
    p.add_argument("--strict", action="store_true", help="warnings also exit 1")
    args = p.parse_args(argv)
    try:
        root = Path(args.root) if args.root else studio.find_root(Path.cwd())
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return 1
    res = run(root)
    if args.json:
        print(json.dumps(res, indent=2, default=str))
    else:
        for f in res["findings"]:
            print(f"{f['level']}: [{f['where']}] {f['message']}")
        s = res["summary"]
        if s:
            print(f"Summary {s.get('date', '')}: phase {s.get('phase')} (cap {s.get('live_cap')}) · inbox {s.get('inbox', 0)} · assessed {s.get('assessed', 0)} · "
                  f"validating {s.get('validating', 0)} (passed {s.get('passed', 0)}, parked {s.get('parked', 0)}) · planned {s.get('planned', 0)} · "
                  f"tickets open {s.get('tickets_open', 0)} · live {s.get('live', 0)} paused {s.get('paused', 0)} stopped {s.get('stopped', 0)}")
        print(f"CHECK {'OK' if res['ok'] else 'FAILED'}: {res['errors']} error(s), {res['warnings']} warning(s)")
    if not res["ok"]:
        return 1
    if args.strict and res["warnings"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
