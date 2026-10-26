# Idea Brief: Python data-extraction and automation service for small firms

- **Id:** 20261026-python-data-extraction-service
- **Category:** 4 Services and gigs
- **Method playbook:** research/playbooks/upwork-python-data-extraction-service.md
- **Date:** 2026-10-26

## What it is
Fixed-price Python scripts that pull public web data into clean Excel or
Google Sheets (price lists, directories, listings, tender notices) and
scheduled automations that refresh them. Sold by direct outreach to small
e-commerce, trading, recruitment and research firms in the GCC, and on
Upwork as a priced catalogue project.

## Who pays, how much, how often
Owners and operations staff of small firms that copy-paste web data by hand.
Upwork fixed-price web-scraping posts cluster at USD 100-250 for a one-off
script and USD 1,000-1,500 for multi-site or expert jobs; a priced Upwork
catalogue project from one seller lists USD 1,500 for an advanced scrape with
3-day delivery. Median Python posting on Upwork: USD 30/h hourly, USD 170
median fixed budget (Upwatcher, May 2026). Purchase frequency: one-off build,
then a monthly refresh retainer (USD 50-150) for a share of clients.

## Evidence (minimum two independent sources, at least one platform-level or first-person with numbers)
| Source | URL | Date seen | Type | What it shows (numbers) |
|--------|-----|-----------|------|-------------------------|
| Upwatcher Python market report, May 2026 | https://www.upwatcher.io/market/python | 2026-10-26 | platform stats (API scrape of Upwork posts) | 3,597 Python postings in May 2026 (~75/day); median hourly USD 30 (n=1,496); median fixed budget USD 170 (n=1,364); 55.7% of fixed jobs under USD 250 |
| Upwork web-scraping job feed | https://www.upwork.com/freelance-jobs/web-scraping | 2026-10-26 | platform-level | 283 web-scraping jobs posted; sample posts at USD 100, USD 1,500 fixed; hourly intermediate posts under 30 h/week |
| Upwork web-crawling freelancer profiles (US) | https://www.upwork.com/hire/crawlers-freelancers/us | 2026-10-26 | first-person (profile stats) | One specialist: USD 40/h, 927 jobs, USD 600K+ earned; another: USD 35/h, 396 jobs, USD 100K+ |
| Upwork catalogue project, scraping with Python | https://www.upwork.com/services/product/development-it-web-scraping-data-extraction-and-data-mining-with-python-1759951218143424512 | 2026-10-26 | platform-level (listed price) | Advanced tier USD 1,500, 3-day delivery |
| Snipework Upwork market index, week 43 2026 | https://snipework.com/market/index | 2026-10-26 | platform stats (API scan) | 18,022 live posts; Web, Mobile & Software Dev 2,903 posts, median fixed USD 123, avg hourly USD 30 |

## Why it works now
Upwork's Python category still receives about 75 new posts a day, most of
them small fixed-price extraction and automation tasks that AI tools have not
removed because each site is different and someone has to own the script.
In the GCC, small traders, recruiters and agencies monitor competitor prices,
tenders and listings by hand. The owner already writes Python tooling; an
agent can draft and test each script, so delivery cost is hours, not days.

## What would kill it
- Site owners block scraping or change layout; scripts break and refresh retainers churn.
- A client asks for personal data; Qatar's PDPPL (Law 13 of 2016) and GDPR make that off-limits, so some requests must be refused.
- Upwork fee (0-15% per contract) and Connects cost; the entry-level gig segment is shrinking (Fiverr -21.9% buyers, Q2 2026).
- No-code tools (n8n, Make, AI agents) absorb the simplest jobs; posts at USD 5-50 already exist.

## Platform and payout check (from research/platform-rules.md and management/payments.md)
- Platform usable by a Qatar-resident seller: direct outreach yes; Upwork UNVERIFIED (no exclusion found, account availability unverified)
- Payout route: PayPal via QNB (route 2) for direct clients; Upwork Direct to Local Bank (QAR UNVERIFIED) or Payoneer (UNVERIFIED); Gumroad not applicable to services
- Published volume caps and disclosure duties that apply: one Upwork account per person; no bulk AI deliverables; honour robots.txt and site terms; no personal data collection without a lawful basis

## Capital needed (itemised)
| Item | USD | One-off / monthly |
|------|-----|-------------------|
| Upwork Connects (optional, 10 proposals) | 15 | monthly |
| Hosting for scheduled refresh jobs (GitHub Actions free tier) | 0 | monthly |
**Total start:** USD 0  **Monthly run:** USD 0-15  **Funding tier:** 0

## Time
- Time to first dollar (typical, from evidence): 1-3 weeks by direct outreach; 3-6 weeks on Upwork for a new profile (first bids go unanswered; evidence: Reddit reports in cycle 1 research)
- Monthly range at 6 months (typical small operator, from evidence; name the median if known): USD 300 - 1,500; median unknown, Upwork median fixed job USD 170 so 2-8 jobs a month
- Owner time per week after launch: 3-5 h (client calls, approvals, invoicing)

## Distribution
Channel 1: direct WhatsApp/LinkedIn outreach to 20 named GCC small firms
that visibly track prices or listings (e-commerce resellers, recruitment
agencies, real-estate brokers, market-research freelancers), offering one
free sample extraction (50 rows) then a fixed quote. First ten customers:
contacts from the owner's non-construction business network and members of
Qatar/UAE e-commerce and recruiter groups. Second channel: Upwork, bidding
only on fixed-price scraping posts above USD 150 with a sample attached.

## Automatability
| Step | Agent / Owner / Either | Note |
|------|------------------------|------|
| Prospect list and message drafts | Agent | Owner sends |
| Scoping call, quote | Owner | 15 min |
| Write, test, document the script | Agent | Owner reviews output file |
| Legal check (terms, personal data) | Agent drafts, Owner decides | refuse if personal data |
| Delivery, invoice, payment | Owner | PayPal/bank |
| Monthly refresh runs | Agent | scheduled |

## Legal / platform notes
Scrape only public pages, respect robots.txt and site terms, no login
bypass, no personal data (Qatar PDPPL, GDPR). Business income needs the
legal basis in ticket 20261025-studio-1 before invoicing. Upwork: one account,
verified name must match bank.

## Research confidence
Medium. Demand and prices are platform-level and current; Qatar-side demand
is inferred from GCC business practice, not measured. Upwork account access
from Qatar unverified.
## Score

| # | Criterion | Score | Weight | Points | Justification |
|---|---|---|---|---|---|
| 1 | Evidence strength | 4 | 4 | 16 | platform stats (Upwatcher medians, Upwork job feed, profile earnings) but no small-operator income distribution |
| 2 | Capital to first dollar | 5 | 3 | 15 | USD 0 |
| 3 | Time to first dollar | 4 | 4 | 16 | 1-3 weeks by outreach to firms the owner must still name |
| 4 | Automatability | 4 | 3 | 12 | agent drafts, builds and tests, owner scopes and delivers |
| 5 | Owner time per week | 3 | 2 | 6 | 3-5 h a week |
| 6 | Earnings ceiling at 6 months | 3 (+1 edge) | 2 | 8 | USD 300-1,500 at 2-8 jobs from the Upwork median fixed budget |
| 7 | Durability | 3 (+1 edge) | 1 | 4 | direct clients plus Upwork, refresh retainers repeat |
| 8 | Legal / platform clarity | 3 | 1 | 3 | public data only, Upwork access from Qatar unverified, scraping terms vary per site |

**Total:** 80/100 — APPROVED (threshold 70); owner-edge bonus applied
