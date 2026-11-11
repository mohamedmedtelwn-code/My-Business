# Dashboard — 2026-11-11 18:42

Capital: ceiling 1000 · released 23.08 · released unspent 23.08 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 31 · validating 17 (passed 0, parked 9) · planned 0 · tickets open 4 (closed 7)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, day 18 of 90; ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-11-11 18:42. Brand: Mteryak Studio, domain mteryakstudio.com (decided 2026-10-30).

Operating rule since 2026-10-27 (signed): agents run every business; the
owner does accounts and set-ups only; outreach goes out by email from
hello@mteryakstudio.com signed "The Mteryak Studio team". Legal basis for
income: owner decision 2026-10-30, payments may be accepted (ticket studio-1
closed). USD 23.08 released against the domain and mailbox tickets; spend is
recorded when the owner reports each purchase paid.

## Runs
| Team | Last run | Outcome | Fails in a row | Breaker | Summary |
|---|---|---|---|---|---|
| research | 2026-11-09T02:51:42 | ok | 0 | closed | cycle 7: 1 brief (email authentication set-up service, free public DNS-check hook), 1 playbook, 23 source rows, 5 rejections at source. Next cycle Thu 2026-11-12 at 02:47 UTC unless the owner approves the hold (ticket studio-6) |
| planning | 2026-11-11T03:48:48 | ok | 0 | closed | inbox empty; 17 validations recounted, all RUNNING at 0 SU; none due before 2026-11-17; 0 tickets |
| preparation | 2026-11-11T05:14:51 | ok | 0 | closed | no owner answers, no new decisions, no plans; 4 studio tickets open, purchases pending |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-11-11T18:42 | running | 0 | closed | nightly: this refresh; weekly review 2026-46 due Fri 2026-11-13 |
Source: tools/runlog.py status, 2026-11-11 18:42. No crashed runs.

## Validations running (7-day agent-run email tests; each starts only once the studio mailbox exists)
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
Source: Verdict block of each brief in pipeline/15-validating/, counted 2026-11-11 by tools/signals.py.
Parked (9): 7 cycle-1 planning tests on hold until 2026-11-25; CV service and finance trackers (no studio-owned consumer channel).

## Businesses
None live.

## Needs owner (oldest first)
- **20261025-studio-2** (account, raised 2026-10-25 by preparation, 17 days, stale; owner said on 2026-10-30 "this week"): open the Gumroad account with the Qatari bank account. Blocks: paid signals for the template presale and the tender digest; any digital-product revenue. About 20 minutes.
- **20261030-studio-4** (account, Tier 0 USD 11.08, raised 2026-10-30, approved 2026-10-30, 12 days, stale, purchase pending): buy mteryakstudio.com at Porkbun, decline add-ons, write DONE. Blocks: the mailbox and all 17 tests. About 5 minutes.
- **20261030-studio-5** (account, Tier 0 USD 12, raised 2026-10-30, approved 2026-10-30, 12 days, stale, purchase pending; after studio-4): Zoho Mail Lite mailbox hello@mteryakstudio.com, DNS records, IMAP on, app password, five secrets in the runner's environment. Blocks: all 17 tests. About 20 minutes.
- **20261106-studio-6** (other, raised 2026-11-06 by management, 5 days, stale): decide whether to pause the Mon and Thu Research cycles until the mailbox is DONE; 17 tests are queued and none can run. One word on the card. Blocks nothing.

Decisions: one pending-owner (Research hold, ticket studio-6); the rest signed (owner hold until 2026-11-25; agents-run rule 2026-10-27; brand 2026-10-30; legal basis 2026-10-30).

## Issues
tools/check.py (2026-11-11 18:42): 0 errors, 4 warnings (studio-2 at 17 days, studio-4 and studio-5 at 12, studio-6 at 5; all four open tickets stale).
Ledger reconcile OK; USD 23.08 released, nothing spent yet.
No owner answer has arrived since 2026-10-30 (12 days). Four tests have
been shifted a week each; the pair due 2026-11-17 moves next on
2026-11-16 unless studio-5 is DONE, and the 17-test queue cascades a
week at a time until then. After the mailbox exists the domain needs
about two weeks of warm-up at 5-10 emails a day, so the first full
20-email batch is realistically three weeks after the purchase. Every
approved idea sells by email, so the three open set-up tickets remain the
studio's only critical path. Research cycle 8 runs tomorrow at 02:47 UTC
and stays lean unless the hold (studio-6) is approved. The five
scheduled-task prompts still carry the old "owner sends" wording;
Management rewrites them the day the mailbox is reported DONE. Weekly
review 2026-46 is due Fri 2026-11-13.
