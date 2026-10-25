"""Tests for tools/studio.py shared helpers."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))

import studio  # noqa: E402


class FieldParsing(unittest.TestCase):
    def test_parse_fields_reads_bold_key_lines(self):
        text = ("# Ticket\n\n- **Ticket:** 20261101-abc-1\n- **Business:** abc\n"
                "- **Raised:** 2026-11-01 by preparation\n- **Blocks:** first publish\n\nbody\n")
        f = studio.parse_fields(text)
        self.assertEqual(f["ticket"], "20261101-abc-1")
        self.assertEqual(f["business"], "abc")
        self.assertEqual(f["raised"], "2026-11-01 by preparation")
        self.assertEqual(f["blocks"], "first publish")

    def test_parse_fields_handles_inline_pairs(self):
        text = "- **Started:** 2026-11-01  **Deadline:** 2026-11-08 (7 days)\n"
        f = studio.parse_fields(text)
        self.assertEqual(f["started"], "2026-11-01")
        self.assertTrue(f["deadline"].startswith("2026-11-08"))

    def test_first_date_extracts_iso_date(self):
        self.assertEqual(studio.first_date("2026-11-01 by preparation"), "2026-11-01")
        self.assertIsNone(studio.first_date("none"))

    def test_owner_decision_detection(self):
        self.assertEqual(studio.owner_decision("...\n**Owner decision:** APPROVED USD 40 — 2026-11-02 — ok\n"), "APPROVED")
        self.assertEqual(studio.owner_decision("**Owner decision:** DONE - 2026-11-02"), "DONE")
        self.assertEqual(studio.owner_decision("**Owner decision:** REJECTED"), "REJECTED")
        self.assertIsNone(studio.owner_decision("**Owner decision:** APPROVED / REJECTED / DONE — date — note"))
        self.assertIsNone(studio.owner_decision("no decision line"))


class RootAndConfig(unittest.TestCase):
    def test_find_root_walks_up_to_claude_md(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "CLAUDE.md").write_text("x", encoding="utf-8")
            deep = root / "businesses" / "abc" / "output"
            deep.mkdir(parents=True)
            self.assertEqual(studio.find_root(deep), root)

    def test_load_config_merges_defaults(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "management").mkdir()
            (root / "management" / "config.json").write_text(json.dumps({"ceiling_usd": 500}), encoding="utf-8")
            cfg = studio.load_config(root)
            self.assertEqual(cfg["ceiling_usd"], 500)
            self.assertIn("phase1_live_cap", cfg)

    def test_phase_from_start_date(self):
        cfg = dict(studio.DEFAULT_CONFIG, studio_start="2026-11-01", phase1_days=90)
        self.assertEqual(studio.phase(cfg, today="2026-11-30"), 1)
        self.assertEqual(studio.phase(cfg, today="2027-01-29"), 1)
        self.assertEqual(studio.phase(cfg, today="2027-01-30"), 2)


if __name__ == "__main__":
    unittest.main()
