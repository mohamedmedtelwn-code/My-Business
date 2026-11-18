# Dashboard — 2026-11-18 18:43

Capital: ceiling 0 · released 0 · released unspent 0 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 32 · validating 18 (passed 0, parked 9) · planned 0 · tickets open 4 (closed 9)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, day 25 of 90; ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-11-18 18:43. Brand: Mteryak Studio, domain mteryakstudio.com (decided 2026-10-30).

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
| research | 2026-11-16T02:48:20 | ok | 0 | closed | cycle 9 (lean): 0 briefs by design, 2 rejections at source (stand-alone checker tools, GCC agency directory), 10 source rows, directory playbook gained listing prices. Next cycle Thu 2026-11-19 re-checks platform-rules.md unless the owner approves the hold (ticket studio-6) |
| planning | 2026-11-18T03:50:44 | ok | 0 | closed | inbox empty; 18 validations recounted, all RUNNING at 0 SU; the pair dated 2026-11-18 reached Started with no mailbox, so signals.py gained a Blocked-by hold (open ticket = RUNNING, deadline not counted; unit test, 115 pass) and all 18 briefs carry Blocked by studio-7; 0 tickets |
| preparation | 2026-11-18T05:14:54 | ok | 0 | closed | no owner answers, no new decisions, no plans; 4 studio tickets open, all free |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-11-18T18:43 | running | 0 | closed | nightly: this refresh; weekly review 2026-46 on 2026-11-13 proposed the phase-1 clock restart (ticket studio-8) |
Source: tools/runlog.py status, 2026-11-18 18:43. No crashed runs.

## Validations running (18 seven-day agent-run email tests; all held by `Blocked by: 20261112-studio-7` since 2026-11-18: dates below are nominal, the deadline does not count while the mailbox ticket is open, and Planning re-dates the whole queue once from DONE + 14 days)
| Id | Test | Started (nominal) | Deadline (nominal) | Signal units so far |
|---|---|---|---|---|
| 20261025-sme-excel-automation-service | email outreach (20 then 30) | 2026-11-24 | 2026-12-01 | 0 (held; shifted three times from 2026-11-03 before the hold) |
| 20261026-python-data-extraction-service | email outreach (20 then 30) | 2026-11-24 | 2026-12-01 | 0 (held; shifted three times from 2026-11-03 before the hold) |
| 20261026-startup-financial-model-service | email presale (20 asks) | 2026-11-18 | 2026-11-25 | 0 (held; Started date arrived 2026-11-18 with no mailbox) |
| 20261026-gcc-linkedin-ghostwriting | email presale (20 asks) | 2026-11-18 | 2026-11-25 | 0 (held; Started date arrived 2026-11-18 with no mailbox) |
| 20261026-arabic-english-business-translation | email outreach (20 then 30) | 2026-11-19 | 2026-11-26 | 0 (held) |
| 20261029-crm-list-cleaning-service | email outreach (20 then 30) | 2026-11-19 | 2026-11-26 | 0 (held) |
| 20261029-salla-zid-merchant-reporting | email outreach (20 then 30) | 2026-11-27 | 2026-12-04 | 0 (held) |
| 20261029-gcc-financial-model-templates | email presale (20 asks) | 2026-11-27 | 2026-12-04 | 0 (held) |
| 20261029-gcc-tender-alert-digest | email outreach (20 then 30) | 2026-12-05 | 2026-12-12 | 0 (held) |
| 20261102-website-technical-audit-service | email outreach (20 then 30) | 2026-12-05 | 2026-12-12 | 0 (held) |
| 20261102-arabic-document-digitisation-service | email outreach (20 then 30) | 2026-12-13 | 2026-12-20 | 0 (held) |
| 20261102-gcc-startup-pitch-deck-service | email outreach (20 then 30) | 2026-12-13 | 2026-12-20 | 0 (held) |
| 20261102-gcc-automation-setup-service | email outreach (20 then 30) | 2026-12-21 | 2026-12-28 | 0 (held) |
| 20261102-arabic-saas-directory | email outreach (20 then 30) | 2026-12-21 | 2026-12-28 | 0 (held; directory site and one DNS ticket needed before 2026-12-14) |
| 20261105-gbp-review-management-service | email outreach (20 then 30) | 2026-12-29 | 2027-01-05 | 0 (held) |
| 20261105-gcc-bid-proposal-writing-service | email outreach (20 then 30) | 2026-12-29 | 2027-01-05 | 0 (held; shares the tender-digest list) |
| 20261109-email-authentication-setup-service | email outreach (20 then 30) | 2027-01-06 | 2027-01-13 | 0 (held; approved 2026-11-09 at 90/100) |
| 20261112-gcc-website-privacy-compliance-pack | email outreach (20 then 30) | 2027-01-14 | 2027-01-21 | 0 (held; approved 2026-11-12 at 90/100; shares one site scan with the audit, listing and email-authentication tests) |
Source: Verdict block of each brief in pipeline/15-validating/, counted 2026-11-18 by tools/signals.py; every verdict reads "Blocked by ticket 20261112-studio-7 (still open)".
Parked (9): 7 cycle-1 planning tests on hold until 2026-11-25; CV service and finance trackers (no studio-owned consumer channel).

