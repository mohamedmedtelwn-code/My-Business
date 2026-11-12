# Idea Brief: Bilingual website privacy-and-consent pack for Saudi and UAE businesses (PDPL)

- **Id:** 20261112-gcc-website-privacy-compliance-pack
- **Category:** 4 Services and gigs
- **Method playbook:** research/playbooks/website-privacy-compliance-pack.md
- **Date:** 2026-11-12

## What it is
A fixed-fee pack that brings a business website in line with the Saudi
Personal Data Protection Law (PDPL) and the UAE federal data protection law
on the points visible from outside: a scan of what the site loads before
any consent (Google tags, Meta pixel, chat widgets), a privacy notice and a
cookie notice in Arabic and English written from that scan and structured
on SDAIA's August 2024 guideline (controller identity, data collected,
purposes, retention, transfers, rights, contact), consent-banner wording in
both languages, and a one-page instruction sheet for the site's developer
on loading tags only after consent (Google Consent Mode v2). USD 190
(QAR 690) per website, delivered in 3 days; optional USD 19 a month for a
monthly re-scan and notice updates when the law or the site's tools change.
Sold by studio-mailbox email to owners and marketing managers of 5-50-staff
firms in Saudi Arabia and the UAE whose site the scan already shows loading
trackers with no banner or carrying no privacy notice. Not legal advice;
every document carries that line and the regulated sectors (health,
finance) are pointed to a licensed lawyer for review.

## Who pays, how much, how often
Online stores, clinics, agencies, schools and service firms with a contact
form, booking tool or analytics on their site. Arqam360 sells "just the
policies" (privacy and cookie policy in Arabic, French and English, written
from a scan) at USD 149 one-time per website and a banner-plus-policies
year at USD 1,499; WaqiSec sells a PDPL starter (bilingual notice plus
records, breach and rights procedures) at USD 1,500; Waqi.ai's scan plan is
SAR 299 a month. One pack per website, then a small monthly retainer for
re-scans; a firm with several brands buys several packs.

## Evidence (minimum two independent sources, at least one platform-level or first-person with numbers)
| Source | URL | Date seen | Type | What it shows (numbers) |
|--------|-----|-----------|------|-------------------------|
| Arqam360, Gulf Website Privacy Readiness Index 2026 (open data, CC BY 4.0) | https://arqam360.com/gulf-privacy-readiness-index | 2026-11-03 | survey with stated sample (monthly scan) | 60% of 1,556 Saudi online stores (Sept 2026) and 51% of 547 UAE business websites (Oct 2026) load advertising or analytics tools with no consent banner |
| arXiv 2602.18616, Evaluating PDPL compliance in e-commerce websites | https://arxiv.org/pdf/2602.18616 | 2026-10-16 | academic study (100 Saudi e-commerce sites, double-coded) | 9% of sites had no privacy policy; 31% failed a further requirement; "Saudi e-commerce websites remain far from compliant" |
| A&O Shearman, Enforcement of the Saudi PDPL | https://www.aoshearman.com/en/insights/enforcement-of-the-saudi-personal-data-protection-law | 2026-01-27 | law-firm note | Grace period ended Sept 2024; committees now impose fines up to SAR 5 million per violation, doubled for repeat offences |
| Arqam360, Saudi PDPL compliance page | https://arqam360.com/regulations/saudi-pdpl | 2026-10-13 | vendor (cites SDAIA announcement, IAPP) | SDAIA confirmed 48 enforcement decisions on 16 January 2026; draft amendments to the Implementing Regulation opened 6 Oct 2026 |
| DLA Piper, Data protection laws of the world: Saudi Arabia | https://www.dlapiperdataprotection.com/?c=SA | 2026-02-11 | law-firm reference | Warning or fine up to SAR 5 million; "as at February 2026 the PDPL is being actively enforced by SDAIA" |
| Arqam360, pricing | https://arqam360.com/ | 2026-11-12 | marketplace listing (competitor price) | Policy pack USD 149 one-time per website (Arabic, French, English, written from a scan, 3 working days); banner plus policies USD 1,499 a year |
| WaqiSec, PDPL privacy notice guide and starter package | https://waqisec.com/en/guides/pdpl-privacy-notice | 2026-10-01 | vendor (competitor price) | Bilingual notice plus procedures at a fixed USD 1,500 in 7 days; notice structure per Articles 12-13 and SDAIA's Aug 2024 guideline |
| Waqi.ai, from website scan to full GRC | https://waqi.ai/blog/from-website-scan-to-full-grc-how-saudi-smes-can-operationalize-pdpl-without-a-c | 2026-05-13 | vendor (context) | Scan Pro SAR 299 a month; "the website is the most common blind spot"; no SME exemption in the PDPL |
| Adyft, UAE PDPL for small business websites | https://www.adyft.com/blog/uae-pdpl-website-privacy-small-business | 2026-10-15 | vendor (context) | UAE penalty schedule still unpublished in 2026; consent and a privacy page expected; DIFC and ADGM have their own regimes |
| Sales.co cold email benchmark 2026 | https://sales.co/research/cold-email-statistics | 2026-10-29 | survey (2M+ emails) | Reply rate 2.09%, positive 14.1% of replies |

