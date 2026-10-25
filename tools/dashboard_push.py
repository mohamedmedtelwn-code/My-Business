#!/usr/bin/env python3
"""Dashboard feed: prints the ArtifactData batch payload for the live dashboard.

Reads the ledger (management/ledger.sqlite), the run log (management/runs.jsonl),
the pipeline folders, the tickets and every businesses/<slug>/ folder, and prints
the exact writes described in skills/management/DASHBOARD.md:

  studio/summary        set     capital, pipeline counts, business counts
  teams/<team>          set     status, summary, last_run, next_run (one per team)
  businesses/<slug>     set     name, category, status, rag, days_live, spent, revenue, last_run, flag, metrics
  tickets/<id>          set     open and closed tickets
  ledger/<entry id>     set     one per ledger entry (never edited)
  activity/<ts-team>    set     the last 25 finished runs
  activity/<old>        delete  only with --versions-dir, when the collection holds more than 200 docs

ArtifactData refuses a write to a document that already exists unless the write
carries that document's current version. Management therefore reads the current
documents first (ArtifactData list per collection with out_dir
management/.dashboard-state) and passes that folder here as --versions-dir so
every write carries if_version. Without it only brand-new documents will succeed.

Usage:
  python tools/dashboard_push.py [--versions-dir management/.dashboard-state] [--url URL] > payload.json
Output: {"url": ..., "batches": [{"action": "batch", "url": ..., "writes": [...]}, ...]} with <= 50 writes per batch.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import studio  # noqa: E402

BATCH_SIZE = 50
ACTIVITY_LIMIT = 25
ACTIVITY_MAX_DOCS = 200
STATUS_FROM_OUTCOME = {"ok": "ok", "warn": "warn", "bad": "bad", "limit": "bad", "crashed": "bad"}


def _num(s):
    if s is None:
        return None
    m = re.search(r"-?\d+(?:\.\d+)?", str(s).replace(",", ""))
    if not m:
        return None
    v = float(m.group(0))
    return int(v) if v == int(v) else v


def _ts_short(iso: str | None) -> str | None:
    if not iso:
        return None
    return iso.replace("T", " ")[:16]


def read_url(root: Path) -> str | None:
    p = root / "management" / "dashboard-url.txt"
    if p.exists():
        for line in studio.read_text(p).splitlines():
            if line.strip().startswith("http"):
                return line.strip()
    return None


# -- versions ------------------------------------------------------------------
def load_versions(versions_dir: Path | None) -> dict:
    """{(collection, doc_id): version}.

    Two sources, both under <versions_dir>:
      * <collection>/<doc_id>.json files saved by ArtifactData list ... out_dir (the file holds the
        document; when it also carries a top-level "version" it is used);
      * versions.json, a mapping {"collection/doc_id": version} that Management writes from the
        version numbers the list results print (the saved files usually hold data only).
    """
    out = {}
    if not versions_dir or not Path(versions_dir).is_dir():
        return out
    side = Path(versions_dir) / "versions.json"
    if side.exists():
        try:
            for key, v in json.loads(studio.read_text(side)).items():
                col, _, doc = key.rpartition("/")
                if col and doc and isinstance(v, int):
                    out[(col, doc)] = v
        except Exception:
            pass
    for p in Path(versions_dir).rglob("*.json"):
        if p == side or p.name in ("payload.json", "writes.json"):
            continue
        try:
            data = json.loads(studio.read_text(p))
        except Exception:
            continue
        rel = p.relative_to(versions_dir)
        if len(rel.parts) < 2:
            continue
        collection = "/".join(rel.parts[:-1])
        doc_id = rel.stem
        v = data.get("version") if isinstance(data, dict) else None
        if isinstance(v, int):
            out[(collection, doc_id)] = v
        else:
            out.setdefault((collection, doc_id), 0)  # exists, version unknown
    return out


# -- sources -------------------------------------------------------------------
def ledger_report(root: Path):
    db = root / "management" / "ledger.sqlite"
    if not db.exists():
        return None, []
    import ledger
    led = ledger.Ledger(root)
    try:
        return led.report(), led.entries()
    finally:
        led.close()


def run_events(root: Path) -> list[dict]:
    try:
        import runlog
        return runlog.read_events(root)
    except Exception:
        return []


def last_runs(events: list[dict]) -> dict:
    """team -> last end event; ('work', slug) -> last end event for that business."""
    out = {}
    for e in events:
        if e.get("event") != "end":
            continue
        out[e.get("team")] = e
        if e.get("team") == "work" and e.get("business"):
            out[("work", e["business"])] = e
    return out


def plan_metrics(plan_text: str) -> list[dict]:
    body = studio.section(plan_text, "Metrics and thresholds") or ""
    rows = []
    for line in body.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0].lower() == "metric" or set(cells[0]) <= set("-: "):
            continue
        if cells[0] in ("1", "2", "3") and not cells[1]:
            continue  # untouched template row
        rows.append({"name": cells[0], "kill": _num(cells[2]), "scale": _num(cells[3])})
    return rows


def last_metric_row(metrics_text: str):
    last = None
    for line in metrics_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0].lower() == "date" or set(cells[0]) <= set("-: "):
            continue
        last = cells
    return last


def business_doc(root: Path, slug: str, biz_totals: dict, last_run: dict | None) -> dict:
    folder = root / "businesses" / slug
    plan = studio.read_text(folder / "plan.md") if (folder / "plan.md").exists() else ""
    f = studio.parse_fields(plan)
    title = next((l.replace("# Execution Plan:", "").strip() for l in plan.splitlines() if l.startswith("# ")), slug)
    status = (f.get("status") or "live").strip().lower()
    if status not in ("live", "paused", "stopped"):
        status = "live"
    launched = studio.first_date(f.get("launched"))
    days_live = studio.days_between(launched, studio.today()) if launched else None
    thresholds = plan_metrics(plan)
    row = last_metric_row(studio.read_text(folder / "metrics.md")) if (folder / "metrics.md").exists() else None
    metrics = []
    for i, m in enumerate(thresholds):
        value = _num(row[i + 1]) if row and len(row) > i + 1 else None
        metrics.append({"name": m["name"], "value": value, "kill": m["kill"], "scale": m["scale"]})
    flag = (folder / "FLAG.md").exists()
    rag = "amber"
    valued = [m for m in metrics if m["value"] is not None]
    if flag or any(m["kill"] is not None and m["value"] < m["kill"] for m in valued):
        rag = "red"
    elif valued and all(m["scale"] is not None and m["value"] >= m["scale"] for m in valued):
        rag = "green"
    totals = biz_totals.get(slug, {"spent": 0, "revenue": 0})
    return {
        "name": title, "category": (f.get("category") or "").strip(), "status": status, "rag": rag,
        "days_live": days_live, "spent": totals.get("spent", 0), "revenue": totals.get("revenue", 0),
        "last_run": _ts_short(last_run.get("end")) if last_run else None, "flag": flag, "metrics": metrics,
    }


ATTACHMENT_CHARS = 6000
VALIDATION_TICKET_RE = re.compile(r"^(?P<vid>\d{8}-[a-z0-9-]+?)-v\d+$")


def ticket_attachments(root: Path, ticket_id: str) -> list[dict]:
    """The drafts the owner must send or publish for a validation ticket: the
    top-level .md files under pipeline/15-validating/output/<validation-id>/."""
    m = VALIDATION_TICKET_RE.match(ticket_id)
    if not m:
        return []
    folder = root / studio.STAGES["validating"] / "output" / m.group("vid")
    if not folder.is_dir():
        return []
    out = []
    for p in sorted(folder.glob("*.md")):
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if len(text) > ATTACHMENT_CHARS:
            text = text[:ATTACHMENT_CHARS].rstrip() + "\n[cut; the full file is in the repository]"
        out.append({"name": p.name, "text": text})
    return out


def ticket_docs(root: Path) -> list[tuple[str, dict]]:
    import check
    out = []
    for key, status in (("tickets_open", "open"), ("tickets_closed", "closed")):
        for t in check.read_tickets(root, key):
            amount = _num(t.get("amount")) or 0
            text = Path(t["path"]).read_text(encoding="utf-8") if t.get("path") else ""
            why = re.sub(r"\s+", " ", (studio.section(text, "Why") or "")).strip()
            out.append((t["id"], {"title": t["title"], "business": t["business"], "type": t["type"],
                                  "amount": amount, "raised": t["raised"] or "", "status": status,
                                  "blocks": t.get("blocks", ""), "steps": t.get("steps", [])[:8],
                                  "why": why, "file": str(Path(t["path"]).relative_to(root)).replace("\\", "/") if t.get("path") else "",
                                  "attachments": ticket_attachments(root, t["id"]) if status == "open" else []}))
    return out


# -- build --------------------------------------------------------------------
def build(root: Path, versions_dir: Path | None = None, url: str | None = None) -> dict:
    root = Path(root)
    cfg = studio.load_config(root)
    url = url or read_url(root) or ""
    versions = load_versions(versions_dir)
    import check
    state = check.run(root)
    s = state["summary"]
    report, entries = ledger_report(root)
    capital = {"ceiling": report["ceiling"], "released": report["released"], "spent": report["spent"],
               "revenue": report["revenue"], "pool": report["pool"]} if report else \
              {"ceiling": cfg["ceiling_usd"], "released": 0, "spent": 0, "revenue": 0, "pool": 0}
    events = run_events(root)
    last = last_runs(events)
    writes: list[dict] = []

    def put(collection: str, doc_id: str, data: dict):
        w = {"op": "set", "collection": collection, "doc_id": doc_id, "data": data}
        v = versions.get((collection, doc_id))
        if v:
            w["if_version"] = v
        writes.append(w)

    put("studio", "summary", {
        "updated": studio.now(), "capital": capital,
        "pipeline": {"inbox": s.get("inbox", 0), "assessed": s.get("assessed", 0), "planned": s.get("planned", 0), "tickets_open": s.get("tickets_open", 0)},
        "businesses": {"live": s.get("live", 0), "paused": s.get("paused", 0), "stopped": s.get("stopped", 0)},
    })
    cadence = cfg.get("team_cadence", {})
    for team in studio.TEAMS:
        e = last.get(team)
        put("teams", team, {
            "status": STATUS_FROM_OUTCOME.get(e.get("outcome"), "warn") if e else "idle",
            "summary": e.get("summary") if e else "No run recorded yet",
            "last_run": _ts_short(e.get("end")) if e else None,
            "next_run": cadence.get(team, ""),
        })
    biz_totals = report["businesses"] if report else {}
    biz_root = root / "businesses"
    if biz_root.is_dir():
        for folder in sorted(p for p in biz_root.iterdir() if p.is_dir()):
            put("businesses", folder.name, business_doc(root, folder.name, biz_totals, last.get(("work", folder.name))))
    for tid, data in ticket_docs(root):
        put("tickets", tid, data)
    for e in entries:
        doc_id = f"{e['date'].replace('-', '')}-{e['business']}-{e['id']}"
        put("ledger", doc_id, {"date": e["date"], "business": e["business"], "item": e["item"],
                               "out": e["usd_out"], "in": e["usd_in"], "tier": e["tier"] or ("release" if e["kind"] == "release" else "")})
    ends = [e for e in events if e.get("event") == "end"][-ACTIVITY_LIMIT:]
    for e in ends:
        ts = e.get("end") or ""
        doc_id = ts[:16].replace("-", "").replace("T", "-").replace(":", "") + "-" + str(e.get("team"))
        put("activity", doc_id, {"ts": _ts_short(ts), "team": e.get("team"), "text": e.get("summary", "")})
    # prune activity beyond 200 docs when we know what is there
    existing = sorted(doc for (col, doc) in versions if col == "activity")
    if len(existing) > ACTIVITY_MAX_DOCS:
        for doc_id in existing[: len(existing) - ACTIVITY_MAX_DOCS]:
            w = {"op": "delete", "collection": "activity", "doc_id": doc_id}
            if versions.get(("activity", doc_id)):
                w["if_version"] = versions[("activity", doc_id)]
            writes.append(w)
    batches = [{"action": "batch", "url": url, "writes": writes[i:i + BATCH_SIZE]} for i in range(0, len(writes), BATCH_SIZE)]
    return {"url": url, "generated": studio.now(), "writes": len(writes), "batches": batches,
            "note": "Send each batch with ArtifactData action=batch. Existing documents need if_version: read them first with list + out_dir and pass --versions-dir." if not versions else ""}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="dashboard_push.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    ap.add_argument("--versions-dir", help="folder written by ArtifactData list ... out_dir (adds if_version to each write)")
    ap.add_argument("--url", help="override management/dashboard-url.txt")
    args = ap.parse_args(argv)
    try:
        root = Path(args.root) if args.root else studio.find_root(Path.cwd())
    except FileNotFoundError as e:
        print(json.dumps({"error": str(e)}))
        return 1
    payload = build(root, versions_dir=Path(args.versions_dir) if args.versions_dir else None, url=args.url)
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