## Businesses
None live.

## Needs owner (oldest first)
- **20261025-studio-2** (account, USD 0, raised 2026-10-25 by preparation, 24 days, stale; owner said on 2026-10-30 "this week"): open the Gumroad account with the Qatari bank account. Blocks: paid signals for the template presale and the tender digest; any digital-product revenue. About 20 minutes.
- **20261106-studio-6** (other, raised 2026-11-06 by management, 12 days, stale): decide whether to pause the Mon and Thu Research cycles until the mailbox is DONE; 18 tests are queued and none can run. One word on the card. Blocks nothing.
- **20261112-studio-7** (account, USD 0, raised 2026-11-12 by management, 6 days, stale): create the free Gmail account "mteryakstudio" (name Mteryak Studio), turn on 2-step verification, make an app password, enable IMAP, store the five STUDIO_* secrets in the runner's environment, write DONE with the address. Blocks: all 18 tests. About 15 minutes. Replaces the withdrawn domain and Zoho tickets.

- **20261113-studio-8** (other, USD 0, raised 2026-11-13 by management, 5 days, stale): one word on whether the 90-day phase-1 clock restarts on the day the mailbox is DONE. Blocks nothing. About a minute.

Decisions: two pending-owner (Research hold, ticket studio-6; phase-1 clock restart, ticket studio-8); the rest signed (owner hold until 2026-11-25; agents-run rule 2026-10-27; brand 2026-10-30; legal basis 2026-10-30; zero external cost 2026-11-12).

## Issues
tools/check.py (2026-11-18 18:43): 0 errors, 4 warnings (studio-2 at 24 days, studio-6 at 12 days, studio-7 at 6 days, studio-8 at 5 days).
Ledger reconcile OK; ceiling USD 0, released 0, spent 0, revenue 0.
Quiet day: three runs, all ok, nothing new to process. Weekly review
2026-46 (2026-11-13) proposed restarting the phase-1 clock on the day the
free mailbox is DONE (ticket studio-8). All 18 tests wait on studio-7. The
pair dated 2026-11-18 reached its Started date with no mailbox; instead of
a fifth re-date Planning gave signals.py a Blocked-by hold (a brief naming
an open ticket stays RUNNING and its deadline does not count) and tagged
all 18 briefs with it, so dates no longer cascade and no idea can be parked
for a studio dependency. The run after studio-7 is DONE re-dates the whole
queue once from "DONE + 14 days". Research cycle 9 wrote no brief by design. The five
scheduled-task prompts still carry the old "owner sends" wording;
Management rewrites them the day studio-7 is DONE. Owner hold on
construction-planning businesses ends 2026-11-25. Platform-rules full
re-check due 2026-11-24.
