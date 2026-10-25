"""Tests for tools/signals.py - validation signal units and verdict."""
import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))

import signals  # noqa: E402
import studio  # noqa: E402

TODAY = dt.date.today()
CFG = dict(studio.DEFAULT_CONFIG)


def d(days):
    return (TODAY + dt.timedelta(days=days)).isoformat()


def brief(test="outreach", started=-7, deadline=0, messages=0, visitors=0, asks=0, extended="no", rows=()):
    rows_md = "\n".join(f"| {d(-1)} | {t} | {who} | output/x.png |" for t, who in rows)
    return (f"# Validation Brief: X\n\n- **Id:** 20261101-x\n- **Started:** {d(started)}  **Deadline:** {d(deadline)} (7 days)\n"
            f"- **Test:** {test}\n- **Extended:** {extended}\n- **Cost:** USD 0\n\n## Denominator\n"
            f"- **Messages sent:** {messages}\n- **Visitors:** {visitors}\n- **Asks:** {asks}\n\n"
            f"## Signals\n| Date | Type | Who / what | Source |\n|------|------|-----------|--------|\n{rows_md}\n")


class SignalUnits(unittest.TestCase):
    def test_payment_alone_passes(self):
        v = signals.verdict(brief(messages=5, rows=[("payment", "stranger pre-ordered")]), CFG)
        self.assertEqual(v["su"], 3)
        self.assertEqual(v["verdict"], "PASSED")

    def test_three_intent_replies_pass_before_deadline(self):
        v = signals.verdict(brief(deadline=3, messages=20, rows=[("intent", "a"), ("intent", "b"), ("call", "c")]), CFG)
        self.assertEqual(v["su"], 3)
        self.assertEqual(v["verdict"], "PASSED")

    def test_two_signals_from_fifty_due_is_parked(self):
        v = signals.verdict(brief(messages=50, rows=[("intent", "a"), ("intent", "b")]), CFG)
        self.assertEqual(v["verdict"], "PARKED")
        self.assertTrue(v["denominator_reached"])

    def test_zero_of_twenty_due_is_parked_early(self):
        v = signals.verdict(brief(messages=20), CFG)
        self.assertEqual(v["verdict"], "PARKED")

    def test_one_signal_from_thirty_due_not_extended_is_inconclusive(self):
        v = signals.verdict(brief(messages=30, rows=[("intent", "a")]), CFG)
        self.assertEqual(v["verdict"], "INCONCLUSIVE")
        self.assertFalse(v["denominator_reached"])

    def test_one_signal_from_thirty_due_already_extended_is_parked(self):
        v = signals.verdict(brief(messages=30, extended="yes", rows=[("intent", "a")]), CFG)
        self.assertEqual(v["verdict"], "PARKED")

    def test_not_due_yet_is_running(self):
        v = signals.verdict(brief(deadline=2, messages=10, rows=[("intent", "a")]), CFG)
        self.assertEqual(v["verdict"], "RUNNING")

    def test_likes_and_followers_count_zero(self):
        v = signals.verdict(brief(messages=50, rows=[("like", "x")] * 10), CFG)
        self.assertEqual(v["su"], 0)
        self.assertTrue(v["ignored"])

    def test_landing_signups_count_a_third_only_above_rate_and_visitors(self):
        # 100 visitors, 9 sign-ups = 9% -> 3 SU but capped at 2 without a second step
        v = signals.verdict(brief(test="landing", visitors=100, rows=[("signup", f"s{i}") for i in range(9)]), CFG)
        self.assertEqual(v["su"], 2)
        self.assertEqual(v["verdict"], "PARKED")
        v = signals.verdict(brief(test="landing", visitors=100, rows=[("signup", f"s{i}") for i in range(9)] + [("intent", "replied with use case")]), CFG)
        self.assertEqual(v["su"], 3)
        self.assertEqual(v["verdict"], "PASSED")
        # 7% sign-up: sign-ups count nothing
        v = signals.verdict(brief(test="landing", visitors=100, rows=[("signup", f"s{i}") for i in range(7)] + [("intent", "x")]), CFG)
        self.assertEqual(v["su"], 1)
        # under 100 visitors: inconclusive, not parked
        v = signals.verdict(brief(test="landing", visitors=60, rows=[("signup", f"s{i}") for i in range(9)]), CFG)
        self.assertEqual(v["verdict"], "INCONCLUSIVE")

    def test_presale_one_payment_passes_and_zero_of_twenty_parks(self):
        v = signals.verdict(brief(test="presale", asks=20, rows=[("payment", "paid USD 29")]), CFG)
        self.assertEqual(v["verdict"], "PASSED")
        v = signals.verdict(brief(test="presale", asks=20), CFG)
        self.assertEqual(v["verdict"], "PARKED")
        v = signals.verdict(brief(test="presale", asks=12), CFG)
        self.assertEqual(v["verdict"], "INCONCLUSIVE")

    def test_missing_deadline_is_an_error(self):
        text = brief().replace(f"**Deadline:** {d(0)} (7 days)", "")
        with self.assertRaises(signals.SignalsError):
            signals.verdict(text, CFG)


class WriteVerdict(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / "CLAUDE.md").write_text("x", encoding="utf-8")
        (self.root / "management").mkdir()
        (self.root / "management" / "config.json").write_text(json.dumps(CFG), encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def test_write_appends_verdict_section_and_is_idempotent(self):
        p = self.root / "20261101-x-validate.md"
        p.write_text(brief(messages=50, rows=[("intent", "a"), ("intent", "b"), ("intent", "c")]), encoding="utf-8")
        v = signals.write_verdict(p, CFG)
        text = p.read_text(encoding="utf-8")
        self.assertEqual(v["verdict"], "PASSED")
        self.assertEqual(text.count("## Verdict"), 1)
        self.assertIn("**Verdict:** PASSED", text)
        signals.write_verdict(p, CFG)
        self.assertEqual(p.read_text(encoding="utf-8").count("## Verdict"), 1)

    def test_write_inconclusive_extends_deadline_once(self):
        p = self.root / "20261101-x-validate.md"
        p.write_text(brief(messages=30, rows=[("intent", "a")]), encoding="utf-8")
        v = signals.write_verdict(p, CFG)
        text = p.read_text(encoding="utf-8")
        self.assertEqual(v["verdict"], "INCONCLUSIVE")
        self.assertIn("**Extended:** yes", text)
        self.assertIn(f"**Deadline:** {d(CFG['validation_days'])}", text)
        # second run after the new deadline would park; before it, RUNNING
        v2 = signals.verdict(text, CFG)
        self.assertEqual(v2["verdict"], "RUNNING")

    def test_cli(self):
        import io
        from contextlib import redirect_stdout
        p = self.root / "20261101-x-validate.md"
        p.write_text(brief(messages=20), encoding="utf-8")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = signals.main(["--root", str(self.root), str(p)])
        self.assertEqual(code, 0)
        self.assertIn("PARKED", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
