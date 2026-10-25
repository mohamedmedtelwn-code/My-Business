"""Tests for tools/runlog.py - run logger, lock, crash sweep, circuit breaker."""
import datetime as dt
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))

import runlog  # noqa: E402
import studio  # noqa: E402


def make_studio(tmp: Path) -> Path:
    for rel in studio.STAGES.values():
        (tmp / rel).mkdir(parents=True, exist_ok=True)
    (tmp / "CLAUDE.md").write_text("# studio\n", encoding="utf-8")
    cfg = dict(studio.DEFAULT_CONFIG, run_stale_hours=3, breaker_failures=3)
    (tmp / "management" / "config.json").write_text(json.dumps(cfg), encoding="utf-8")
    return tmp


def read_events(root: Path):
    p = root / "management" / "runs.jsonl"
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


class RunlogBasics(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self._tmp.name))

    def tearDown(self):
        self._tmp.cleanup()

    def test_start_writes_start_event_and_lock(self):
        info = runlog.start(self.root, "research", note="cycle 1")
        self.assertTrue(info["run_id"].startswith("research-"))
        ev = read_events(self.root)
        self.assertEqual(len(ev), 1)
        self.assertEqual(ev[0]["event"], "start")
        self.assertEqual(ev[0]["team"], "research")
        self.assertTrue((self.root / "management" / ".lock-research").exists())

    def test_second_start_while_locked_is_refused(self):
        runlog.start(self.root, "research")
        with self.assertRaises(runlog.RunlogError) as cm:
            runlog.start(self.root, "research")
        self.assertIn("already running", str(cm.exception))

    def test_different_teams_can_run_at_once(self):
        runlog.start(self.root, "research")
        runlog.start(self.root, "planning")  # no exception
        self.assertEqual(len(read_events(self.root)), 2)

    def test_end_records_files_touched_tickets_and_outcome_and_releases_lock(self):
        info = runlog.start(self.root, "preparation")
        (self.root / "pipeline" / "30-tickets" / "open" / "20261101-abc-1.md").write_text("# Approval Ticket\n", encoding="utf-8")
        (self.root / "pipeline" / "20-planned" / "20261101-abc-plan.md").write_text("# plan\n", encoding="utf-8")
        rec = runlog.end(self.root, info["run_id"], outcome="ok", summary="1 plan processed, 1 ticket raised")
        self.assertEqual(rec["outcome"], "ok")
        self.assertIn("pipeline/30-tickets/open/20261101-abc-1.md", rec["files_touched"]["added"])
        self.assertIn("pipeline/20-planned/20261101-abc-plan.md", rec["files_touched"]["added"])
        self.assertEqual(rec["tickets_raised"], ["20261101-abc-1"])
        self.assertFalse((self.root / "management" / ".lock-preparation").exists())
        ev = read_events(self.root)
        self.assertEqual(ev[-1]["event"], "end")
        self.assertEqual(ev[-1]["summary"], "1 plan processed, 1 ticket raised")

    def test_end_unknown_run_is_refused(self):
        with self.assertRaises(runlog.RunlogError):
            runlog.end(self.root, "research-nope", outcome="ok", summary="x")

    def test_end_rejects_unknown_outcome(self):
        info = runlog.start(self.root, "work", business="abc")
        with self.assertRaises(runlog.RunlogError):
            runlog.end(self.root, info["run_id"], outcome="fine", summary="x")

    def test_work_runs_carry_business_slug(self):
        info = runlog.start(self.root, "work", business="abc")
        rec = runlog.end(self.root, info["run_id"], outcome="ok", summary="posted")
        self.assertEqual(rec["business"], "abc")


class CrashSweepAndBreaker(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self._tmp.name))
        self.log = self.root / "management" / "runs.jsonl"

    def tearDown(self):
        self._tmp.cleanup()

    def _append(self, obj):
        with open(self.log, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(obj) + "\n")

    def test_old_start_without_end_is_marked_crashed_on_next_start(self):
        old = (dt.datetime.now() - dt.timedelta(hours=5)).replace(microsecond=0).isoformat()
        self._append({"event": "start", "run_id": "planning-old", "team": "planning", "ts": old, "note": ""})
        runlog.start(self.root, "research")
        ev = read_events(self.root)
        crashed = [e for e in ev if e["event"] == "end" and e["run_id"] == "planning-old"]
        self.assertEqual(len(crashed), 1)
        self.assertEqual(crashed[0]["outcome"], "crashed")

    def test_recent_start_without_end_is_left_alone(self):
        recent = (dt.datetime.now() - dt.timedelta(minutes=10)).replace(microsecond=0).isoformat()
        self._append({"event": "start", "run_id": "planning-recent", "team": "planning", "ts": recent, "note": ""})
        runlog.start(self.root, "research")
        ev = read_events(self.root)
        self.assertFalse(any(e["event"] == "end" and e["run_id"] == "planning-recent" for e in ev))

    def test_stale_lock_is_cleared(self):
        old = (dt.datetime.now() - dt.timedelta(hours=5)).replace(microsecond=0).isoformat()
        (self.root / "management" / ".lock-research").write_text(json.dumps({"run_id": "research-old", "team": "research", "start": old}), encoding="utf-8")
        info = runlog.start(self.root, "research")  # must not raise
        self.assertNotEqual(info["run_id"], "research-old")

    def test_three_failures_open_the_breaker_and_reset_closes_it(self):
        for i in range(3):
            info = runlog.start(self.root, "work", business="abc")
            runlog.end(self.root, info["run_id"], outcome="bad", summary=f"fail {i}")
        with self.assertRaises(runlog.RunlogError) as cm:
            runlog.start(self.root, "work", business="abc")
        self.assertIn("circuit", str(cm.exception).lower())
        st = runlog.status(self.root)
        self.assertTrue(st["work"]["breaker_open"])
        runlog.reset(self.root, "work")
        info = runlog.start(self.root, "work", business="abc")
        self.assertTrue(info["run_id"])
        self.assertFalse(runlog.status(self.root)["work"]["breaker_open"])

    def test_success_resets_failure_count(self):
        for outcome in ("bad", "bad", "ok", "bad", "bad"):
            info = runlog.start(self.root, "planning")
            runlog.end(self.root, info["run_id"], outcome=outcome, summary=outcome)
        runlog.start(self.root, "planning")  # only 2 consecutive failures: allowed

    def test_status_summarises_last_run_per_team(self):
        info = runlog.start(self.root, "research")
        runlog.end(self.root, info["run_id"], outcome="warn", summary="3 briefs")
        st = runlog.status(self.root)
        self.assertEqual(st["research"]["last_outcome"], "warn")
        self.assertEqual(st["research"]["last_summary"], "3 briefs")
        self.assertEqual(st["planning"]["last_outcome"], None)


class GitCommit(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self._tmp.name))

    def tearDown(self):
        self._tmp.cleanup()

    @unittest.skipIf(shutil.which("git") is None, "git not installed")
    def test_end_with_commit_creates_a_git_commit(self):
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "--allow-empty", "-m", "init"], cwd=self.root, check=True)
        info = runlog.start(self.root, "research")
        (self.root / "pipeline" / "00-inbox" / "20261101-idea.md").write_text("# Idea Brief\n", encoding="utf-8")
        runlog.end(self.root, info["run_id"], outcome="ok", summary="one brief", commit=True)
        log = subprocess.run(["git", "log", "--oneline"], cwd=self.root, capture_output=True, text=True, check=True).stdout
        self.assertIn("run(research)", log)


if __name__ == "__main__":
    unittest.main()
