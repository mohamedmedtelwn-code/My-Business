# Dashboard — 2026-11-01 18:43

Capital: ceiling 1000 · released 23.08 · released unspent 23.08 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 22 · validating 9 (passed 0, parked 9) · planned 0 · tickets open 3 (closed 7)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, day 8 of 90; ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-11-01 18:43. Brand: Mteryak Studio, domain mteryakstudio.com (decided 2026-10-30).

Operating rule since 2026-10-27 (signed): agents run every business; the
owner does accounts and set-ups only; outreach goes out by email from
hello@mteryakstudio.com signed "The Mteryak Studio team". Legal basis for
income: owner decision 2026-10-30, payments may be accepted (ticket studio-1
closed). USD 23.08 released against the domain and mailbox tickets; spend is
recorded when the owner reports each purchase paid.

## Runs
| Team | Last run | Outcome | Fails in a row | Breaker | Summary |
|---|---|---|---|---|---|
| research | 2026-10-29T02:52:12 | warn | 0 | closed | cycle 4: 4 briefs; 3 rejected at source; 4 of 8 target. Next cycle Mon 2026-11-02 |
| planning | 2026-11-01T03:48:28 | ok | 0 | closed | inbox empty; 9 validations re-counted, all RUNNING at 0 SU, none started; 0 tickets raised |
| preparation | 2026-11-01T05:15:37 | ok | 0 | closed | studio-4 and studio-5 approved and released, purchases not yet reported; studio-2 open 7 days |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-10-31T18:44:25 | ok | 0 | closed | nightly: dashboard refreshed, 43 writes; 3 tickets waiting |
Source: tools/runlog.py status, 2026-11-01 18:43. No crashed runs. Research cycle 5 due Mon 2026-11-02.

## Validations running (7-day agent-run email tests; each starts only once the studio mailbox exists)
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
Source: Verdict block of each brief in pipeline/15-validating/, counted 2026-11-01 by tools/signals.py.
Parked (9): 7 cycle-1 planning tests on hold until 2026-11-25; CV service and finance trackers (no studio-owned consumer channel).

## Businesses
None live.

## Needs owner (oldest first)
- **20261025-studio-2** (account, raised 2026-10-25 by preparation, 7 days, stale; owner said on 2026-10-30 "this week"): open the Gumroad account with the Qatari bank account. Blocks: paid signals for the template presale and the tender digest; any digital-product revenue. About 20 minutes.
- **20261030-studio-4** (account, Tier 0 USD 11.08, raised 2026-10-30, approved 2026-10-30, purchase pending): buy mteryakstudio.com at Porkbun, decline add-ons, write DONE. Blocks: the mailbox and all 9 tests. About 5 minutes.
- **20261030-studio-5** (account, Tier 0 USD 12, raised 2026-10-30, approved 2026-10-30, purchase pending; after studio-4): Zoho Mail Lite mailbox hello@mteryakstudio.com, DNS records, IMAP on, app password, five secrets in the runner's environment. Blocks: all 9 tests. About 20 minutes.

Decisions: all signed (owner hold until 2026-11-25; agents-run rule 2026-10-27; brand 2026-10-30; legal basis 2026-10-30). None pending.

## Issues
tools/check.py (2026-11-01 18:43): 0 errors, 1 warning (studio-2 older
than 3 days, now 7). Ledger reconcile OK; USD 23.08 released, nothing spent yet.
The first two tests dated 2026-11-03 will not start on time: the domain
and mailbox are not yet bought, and the domain needs a few hours of DNS
settling. Planning re-dates them the morning after the mailbox is DONE. The five scheduled-task prompts still carry the old "owner sends"
wording; Management rewrites them the day the mailbox is reported DONE.
