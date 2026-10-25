"""Tests for tools/check.py - the pipeline state checker."""
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

import check  # noqa: E402
import ledger  # noqa: E402
import studio  # noqa: E402

TODAY = dt.date.today()


def d(days: int) -> str:
    return (TODAY + dt.timedelta(days=days)).isoformat()


def make_studio(tmp: Path, **cfg_over) -> Path:
    for rel in studio.STAGES.values():
        (tmp / rel).mkdir(parents=True, exist_ok=True)
    (tmp / "CLAUDE.md").write_text("# studio\n", encoding="utf-8")
    cfg = dict(studio.DEFAULT_CONFIG, studio_start=d(-10), payout_route_verified=True)
    cfg.update(cfg_over)
    (tmp / "management" / "config.json").write_text(json.dumps(cfg), encoding="utf-8")
    (tmp / "research" / "platform-rules.md").write_text(f"# Platform rules\n\n- **Checked:** {d(-1)}\n", encoding="utf-8")
    return tmp


def write(root: Path, rel: str, text: str) -> Path:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


BRIEF = "# Idea Brief: X\n\n- **Id:** 20261101-x\n- **Category:** 4\n\n## What it is\nx\n"
SCORE_OK = "\n## Score\n| # | Criterion | Score | Weight | Points |\n|---|---|---|---|---|\n\n**Total:** 76/100\n"
SCORE_LOW = "\n## Score\n\n**Total:** 55/100\n"


def ticket(tid: str, business: str, raised: str, by: str = "preparation", decision: str = "", blocks: str = "first publish") -> str:
    t = (f"# Approval Ticket\n\n- **Ticket:** {tid}\n- **Business:** {business}\n- **Type:** account\n"
         f"- **Raised:** {raised} by {by}\n- **Blocks:** {blocks}\n\n## What we need you to do\n1. x\n\n---\n")
    t += f"**Owner decision:** {decision}\n" if decision else "**Owner decision:** APPROVED / REJECTED / DONE — date — note\n"
    return t


def business(root: Path, slug: str, status: str = "live", launched: str | None = None, with_work=True):
    launched = launched or d(-5)
    write(root, f"businesses/{slug}/plan.md", f"# Execution Plan: {slug}\n\n- **Id:** 20261101-{slug}\n- **Status:** {status}\n- **Launched:** {launched}\n")
    if with_work:
        write(root, f"businesses/{slug}/WORK.md", f"# WORK — {slug}\n")
    write(root, f"businesses/{slug}/logbook.md", "# Logbook\n")
    write(root, f"businesses/{slug}/metrics.md", "| Date | Metric 1 | Metric 2 | Metric 3 | Source | Note |\n|---|---|---|---|---|---|\n")
    write(root, f"businesses/{slug}/ledger.md", "| Date | Item | USD out | USD in | Ticket / tier | Balance |\n|---|---|---|---|---|---|\n")


