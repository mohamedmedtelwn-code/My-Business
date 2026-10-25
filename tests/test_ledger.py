"""Tests for tools/ledger.py - the studio ledger as code."""
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))

import ledger  # noqa: E402
import studio  # noqa: E402


def make_studio(tmp: Path) -> Path:
    """Create a minimal studio folder: config, management/, businesses/."""
    (tmp / "management").mkdir()
    (tmp / "businesses").mkdir()
    (tmp / "tools").mkdir()
    (tmp / "CLAUDE.md").write_text("# studio\n", encoding="utf-8")
    cfg = dict(studio.DEFAULT_CONFIG)
    cfg["ceiling_usd"] = 1000
    (tmp / "management" / "config.json").write_text(json.dumps(cfg), encoding="utf-8")
    return tmp


class LedgerCore(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self._tmp.name))
        self.led = ledger.Ledger(self.root)
        self.led.init()

    def tearDown(self):
        self.led.close()
        self._tmp.cleanup()

    def test_init_creates_db_and_markdown_view(self):
        self.assertTrue((self.root / "management" / "ledger.sqlite").exists())
        md = (self.root / "management" / "ledger.md").read_text(encoding="utf-8")
        self.assertIn("Studio Ledger", md)
        self.assertIn("1,000", md)
        r = self.led.report()
        self.assertEqual(r["ceiling"], 1000)
        self.assertEqual(r["released"], 0)
        self.assertEqual(r["spent"], 0)
        self.assertEqual(r["revenue"], 0)
        self.assertEqual(r["pool"], 0)

    def test_release_records_ceiling_release(self):
        self.led.release(ticket="20261101-abc-1", business="abc", amount=120, date="2026-11-01")
        r = self.led.report()
        self.assertEqual(r["released"], 120)
        self.assertEqual(r["ceiling_remaining"], 880)
        self.assertEqual(r["released_unspent"], 120)

    def test_release_beyond_ceiling_is_refused(self):
        self.led.release(ticket="t-1", business="abc", amount=900)
        with self.assertRaises(ledger.LedgerError) as cm:
            self.led.release(ticket="t-2", business="abc", amount=200)
        self.assertIn("ceiling", str(cm.exception).lower())
        self.assertEqual(self.led.report()["released"], 900)

    def test_spend_from_unreleased_ceiling_is_refused(self):
        with self.assertRaises(ledger.LedgerError) as cm:
            self.led.add(business="abc", item="domain", out=12, source="ceiling", ticket="t-9", tier="0")
        self.assertIn("unreleased", str(cm.exception).lower())
        self.assertEqual(self.led.report()["spent"], 0)

    def test_spend_within_release_is_accepted(self):
        self.led.release(ticket="t-1", business="abc", amount=100)
        self.led.add(business="abc", item="domain", out=12, source="ceiling", ticket="t-1", tier="0")
        r = self.led.report()
        self.assertEqual(r["spent"], 12)
        self.assertEqual(r["spent_from_ceiling"], 12)
        self.assertEqual(r["released_unspent"], 88)

    def test_spend_beyond_ticket_release_is_refused(self):
        self.led.release(ticket="t-1", business="abc", amount=50)
        self.led.add(business="abc", item="ads", out=40, source="ceiling", ticket="t-1", tier="0")
        with self.assertRaises(ledger.LedgerError):
            self.led.add(business="abc", item="ads", out=20, source="ceiling", ticket="t-1", tier="0")
        self.assertEqual(self.led.report()["spent"], 40)

    def test_revenue_fills_the_pool(self):
        self.led.add(business="abc", item="sale", inc=75)
        r = self.led.report()
        self.assertEqual(r["revenue"], 75)
        self.assertEqual(r["pool"], 75)

    def test_spend_from_empty_pool_is_refused(self):
        with self.assertRaises(ledger.LedgerError) as cm:
            self.led.add(business="abc", item="tool", out=5, source="pool", ticket="t-3", tier="0")
        self.assertIn("pool", str(cm.exception).lower())

    def test_spend_from_pool_within_balance_is_accepted(self):
        self.led.add(business="abc", item="sale", inc=75)
        self.led.add(business="abc", item="tool", out=30, source="pool", ticket="t-3", tier="0")
        r = self.led.report()
        self.assertEqual(r["pool"], 45)
        self.assertEqual(r["spent_from_pool"], 30)
        with self.assertRaises(ledger.LedgerError):
            self.led.add(business="abc", item="tool", out=50, source="pool", ticket="t-4", tier="0")

    def test_spend_requires_ticket(self):
        self.led.release(ticket="t-1", business="abc", amount=100)
        with self.assertRaises(ledger.LedgerError) as cm:
            self.led.add(business="abc", item="x", out=1, source="ceiling", ticket="", tier="0")
        self.assertIn("ticket", str(cm.exception).lower())

    def test_entry_cannot_have_both_in_and_out(self):
        with self.assertRaises(ledger.LedgerError):
            self.led.add(business="abc", item="x", out=1, inc=1, source="pool", ticket="t")

    def test_render_lists_entries_and_running_totals(self):
        self.led.release(ticket="t-1", business="abc", amount=100, date="2026-11-01")
        self.led.add(business="abc", item="domain", out=12, source="ceiling", ticket="t-1", tier="0", date="2026-11-02")
        self.led.add(business="abc", item="first sale", inc=40, date="2026-11-05")
        md = (self.root / "management" / "ledger.md").read_text(encoding="utf-8")
        self.assertIn("domain", md)
        self.assertIn("first sale", md)
        self.assertIn("Do not edit by hand", md)
        # running totals: released 100, spent 12, revenue 40, pool 40
        self.assertRegex(md, r"\|\s*100\s*\|\s*12\s*\|\s*40\s*\|\s*40\s*\|")

    def test_add_appends_to_business_ledger_when_folder_exists(self):
        biz = self.root / "businesses" / "abc"
        biz.mkdir()
        self.led.release(ticket="t-1", business="abc", amount=100)
        self.led.add(business="abc", item="domain", out=12, source="ceiling", ticket="t-1", tier="0", date="2026-11-02")
        self.led.add(business="abc", item="sale", inc=30, date="2026-11-03")
        txt = (biz / "ledger.md").read_text(encoding="utf-8")
        self.assertIn("| 2026-11-02 | domain | 12 | 0 |", txt)
        self.assertIn("| 2026-11-03 | sale | 0 | 30 |", txt)
        self.assertIn("| 18 |", txt)  # balance after both rows: 30 - 12

    def test_reconcile_passes_when_business_ledger_matches(self):
        (self.root / "businesses" / "abc").mkdir()
        self.led.add(business="abc", item="sale", inc=30)
        ok, issues = self.led.reconcile()
        self.assertTrue(ok, issues)
        self.assertEqual(issues, [])

    def test_reconcile_flags_manual_rows_not_in_db(self):
        biz = self.root / "businesses" / "abc"
        biz.mkdir()
        self.led.add(business="abc", item="sale", inc=30)
        with open(biz / "ledger.md", "a", encoding="utf-8") as fh:
            fh.write("| 2026-11-09 | cash sale not recorded | 0 | 20 | - | 50 |\n")
        ok, issues = self.led.reconcile()
        self.assertFalse(ok)
        self.assertTrue(any("abc" in i for i in issues))

    def test_reconcile_flags_business_folder_without_ledger_rows_in_db(self):
        biz = self.root / "businesses" / "xyz"
        biz.mkdir()
        (biz / "ledger.md").write_text(
            "| Date | Item | USD out | USD in | Ticket / tier | Balance |\n|---|---|---|---|---|---|\n"
            "| 2026-11-09 | sale | 0 | 20 | - | 20 |\n", encoding="utf-8")
        ok, issues = self.led.reconcile()
        self.assertFalse(ok)

    def test_per_business_totals_in_report(self):
        self.led.add(business="abc", item="sale", inc=30)
        self.led.add(business="def", item="sale", inc=10)
        r = self.led.report()
        self.assertEqual(r["businesses"]["abc"]["revenue"], 30)
        self.assertEqual(r["businesses"]["def"]["revenue"], 10)


