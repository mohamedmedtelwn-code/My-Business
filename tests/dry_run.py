#!/usr/bin/env python3
"""Dry run: walk three fixture idea briefs through the whole pipeline with the tools.

No web access, no real tickets. Everything happens in a scratch copy of the
studio (default tests/.dryrun/, ignored by git), so the real folder is untouched.

  python tests/dry_run.py            # run; prints each stage, ends with check.py and a dashboard payload
  python tests/dry_run.py --keep     # keep the scratch folder for inspection (default deletes it on success)

Fixtures (tests/fixtures/):
  20261101-gulf-fidic-claim-pack   strong: passes the gates, scores 76 with the edge bonus, validates with 3 SU,
                                   gets a plan, tickets, a launch, a sale
  20261101-faceless-shorts-history fails gate 5 (mass-produced content on a platform that penalises it)
  20261101-p6-dcma-health-report   borderline: scores 71, approved, but validation parks it (1 SU from 50 messages)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(REPO / "tools"))

import check  # noqa: E402
import dashboard_push  # noqa: E402
import ledger  # noqa: E402
import rubric  # noqa: E402
import runlog  # noqa: E402
import signals  # noqa: E402
import studio  # noqa: E402

TODAY = dt.date.today()


def d(days: int) -> str:
    return (TODAY + dt.timedelta(days=days)).isoformat()


def say(msg: str) -> None:
    print(msg, flush=True)


def write(root: Path, rel: str, text: str) -> Path:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    studio.write_text(p, text)
    return p


def must_pass(root: Path, stage: str) -> dict:
    res = check.run(root)
    errs = [f for f in res["findings"] if f["level"] == "ERROR"]
    if errs:
        for f in errs:
            say(f"  ERROR [{f['where']}] {f['message']}")
        raise SystemExit(f"check.py failed after {stage}")
    warns = [f for f in res["findings"] if f["level"] == "WARN"]
    say(f"  check.py after {stage}: OK, {len(warns)} warning(s)")
    return res


# ---------------------------------------------------------------------------
def make_scratch(root: Path) -> None:
    if root.exists():
        shutil.rmtree(root)
    for rel in studio.STAGES.values():
        (root / rel).mkdir(parents=True, exist_ok=True)
    (root / "pipeline" / "15-validating" / "output").mkdir(parents=True, exist_ok=True)
    (root / "research" / "playbooks").mkdir(parents=True, exist_ok=True)
    shutil.copy(REPO / "CLAUDE.md", root / "CLAUDE.md")
    shutil.copy(REPO / "research" / "platform-rules.md", root / "research" / "platform-rules.md")
    cfg = json.loads(studio.read_text(REPO / "management" / "config.json"))
    cfg["studio_start"] = d(-20)
    write(root, "management/config.json", json.dumps(cfg, indent=2))
    write(root, "management/dashboard-url.txt", "https://claude.ai/artifact/DRYRUN\n")
    write(root, "research/feedback.md", "# Feedback to Research and Planning\n\n")
    for fx in sorted((HERE / "fixtures").glob("*.md")):
        shutil.copy(fx, root / studio.STAGES["inbox"] / fx.name)
    ledger.Ledger(root).init()


def stage_planning(root: Path) -> None:
    say("\n== Planning run 1: gates, scores, validation briefs ==")
    run = runlog.start(root, "planning", note="dry run")
    inbox = root / studio.STAGES["inbox"]
    cfg = studio.load_config(root)
    # 1. gate failure
    p = inbox / "20261101-faceless-shorts-history.md"
    text = studio.read_text(p) + ("\n## Rejected: gate 5\nTemplated AI-narrated Shorts are the profile named by YouTube's "
                                  "inauthentic-content policy (research/platform-rules.md); evidence is two tool vendors (gate 3).\n")
    studio.write_text(root / studio.STAGES["rejected"] / p.name, text)
    p.unlink()
    say("  faceless-shorts-history -> rejected (gate 5, gate 3)")
    # 2. strong brief
    p = inbox / "20261101-gulf-fidic-claim-pack.md"
    r = rubric.score([3, 5, 4, 4, 3, 3, 2, 4], cfg, edge=True, notes=[
        "price anchors from three platform pages, no sales distribution", "USD 0 on Gumroad",
        "direct outreach to named planners; Gumroad pays QAR", "agent drafts, owner reviews legal statements",
        "about 2 h review a week", "Softedemy utilities sell at USD 15-90; no median", "two channels, both outreach-based",
        "Gumroad allowed; not legal advice disclaimer"])
    assert r["approved"], r
    studio.write_text(root / studio.STAGES["approved"] / p.name, studio.read_text(p) + "\n" + rubric.render(r))
    p.unlink()
    say(f"  gulf-fidic-claim-pack -> approved ({r['total']}/100, edge bonus)")
    # 3. borderline brief
    p = inbox / "20261101-p6-dcma-health-report.md"
    r2 = rubric.score([3, 5, 3, 4, 4, 3, 2, 4], cfg, edge=False, notes=[
        "price anchors, free substitutes", "USD 0", "build then outreach: 1-3 months", "agent builds and lists",
        "about 1 h a week", "USD 50-400, no median", "two channels", "Gumroad allowed; LGPL parser"])
    assert r2["approved"] and r2["total"] < 75, r2
    studio.write_text(root / studio.STAGES["approved"] / p.name, studio.read_text(p) + "\n" + rubric.render(r2))
    p.unlink()
    say(f"  p6-dcma-health-report -> approved, borderline ({r2['total']}/100)")
    # validation briefs, dated so that they are due today
    for slug, title in (("gulf-fidic-claim-pack", "Bilingual Gulf FIDIC claim pack"), ("p6-dcma-health-report", "XER to DCMA-14 health report")):
        write(root, f"pipeline/15-validating/output/20261101-{slug}/outreach-list.md", "# 50 planning engineers at GCC contractors (public LinkedIn profiles)\n")
        write(root, f"pipeline/15-validating/20261101-{slug}-validate.md",
              f"# Validation Brief: {title}\n\n- **Id:** 20261101-{slug}\n- **Started:** {d(-8)}  **Deadline:** {d(-1)} (7 days)\n"
              f"- **Test:** outreach\n- **Extended:** no\n- **Cost:** USD 0\n\n## The test\n50 personalised LinkedIn messages; list and message in output/20261101-{slug}/.\n\n"
              f"## Denominator (update as the test runs)\n- **Messages sent:** 0\n- **Visitors:** 0\n- **Asks:** 0\n\n"
              f"## Owner steps (ticket raised if any)\n1. none (owner sends the messages from the list)\n\n"
              f"## Signals\n| Date | Type | Who / what | Source |\n|------|------|-----------|--------|\n")
    say("  two validation briefs written (outreach, 7 days)")
    must_pass(root, "planning run 1")
    runlog.end(root, run["run_id"], outcome="ok", summary="3 assessed: 2 approved, 1 rejected; 2 validations started")


def stage_validation(root: Path) -> None:
    say("\n== Planning run 2: validation deadlines reached ==")
    run = runlog.start(root, "planning", note="dry run: close validations")
    cfg = studio.load_config(root)
    strong = root / studio.STAGES["validating"] / "20261101-gulf-fidic-claim-pack-validate.md"
    text = studio.read_text(strong).replace("**Messages sent:** 0", "**Messages sent:** 50")
    text += (f"| {d(-5)} | intent | contracts manager at a Doha subcontractor asked for the price | output/20261101-gulf-fidic-claim-pack/reply-1.txt |\n"
             f"| {d(-3)} | intent | planner in Riyadh asked for the Arabic sample | output/20261101-gulf-fidic-claim-pack/reply-2.txt |\n"
             f"| {d(-2)} | call | 20-minute call booked with a UAE contracts engineer | output/20261101-gulf-fidic-claim-pack/call-1.txt |\n"
             f"| {d(-2)} | like | 14 post likes | output/20261101-gulf-fidic-claim-pack/likes.png |\n")
    studio.write_text(strong, text)
    v = signals.write_verdict(strong, cfg)
    assert v["verdict"] == "PASSED", v
    shutil.move(str(strong), str(root / studio.STAGES["passed"] / strong.name))
    say(f"  gulf-fidic-claim-pack: {v['su']:g} SU from 50 messages -> PASSED (likes ignored)")
    border = root / studio.STAGES["validating"] / "20261101-p6-dcma-health-report-validate.md"
    text = studio.read_text(border).replace("**Messages sent:** 0", "**Messages sent:** 50")
    text += f"| {d(-4)} | intent | one freelance planner asked if it handles XER 23 | output/20261101-p6-dcma-health-report/reply-1.txt |\n"
    studio.write_text(border, text)
    v2 = signals.write_verdict(border, cfg)
    assert v2["verdict"] == "PARKED", v2
    shutil.move(str(border), str(root / studio.STAGES["parked"] / border.name))
    studio.append_text(root / "research" / "feedback.md", f"- {d(0)}: p6-dcma-health-report parked: 1 SU from 50 messages; free DCMA workbooks compete.\n")
    say(f"  p6-dcma-health-report: {v2['su']:g} SU from 50 messages -> PARKED")
    # plan for the passed idea
    write(root, "pipeline/20-planned/20261101-gulf-fidic-claim-pack-plan.md",
          "# Execution Plan: Bilingual Gulf FIDIC claim pack\n\n- **Id:** 20261101-gulf-fidic-claim-pack\n"
          "- **Brief:** pipeline/10-assessed/approved/20261101-gulf-fidic-claim-pack.md\n"
          "- **Validation:** pipeline/15-validating/passed/20261101-gulf-fidic-claim-pack-validate.md (3 SU from 50 messages)\n"
          "- **Score:** 76/100\n- **Category:** 10 Professional tooling and expertise products\n- **Funding tier:** 0\n- **Status:** planned\n- **Launched:** \n\n"
          "## Goal and first milestone\nLaunched = pack listed on Gumroad; first dollar = first stranger purchase within 14 days.\n\n"
          "## Offer and price guard\nUSD 49; minimum USD 29; maximum discount 40%; maximum refund USD 49.\n\n"
          "## Tools, accounts, access\n| Item | Needed for | Who sets it up | Cost |\n|---|---|---|---|\n| Gumroad account | selling | owner | 0 |\n| Domain for landing page | optional | owner pays | 12 |\n\n"
          "## Capital (itemised)\n| Item | USD | When |\n|---|---|---|\n| Domain | 12 | week 2 |\n**Total ask:** USD 12  (Tier 0)\n**Zero-capital path:** sell from the Gumroad page without a domain.\n\n"
          "## First 14 days\n| Day | Action | Who | Output |\n|---|---|---|---|\n| 1 | Draft pack v1 | agent | output/ |\n| 3 | Legal review | owner | notes |\n| 5 | Listing live | owner publishes | ticket |\n\n"
          "## Work schedule\nDaily 08:00, 30 minutes, 10 messages per run (max 20 a day).\n\n"
          "## Distribution and channel mix\nChannel 1: LinkedIn outreach (60%). Channel 2: Arabic P6 YouTube and Telegram groups with a free sample (40%).\n\n"
          "## Owner edge used\nEOT claim preparation; +1 Durability, +1 Earnings ceiling.\n\n"
          "## Metrics and thresholds\n| Metric | Source | Kill below | Scale above | Check |\n|---|---|---|---|---|\n"
          "| Sales | Gumroad sales export | 1 | 10 | weekly |\n| Visitors | Gumroad analytics | 50 | 500 | weekly |\n| Replies | outreach log | 2 | 20 | weekly |\n\n"
          "## Risks and compliance\nNot legal advice; disclaimer on the listing. No platform caps apply.\n\n## Portfolio conflicts\nNone.\n\n## Exit\nUnpublish the listing; refund open orders; keep the drafts.\n")
    say("  plan written for gulf-fidic-claim-pack")
    must_pass(root, "planning run 2")
    runlog.end(root, run["run_id"], outcome="ok", summary="validations: 1 passed, 1 parked; 1 plan written")


def ticket_text(tid: str, business: str, kind: str, raised_by: str, blocks: str, title: str, amount: float | None = None) -> str:
    head = "# Investment Ticket" if amount and amount >= 50 else "# Approval Ticket"
    lines = [head, "", f"- **Ticket:** {tid}", f"- **Business:** {business}", f"- **Type:** {kind}",
             f"- **Raised:** {d(0)} by {raised_by}", f"- **Blocks:** {blocks}"]
    if amount is not None:
        lines.append(f"- **Amount requested:** USD {amount:g}  (Tier 0)")
    lines += ["", "## What we need you to do", f"1. {title}", "", "## Why", "Dry run.", "", "## After you're done", "The agent continues.", "", "---",
              "**Owner decision:** APPROVED / REJECTED / DONE — date — note", ""]
    return "\n".join(lines)


def owner_decides(root: Path, tid: str, decision: str) -> None:
    src = root / studio.STAGES["tickets_open"] / f"{tid}.md"
    text = studio.read_text(src).replace("**Owner decision:** APPROVED / REJECTED / DONE — date — note",
                                         f"**Owner decision:** {decision} — {d(0)} — dry run")
    studio.write_text(root / studio.STAGES["tickets_closed"] / src.name, text)
    src.unlink()


def stage_preparation(root: Path) -> None:
    say("\n== Preparation run: tickets, ledger release, launch ==")
    run = runlog.start(root, "preparation", note="dry run")
    slug = "gulf-fidic-claim-pack"
    open_dir = studio.STAGES["tickets_open"]
    write(root, f"{open_dir}/20261101-studio-1.md", ticket_text("20261101-studio-1", "studio", "legal", "preparation", "accepting money", "Confirm the legal basis for receiving income (management/payments.md)"))
    write(root, f"{open_dir}/20261101-studio-2.md", ticket_text("20261101-studio-2", "studio", "account", "preparation", "accepting money", "Set up payout route 1: Gumroad (management/payments.md steps)"))
    write(root, f"{open_dir}/20261101-{slug}-1.md", ticket_text(f"20261101-{slug}-1", slug, "account", "preparation", "first publish", "Open the Gumroad listing with the draft in output/"))
    write(root, f"{open_dir}/20261101-{slug}-2.md", ticket_text(f"20261101-{slug}-2", slug, "money", "preparation", "nothing", "Pay USD 12 for the domain", amount=12))
    say("  4 tickets raised (legal basis, Gumroad route, listing, USD 12 domain)")
    res = check.run(root)
    say(f"  check.py with tickets open: {res['errors']} error(s), {res['warnings']} warning(s) (plan not launched yet, so no blocking error)")
    # the owner acts (simulated): everything approved
    for tid, decision in (("20261101-studio-1", "DONE"), ("20261101-studio-2", "DONE"), (f"20261101-{slug}-1", "DONE"), (f"20261101-{slug}-2", "APPROVED USD 12")):
        owner_decides(root, tid, decision)
    cfg_path = root / "management" / "config.json"
    cfg = json.loads(studio.read_text(cfg_path))
    cfg["payout_route_verified"] = True
    studio.write_text(cfg_path, json.dumps(cfg, indent=2))
    say("  owner closed all four tickets; payout route marked verified")
    led = ledger.Ledger(root)
    try:
        led.release(ticket=f"20261101-{slug}-2", business=slug, amount=12)
        led.add(business=slug, item="domain registration", out=12, source="ceiling", ticket=f"20261101-{slug}-2", tier="0")
        refused = []
        for attempt, kw in (("spend beyond the release", dict(business=slug, item="ads", out=5, source="ceiling", ticket=f"20261101-{slug}-2", tier="0")),
                            ("spend from the empty pool", dict(business=slug, item="tool", out=5, source="pool", ticket=f"20261101-{slug}-2", tier="0")),
                            ("spend on an unreleased ticket", dict(business=slug, item="ads", out=5, source="ceiling", ticket="20261101-nope-9", tier="0"))):
            try:
                led.add(**kw)
            except ledger.LedgerError as e:
                refused.append(f"{attempt}: {e}")
        assert len(refused) == 3, refused
        for r in refused:
            say(f"  ledger refused {r.split(':')[0]}")
        rep = led.report()
    finally:
        led.close()
    say(f"  ledger: released {rep['released']:g}, spent {rep['spent']:g}, pool {rep['pool']:g}")
    # launch
    plan_src = root / studio.STAGES["planned"] / f"20261101-{slug}-plan.md"
    biz = root / "businesses" / slug
    biz.mkdir(parents=True)
    text = studio.read_text(plan_src).replace("- **Status:** planned", "- **Status:** live").replace("- **Launched:** \n", f"- **Launched:** {d(0)}\n")
    studio.write_text(biz / "plan.md", text)
    plan_src.unlink()
    write(root, f"businesses/{slug}/WORK.md", f"# WORK — {slug}\nRun cadence: daily 08:00\nTime budget per run: 30 min\nOutbound cap: 10 per run\n"
          "Platform rules to re-check monthly: Gumroad row\nPrice guard: min USD 29, max discount 40%, max refund USD 49\n\nEach run:\n"
          f"0. python tools/check.py; python tools/runlog.py start --team work --business {slug}\n1. Send 10 messages from the list\n2. Answer replies\n"
          f"3. python tools/ledger.py add --business {slug} ...\n4. Update metrics.md, append logbook.md\n5. python tools/check.py; python tools/runlog.py end ...\nStop and ticket if: a buyer asks for legal advice\n")
    write(root, f"businesses/{slug}/logbook.md", "# Logbook\n")
    write(root, f"businesses/{slug}/metrics.md", "| Date | Sales | Visitors | Replies | Source | Note |\n|------|-------|----------|---------|--------|------|\n")
    led = ledger.Ledger(root)
    try:
        led.render_all_businesses()  # the pre-launch domain spend now shows in businesses/<slug>/ledger.md
    finally:
        led.close()
    write(root, f"{open_dir}/20261101-{slug}-3.md", ticket_text(f"20261101-{slug}-3", slug, "schedule", "preparation", "nothing", "Create the scheduled Work task from SCHEDULE.md"))
    say(f"  business launched: businesses/{slug}/ (Status live, Launched {d(0)}); schedule ticket raised (blocks nothing)")
    must_pass(root, "preparation")
    runlog.end(root, run["run_id"], outcome="ok", summary="1 plan processed, 5 tickets raised, 1 business launched")


def stage_work(root: Path) -> None:
    say("\n== Work runs: two days of operating the business ==")
    slug = "gulf-fidic-claim-pack"
    for day, (sales, visitors, replies, sale) in enumerate(((0, 38, 3, None), (1, 95, 7, 49.0)), start=1):
        run = runlog.start(root, "work", business=slug, note=f"dry run day {day}")
        write(root, f"businesses/{slug}/output/{d(0).replace('-', '')}/messages-day{day}.md", f"# 10 messages sent on day {day}\n")
        if sale:
            led = ledger.Ledger(root)
            try:
                led.add(business=slug, item="Gumroad sale: claim pack", inc=sale)
            finally:
                led.close()
        studio.append_text(root / "businesses" / slug / "metrics.md",
                           f"| {d(0)} | {sales} | {visitors} | {replies} | output/{d(0).replace('-', '')}/gumroad-export-day{day}.csv | |\n")
        studio.append_text(root / "businesses" / slug / "logbook.md",
                           f"\n## {d(0)} (run {run['run_id']})\n- Did: sent 10 messages, answered {replies} replies\n- Outputs: output/{d(0).replace('-', '')}/\n"
                           f"- Metrics: sales {sales}, visitors {visitors}, replies {replies}\n- Money: USD in {sale or 0:g} / out 0\n- Problems: none\n- Next run: follow up day-3 replies\n")
        runlog.end(root, run["run_id"], outcome="ok", summary=f"day {day}: 10 messages, {replies} replies" + (f", first sale USD {sale:g}" if sale else ""))
        say(f"  day {day}: metrics recorded with sources" + (f"; sale USD {sale:g} in the ledger" if sale else ""))
    must_pass(root, "work")


def stage_management(root: Path) -> dict:
    say("\n== Management run: reconcile, report, dashboard payload ==")
    run = runlog.start(root, "management", note="dry run nightly")
    led = ledger.Ledger(root)
    try:
        ok, issues = led.reconcile()
        rep = led.report()
    finally:
        led.close()
    assert ok, issues
    say(f"  ledger reconciled: business ledgers match; ceiling {rep['ceiling']:g}, released {rep['released']:g}, spent {rep['spent']:g}, revenue {rep['revenue']:g}, pool {rep['pool']:g}")
    st = runlog.status(root)
    say("  runs: " + ", ".join(f"{t} {v['last_outcome'] or 'idle'}" for t, v in st.items()))
    res = check.run(root)
    s = res["summary"]
    write(root, "management/dashboard.md",
          f"# Dashboard — {studio.now()} (dry run)\n\nCapital: ceiling {rep['ceiling']:g} · released {rep['released']:g} · spent {rep['spent']:g} · revenue {rep['revenue']:g} · pool {rep['pool']:g}\n"
          f"Pipeline: inbox {s['inbox']} · assessed {s['assessed']} · validating {s['validating']} (passed {s['passed']}, parked {s['parked']}) · planned {s['planned']} · tickets open {s['tickets_open']}\n"
          f"Businesses: live {s['live']} · paused {s['paused']} · stopped {s['stopped']} (Phase {s['phase']}, cap {s['live_cap']})\n\n## Needs owner\n"
          + "".join(f"- {f['message']}\n" for f in res["findings"] if f["level"] == "WARN") + "\n")
    payload = dashboard_push.build(root)
    write(root, "management/dashboard-payload.json", json.dumps(payload, indent=2))
    runlog.end(root, run["run_id"], outcome="ok", summary=f"dashboard refreshed; {res['warnings']} warning(s); {payload['writes']} dashboard writes")
    must_pass(root, "management")
    return payload


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(HERE / ".dryrun"), help="scratch folder (default tests/.dryrun)")
    ap.add_argument("--keep", action="store_true", help="keep the scratch folder after a successful run")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    root = Path(args.root)
    global say
    if args.quiet:
        say = lambda msg: None  # noqa: E731
    say(f"Dry run in {root}")
    make_scratch(root)
    stage_planning(root)
    stage_validation(root)
    stage_preparation(root)
    stage_work(root)
    payload = stage_management(root)
    final = check.run(root)
    say("\n== Final check ==")
    for f in final["findings"]:
        say(f"  {f['level']}: [{f['where']}] {f['message']}")
    say(f"  CHECK {'OK' if final['ok'] else 'FAILED'}: {final['errors']} error(s), {final['warnings']} warning(s)")
    say("\n== Sample dashboard payload (first batch, first 4 writes) ==")
    sample = {"action": "batch", "url": payload["url"], "writes": payload["batches"][0]["writes"][:4]}
    say(json.dumps(sample, indent=2))
    say(f"  ... {payload['writes']} writes in {len(payload['batches'])} batch(es); full payload in {root / 'management' / 'dashboard-payload.json'}")
    if not final["ok"]:
        return 1
    if not args.keep:
        shutil.rmtree(root, ignore_errors=True)
        say("\nScratch folder removed (use --keep to inspect it). DRY RUN PASSED.")
    else:
        say(f"\nScratch folder kept at {root}. DRY RUN PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
