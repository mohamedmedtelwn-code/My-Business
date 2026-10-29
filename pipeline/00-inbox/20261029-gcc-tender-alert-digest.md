# Idea Brief: Keyword-filtered GCC public-tender alert digest by email, Qatar first

- **Id:** 20261029-gcc-tender-alert-digest
- **Category:** 5 Software (data product on subscription; category 1 newsletter used as the free tier)
- **Method playbook:** research/playbooks/tender-alert-digest.md
- **Date:** 2026-10-29

## What it is
A daily email digest of new public tenders from the official GCC portals
(Qatar Monaqasat, Saudi Etimad, UAE and Oman portals), filtered by each
subscriber's keywords and sector, with deadline, buyer and document link, in
English and Arabic. Free weekly "Qatar tenders this week" newsletter as the
lead magnet; paid daily keyword alerts at USD 29 a month (QAR 105) sold as a
Gumroad membership. During the owner hold the product covers supplies, IT,
medical, catering, cleaning, events, training and consultancy categories only,
not construction works.

## Who pays, how much, how often
Sales and bid staff at SMEs that sell to government and semi-government
buyers in Qatar and the GCC. Incumbents charge USD 97 a month for a Gulf
subscription (TenderGlobal, 13-month plan USD 1,260) and USD 60-154 for other
regional bundles; TendersInfo lists 8,157 live Qatar tenders and 83,420 Saudi
tenders and sells daily alerts by subscription. Price to copy: USD 29 a
month, monthly recurring, with an annual option at USD 290.

## Evidence (minimum two independent sources, at least one platform-level or first-person with numbers)
| Source | URL | Date seen | Type | What it shows (numbers) |
|--------|-----|-----------|------|-------------------------|
| TendersInfo, GCC tenders page | https://www.tendersinfo.com/global-gcc-countries-tenders.php | 2026-10-29 | platform stats (incumbent's live counts) | 8,157 live Qatar tenders; 83,420 Saudi; 30,780 UAE; 28,280 Oman; sells "daily alerts" subscriptions |
| TenderGlobal / TenderUAE regional subscription offer | https://www.tenderuae.com/specialoffer.aspx | 2026-10-29 | marketplace listing (incumbent price) | Gulf subscription USD 1,260 for 13 months (USD 97/month), Levant USD 775, all countries USD 1,999; includes daily tender newsletter; offer valid to 2026-10-31 |
| Tarsiya, GCC tender portals guide | https://tarsiya.ae/guides/gcc-tender-portals | 2026-10-29 | first-person (operator of a tender-intelligence service) | Qatar Monaqasat (monaqasat.mof.gov.qa) lists tenders publicly; Oman eTendering public dashboard; Tarsiya automates Saudi and UAE portals only, Qatar not automated |
| Tenders Alerts Platform (Saudi) plans page | https://tendersalerts.com/en/plans | 2026-10-29 | vendor (context) | Paid plans for Etimad and Forsa alerts: daily newsletter, keyword search, competitor award data |
| GCC Tenders Gate (GCC Chambers) | https://gcctendergate.com/ | 2026-10-29 | platform-level (official chambers portal) | Official GCC chambers tender platform with paid subscription; one portal per country |

## Why it works now
Government procurement in the GCC is published on fragmented portals in two
languages, and the incumbents that aggregate it charge USD 60-154 a month
with clunky interfaces; Qatar's Monaqasat is public but not covered by the
newer automated services. An agent can read the public portals daily, filter
by keyword and send a clean digest at a fraction of the price, and the
free weekly newsletter builds the studio's first owned list. The studio's
Python tooling edge applies; buyers are reachable by company email.

## What would kill it
- Portal terms or technical blocks on automated reading; the product must respect robots.txt and rate limits and only use public listings.
- Incumbents cutting prices or GCC Tenders Gate offering free alerts.
- Low willingness to pay below the incumbents' enterprise buyers; needs 10+ subscribers to matter.
- Construction tenders dominate volume; excluding them during the hold shrinks the catalogue.

## Platform and payout check (from research/platform-rules.md and management/payments.md)
- Platform usable by a Qatar-resident seller: Gumroad memberships yes (route 1); email sending from the studio domain (rule 15)
- Payout route: Gumroad (bank payout in QAR), needs ticket 20261025-studio-2
- Published volume caps and disclosure duties that apply: Gumroad 10% + USD 0.50 per sale; email opt-out line and 20 cold emails a day studio-wide; public data only, no login scraping

## Capital needed (itemised)
| Item | USD | One-off / monthly |
|------|-----|-------------------|
| Studio domain (shared, already planned) | 0 | |
| Scheduled scraping on GitHub Actions free tier | 0 | monthly |
| Transactional email beyond the free tier (after 50 subscribers) | 0-15 | monthly |
**Total start:** USD 0  **Monthly run:** USD 0-15  **Funding tier:** 0

## Time
- Time to first dollar (typical, from evidence): 3-5 weeks (build 1-2 weeks, free newsletter plus 50 outreach emails, first paid subscriber within the 7-day test window if 1 in 157 cold contacts converts, Sales.co 2026)
- Monthly range at 6 months (typical small operator, from evidence; name the median if known): USD 150 - 900 (5-30 subscribers at USD 29); median unknown, no small-operator income report found
- Owner time per week after launch: 0 h (accounts only)

## Distribution
Channel 1: studio-domain email to 20 then 30 sales or bid contacts at Qatar
and GCC suppliers that appear as awardees or registered suppliers in public
award lists (non-construction categories), offering the free weekly digest
and a 14-day trial of keyword alerts. First ten customers: those suppliers.
Second channel: the free weekly "Qatar tenders this week" landing page and
newsletter (agent-published), converting readers to paid alerts; Gumroad
Discover as a third.

## Automatability
| Step | Agent / Owner / Either | Note |
|------|------------------------|------|
| Portal readers, keyword filter, digest renderer | Agent | Python, scheduled |
| Landing page and weekly newsletter | Agent | published by the agent |
| Prospect list from public award lists | Agent | business addresses only |
| Outreach emails and replies | Agent | studio domain |
| Gumroad membership product | Owner creates account; Agent drafts listing | |
| Billing, payouts | Gumroad | |

## Legal / platform notes
Public tender listings are public information; the digest links to the
source and republishes title, buyer, deadline and category only. Respect
portal robots.txt and rate limits. Income legal basis per ticket
20261025-studio-1. Owner hold: no construction-works categories until
2026-11-25.

## Research confidence
Medium. Demand and price anchors come from incumbents' live counts and
published prices; no small-operator earnings report exists for this niche,
so the ceiling is an estimate.