class LedgerCli(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self._tmp.name))

    def tearDown(self):
        self._tmp.cleanup()

    def run_cli(self, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = ledger.main(["--root", str(self.root), *args])
        return code, buf.getvalue()

    def test_cli_round_trip(self):
        code, _ = self.run_cli("init")
        self.assertEqual(code, 0)
        code, _ = self.run_cli("release", "--ticket", "t-1", "--business", "abc", "--amount", "100")
        self.assertEqual(code, 0)
        code, out = self.run_cli("add", "--business", "abc", "--item", "domain", "--out", "12",
                                 "--source", "ceiling", "--ticket", "t-1", "--tier", "0")
        self.assertEqual(code, 0, out)
        code, out = self.run_cli("report", "--json")
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual(data["spent"], 12)
        self.assertEqual(data["released"], 100)

    def test_cli_refusal_exits_nonzero_and_explains(self):
        self.run_cli("init")
        code, out = self.run_cli("add", "--business", "abc", "--item", "ads", "--out", "5",
                                 "--source", "ceiling", "--ticket", "t-1", "--tier", "0")
        self.assertEqual(code, 1)
        self.assertIn("REFUSED", out)

    def test_cli_reconcile_exit_codes(self):
        self.run_cli("init")
        (self.root / "businesses" / "abc").mkdir()
        self.run_cli("add", "--business", "abc", "--item", "sale", "--in", "30")
        code, out = self.run_cli("reconcile")
        self.assertEqual(code, 0, out)
        with open(self.root / "businesses" / "abc" / "ledger.md", "a", encoding="utf-8") as fh:
            fh.write("| 2026-11-09 | extra | 0 | 20 | - | 50 |\n")
        code, out = self.run_cli("reconcile")
        self.assertEqual(code, 1)
        self.assertIn("abc", out)


if __name__ == "__main__":
    unittest.main()
