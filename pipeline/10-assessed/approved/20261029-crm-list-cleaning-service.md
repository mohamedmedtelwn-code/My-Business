# Idea Brief: Fixed-fee CRM and mailing-list cleaning for GCC SMEs

- **Id:** 20261029-crm-list-cleaning-service
- **Category:** 4 Services and gigs
- **Method playbook:** research/playbooks/list-cleaning-service.md
- **Date:** 2026-10-29

## What it is
A fixed-fee clean-up of a company's customer, lead or supplier list
(CRM export, mailing list, Excel): deduplication, Arabic and English name
and address standardisation, phone and email format checks, company
matching, flagged bounces, delivered as a clean file plus a one-page
quality report. USD 290 (QAR 1,050) for up to 5,000 records, USD 0.05 per
record above, and an optional monthly hygiene retainer at USD 60. Sold by
studio-domain email to marketing and sales leads at GCC SMEs.

## Who pays, how much, how often
Marketing, sales and operations staff at firms of 10-200 staff with a CRM
or mailing tool. Upwork: data-cleaning projects "typically cost USD 500-1,500"
(platform guidance); managed services price USD 0.05-0.50 per record and
flat USD 500-3,000 per clean-up (WissaSystems, Ivris, 2026); Implisense
sells CRM cleansing from EUR 299 with a free 48-hour quality report. One-off
per clean-up, with quarterly repeats and a retainer for a share of clients.

## Evidence (minimum two independent sources, at least one platform-level or first-person with numbers)
| Source | URL | Date seen | Type | What it shows (numbers) |
|--------|-----|-----------|------|-------------------------|
| Upwork, data cleaning professionals | https://www.upwork.com/hire/data-cleansing-freelancers | 2026-10-29 | platform stats | Projects typically USD 500-1,500; profiles at USD 5-8/h with 349-1,498 jobs and USD 100K+ earned |
| Implisense, CRM data cleansing service | https://implisense.com/en/services/crm-datenbereinigung | 2026-10-29 | marketplace listing (competitor price) | From EUR 299; free quality report in 48 hours; 60-80% of rows matchable in a typical CRM list |
| WissaSystems, data cleaning services price | https://www.wissasystems.com/blog/data-cleaning-services-price | 2026-10-29 | vendor (context) | USD 0.05-0.50 per record; flat USD 500-3,000 per defined clean-up; Upwork specialists USD 25-75/h |
| Ivris Tech, data cleansing services guide | https://ivristech.com/data-cleansing-services | 2026-10-29 | vendor (context) | Per-record USD 0.05-0.50; four pricing models; Q3 2026 |
| Cleanlist, CRM data cleaning costs | https://www.cleanlist.ai/learn/crm-data-cleaning | 2026-10-29 | vendor (context, 37-vendor pricing index) | Verification credits USD 5.30-9.90 per 1,000 addresses; managed cleanup USD 0.05-0.50 per record (DIGI-TEXX) |
| Sales.co cold email benchmark 2026 | https://sales.co/research/cold-email-statistics | 2026-10-29 | survey (2M+ emails) | Reply rate 2.09%, positive 14.1% of replies; firms with 1-10 staff reply at 2.40% |