class CheckSuite(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self._tmp.name))

    def tearDown(self):
        self._tmp.cleanup()

    def run_check(self):
        return check.run(self.root)

    def errors(self, res):
        return [f["message"] for f in res["findings"] if f["level"] == "ERROR"]

    def warns(self, res):
        return [f["message"] for f in res["findings"] if f["level"] == "WARN"]

    def test_clean_skeleton_passes(self):
        res = self.run_check()
        self.assertEqual(self.errors(res), [])
        self.assertTrue(res["ok"])

    def test_missing_stage_folder_is_an_error(self):
        import shutil
        shutil.rmtree(self.root / "pipeline" / "20-planned")
        res = self.run_check()
        self.assertTrue(any("20-planned" in e for e in self.errors(res)))

    def test_scored_brief_still_in_inbox_is_an_error(self):
        write(self.root, "pipeline/00-inbox/20261101-x.md", BRIEF + SCORE_OK)
        res = self.run_check()
        self.assertTrue(any("inbox" in e and "Score" in e for e in self.errors(res)))

    def test_unscored_brief_in_approved_is_an_error(self):
        write(self.root, "pipeline/10-assessed/approved/20261101-x.md", BRIEF)
        res = self.run_check()
        self.assertTrue(any("approved" in e and "Score" in e for e in self.errors(res)))

    def test_approved_below_threshold_is_an_error(self):
        write(self.root, "pipeline/10-assessed/approved/20261101-x.md", BRIEF + SCORE_LOW)
        res = self.run_check()
        self.assertTrue(any("below" in e for e in self.errors(res)))

    def test_bad_filename_in_inbox_is_a_warning(self):
        write(self.root, "pipeline/00-inbox/My Idea.md", BRIEF)
        res = self.run_check()
        self.assertTrue(any("name" in w.lower() for w in self.warns(res)))

    def test_validation_past_deadline_is_flagged(self):
        write(self.root, "pipeline/15-validating/20261101-x-validate.md",
              f"# Validation Brief\n\n- **Id:** 20261101-x\n- **Started:** {d(-9)}  **Deadline:** {d(-2)} (7 days)\n")
        res = self.run_check()
        self.assertTrue(any("deadline" in w.lower() for w in self.warns(res)))

    def test_validation_with_final_verdict_still_in_validating_is_an_error(self):
        write(self.root, "pipeline/15-validating/20261101-x-validate.md",
              f"# Validation Brief\n\n- **Id:** 20261101-x\n- **Started:** {d(-9)}  **Deadline:** {d(-2)}\n\n## Verdict\n**Verdict:** PASSED\n")
        res = self.run_check()
        self.assertTrue(any("PASSED" in e for e in self.errors(res)))

    def test_plan_without_status_is_an_error(self):
        write(self.root, "pipeline/20-planned/20261101-x-plan.md", "# Execution Plan: x\n\n- **Id:** 20261101-x\n")
        res = self.run_check()
        self.assertTrue(any("Status" in e for e in self.errors(res)))

    def test_open_ticket_older_than_three_days_is_a_warning(self):
        write(self.root, "pipeline/30-tickets/open/20261101-x-1.md", ticket("20261101-x-1", "x", d(-4)))
        res = self.run_check()
        self.assertTrue(any("older than" in w for w in self.warns(res)))
        write(self.root, "pipeline/30-tickets/open/20261101-y-1.md", ticket("20261101-y-1", "y", d(-1)))
        res = self.run_check()
        self.assertEqual(sum("older than" in w for w in self.warns(res)), 1)

    def test_decided_ticket_in_open_is_an_error(self):
        write(self.root, "pipeline/30-tickets/open/20261101-x-1.md", ticket("20261101-x-1", "x", d(-1), decision=f"APPROVED — {d(0)} — ok"))
        res = self.run_check()
        self.assertTrue(any("closed/" in e for e in self.errors(res)))

    def test_closed_ticket_without_decision_is_an_error(self):
        write(self.root, "pipeline/30-tickets/closed/20261101-x-1.md", ticket("20261101-x-1", "x", d(-1)))
        res = self.run_check()
        self.assertTrue(any("decision" in e for e in self.errors(res)))

    def test_too_many_open_tickets_is_a_warning(self):
        for i in range(11):
            write(self.root, f"pipeline/30-tickets/open/20261101-x-{i}.md", ticket(f"20261101-x-{i}", "x", d(0)))
        res = self.run_check()
        self.assertTrue(any("open tickets" in w for w in self.warns(res)))

    def test_business_missing_work_md_is_an_error(self):
        business(self.root, "abc", with_work=False)
        res = self.run_check()
        self.assertTrue(any("WORK.md" in e for e in self.errors(res)))

    def test_live_cap_exceeded_is_an_error(self):
        cfg = json.loads((self.root / "management" / "config.json").read_text())
        cfg["phase1_live_cap"] = 2
        (self.root / "management" / "config.json").write_text(json.dumps(cfg))
        for s in ("a", "b", "c"):
            business(self.root, s)
        res = self.run_check()
        self.assertTrue(any("cap" in e for e in self.errors(res)))
        business(self.root, "c", status="stopped")
        res = self.run_check()
        self.assertFalse(any("cap" in e for e in self.errors(res)))

    def test_phase_two_cap_applies_after_ninety_days(self):
        cfg = json.loads((self.root / "management" / "config.json").read_text())
        cfg["studio_start"] = d(-100)
        cfg["phase2_live_cap"] = 1
        (self.root / "management" / "config.json").write_text(json.dumps(cfg))
        business(self.root, "a")
        business(self.root, "b")
        res = self.run_check()
        self.assertTrue(any("Phase 2" in e for e in self.errors(res)))

    def test_live_business_with_open_preparation_ticket_is_an_error(self):
        business(self.root, "abc")
        write(self.root, "pipeline/30-tickets/open/20261101-abc-1.md", ticket("20261101-abc-1", "abc", d(0), by="preparation"))
        res = self.run_check()
        self.assertTrue(any("blocking" in e for e in self.errors(res)))

    def test_live_business_with_open_work_ticket_is_only_a_warning_when_fresh(self):
        business(self.root, "abc")
        write(self.root, "pipeline/30-tickets/open/20261101-abc-2.md", ticket("20261101-abc-2", "abc", d(0), by="work"))
        res = self.run_check()
        self.assertFalse(any("blocking" in e for e in self.errors(res)))

    def test_ticket_older_than_pause_days_asks_to_pause_business(self):
        business(self.root, "abc")
        write(self.root, "pipeline/30-tickets/open/20261101-abc-2.md", ticket("20261101-abc-2", "abc", d(-8), by="work"))
        res = self.run_check()
        self.assertTrue(any("pause" in w.lower() for w in self.warns(res)))

    def test_metric_row_without_source_is_a_warning(self):
        business(self.root, "abc")
        with open(self.root / "businesses/abc/metrics.md", "a", encoding="utf-8") as fh:
            fh.write(f"| {d(0)} | 12 | 3 | 0 |  | guessed |\n")
        res = self.run_check()
        self.assertTrue(any("source" in w.lower() for w in self.warns(res)))

    def test_stale_platform_rules_is_a_warning(self):
        write(self.root, "research/platform-rules.md", f"# Platform rules\n\n- **Checked:** {d(-40)}\n")
        res = self.run_check()
        self.assertTrue(any("platform-rules" in w for w in self.warns(res)))

    def test_unverified_payout_route_with_live_business_is_a_warning(self):
        cfg = json.loads((self.root / "management" / "config.json").read_text())
        cfg["payout_route_verified"] = False
        (self.root / "management" / "config.json").write_text(json.dumps(cfg))
        business(self.root, "abc")
        res = self.run_check()
        self.assertTrue(any("payout" in w.lower() for w in self.warns(res)))

    def test_crashed_runs_and_open_breaker_are_warnings(self):
        import runlog
        for i in range(3):
            info = runlog.start(self.root, "work", business="abc")
            runlog.end(self.root, info["run_id"], outcome="bad", summary="x")
        old = (dt.datetime.now() - dt.timedelta(hours=5)).replace(microsecond=0).isoformat()
        with open(self.root / "management" / "runs.jsonl", "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"event": "start", "run_id": "planning-old", "team": "planning", "ts": old}) + "\n")
        res = self.run_check()
        self.assertTrue(any("breaker" in w.lower() for w in self.warns(res)))
        self.assertTrue(any("crash" in w.lower() or "no end" in w.lower() for w in self.warns(res)))

    def test_ledger_mismatch_is_an_error(self):
        business(self.root, "abc")
        led = ledger.Ledger(self.root)
        led.init()
        led.add(business="abc", item="sale", inc=30)
        led.close()
        with open(self.root / "businesses/abc/ledger.md", "a", encoding="utf-8") as fh:
            fh.write("| 2026-11-09 | extra | 0 | 20 | - | 50 |\n")
        res = self.run_check()
        self.assertTrue(any("ledger" in e.lower() for e in self.errors(res)))

    def test_flag_file_is_reported(self):
        business(self.root, "abc")
        write(self.root, "businesses/abc/FLAG.md", "metric 1 below kill\n")
        res = self.run_check()
        self.assertTrue(any("FLAG" in w for w in self.warns(res)))

    def test_summary_counts(self):
        write(self.root, "pipeline/00-inbox/20261101-x.md", BRIEF)
        write(self.root, "pipeline/20-planned/20261101-y-plan.md", "# Execution Plan: y\n\n- **Status:** planned\n")
        business(self.root, "abc")
        res = self.run_check()
        self.assertEqual(res["summary"]["inbox"], 1)
        self.assertEqual(res["summary"]["planned"], 1)
        self.assertEqual(res["summary"]["live"], 1)
        self.assertEqual(res["summary"]["phase"], 1)


class CheckCli(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self._tmp.name))

    def tearDown(self):
        self._tmp.cleanup()

    def run_cli(self, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check.main(["--root", str(self.root), *args])
        return code, buf.getvalue()

    def test_exit_codes(self):
        code, out = self.run_cli()
        self.assertEqual(code, 0)
        self.assertIn("CHECK OK", out)
        write(self.root, "pipeline/30-tickets/open/20261101-x-1.md", ticket("20261101-x-1", "x", d(-4)))
        code, out = self.run_cli()
        self.assertEqual(code, 0)
        self.assertIn("WARN", out)
        code, _ = self.run_cli("--strict")
        self.assertEqual(code, 1)
        write(self.root, "pipeline/20-planned/20261101-x-plan.md", "# plan\n")
        code, out = self.run_cli()
        self.assertEqual(code, 1)
        self.assertIn("ERROR", out)

    def test_json_output(self):
        code, out = self.run_cli("--json")
        data = json.loads(out)
        self.assertIn("findings", data)
        self.assertIn("summary", data)
        self.assertTrue(data["ok"])


if __name__ == "__main__":
    unittest.main()
