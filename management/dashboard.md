# Dashboard — 2026-10-25 18:43

Capital: ceiling 1000 · released 0 · released unspent 0 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 12 · validating 3 (passed 0, parked 7) · planned 0 · tickets open 4 (closed 3)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, cap 8; Phase 1 ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-10-25 18:43.

## Runs
| Team | Last run | Outcome | Fails in a row | Breaker | Summary |
|---|---|---|---|---|---|
| research | 2026-10-25T18:07:53 | ok | 0 | closed | cycle 2 under the owner hold: 4 non-planning briefs (SME Excel automation, GCC bilingual CV service, Arabic modern-Excel course, bilingual finance trackers), 2 playbooks, 2 methods rejected at source |
| planning | 2026-10-25T18:19:19 | ok | 0 | closed | cycle 2 assessed 4: approved 3 (gcc-bilingual-cv-service 86, sme-excel-automation-service 77, freelancer-finance-tracker-templates 77), rejected 1 (arabic-excel-power-query-course 66); 3 validations opened (2 start today with owner tickets -v1, trackers start 2026-11-02); gate 9 owner hold passed by all |
| preparation | 2026-10-25T17:54:41 | ok | 0 | closed | 0 plans (none passed validation yet); 2 studio tickets raised: legal basis for income, Gumroad payout route |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-10-25T17:58:39 | ok | 0 | closed | first nightly: dashboard.md rebuilt, live dashboard pushed (15 writes), 5 tickets waiting for the owner |
Source: tools/runlog.py status, 2026-10-25 18:43. No crashed runs.

## Validations running (7-day tests, owner sends the messages)
| Id | Test | Started | Deadline | Signal units so far |
|---|---|---|---|---|
| 20261025-sme-excel-automation-service | outreach (20 then 30 messages) | 2026-10-25 | 2026-11-01 | 0 (0 of 50 messages sent) |
| 20261025-gcc-bilingual-cv-service | presale (20 direct asks) | 2026-10-25 | 2026-11-01 | 0 (0 of 20 asks) |
| 20261025-freelancer-finance-tracker-templates | landing (100 visitors, Gumroad) | 2026-11-02 | 2026-11-09 | 0 (not started; needs ticket 20261025-studio-2) |
Source: Signals table and Verdict block of each brief in pipeline/15-validating/, counted 2026-10-25 by tools/signals.py.

Parked (7, cycle 1): all seven planning-related validations are on hold until
2026-11-25 by the owner's signed hold (management/decisions.md, 2026-10-25).
Their -v1 tickets are closed.

## Businesses
None live. The first business launches only after a validation passes
(3 signal units by its deadline) and Preparation completes the plan checklist.

## Needs owner (oldest first)
All four raised 2026-10-25 (0 days old; stale after 3 days, pause after 7).
- **20261025-sme-excel-automation-service-v1** (approval / send, raised 2026-10-25 by planning): send the outreach message to 20 small-business contacts; day-3 follow-up; record replies on the card. Blocks: validation of sme-excel-automation-service (deadline 2026-11-01). Priority 1 of 2 this week.
- **20261025-gcc-bilingual-cv-service-v1** (approval / send, raised 2026-10-25 by planning): ask 20 Gulf job seekers to buy the bilingual CV package; record replies on the card. Blocks: validation of gcc-bilingual-cv-service (deadline 2026-11-01). Priority 2 of 2 this week.
- **20261025-studio-1** (approval / legal, raised 2026-10-25 by preparation): decide the legal basis for receiving side income in Qatar and note it in management/payments.md. Blocks: accepting any payment (validations continue in audience mode meanwhile).
- **20261025-studio-2** (approval / account, raised 2026-10-25 by preparation): open the Gumroad account, add the Qatari bank account, pass the identity check. Blocks: accepting any payment for digital products and the finance-tracker landing test (starts 2026-11-02).

Decisions pending: none. One signed decision on file (hold on cycle-1 planning
validations until 2026-11-25).

## Issues
None. tools/check.py: 0 errors, 0 warnings (2026-10-25 18:43). Ledger reconcile OK.
