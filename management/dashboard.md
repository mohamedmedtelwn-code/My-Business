# Dashboard — 2026-11-02 18:43

Capital: ceiling 1000 · released 23.08 · released unspent 23.08 · spent 0 · revenue 0 · pool 0
Pipeline: inbox 0 · assessed 27 · validating 14 (passed 0, parked 9) · planned 0 · tickets open 3 (closed 7)
Businesses: live 0 · paused 0 · stopped 0 (Phase 1, day 9 of 90; ends 2027-01-23)
Source: tools/ledger.py report and tools/check.py, 2026-11-02 18:43. Brand: Mteryak Studio, domain mteryakstudio.com (decided 2026-10-30).

Operating rule since 2026-10-27 (signed): agents run every business; the
owner does accounts and set-ups only; outreach goes out by email from
hello@mteryakstudio.com signed "The Mteryak Studio team". Legal basis for
income: owner decision 2026-10-30, payments may be accepted (ticket studio-1
closed). USD 23.08 released against the domain and mailbox tickets; spend is
recorded when the owner reports each purchase paid.

## Runs
| Team | Last run | Outcome | Fails in a row | Breaker | Summary |
|---|---|---|---|---|---|
| research | 2026-11-02T02:57:20 | ok | 0 | closed | cycle 5: 5 briefs (website audit, automation builds, pitch decks, document digitisation, Arabic SaaS directory), 5 playbooks, 4 rejections at source. Next cycle Thu 2026-11-05 |
| planning | 2026-11-02T03:51:55 | ok | 0 | closed | 5 assessed, 5 approved (88, 87, 85, 83, 75); 5 validation briefs staggered 2026-12-05 to 2026-12-28; 14 validations counted, all RUNNING; 0 tickets |
| preparation | 2026-11-02T05:15:11 | ok | 0 | closed | no owner answers, no plans; 3 studio tickets open, purchases pending |
| work | - | idle | 0 | closed | no business live yet |
| management | 2026-11-02T18:42:59 | running | 0 | closed | nightly: this refresh |
Source: tools/runlog.py status, 2026-11-02 18:43. No crashed runs.

## Validations running (7-day agent-run email tests; each starts only once the studio mailbox exists)
| Id | Test | Started | Deadline | Signal units so far |
|---|---|---|---|---|
| 20261025-sme-excel-automation-service | email outreach (20 then 30) | 2026-11-03 | 2026-11-10 | 0 (not started; will slip, no mailbox) |
| 20261026-python-data-extraction-service | email outreach (20 then 30) | 2026-11-03 | 2026-11-10 | 0 (not started; will slip, no mailbox) |
| 20261026-startup-financial-model-service | email presale (20 asks) | 2026-11-11 | 2026-11-18 | 0 (not started) |
| 20261026-gcc-linkedin-ghostwriting | email presale (20 asks) | 2026-11-11 | 2026-11-18 | 0 (not started) |
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
Source: Verdict block of each brief in pipeline/15-validating/, counted 2026-11-02 by tools/signals.py.
Parked (9): 7 cycle-1 planning tests on hold until 2026-11-25; CV service and finance trackers (no studio-owned consumer channel).

## Businesses
None live.

## Needs owner (oldest first)
- **20261025-studio-2** (account, raised 2026-10-25 by preparation, 8 days, stale; owner said on 2026-10-30 "this week"): open the Gumroad account with the Qatari bank account. Blocks: paid signals for the template presale and the tender digest; any digital-product revenue. About 20 minutes.
- **20261030-studio-4** (account, Tier 0 USD 11.08, raised 2026-10-30, approved 2026-10-30, purchase pending): buy mteryakstudio.com at Porkbun, decline add-ons, write DONE. Blocks: the mailbox and all 14 tests. About 5 minutes.
- **20261030-studio-5** (account, Tier 0 USD 12, raised 2026-10-30, approved 2026-10-30, purchase pending; after studio-4): Zoho Mail Lite mailbox hello@mteryakstudio.com, DNS records, IMAP on, app password, five secrets in the runner's environment. Blocks: all 14 tests. About 20 minutes.

Decisions: all signed (owner hold until 2026-11-25; agents-run rule 2026-10-27; brand 2026-10-30; legal basis 2026-10-30). None pending.

## Issues
tools/check.py (2026-11-02 18:43): 0 errors, 1 warning (studio-2 older
than 3 days, now 8). Ledger reconcile OK; USD 23.08 released, nothing spent yet.
The two tests dated 2026-11-03 will not start tomorrow: the domain and
mailbox are not bought. Planning re-dates them the morning after the mailbox
is DONE; every later test keeps its slot until then. All 14 approved ideas
are services or vendor-paid listings sold by email; nothing can be learned
about demand until the mailbox exists, so the three open tickets are the
studio's only critical path. The five scheduled-task prompts still carry the
old "owner sends" wording; Management rewrites them the day the mailbox is
reported DONE.