## Why it works now
The Saudi PDPL has been enforced since September 2024 with 48 published
decisions by January 2026 and fines up to SAR 5 million, and the UAE law is
in force with its penalty schedule still pending; yet 60% of Saudi stores
and 51% of UAE business sites scanned in autumn 2026 load trackers with no
consent banner, and a tenth of Saudi stores have no privacy policy at all.
The fault is visible from outside: a headless browser visit shows which
third-party tags load before any click and whether a privacy link exists,
so the first email states a true finding about the prospect's own site.
Delivery is text (two notices, banner wording, a developer sheet) in the
studio's two languages, with Playwright already in the runner, at zero
cost. The USD 149-1,500 competitor band leaves room at USD 190 with a
bilingual scan report attached.

## What would kill it
- A client treating the pack as legal certification; every document says it is not legal advice, regulated sectors are sent to a lawyer, and the studio never claims compliance, only the documents and the findings.
- Platforms shipping their own banners (Shopify, Salla, Zid): the pack still sells the notices and the before-consent fix, which the platform banner does not provide.
- Sites built by agencies that will not change tag loading; the pack delivers the instruction sheet and the client decides.
- SDAIA's October 2026 draft amendments changing notice requirements; the monthly retainer exists for exactly that.

## Platform and payout check (from research/platform-rules.md and management/payments.md)
- Platform usable by a Qatar-resident seller: direct invoicing yes; Gumroad product for the pack and subscription for the re-scan
- Payout route: Gumroad (QAR) or PayPal via QNB
- Published volume caps and disclosure duties that apply: email rule 15 (20 cold emails a day, business addresses, opt-out line); public page loads only, no form submissions, no account creation on the prospect's site

## Capital needed (itemised)
| Item | USD | One-off / monthly |
|------|-----|-------------------|
| Playwright scan in the runner, document templates, the studio mailbox | 0 | |
**Total start:** USD 0  **Monthly run:** USD 0  **Funding tier:** 0

## Time
- Time to first dollar (typical, from evidence): 2-3 weeks (finding in the first email, fixed fee on reply, 3-day delivery)
- Monthly range at 6 months (typical small operator, from evidence; name the median if known): USD 400 - 1,500 (2-6 packs a month at USD 190 plus 10-30 sites on the USD 19 re-scan); median unknown
- Owner time per week after launch: 0 h

## Distribution
Channel 1: studio-mailbox email to 20 then 30 owners or marketing managers
of 5-50-staff firms in Saudi Arabia and the UAE whose site the scan shows
loading trackers before consent or carrying no privacy notice, each email
quoting the tags found and the missing notice. First ten customers: those
firms. Second channel: a free "scan your site" page on the studio's free
hosting with a Gumroad pack; cross-sell to every website-audit and
email-authentication prospect, whose domains the studio already knows.

## Automatability
| Step | Agent / Owner / Either | Note |
|------|------------------------|------|
| Prospect list from public directories and the audit lists, headless scan, outreach | Agent | business addresses only; public page loads only |
| Scan report, bilingual notices, banner text, developer sheet | Agent | SDAIA guideline structure; disclaimer on every page |
| Monthly re-scan, update note, invoice | Agent | scheduled |

## Legal / platform notes
The pack is a document and findings service, not legal advice, and says so;
no compliance guarantee is given. Only public page loads are made; no
personal data is collected from the prospect's site. Income legal basis per
ticket 20261025-studio-1. Zero-cost rule (owner decision 2026-11-12): every
tool is free.

## Research confidence
High on demand (two independent scans with stated samples, enforcement
confirmed by two law firms) and on price (two competitor price pages, one
vendor plan); Medium on GCC conversion by email from a free mailbox.

## Score

| # | Criterion | Score | Weight | Points | Justification |
|---|---|---|---|---|---|
| 1 | Evidence strength | 5 | 4 | 20 | two independent scans with stated samples (1,556 Saudi stores and 547 UAE sites), one academic study of 100 sites, enforcement confirmed by two law firms, two competitor price pages, no operator income distribution |
| 2 | Capital to first dollar | 5 | 3 | 15 | USD 0: Playwright in the runner, document templates, the free studio mailbox |
| 3 | Time to first dollar | 4 | 4 | 16 | 2-3 weeks: the fault is proven in the first email, fixed fee on reply, 3-day delivery |
| 4 | Automatability | 5 | 3 | 15 | agent scans, drafts both notices and the banner text, re-scans monthly and invoices |
| 5 | Owner time per week | 5 | 2 | 10 | owner does nothing |
| 6 | Earnings ceiling at 6 months | 3 | 2 | 6 | USD 400-1,500 at 2-6 packs a month plus 10-30 sites on the USD 19 re-scan |
| 7 | Durability | 4 | 1 | 4 | the law is in force with active enforcement and amendments pending, and the retainer tracks changes |
| 8 | Legal / platform clarity | 4 | 1 | 4 | document service with a not-legal-advice line, public page loads only, studio email rule 15, regulated sectors referred to a lawyer |

**Total:** 90/100 — APPROVED (threshold 70)

