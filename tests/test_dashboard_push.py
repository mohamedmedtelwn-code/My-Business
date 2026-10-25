"""Tests for tools/dashboard_push.py - ArtifactData batch payload."""
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

import dashboard_push as dp  # noqa: E402
import ledger  # noqa: E402
import runlog  # noqa: E402
import studio  # noqa: E402

TODAY = dt.date.today()
URL = "https://claude.ai/artifact/TESTID"


def d(days):
    return (TODAY + dt.timedelta(days=days)).isoformat()


def write(root, rel, text):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def make_studio(tmp: Path) -> Path:
    for rel in studio.STAGES.values():
        (tmp / rel).mkdir(parents=True, exist_ok=True)
    write(tmp, "CLAUDE.md", "# studio\n")
    write(tmp, "management/config.json", json.dumps(dict(studio.DEFAULT_CONFIG, studio_start=d(-20), payout_route_verified=True)))
    write(tmp, "management/dashboard-url.txt", URL + "\n")
    write(tmp, "research/platform-rules.md", f"- **Checked:** {d(-1)}\n")
    # pipeline
    write(tmp, "pipeline/00-inbox/20261101-a.md", "# Idea Brief: A\n\n- **Id:** 20261101-a\n")
    write(tmp, "pipeline/00-inbox/20261101-b.md", "# Idea Brief: B\n\n- **Id:** 20261101-b\n")
    write(tmp, "pipeline/10-assessed/approved/20261101-c.md", "# Idea Brief: C\n\n## Score\n\n**Total:** 80/100\n")
    write(tmp, "pipeline/20-planned/20261101-d-plan.md", "# Execution Plan: D\n\n- **Status:** planned\n")
    # business
    write(tmp, "businesses/abc/plan.md",
          "# Execution Plan: ABC claim pack\n\n- **Id:** 20261101-abc\n- **Category:** 10 Professional tooling\n- **Status:** live\n"
          f"- **Launched:** {d(-10)}\n\n## Metrics and thresholds\n| Metric | Source | Kill below | Scale above | Check |\n|---|---|---|---|---|\n"
          "| Sales | Gumroad | 1 | 10 | weekly |\n| Visitors | Gumroad analytics | 50 | 500 | weekly |\n| Replies | outreach log | 2 | 20 | weekly |\n")
    write(tmp, "businesses/abc/WORK.md", "# WORK\n")
    write(tmp, "businesses/abc/metrics.md",
          "| Date | Sales | Visitors | Replies | Source | Note |\n|---|---|---|---|---|---|\n"
          f"| {d(-3)} | 0 | 40 | 1 | gumroad export | |\n| {d(-1)} | 2 | 120 | 5 | gumroad export | |\n")
    # tickets
    write(tmp, "pipeline/30-tickets/open/20261101-abc-2.md",
          f"# Approval Ticket\n\n- **Ticket:** 20261101-abc-2\n- **Business:** abc\n- **Type:** publish\n- **Raised:** {d(-1)} by work\n- **Blocks:** publish\n\n## What we need you to do\n1. Open Gumroad\n2. Press publish\n\n---\n**Owner decision:** APPROVED / REJECTED / DONE — date — note\n")
    write(tmp, "pipeline/30-tickets/closed/20261101-abc-1.md",
          f"# Investment Ticket\n\n- **Ticket:** 20261101-abc-1\n- **Business:** abc\n- **Amount requested:** USD 40  (Tier 0)\n- **Raised:** {d(-6)} by preparation\n\n---\n**Owner decision:** APPROVED USD 40 — {d(-5)} — ok\n")
    # ledger
    led = ledger.Ledger(tmp)
    led.init()
    led.release(ticket="20261101-abc-1", business="abc", amount=40, date=d(-5))
    led.add(business="abc", item="domain", out=12, source="ceiling", ticket="20261101-abc-1", tier="0", date=d(-4))
    led.add(business="abc", item="first sale", inc=29, date=d(-1))
    led.close()
    # runs
    info = runlog.start(tmp, "research", note="cycle")
    runlog.end(tmp, info["run_id"], outcome="ok", summary="5 briefs written")
    info = runlog.start(tmp, "work", business="abc")
    runlog.end(tmp, info["run_id"], outcome="warn", summary="posted, waiting on publish ticket")
    return tmp


