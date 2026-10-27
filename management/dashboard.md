# Dashboard — 2026-10-27 18:44

Capital: ceiling 1000 · released 0 · released unspent 0 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 18 · validating 7 (passed 0, parked 7) · planned 0 · tickets open 4 (closed 3)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, cap 8; Phase 1 ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-10-27 18:44.

## Runs
| Team | Last run | Outcome | Fails in a row | Breaker | Summary |
|---|---|---|---|---|---|
| research | 2026-10-26T02:55:28 | warn | 0 | closed | cycle 3 under the owner hold: 6 briefs; 5 methods rejected at source; 6 of 8 target. Next cycle Thu 2026-10-29 |
| planning | 2026-10-27T03:48:23 | ok | 0 | closed | inbox empty (0 assessed); 0 owner answers; 7 running validations re-counted, all RUNNING at 0 SU; cycle-2 tests close 2026-11-01 with 0 messages reported; 0 tickets raised |
| preparation | 2026-10-27T05:15:08 | ok | 0 | closed | 0 owner answers; 0 plans; 0 tickets raised; studio-1 and studio-2 open 2 days; payout_route_verified stays false |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-10-26T18:44:41 | ok | 0 | closed | nightly: dashboard.md refreshed, live dashboard pushed (24 writes); 0 issues; 4 tickets waiting |
Source: tools/runlog.py status, 2026-10-27 18:44. No crashed runs.

## Validations running (7-day tests)
| Id | Test | Started | Deadline | Signal units so far |
|---|---|---|---|---|
| 20261025-sme-excel-automation-service | outreach (20 then 30 messages) | 2026-10-25 | 2026-11-01 | 0 (0 of 50 messages sent) |
| 20261025-gcc-bilingual-cv-service | presale (20 direct asks) | 2026-10-25 | 2026-11-01 | 0 (0 of 20 asks) |
| 20261025-freelancer-finance-tracker-templates | landing (100 visitors, Gumroad) | 2026-11-02 | 2026-11-09 | 0 (not started; needs ticket 20261025-studio-2) |
| 20261026-python-data-extraction-service | outreach (20 then 30 messages) | 2026-11-02 | 2026-11-09 | 0 (not started) |
| 20261026-gcc-linkedin-ghostwriting | presale (20 direct asks) | 2026-11-10 | 2026-11-17 | 0 (not started) |
| 20261026-startup-financial-model-service | presale (20 direct asks) | 2026-11-10 | 2026-11-17 | 0 (not started) |
| 20261026-arabic-english-business-translation | outreach (20 then 30 messages) | 2026-11-18 | 2026-11-25 | 0 (not started) |
Source: Signals table and Verdict block of each brief in pipeline/15-validating/, counted 2026-10-27 by tools/signals.py.

All seven tests were designed around messages the owner sends from the
owner's own network. On 2026-10-27 the owner said in chat that the owner's
network and name must not be used and that agents must run every business,
with the owner doing only accounts and set-ups. Pending the owner's written
confirmation (see Decisions), the two cycle-2 tests will park on 2026-11-01
with nothing sent, and every test will be re-planned as an agent-run test
(landing page plus email outreach from a studio brand). Parked (7, cycle 1):
on hold until 2026-11-25 by the owner's signed hold.

## Businesses
None live.

## Needs owner (oldest first)
All four raised 2026-10-25 (2 days old; stale after 3 days, pause after 7).
- **20261025-sme-excel-automation-service-v1** (approval / send, raised 2026-10-25 by planning): send 20 outreach messages. Blocks: validation of sme-excel-automation-service (deadline 2026-11-01). Owner has said this will not be done by hand; expected to park.
- **20261025-gcc-bilingual-cv-service-v1** (approval / send, raised 2026-10-25 by planning): 20 presale asks. Blocks: validation of gcc-bilingual-cv-service (deadline 2026-11-01). Same as above.
- **20261025-studio-1** (approval / legal, raised 2026-10-25 by preparation): decide the legal basis for receiving side income in Qatar. Blocks: accepting any payment.
- **20261025-studio-2** (approval / account, raised 2026-10-25 by preparation): open the Gumroad account with the Qatari bank account. Blocks: accepting any payment for digital products and the finance-tracker landing test.

Decisions pending (owner, in chat, not yet signed in management/decisions.md):
1. Operating rule change: agent-run outreach only, no use of the owner's
   network or name, owner does accounts and set-ups only. Consequences:
   LinkedIn messaging, Upwork and Fiverr leave the channel list (platform
   rules forbid agent-operated accounts); validations become landing page
   plus studio-brand email tests; needs a brand name, a domain (Tier 0), an
   email-sending account and its API key in the runner's secrets.
2. Brand name for the studio's businesses (owner names it or asks for proposals).
One signed decision on file (hold on cycle-1 planning validations until 2026-11-25).

## Issues
None from tools/check.py: 0 errors, 0 warnings (2026-10-27 18:44). Ledger
reconcile OK. Operational: no owner action in 2 days; both cycle-2 tests are
on course to park with a zero denominator.
