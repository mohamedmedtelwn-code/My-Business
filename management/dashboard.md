# Dashboard — 2026-11-12 18:43

Capital: ceiling 0 · released 0 · released unspent 0 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 32 · validating 18 (passed 0, parked 9) · planned 0 · tickets open 3 (closed 9)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, day 19 of 90; ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-11-12 18:43. Brand: Mteryak Studio, domain mteryakstudio.com (decided 2026-10-30).

Operating rule since 2026-10-27 (signed): agents run every business; the
owner does accounts and set-ups only. **Funding rule since 2026-11-12
(signed): zero external cost.** The ceiling is USD 0; the studio spends only
what it earns; the two unspent releases (domain, mailbox) were withdrawn and
their tickets closed. Outreach goes out by email from a free studio-brand
mailbox (ticket studio-7) signed "The Mteryak Studio team" until the pool
funds mteryakstudio.com. Legal basis for income: owner decision 2026-10-30.

## Runs
| Team | Last run | Outcome | Fails in a row | Breaker | Summary |
|---|---|---|---|---|---|
| research | 2026-11-12T02:49:31 | ok | 0 | closed | cycle 8 (zero-cost): 1 brief (privacy-and-consent pack for Saudi and UAE sites, public site-scan hook), 1 playbook, accessibility folded into the audit playbook, 16 source rows, 2 rejections. Next cycle Mon 2026-11-16 unless the owner approves the hold (ticket studio-6) |
| planning | 2026-11-12T03:49:02 | ok | 0 | closed | 1 brief assessed and approved (90/100); validation brief written for 2027-01-14; 18 validations recounted, all RUNNING at 0 SU; 0 tickets |
| preparation | 2026-11-12T05:15:09 | ok | 0 | closed | no owner answers, no new decisions, no plans; 3 studio tickets open, all free |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-11-12T18:43 | running | 0 | closed | nightly: this refresh; 01:10 run applied the owner's zero-cost decision; weekly review 2026-46 due Fri 2026-11-13 |
Source: tools/runlog.py status, 2026-11-12 18:43. No crashed runs.

## Validations running (18 seven-day agent-run email tests; each starts only once the free studio mailbox exists)
| Id | Test | Started | Deadline | Signal units so far |
|---|---|---|---|---|
| 20261025-sme-excel-automation-service | email outreach (20 then 30) | 2026-11-17 | 2026-11-24 | 0 (not started; shifted twice from 2026-11-03, no mailbox) |
| 20261026-python-data-extraction-service | email outreach (20 then 30) | 2026-11-17 | 2026-11-24 | 0 (not started; shifted twice from 2026-11-03, no mailbox) |
| 20261026-startup-financial-model-service | email presale (20 asks) | 2026-11-18 | 2026-11-25 | 0 (not started; shifted from 2026-11-11, no mailbox) |
| 20261026-gcc-linkedin-ghostwriting | email presale (20 asks) | 2026-11-18 | 2026-11-25 | 0 (not started; shifted from 2026-11-11, no mailbox) |
| 20261026-arabic-english-business-translation | email outreach (20 then 30) | 2026-11-19 | 2026-11-26 | 0 (not started) |
| 20261029-crm-list-cleaning-service | email outreach (20 then 30) | 2026-11-19 | 2026-11-26 | 0 (not started) |
| 20261029-salla-zid-merchant-reporting | email outreach (20 then 30) | 2026-11-27 | 2026-12-04 | 0 (not started) |
| 20261029-gcc-financial-model-templates | email presale (20 asks) | 2026-11-27 | 2026-12-04 | 0 (not started) |
| 20261029-gcc-tender-alert-digest | email outreach (20 then 30) | 2026-12-05 | 2026-12-12 | 0 (not started) |
| 20261102-website-technical-audit-service | email outreach (20 then 30) | 2026-12-05 | 2026-12-12 | 0 (not started) |
| 20261102-arabic-document-digitisation-service | email outreach (20 then 30) | 2026-12-13 | 2026-12-20 | 0 (not started) |
| 20261102-gcc-startup-pitch-deck-service | email outreach (20 then 30) | 2026-12-13 | 2026-12-20 | 0 (not started) |
| 20261102-gcc-automation-setup-service | email outreach (20 then 30) | 2026-12-21 | 2026-12-28 | 0 (not started) |
| 20261102-arabic-saas-directory | email outreach (20 then 30) | 2026-12-21 | 2026-12-28 | 0 (not started; directory site and one DNS ticket needed before 2026-12-14) |
| 20261105-gbp-review-management-service | email outreach (20 then 30) | 2026-12-29 | 2027-01-05 | 0 (not started) |
| 20261105-gcc-bid-proposal-writing-service | email outreach (20 then 30) | 2026-12-29 | 2027-01-05 | 0 (not started; shares the tender-digest list) |
| 20261109-email-authentication-setup-service | email outreach (20 then 30) | 2027-01-06 | 2027-01-13 | 0 (not started; approved 2026-11-09 at 90/100) |
| 20261112-gcc-website-privacy-compliance-pack | email outreach (20 then 30) | 2027-01-14 | 2027-01-21 | 0 (not started; approved 2026-11-12 at 90/100; shares one site scan with the audit, listing and email-authentication tests) |
Source: Verdict block of each brief in pipeline/15-validating/, counted 2026-11-12 by tools/signals.py.
Parked (9): 7 cycle-1 planning tests on hold until 2026-11-25; CV service and finance trackers (no studio-owned consumer channel).