class Payload(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = make_studio(Path(self._tmp.name))
        self.payload = dp.build(self.root)
        self.writes = [w for b in self.payload["batches"] for w in b["writes"]]

    def tearDown(self):
        self._tmp.cleanup()

    def doc(self, collection, doc_id):
        for w in self.writes:
            if w["collection"] == collection and w["doc_id"] == doc_id:
                return w
        return None

    def test_batches_use_the_dashboard_url_and_batch_action(self):
        self.assertTrue(self.payload["batches"])
        for b in self.payload["batches"]:
            self.assertEqual(b["action"], "batch")
            self.assertEqual(b["url"], URL)
            self.assertLessEqual(len(b["writes"]), 50)

    def test_summary_doc_matches_ledger_and_pipeline(self):
        w = self.doc("studio", "summary")
        self.assertEqual(w["op"], "set")
        data = w["data"]
        self.assertEqual(data["capital"], {"ceiling": 1000, "released": 40, "spent": 12, "revenue": 29, "pool": 29})
        self.assertEqual(data["pipeline"], {"inbox": 2, "assessed": 1, "planned": 1, "tickets_open": 1})
        self.assertEqual(data["businesses"], {"live": 1, "paused": 0, "stopped": 0})
        self.assertRegex(data["updated"], r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}")

    def test_team_docs_for_all_five_teams(self):
        for team in studio.TEAMS:
            self.assertIsNotNone(self.doc("teams", team), team)
        r = self.doc("teams", "research")["data"]
        self.assertEqual(r["status"], "ok")
        self.assertEqual(r["summary"], "5 briefs written")
        self.assertTrue(r["last_run"])
        self.assertEqual(r["next_run"], studio.DEFAULT_CONFIG["team_cadence"]["research"])
        self.assertEqual(self.doc("teams", "work")["data"]["status"], "warn")
        self.assertEqual(self.doc("teams", "planning")["data"]["status"], "idle")

    def test_business_doc(self):
        b = self.doc("businesses", "abc")["data"]
        self.assertEqual(b["name"], "ABC claim pack")
        self.assertEqual(b["category"], "10 Professional tooling")
        self.assertEqual(b["status"], "live")
        self.assertEqual(b["days_live"], 10)
        self.assertEqual(b["spent"], 12)
        self.assertEqual(b["revenue"], 29)
        self.assertFalse(b["flag"])
        self.assertEqual(b["rag"], "amber")  # between kill and scale
        self.assertEqual([m["name"] for m in b["metrics"]], ["Sales", "Visitors", "Replies"])
        self.assertEqual(b["metrics"][0], {"name": "Sales", "value": 2, "kill": 1, "scale": 10})
        self.assertTrue(b["last_run"])

    def test_rag_red_when_below_kill_or_flagged_and_green_when_all_above_scale(self):
        write(self.root, "businesses/abc/metrics.md",
              "| Date | Sales | Visitors | Replies | Source | Note |\n|---|---|---|---|---|---|\n| 2026-11-09 | 0 | 120 | 5 | x | |\n")
        self.assertEqual(dp.business_doc(self.root, "abc", {}, None)["rag"], "red")
        write(self.root, "businesses/abc/metrics.md",
              "| Date | Sales | Visitors | Replies | Source | Note |\n|---|---|---|---|---|---|\n| 2026-11-09 | 12 | 600 | 25 | x | |\n")
        self.assertEqual(dp.business_doc(self.root, "abc", {}, None)["rag"], "green")
        write(self.root, "businesses/abc/FLAG.md", "kill crossed\n")
        b = dp.business_doc(self.root, "abc", {}, None)
        self.assertEqual(b["rag"], "red")
        self.assertTrue(b["flag"])

    def test_ticket_docs(self):
        o = self.doc("tickets", "20261101-abc-2")["data"]
        self.assertEqual(o["status"], "open")
        self.assertEqual(o["type"], "approval")
        self.assertEqual(o["business"], "abc")
        self.assertEqual(o["raised"], d(-1))
        self.assertEqual(o["steps"], ["Open Gumroad", "Press publish"])
        self.assertEqual(o["blocks"], "publish")
        c = self.doc("tickets", "20261101-abc-1")["data"]
        self.assertEqual(c["status"], "closed")
        self.assertEqual(c["type"], "investment")
        self.assertEqual(c["amount"], 40)

    def test_ledger_docs_one_per_entry(self):
        docs = [w for w in self.writes if w["collection"] == "ledger"]
        self.assertEqual(len(docs), 3)  # release, spend, revenue
        spend = next(w["data"] for w in docs if w["data"]["item"] == "domain")
        self.assertEqual(spend["out"], 12)
        self.assertEqual(spend["in"], 0)
        self.assertEqual(spend["tier"], "0")
        self.assertEqual(spend["business"], "abc")

    def test_activity_docs_from_run_log(self):
        docs = [w for w in self.writes if w["collection"] == "activity"]
        self.assertEqual(len(docs), 2)
        self.assertTrue(all(w["doc_id"].endswith(("-research", "-work")) for w in docs))
        a = docs[0]["data"]
        self.assertIn("team", a)
        self.assertIn("text", a)
        self.assertRegex(a["ts"], r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}")

    def test_versions_dir_adds_if_version(self):
        vdir = self.root / "management" / ".dashboard-state"
        write(self.root, "management/.dashboard-state/studio/summary.json", json.dumps({"version": 7, "data": {}}))
        payload = dp.build(self.root, versions_dir=vdir)
        writes = [w for b in payload["batches"] for w in b["writes"]]
        s = next(w for w in writes if w["collection"] == "studio")
        self.assertEqual(s["if_version"], 7)
        t = next(w for w in writes if w["collection"] == "teams")
        self.assertNotIn("if_version", t)

    def test_versions_sidecar_is_used_when_files_hold_only_data(self):
        write(self.root, "management/.dashboard-state/teams/research.json", json.dumps({"status": "idle"}))
        write(self.root, "management/.dashboard-state/versions.json", json.dumps({"teams/research": 4, "studio/summary": 2}))
        payload = dp.build(self.root, versions_dir=self.root / "management" / ".dashboard-state")
        writes = [w for b in payload["batches"] for w in b["writes"]]
        self.assertEqual(next(w for w in writes if w["doc_id"] == "research")["if_version"], 4)
        self.assertEqual(next(w for w in writes if w["doc_id"] == "summary")["if_version"], 2)
        self.assertNotIn("if_version", next(w for w in writes if w["doc_id"] == "planning"))

    def test_ticket_title_is_actionable_when_heading_is_generic(self):
        o = self.doc("tickets", "20261101-abc-2")["data"]
        self.assertEqual(o["title"], "Publish for abc: Open Gumroad")

    def test_versions_dir_prunes_activity_beyond_200(self):
        for i in range(205):
            write(self.root, f"management/.dashboard-state/activity/2026010{i // 100}-{i % 100:02d}00-x.json", json.dumps({"version": 1, "data": {"ts": f"2026-01-0{i // 100} {i % 100:02d}:00"}}))
        payload = dp.build(self.root, versions_dir=self.root / "management" / ".dashboard-state")
        deletes = [w for b in payload["batches"] for w in b["writes"] if w["op"] == "delete"]
        self.assertTrue(len(deletes) >= 5)

    def test_many_writes_are_chunked(self):
        led = ledger.Ledger(self.root)
        for i in range(60):
            led.add(business="abc", item=f"sale {i}", inc=1, date=d(0))
        led.close()
        payload = dp.build(self.root)
        self.assertGreater(len(payload["batches"]), 1)
        self.assertTrue(all(len(b["writes"]) <= 50 for b in payload["batches"]))

    def test_cli_prints_json(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = dp.main(["--root", str(self.root)])
        self.assertEqual(code, 0)
        data = json.loads(buf.getvalue())
        self.assertIn("batches", data)
        self.assertEqual(data["url"], URL)


if __name__ == "__main__":
    unittest.main()