## Why it works now
Every SME that emails customers now faces bounce-based spam filtering
(Google's 2024 rules), so dirty lists cost deliverability, and Arabic and
English duplicates ("Mohammed", "Mohamed", "محمد") defeat the built-in
CRM tools. Vendors price the work at USD 500-3,000 or per record; a
Python-driven clean-up with a native bilingual check can be offered at a
fixed USD 290 with a free quality report as the hook, exactly the
Implisense model. Buyers are reachable by company email, and the free
report gives an honest reason to write to them.

## What would kill it
- Personal data handling: lists contain personal data; the studio must process under a short agreement, delete after delivery and never reuse (Qatar PDPPL, Saudi PDPL, GDPR for EU contacts).
- Free native deduplication in HubSpot, Salesforce and Mailchimp for simple cases.
- Email verification costs USD 5-10 per 1,000 addresses if the client wants it (Tier 0 pass-through).
- Price pressure from USD 5-8/h freelancers for basic work.

## Platform and payout check (from research/platform-rules.md and management/payments.md)
- Platform usable by a Qatar-resident seller: direct invoicing yes; PayPal via QNB; Gumroad for the fixed package
- Payout route: PayPal via QNB or Gumroad (QAR)
- Published volume caps and disclosure duties that apply: email rule 15; data-processing terms in every order; no verification credits spent without a Tier 0 ticket

## Capital needed (itemised)
| Item | USD | One-off / monthly |
|------|-----|-------------------|
| Email verification credits, only when a client orders them | 5-10 per 1,000 (pass-through) | per job |
| Python tooling, free | 0 | |
**Total start:** USD 0  **Monthly run:** USD 0  **Funding tier:** 0

## Time
- Time to first dollar (typical, from evidence): 2-4 weeks (free 48-hour quality report on the prospect's own sample, then the fixed quote)
- Monthly range at 6 months (typical small operator, from evidence; name the median if known): USD 300 - 1,500 (1-5 clean-ups a month at USD 290 plus retainers); median unknown
- Owner time per week after launch: 0 h

## Distribution
Channel 1: studio-domain email to 20 then 30 marketing or sales leads at GCC
SMEs that visibly run newsletters or CRM-driven campaigns (newsletter
sign-up on site, HubSpot or Mailchimp footer), offering the free 48-hour
quality report on a 500-row sample. First ten customers: those firms.
Second channel: a landing page with a self-serve "paste 50 rows, get a
duplicate score" tool and a Gumroad package; referrals from the Excel
automation and Salla reporting clients, who share the audience.

## Automatability
| Step | Agent / Owner / Either | Note |
|------|------------------------|------|
| Prospect list, outreach, replies | Agent | business addresses only |
| Quality report on the sample | Agent | within 48 h |
| Clean-up pipeline (dedupe, normalise, Arabic transliteration map) | Agent | Python |
| Bilingual spot-check of ambiguous merges | Agent | flagged, never auto-merged |
| Data-processing terms, invoice | Agent drafts, Owner signs the first template once | |
| Delivery and deletion log | Agent | |

## Legal / platform notes
Client lists are personal data: process only under written terms, keep for
30 days, delete and confirm. No enrichment from third-party sources without
the client's lawful basis. Income legal basis per ticket 20261025-studio-1.

## Research confidence
Medium-High on price (platform guidance plus three independent vendor
ranges); Medium on GCC demand, inferred from the general market.
## Score

| # | Criterion | Score | Weight | Points | Justification |
|---|---|---|---|---|---|
| 1 | Evidence strength | 4 | 4 | 16 | Upwork project guidance, a competitor price page and a 2M-email reply-rate survey, no operator income distribution |
| 2 | Capital to first dollar | 5 | 3 | 15 | USD 0, verification credits are a pass-through |
| 3 | Time to first dollar | 4 | 4 | 16 | 2-4 weeks: free 48-hour report then a fixed quote, buyers reachable by company email |
| 4 | Automatability | 5 | 3 | 15 | agent prospects, reports, cleans and delivers, owner signs the terms template once |
| 5 | Owner time per week | 5 | 2 | 10 | 0 h |
| 6 | Earnings ceiling at 6 months | 3 (+1 edge) | 2 | 8 | USD 300-1,500 at 1-5 jobs a month on the Upwork band |
| 7 | Durability | 3 (+1 edge) | 1 | 4 | studio email plus a landing tool and referrals from sister services |
| 8 | Legal / platform clarity | 3 | 1 | 3 | personal data processing needs written terms and deletion |

**Total:** 87/100 — APPROVED (threshold 70); owner-edge bonus applied
