# Dashboard — 2026-10-30 18:44 (weekly review 2026-44 written 14:46)

Capital: ceiling 1000 · released 0 · released unspent 0 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 22 · validating 9 (passed 0, parked 9) · planned 0 · tickets open 3 (closed 5)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, day 6 of 90; ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-10-30 18:44. Weekly review: management/reviews/2026-44.md.

Operating rule since 2026-10-27 (signed): agents run every business; the
owner does accounts and set-ups only; outreach goes out by email from a
studio domain under a studio brand.

## Runs
| Team | Last run | Outcome | Fails in a row | Breaker | Summary |
|---|---|---|---|---|---|
| research | 2026-10-29T02:52:12 | warn | 0 | closed | cycle 4: 4 briefs (tender-alert digest, financial-model templates, Salla/Zid reporting, CRM list cleaning); 3 rejected at source; 4 of 8 target |
| planning | 2026-10-30T03:48:10 | ok | 0 | closed | inbox empty; 9 validations re-counted, all RUNNING at 0 SU, none started; 0 tickets raised |
| preparation | 2026-10-30T05:15:25 | ok | 0 | closed | 0 answers; 0 plans; 0 tickets raised; studio-1 and studio-2 open 5 days |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-10-30T14:46:33 | ok | 0 | closed | weekly review 2026-44 written: 0 revenue, 0 live, 25 runs (23 ok, 2 warn); 1 decision proposed (brand name, ticket 20261030-studio-3); 3 lessons recorded |
Week 2026-44: 25 runs, 23 ok, 2 warn, 0 bad, 0 crashed, no breaker open. Source: management/runs.jsonl, 2026-10-30.

## Validations running (7-day agent-run email tests; each starts only once the studio email sender exists)
| Id | Test | Started | Deadline | Signal units so far |
|---|---|---|---|---|
| 20261025-sme-excel-automation-service | email outreach (20 then 30) | 2026-11-03 | 2026-11-10 | 0 (not started) |
| 20261026-python-data-extraction-service | email outreach (20 then 30) | 2026-11-03 | 2026-11-10 | 0 (not started) |
| 20261026-startup-financial-model-service | email presale (20 asks) | 2026-11-11 | 2026-11-18 | 0 (not started) |
| 20261026-gcc-linkedin-ghostwriting | email presale (20 asks) | 2026-11-11 | 2026-11-18 | 0 (not started) |
| 20261026-arabic-english-business-translation | email outreach (20 then 30) | 2026-11-19 | 2026-11-26 | 0 (not started) |
| 20261029-crm-list-cleaning-service | email outreach (20 then 30) | 2026-11-19 | 2026-11-26 | 0 (not started) |
| 20261029-salla-zid-merchant-reporting | email outreach (20 then 30) | 2026-11-27 | 2026-12-04 | 0 (not started) |
| 20261029-gcc-financial-model-templates | email presale (20 asks) | 2026-11-27 | 2026-12-04 | 0 (not started) |
| 20261029-gcc-tender-alert-digest | email outreach (20 then 30) | 2026-12-05 | 2026-12-12 | 0 (not started) |
Source: Verdict block of each brief in pipeline/15-validating/, counted 2026-10-30 by tools/signals.py.
Parked (9): 7 cycle-1 planning tests on hold until 2026-11-25; CV service and finance trackers (no studio-owned consumer channel).

## Businesses
None live.

## Needs owner (oldest first)
- **20261025-studio-1** (approval / legal, raised 2026-10-25 by preparation, 5 days, stale): decide the legal basis for receiving side income in Qatar. Blocks: accepting any payment. About 10 minutes.
- **20261025-studio-2** (approval / account, raised 2026-10-25 by preparation, 5 days, stale): open the Gumroad account with the Qatari bank account. Blocks: accepting any payment. About 20 minutes.
- **20261030-studio-3** (other, raised 2026-10-30 by management): choose the studio brand name: Qanat Works, Sidra Desk, Marbat Studio, or your own. Blocks: the domain, the email sender and all 9 tests. One minute.

Decisions pending-owner: brand name (2026-10-30). Signed: owner hold on cycle-1 planning tests until 2026-11-25; agents-run-everything rule (2026-10-27).

## Issues
tools/check.py (2026-10-30 18:44): 0 errors, 2 warnings (studio-1 and
studio-2 older than 3 days). Ledger reconcile OK. The five scheduled-task
prompts still carry the old "owner sends" wording; Management rewrites them
the day the sender exists. Owner hold ends 2026-11-25; the 7 parked cycle-1
tests then need re-planning as email tests.
