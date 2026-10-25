"""Ticket documents on the dashboard carry what the owner needs to act: the why, the file, the drafts."""
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
sys.path.insert(0, str(HERE))

import dashboard_push as dp  # noqa: E402
from test_dashboard_push import make_studio, write  # noqa: E402


class TicketCards(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self.tmpdir.name))
        write(self.root, "pipeline/30-tickets/open/20261101-xyz-v1.md",
              "# Approval Ticket\n\n- **Ticket:** 20261101-xyz-v1\n- **Business:** xyz\n- **Type:** send\n- **Raised:** 2026-11-01 by planning\n"
              "- **Blocks:** validation of xyz\n\n## What we need you to do\n1. Send message.md to 20 people\n\n## Why\nRule 10: three signals first.\n\n"
              "## After you're done\nPlanning counts.\n\n---\n**Owner decision:** APPROVED / REJECTED / DONE — date — note\n")
        write(self.root, "pipeline/15-validating/output/20261101-xyz/message.md", "# Message\nHi <name>, buy this.\n")
        write(self.root, "pipeline/15-validating/output/20261101-xyz/prospect-criteria.md", "# Who\nPeople who need it.\n")
        write(self.root, "pipeline/15-validating/output/20261101-xyz/replies/r.md", "a reply, not an attachment\n")
        self.docs = {(w["collection"], w["doc_id"]): w["data"] for b in dp.build(self.root)["batches"] for w in b["writes"] if w["op"] == "set"}

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_validation_ticket_carries_why_file_and_drafts(self):
        t = self.docs[("tickets", "20261101-xyz-v1")]
        self.assertEqual(t["why"], "Rule 10: three signals first.")
        self.assertEqual(t["file"], "pipeline/30-tickets/open/20261101-xyz-v1.md")
        names = [a["name"] for a in t["attachments"]]
        self.assertEqual(names, ["message.md", "prospect-criteria.md"])
        self.assertIn("Hi <name>, buy this.", t["attachments"][0]["text"])

    def test_plain_ticket_has_empty_attachments(self):
        t = self.docs[("tickets", "20261101-abc-2")]
        self.assertEqual(t["attachments"], [])
        self.assertEqual(t["file"], "pipeline/30-tickets/open/20261101-abc-2.md")


if __name__ == "__main__":
    unittest.main()
