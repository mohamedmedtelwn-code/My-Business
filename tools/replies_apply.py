"""Apply the owner's answers from the live dashboard to the ticket files.

The dashboard's ticket cards let the owner answer without editing files: each
answer is a document in the artifact database, collection `replies`:
    {"ticket": "<ticket id>", "decision": "done|approved|rejected|note",
     "note": "<free text>", "at": "<ISO timestamp>"}
A run saves them with `ArtifactData list --out_dir <dir>` (one JSON file per
document, named by document id) and calls:
    python tools/replies_apply.py <dir> [--versions versions.json] [--delete-out replies-delete.json]
For each answer: done / approved / rejected writes the owner decision line and
moves the ticket to closed/; note appends an owner note and leaves it open; a
note on a validation ticket (<validation-id>-vN) is also saved under
pipeline/15-validating/output/<validation-id>/replies/ so Planning can count
signals. The delete batch (ArtifactData action batch) removes the applied
documents; without versions it is written without pins and the run must list
again before deleting.

Stdlib only. Exit 0 always (skips are reported, not failures).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import studio  # noqa: E402

DECISIONS = {"done": "DONE", "approved": "APPROVED", "rejected": "REJECTED"}
TEMPLATE_RE = re.compile(r"^\*\*Owner decision:\*\*\s*APPROVED\s*/\s*REJECTED\s*/\s*DONE.*$", re.M)
VALIDATION_TICKET_RE = re.compile(r"^(?P<vid>\d{8}-[a-z0-9-]+?)-v\d+$")


def _date_of(at: str) -> str:
    at = (at or "").strip()
    m = re.match(r"\d{4}-\d{2}-\d{2}", at)
    return m.group(0) if m else studio.today()


def _find_ticket(root: Path, ticket: str) -> tuple[Path | None, str]:
    for key in ("tickets_open", "tickets_closed"):
        p = root / studio.STAGES[key] / f"{ticket}.md"
        if p.exists():
            return p, key
    return None, ""


def _reply_file(root: Path, ticket: str, date: str, decision: str, note: str, doc_id: str) -> str | None:
    m = VALIDATION_TICKET_RE.match(ticket)
    if not m or not note.strip():
        return None
    out = root / studio.STAGES["validating"] / "output" / m.group("vid") / "replies"
    if not out.parent.is_dir():
        return None
    out.mkdir(parents=True, exist_ok=True)
    p = out / f"{date.replace('-', '')}-dashboard-{re.sub(r'[^A-Za-z0-9]+', '', doc_id)[:12] or 'reply'}.md"
    studio.write_text(p, f"# Owner report via dashboard ({date}, {decision})\n\nTicket: {ticket}\n\n{note.strip()}\n")
    return studio.rel(root, p) if hasattr(studio, "rel") else str(p.relative_to(root))


def apply(root: Path | str, replies: list[dict]) -> list[dict]:
    """Apply reply documents ({"id":..., "data": {...}}); return one result row per document."""
    root = Path(root)
    results = []
    for r in replies:
        doc_id = str(r.get("id", ""))
        data = r.get("data") or {}
        ticket = str(data.get("ticket", "")).strip()
        decision = str(data.get("decision", "")).strip().lower()
        note = str(data.get("note", "")).strip()
        date = _date_of(str(data.get("at", "")))
        row = {"doc_id": doc_id, "ticket": ticket, "decision": decision, "action": "skipped", "reason": ""}
        path, key = _find_ticket(root, ticket)
        if path is None:
            row["reason"] = "no such ticket"
            results.append(row)
            continue
        if decision not in DECISIONS and decision != "note":
            row["reason"] = f"unknown decision '{decision}'"
            results.append(row)
            continue
        text = path.read_text(encoding="utf-8")
        already = studio.owner_decision(text)
        if decision in DECISIONS and already is None and key == "tickets_open":
            line = f"**Owner decision:** {DECISIONS[decision]} — {date} — {note or 'no note'} (via dashboard)"
            if TEMPLATE_RE.search(text):
                text = TEMPLATE_RE.sub(lambda _m: line, text, count=1)
            else:
                text = text.rstrip("\n") + "\n\n---\n" + line + "\n"
            dest = root / studio.STAGES["tickets_closed"] / path.name
            studio.write_text(dest, text)
            path.unlink()
            row.update(action="closed", path=str(dest.relative_to(root)))
        else:
            label = decision if decision == "note" else f"{decision}, already decided {already}"
            text = text.rstrip("\n") + f"\n**Owner note ({date}):** {note or 'no note'}" + (f" [{label}]" if decision != "note" else "") + "\n"
            studio.write_text(path, text)
            row.update(action="noted", path=str(path.relative_to(root)))
        rf = _reply_file(root, ticket, date, decision, note, doc_id)
        if rf:
            row["reply_file"] = rf
        results.append(row)
    return results


def load_dir(folder: Path) -> list[dict]:
    out = []
    for p in sorted(Path(folder).glob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(data, dict) and "data" in data and isinstance(data["data"], dict) and "ticket" not in data:
            data = data["data"]
        if isinstance(data, dict):
            out.append({"id": p.stem, "data": data})
    return out


def delete_batch(results: list[dict], versions: dict, url: str) -> dict:
    writes = []
    for r in results:
        w = {"op": "delete", "collection": "replies", "doc_id": r["doc_id"]}
        v = versions.get(f"replies/{r['doc_id']}")
        if v:
            w["if_version"] = int(v)
        writes.append(w)
    return {"action": "batch", "url": url, "writes": writes[:50]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("folder", help="directory of reply documents saved by ArtifactData list --out_dir")
    ap.add_argument("--root", default=None)
    ap.add_argument("--versions", default=None, help="versions.json ({'replies/<doc_id>': version})")
    ap.add_argument("--url", default=None, help="artifact url (default: management/dashboard-url.txt)")
    ap.add_argument("--delete-out", default=None, help="where to write the ArtifactData delete batch")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    root = Path(a.root) if a.root else studio.find_root()
    folder = Path(a.folder)
    if not folder.is_dir():
        print(f"applied 0, skipped 0 (no folder {folder})")
        return 0
    replies = load_dir(folder)
    results = apply(root, replies)
    versions = {}
    if a.versions and Path(a.versions).exists():
        try:
            versions = json.loads(Path(a.versions).read_text(encoding="utf-8"))
        except ValueError:
            versions = {}
    url = a.url
    if not url:
        f = root / "management" / "dashboard-url.txt"
        url = f.read_text(encoding="utf-8").strip() if f.exists() else ""
    batch = delete_batch(results, versions, url)
    if a.delete_out and results:
        studio.write_text(Path(a.delete_out), json.dumps(batch, indent=1, ensure_ascii=False))
    if a.json:
        print(json.dumps({"results": results, "delete": batch}, indent=1, ensure_ascii=False))
    else:
        applied = sum(1 for r in results if r["action"] != "skipped")
        skipped = len(results) - applied
        for r in results:
            extra = f" ({r['reason']})" if r.get("reason") else ""
            print(f"{r['action']:8s} {r['ticket']} <- {r['decision'] or '?'} [{r['doc_id']}]{extra}")
        print(f"applied {applied}, skipped {skipped}" + (f"; delete batch -> {a.delete_out}" if a.delete_out and results else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