## Businesses
None live.

## Needs owner (oldest first)
- **20261025-studio-2** (account, USD 0, raised 2026-10-25 by preparation, 18 days, stale; owner said on 2026-10-30 "this week"): open the Gumroad account with the Qatari bank account. Blocks: paid signals for the template presale and the tender digest; any digital-product revenue. About 20 minutes.
- **20261106-studio-6** (other, raised 2026-11-06 by management, 6 days, stale): decide whether to pause the Mon and Thu Research cycles until the mailbox is DONE; 18 tests are queued and none can run. One word on the card. Blocks nothing.
- **20261112-studio-7** (account, USD 0, raised 2026-11-12 by management): create the free Gmail account "mteryakstudio" (name Mteryak Studio), turn on 2-step verification, make an app password, enable IMAP, store the five STUDIO_* secrets in the runner's environment, write DONE with the address. Blocks: all 18 tests. About 15 minutes. Replaces the withdrawn domain and Zoho tickets.

Decisions: one pending-owner (Research hold, ticket studio-6); the rest signed (owner hold until 2026-11-25; agents-run rule 2026-10-27; brand 2026-10-30; legal basis 2026-10-30; zero external cost 2026-11-12).

## Issues
tools/check.py (2026-11-12 18:43): 0 errors, 2 warnings (studio-2 at 18 days, studio-6 at 6 days; studio-7 raised today, not yet stale).
Ledger reconcile OK; ceiling USD 0, released 0, spent 0, revenue 0 (owner's zero-cost decision, 2026-11-12).
Four runs today, all ok: the owner's decision applied at 01:10, Research
cycle 8 (one brief, zero-cost), Planning (approved it at 90), Preparation
(nothing to do). All 18 tests wait on the free studio mailbox (studio-7);
the pair due 2026-11-17 moves on 2026-11-16 unless it is DONE, and the
queue cascades a week at a time until then. Four queued services now
share one "check from outside" prospect list (email authentication,
website audit, Google listing, privacy scan); Planning will run them on
the same 50 domains. The domain mteryakstudio.com is the first pool
spend once a business has earned USD 25. The five scheduled-task prompts
still carry the old "owner sends" wording; Management rewrites them the
day studio-7 is DONE. Weekly review 2026-46 is due tomorrow, Fri
2026-11-13.
