# Dashboard — 2026-10-29 18:43

Capital: ceiling 1000 · released 0 · released unspent 0 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 22 · validating 9 (passed 0, parked 9) · planned 0 · tickets open 2 (closed 5)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, cap 8; Phase 1 ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-10-29 18:43.

Operating rule since 2026-10-27 (signed): agents run every business; the
owner does accounts and set-ups only; outreach goes out by email from a
studio domain under a studio brand. Nothing can be sent until the brand,
domain and email sender exist.

## Runs
| Team | Last run | Outcome | Fails in a row | Breaker | Summary |
|---|---|---|---|---|---|
| research | 2026-10-29T02:52:12 | warn | 0 | closed | cycle 4 under rule 15: 4 briefs (tender-alert digest, financial-model templates, Salla/Zid reporting, CRM list cleaning); 3 rejected at source; cold-email benchmarks recorded; 4 of 8 target |
| planning | 2026-10-29T03:51:11 | ok | 0 | closed | cycle 4 assessed 4, approved 4 (87, 83, 82, 79); 4 email validations opened, staggered 11-19, 11-27 x2, 12-05; 9 running at 0 SU; 0 tickets raised |
| preparation | 2026-10-29T05:15:05 | ok | 0 | closed | 0 owner answers; 0 plans; 0 tickets raised; studio-1 and studio-2 open 4 days; brand, domain and sender await the owner |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-10-28T18:44:12 | ok | 0 | closed | nightly: dashboard refreshed, 31 writes pushed; 2 tickets waiting; brand name awaited |
Source: tools/runlog.py status, 2026-10-29 18:43. No crashed runs. Research warn = 4 briefs against a target of 8.

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
Source: Verdict block of each brief in pipeline/15-validating/, counted 2026-10-29 by tools/signals.py.
Parked (9): 7 cycle-1 planning tests on hold until 2026-11-25; CV service and finance trackers parked 2026-10-27 (no studio-owned consumer channel).
Queue: 9 tests at two in parallel need about 5 weeks of sending once the sender exists; the first start date of 2026-11-03 slips day for day until then.

## Businesses
None live.

## Needs owner (oldest first)
- **20261025-studio-1** (approval / legal, raised 2026-10-25 by preparation, 4 days old, stale; pauses nothing yet at 7 days because no business is live): decide the legal basis for receiving side income in Qatar. Blocks: accepting any payment.
- **20261025-studio-2** (approval / account, raised 2026-10-25 by preparation, 4 days old, stale): open the Gumroad account with the Qatari bank account. Blocks: accepting any payment; the template presale and the tender digest need it for paid signals.
- **Answer in chat (no ticket yet):** the studio brand name. Blocks: the domain ticket, the email sender, and all 9 validations. Proposed 2026-10-27: Qanat Works, Sidra Desk, Marbat Studio, or the owner's own.

Decisions pending: none. Signed: owner hold on cycle-1 planning tests until 2026-11-25; agents-run-everything rule (2026-10-27).

## Issues
tools/check.py (2026-10-29 18:43): 0 errors, 2 warnings, both "ticket open 4
days, older than 3 days" on studio-1 and studio-2. Ledger reconcile OK.
Operational: no owner action since 2026-10-25; the whole pipeline (22 briefs
assessed, 9 tests ready) is idle for lack of a brand name, domain and email
sender. The scheduled-task prompts still say "the owner sends every outreach
message" and must be updated before the first email test starts.
