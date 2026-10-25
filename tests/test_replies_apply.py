"""Tests for tools/replies_apply.py - owner answers from the dashboard applied to ticket files."""
import datetime as dt
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))

import replies_apply as ra  # noqa: E402
import studio  # noqa: E402

TODAY = dt.date.today().isoformat()
TEMPLATE_LINE = "**Owner decision:** APPROVED / REJECTED / DONE — date — note"


def write(root, rel, text):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def make_studio(tmp: Path) -> Path:
    for rel in studio.STAGES.values():
        (tmp / rel).mkdir(parents=True, exist_ok=True)
    write(tmp, "CLAUDE.md", "# studio\n")
    write(tmp, "management/config.json", json.dumps(studio.DEFAULT_CONFIG))
    write(tmp, "pipeline/30-tickets/open/20261101-abc-v1.md",
          "# Approval Ticket\n\n- **Ticket:** 20261101-abc-v1\n- **Business:** abc\n- **Type:** send\n"
          "- **Raised:** 2026-11-01 by planning\n- **Blocks:** validation of abc\n\n## What we need you to do\n1. Send\n\n---\n" + TEMPLATE_LINE + "\n")
    write(tmp, "pipeline/30-tickets/open/20261101-studio-9.md",
          "# Approval Ticket\n\n- **Ticket:** 20261101-studio-9\n- **Business:** studio\n- **Type:** legal\n"
          "- **Raised:** 2026-11-01 by preparation\n- **Blocks:** taking money\n\n## What we need you to do\n1. Decide\n\n---\n" + TEMPLATE_LINE + "\n")
    (tmp / "pipeline/15-validating/output/20261101-abc/replies").mkdir(parents=True)
    return tmp


class Apply(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self.tmpdir.name))

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_done_closes_ticket_and_keeps_the_note_as_a_reply_file(self):
        res = ra.apply(self.root, [{"id": "r1", "data": {"ticket": "20261101-abc-v1", "decision": "done",
                                                          "note": "Sent 20. Ahmed (clinic) asked for the price.", "at": "2026-11-03T10:15:00Z"}}])
        self.assertEqual(res[0]["action"], "closed")
        closed = self.root / "pipeline/30-tickets/closed/20261101-abc-v1.md"
        self.assertTrue(closed.exists())
        self.assertFalse((self.root / "pipeline/30-tickets/open/20261101-abc-v1.md").exists())
        text = closed.read_text(encoding="utf-8")
        self.assertNotIn(TEMPLATE_LINE, text)
        self.assertIn("**Owner decision:** DONE — 2026-11-03 — Sent 20. Ahmed (clinic) asked for the price. (via dashboard)", text)
        self.assertEqual(studio.owner_decision(text), "DONE")
        files = list((self.root / "pipeline/15-validating/output/20261101-abc/replies").glob("*.md"))
        self.assertEqual(len(files), 1)
        self.assertIn("Ahmed (clinic) asked for the price.", files[0].read_text(encoding="utf-8"))

    def test_note_keeps_ticket_open_and_appends_the_note(self):
        res = ra.apply(self.root, [{"id": "r2", "data": {"ticket": "20261101-abc-v1", "decision": "note",
                                                          "note": "3 sent so far, no replies", "at": "2026-11-02T08:00:00Z"}}])
        self.assertEqual(res[0]["action"], "noted")
        p = self.root / "pipeline/30-tickets/open/20261101-abc-v1.md"
        text = p.read_text(encoding="utf-8")
        self.assertIn(TEMPLATE_LINE, text)
        self.assertIn("**Owner note (2026-11-02):** 3 sent so far, no replies", text)
        self.assertIsNone(studio.owner_decision(text))
        files = list((self.root / "pipeline/15-validating/output/20261101-abc/replies").glob("*.md"))
        self.assertEqual(len(files), 1)

    def test_rejected_studio_ticket_closes_without_reply_file(self):
        res = ra.apply(self.root, [{"id": "r3", "data": {"ticket": "20261101-studio-9", "decision": "rejected", "note": "", "at": ""}}])
        self.assertEqual(res[0]["action"], "closed")
        text = (self.root / "pipeline/30-tickets/closed/20261101-studio-9.md").read_text(encoding="utf-8")
        self.assertIn(f"**Owner decision:** REJECTED — {TODAY} —", text)
        self.assertEqual(studio.owner_decision(text), "REJECTED")

    def test_unknown_ticket_or_decision_is_skipped(self):
        res = ra.apply(self.root, [{"id": "r4", "data": {"ticket": "nope-1", "decision": "done", "note": "x", "at": ""}},
                                   {"id": "r5", "data": {"ticket": "20261101-studio-9", "decision": "maybe", "note": "x", "at": ""}}])
        self.assertEqual([r["action"] for r in res], ["skipped", "skipped"])
        self.assertTrue((self.root / "pipeline/30-tickets/open/20261101-studio-9.md").exists())

    def test_second_decision_on_a_closed_ticket_is_kept_as_a_note(self):
        ra.apply(self.root, [{"id": "r6", "data": {"ticket": "20261101-studio-9", "decision": "approved", "note": "ok", "at": "2026-11-02T08:00:00Z"}}])
        res = ra.apply(self.root, [{"id": "r7", "data": {"ticket": "20261101-studio-9", "decision": "done", "note": "also done", "at": "2026-11-03T08:00:00Z"}}])
        self.assertEqual(res[0]["action"], "noted")
        text = (self.root / "pipeline/30-tickets/closed/20261101-studio-9.md").read_text(encoding="utf-8")
        self.assertEqual(studio.owner_decision(text), "APPROVED")
        self.assertIn("**Owner note (2026-11-03):** also done", text)


class Cli(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self.tmpdir.name))
        self.state = self.root / "management/.dashboard-state"
        (self.state / "replies").mkdir(parents=True)
        write(self.root, "management/.dashboard-state/replies/r1.json",
              json.dumps({"ticket": "20261101-abc-v1", "decision": "done", "note": "sent", "at": "2026-11-03T10:00:00Z"}))
        write(self.root, "management/.dashboard-state/replies/r2.json",
              json.dumps({"ticket": "nope", "decision": "done", "note": "", "at": ""}))
        write(self.root, "management/.dashboard-state/versions.json", json.dumps({"replies/r1": 2, "replies/r2": 1}))

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_cli_applies_files_and_writes_the_delete_batch(self):
        out = io.StringIO()
        with redirect_stdout(out):
            code = ra.main(["--root", str(self.root), str(self.state / "replies"), "--versions", str(self.state / "versions.json"),
                            "--url", "https://claude.ai/artifact/X", "--delete-out", str(self.state / "replies-delete.json")])
        self.assertEqual(code, 0)
        self.assertIn("applied 1", out.getvalue())
        self.assertIn("skipped 1", out.getvalue())
        batch = json.loads((self.state / "replies-delete.json").read_text(encoding="utf-8"))
        self.assertEqual(batch["action"], "batch")
        self.assertEqual(batch["url"], "https://claude.ai/artifact/X")
        ops = {w["doc_id"]: w for w in batch["writes"]}
        self.assertEqual(ops["r1"], {"op": "delete", "collection": "replies", "doc_id": "r1", "if_version": 2})
        self.assertEqual(ops["r2"], {"op": "delete", "collection": "replies", "doc_id": "r2", "if_version": 1})
        self.assertTrue((self.root / "pipeline/30-tickets/closed/20261101-abc-v1.md").exists())


if __name__ == "__main__":
    unittest.main()
