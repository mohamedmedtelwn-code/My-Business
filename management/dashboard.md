# Dashboard — 2026-10-28 18:43

Capital: ceiling 1000 · released 0 · released unspent 0 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 18 · validating 5 (passed 0, parked 9) · planned 0 · tickets open 2 (closed 5)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, cap 8; Phase 1 ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-10-28 18:43.

Operating rule since 2026-10-27 (signed, management/decisions.md): agents run
every business; the owner does accounts and set-ups only; outreach goes out by
email from a studio domain under a studio brand. Nothing can be sent until the
brand, domain and email sender exist.

## Runs
| Team | Last run | Outcome | Fails in a row | Breaker | Summary |
|---|---|---|---|---|---|
| research | 2026-10-26T02:55:28 | warn | 0 | closed | cycle 3: 6 briefs, 5 methods rejected at source, 6 of 8 target. Next cycle Thu 2026-10-29 under rule 15 |
| planning | 2026-10-28T03:49:08 | ok | 0 | closed | inbox empty; 0 owner answers; 5 agent-run validations re-counted, all RUNNING at 0 SU, none started; 0 tickets raised |
| preparation | 2026-10-28T05:15:17 | ok | 0 | closed | 0 owner answers; 0 plans; 0 tickets raised; studio-1 and studio-2 open 3 days; brand, domain and email sender await the owner |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-10-27T19:11:46 | ok | 0 | closed | owner decision recorded: rule 15 added, 2 send tickets withdrawn, 2 consumer tests parked, 5 B2B tests re-planned as email tests |
Source: tools/runlog.py status, 2026-10-28 18:43. No crashed runs.

## Validations running (7-day agent-run tests; start only once the studio email sender exists)
| Id | Test | Started | Deadline | Signal units so far |
|---|---|---|---|---|
| 20261025-sme-excel-automation-service | email outreach (20 then 30) | 2026-11-03 | 2026-11-10 | 0 (not started) |
| 20261026-python-data-extraction-service | email outreach (20 then 30) | 2026-11-03 | 2026-11-10 | 0 (not started) |
| 20261026-startup-financial-model-service | email presale (20 asks) | 2026-11-11 | 2026-11-18 | 0 (not started) |
| 20261026-gcc-linkedin-ghostwriting | email presale (20 asks) | 2026-11-11 | 2026-11-18 | 0 (not started) |
| 20261026-arabic-english-business-translation | email outreach (20 then 30) | 2026-11-19 | 2026-11-26 | 0 (not started) |
Source: Verdict block of each brief in pipeline/15-validating/, counted 2026-10-28 by tools/signals.py.
Parked (9): 7 cycle-1 planning tests on hold until 2026-11-25; CV service and finance trackers parked 2026-10-27 (no studio-owned consumer channel).

## Businesses
None live.

## Needs owner (oldest first)
- **20261025-studio-1** (approval / legal, raised 2026-10-25 by preparation, 3 days old, stale): decide the legal basis for receiving side income in Qatar. Blocks: accepting any payment.
- **20261025-studio-2** (approval / account, raised 2026-10-25 by preparation, 3 days old, stale): open the Gumroad account with the Qatari bank account. Blocks: accepting any payment for digital products.
- **Answer in chat (no ticket yet):** the studio brand name. Blocks: the domain ticket, the email sender, and every validation above. Proposed 2026-10-27: Qanat Works, Sidra Desk, Marbat Studio, or the owner's own.

Decisions pending: none. Signed: owner hold on cycle-1 planning tests until 2026-11-25; agents-run-everything rule (2026-10-27).

## Issues
None from tools/check.py: 0 errors, 0 warnings (2026-10-28 18:43). Ledger
reconcile OK. Operational: the studio has had no owner action since 2026-10-25;
the first two email tests dated 2026-11-03 will slip unless the brand, domain
and sender exist by then. Both studio tickets pass 7 days on 2026-11-01, which
would pause any business they block (none live yet).
