# Idea Brief: Automated weekly sales and stock reports for Salla and Zid merchants

- **Id:** 20261029-salla-zid-merchant-reporting
- **Category:** 4 Services and gigs (reporting as a service; category 5 app on the Salla and Zid stores as a later step)
- **Method playbook:** research/playbooks/ecommerce-platform-reporting-service.md
- **Date:** 2026-10-29

## What it is
A monthly subscription that connects a Salla or Zid store through the
platform API (the merchant authorises a studio app, no password shared) and
delivers every Monday a Google Sheets dashboard and a one-screen Arabic and
English summary: sales by product, city and payment method, repeat-customer
share, low-stock list, refunds. Sold by studio-domain email to merchants
whose store sites publish a business address. Price USD 49 a month
(SAR 185) after a free two-week pilot.

## Who pays, how much, how often
Owners of Saudi and Gulf online stores on Salla (68,000+ active merchants,
USD 13.3B processed, official) and Zid (about 10,000-14,000 active stores,
StoreLeads 2026). Zid gates "detailed analysis of orders and customers" and
"exporting sales reports" to its Professional plan at SAR 18,000 a year;
Salla's help centre tells merchants to link order data to Google Data Studio
or Excel for weekly reports via Zapier. Recurring monthly; typical tenure
unknown.

## Evidence (minimum two independent sources, at least one platform-level or first-person with numbers)
| Source | URL | Date seen | Type | What it shows (numbers) |
|--------|-----|-----------|------|-------------------------|
| Salla official information page | https://salla.com/en/ai-info | 2026-10-29 | platform stats | 68,000+ active merchants; USD 13.3B processed; 900+ integrations; built-in dashboards plus Google Analytics |
| StoreLeads, state of Salla 2026 | https://storeleads.app/reports/salla | 2026-10-29 | platform stats (third-party crawl) | 26,284 active stores detected in Q4 2026; 50% of Salla stores (13,169) publish an email address, 28% a phone number |
| StoreLeads, state of Zid 2026 | https://storeleads.app/reports/zid | 2026-10-29 | platform stats (third-party crawl) | 14,439 active Zid stores in Q4 2026; 41% publish an email (5,957); 80% a phone |
| Zid pricing page | https://zid.sa/en/pricing | 2026-10-29 | platform-level (price anchor) | Lite SAR 83/month with "basic analytics"; Professional SAR 18,000/year includes "detailed analysis of orders and customers" and "exporting and printing sales reports" |
| Salla help centre, Zapier integration | https://help.salla.sa/en/article/integration-with-zapier-platform/ftl5qsb41goyjq6o0ecxdohn | 2026-10-29 | platform-level (demand signal) | Lists "automatically generating sales reports" by linking order data to Data Studio or Excel as a use case |
| Salla developer docs | https://docs.salla.dev/ | 2026-10-29 | platform-level (feasibility) | Merchant REST APIs, OAuth access tokens, webhooks, app store; 60,000+ stores reachable by apps |
| Upwork dashboard freelancers (cycle 1 source) | https://www.upwork.com/hire/dashboard-freelancers/ | 2026-10-25 | platform stats (price anchor) | Dashboard projects typically USD 500-2,500 |

## Why it works now
Tens of thousands of Gulf merchants run on two platforms whose built-in
reporting is basic on the plans most of them buy, and the platforms
themselves point merchants to Sheets and Data Studio for proper reports.
Half of Salla stores publish an email address, so the agents can prospect
without any personal network. The API lets the merchant authorise access in
two clicks. Python tooling is an owner-edge skill; the agent builds and runs
the pipeline.

## What would kill it
- Salla or Zid adding rich reporting to cheap plans.
- Salla Partners app review requirements or a developer account that needs a Saudi commercial registration (UNVERIFIED).
- API rate limits or token refresh failures breaking Monday reports.
- Merchants treating USD 49 as high against SAR 83 platform fees; the pilot must show a decision the report changed.

## Platform and payout check (from research/platform-rules.md and management/payments.md)
- Platform usable by a Qatar-resident seller: direct subscription billing through Gumroad membership yes; Salla Partners developer account from Qatar UNVERIFIED; Zid app store UNVERIFIED
- Payout route: Gumroad (QAR) or PayPal via QNB for invoices
- Published volume caps and disclosure duties that apply: Salla API rate limits and 14-day tokens with refresh; merchant data stays in the merchant's own Google Sheet; email rule 15

## Capital needed (itemised)
| Item | USD | One-off / monthly |
|------|-----|-------------------|
| Scheduled jobs on GitHub Actions free tier | 0 | monthly |
| Salla Partners account | 0 (UNVERIFIED) | one-off |
**Total start:** USD 0  **Monthly run:** USD 0  **Funding tier:** 0

## Time
- Time to first dollar (typical, from evidence): 4-6 weeks (app build and partner approval 2-3 weeks, pilot 2 weeks, then first paid month)
- Monthly range at 6 months (typical small operator, from evidence; name the median if known): USD 250 - 1,500 (5-30 merchants at USD 49); median unknown
- Owner time per week after launch: 0 h (developer account and Gumroad only)

## Distribution
Channel 1: studio-domain email to 20 then 30 Salla and Zid merchants with a
published business address in categories with repeat purchase (coffee,
beauty, abayas, perfume, supplements), offering the free two-week report
pilot. First ten customers: those merchants, found through the store sites
themselves. Second channel: a listing on the Salla App Store and Zid App
Market once the app is approved (studio brand), plus a landing page with a
sample report.

## Automatability
| Step | Agent / Owner / Either | Note |
|------|------------------------|------|
| Prospect list from store sites | Agent | business addresses only |
| Outreach, pilot onboarding emails | Agent | |
| App build, OAuth flow, weekly pipeline, Sheets dashboard | Agent | Python |
| Salla Partners and Zid developer accounts | Owner | identity-gated |
| App store listing copy | Agent drafts, Owner publishes | |
| Weekly reports and support replies | Agent | |

## Legal / platform notes
Merchant data accessed only through the authorised API scopes, stored in
the merchant's own Sheet, deleted on cancellation (Saudi PDPL, Qatar
PDPPL). Not tax advice; ZATCA e-invoicing untouched. Income legal basis per
ticket 20261025-studio-1.

## Research confidence
Medium. Merchant counts, reporting gaps and reachability are platform-level;
willingness to pay USD 49 and the developer-account access from Qatar are
unverified.
## Score

| # | Criterion | Score | Weight | Points | Justification |
|---|---|---|---|---|---|
| 1 | Evidence strength | 4 | 4 | 16 | official merchant counts, third-party store crawls, platform pricing that gates reports, help-centre demand signal |
| 2 | Capital to first dollar | 5 | 3 | 15 | USD 0 |
| 3 | Time to first dollar | 3 | 4 | 12 | 4-6 weeks: app build, pilot, then first paid month |
| 4 | Automatability | 5 | 3 | 15 | agent builds, prospects, onboards and runs weekly reports, owner holds the developer account |
| 5 | Owner time per week | 5 | 2 | 10 | 0 h |
| 6 | Earnings ceiling at 6 months | 3 (+1 edge) | 2 | 8 | USD 250-1,500 at 5-30 merchants |
| 7 | Durability | 3 (+1 edge) | 1 | 4 | studio email plus app-store listing, monthly recurring |
| 8 | Legal / platform clarity | 3 | 1 | 3 | developer-account eligibility from Qatar unverified, merchant data stays in their Sheet |

**Total:** 83/100 — APPROVED (threshold 70); owner-edge bonus applied
