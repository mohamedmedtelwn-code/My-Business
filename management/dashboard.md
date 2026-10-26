# Dashboard — 2026-10-26 18:44

Capital: ceiling 1000 · released 0 · released unspent 0 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 18 · validating 7 (passed 0, parked 7) · planned 0 · tickets open 4 (closed 3)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, cap 8; Phase 1 ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-10-26 18:44.

## Runs
| Team | Last run | Outcome | Fails in a row | Breaker | Summary |
|---|---|---|---|---|---|
| research | 2026-10-26T02:55:28 | warn | 0 | closed | cycle 3 under the owner hold: 6 briefs (python data-extraction service, startup financial-model service, Arabic-English business translation, GCC LinkedIn ghostwriting, tafqeet/invoice Sheets add-on, Qatar pay-per-lead Meta campaigns); 5 methods rejected at source; 6 of 8 target |
| planning | 2026-10-26T03:52:46 | ok | 0 | closed | cycle 3 assessed 6: approved 4 (python-data-extraction-service 80, gcc-linkedin-ghostwriting 79, startup-financial-model-service 78, arabic-english-business-translation 78), rejected 2 (tafqeet-invoice-sheets-addon 64, qatar-home-services-lead-gen 62); 4 validations opened, staggered; 7 running validations at 0 SU; 0 tickets raised |
| preparation | 2026-10-26T05:15:18 | ok | 0 | closed | 0 owner answers; 0 plans (no validation passed yet); 0 tickets raised; studio-1 and studio-2 still open; payout_route_verified stays false |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-10-25T18:43:54 | ok | 0 | closed | nightly: dashboard.md refreshed, live dashboard pushed (20 writes); 0 issues; 4 tickets waiting for the owner |
Source: tools/runlog.py status, 2026-10-26 18:44. No crashed runs. Research warn = 6 briefs against a target of 8, not a failure.

## Validations running (7-day tests, owner sends the messages)
| Id | Test | Started | Deadline | Signal units so far |
|---|---|---|---|---|
| 20261025-sme-excel-automation-service | outreach (20 then 30 messages) | 2026-10-25 | 2026-11-01 | 0 (0 of 50 messages sent) |
| 20261025-gcc-bilingual-cv-service | presale (20 direct asks) | 2026-10-25 | 2026-11-01 | 0 (0 of 20 asks) |
| 20261025-freelancer-finance-tracker-templates | landing (100 visitors, Gumroad) | 2026-11-02 | 2026-11-09 | 0 (not started; needs ticket 20261025-studio-2) |
| 20261026-python-data-extraction-service | outreach (20 then 30 messages) | 2026-11-02 | 2026-11-09 | 0 (not started; ticket raised by Planning on the start date) |
| 20261026-gcc-linkedin-ghostwriting | presale (20 direct asks) | 2026-11-10 | 2026-11-17 | 0 (not started; owner sends 20 profile links by 2026-11-08) |
| 20261026-startup-financial-model-service | presale (20 direct asks) | 2026-11-10 | 2026-11-17 | 0 (not started) |
| 20261026-arabic-english-business-translation | outreach (20 then 30 messages) | 2026-11-18 | 2026-11-25 | 0 (not started) |
Source: Signals table and Verdict block of each brief in pipeline/15-validating/, counted 2026-10-26 by tools/signals.py.

The two cycle-2 tests close on 2026-11-01; no messages have been reported
sent yet (owner tickets open 1 day). Parked (7, cycle 1): all seven
planning-related validations stay on hold until 2026-11-25 by the owner's
signed hold (management/decisions.md, 2026-10-25).

## Businesses
None live. The first business launches only after a validation passes
(3 signal units by its deadline) and Preparation completes the plan checklist.

## Needs owner (oldest first)
All four raised 2026-10-25 (1 day old; stale after 3 days, pause after 7).
- **20261025-sme-excel-automation-service-v1** (approval / send, raised 2026-10-25 by planning): send the outreach message to 20 small-business contacts; day-3 follow-up; record replies on the card. Blocks: validation of sme-excel-automation-service (deadline 2026-11-01). Priority 1 of 2 this week.
- **20261025-gcc-bilingual-cv-service-v1** (approval / send, raised 2026-10-25 by planning): ask 20 Gulf job seekers to buy the bilingual CV package; record replies on the card. Blocks: validation of gcc-bilingual-cv-service (deadline 2026-11-01). Priority 2 of 2 this week.
- **20261025-studio-1** (approval / legal, raised 2026-10-25 by preparation): decide the legal basis for receiving side income in Qatar and note it in management/payments.md. Blocks: accepting any payment (validations continue in audience mode meanwhile).
- **20261025-studio-2** (approval / account, raised 2026-10-25 by preparation): open the Gumroad account, add the Qatari bank account, pass the identity check. Blocks: accepting any payment for digital products and the finance-tracker landing test (starts 2026-11-02).

Decisions pending: none. One signed decision on file (hold on cycle-1 planning
validations until 2026-11-25). Owner time this week: about 80 minutes for the
two send tickets; the next tests start 2026-11-02.

## Issues
None. tools/check.py: 0 errors, 0 warnings (2026-10-26 18:44). Ledger reconcile OK.
