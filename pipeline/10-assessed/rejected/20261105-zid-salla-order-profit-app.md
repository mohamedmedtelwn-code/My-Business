# Idea Brief: Order-profit and fee tracking app on the Zid and Salla app markets

- **Id:** 20261105-zid-salla-order-profit-app
- **Category:** 3 Marketplaces and app stores (software, category 5 method)
- **Method playbook:** research/playbooks/zid-salla-app.md
- **Date:** 2026-11-05

## What it is
A subscription app listed on the Zid App Market and the Salla App Store
that shows a Saudi or GCC merchant the real profit of every order after
product cost, payment-gateway fees, shipping, discounts, VAT and app
subscriptions, with a daily Arabic-English summary and a monthly
statement. SAR 49 (USD 13) a month per store with a 14-day trial. The
productised version of the reporting service already in validation
(20261029-salla-zid-merchant-reporting); the two share prospects and the
service hands clients to the app once it is live.

## Who pays, how much, how often
Owners of Zid and Salla stores doing 50-2,000 orders a month who cannot
see margin per order in the platform's own reports. Zid: 13,500+ active
stores, 71% of merchants use at least one paid app, median partner
revenue growth 30% a year, apps earning revenue up 60% (Zid partner page,
2026-11-05). Salla: 60,000+ merchants, 500+ app developers, earnings
example SAR 4,130 a month for 100 subscriptions at SAR 59 (about 70% to
the developer). Monthly subscription per store.

## Evidence (minimum two independent sources, at least one platform-level or first-person with numbers)
| Source | URL | Date seen | Type | What it shows (numbers) |
|--------|-----|-----------|------|-------------------------|
| Zid, app partners page | https://zid.sa/en/partners/developers/apps | 2026-11-05 | platform stats | 13,500+ active stores; 71% use at least one paid app; 30% median annual growth in partner revenue; +60% apps earning revenue |
| Zid Partners help, app payouts | https://help-partner.zid.sa/en/articles/11501759-app-payouts | 2026-11-05 | platform (payout page) | Monthly payouts; subscription apps on a 20% default rate in the partner agreement; non-Saudi partners invoice in USD (subscription apps only) |
| Salla Partners, build apps | https://partners.salla.com/en/apps | 2026-11-05 | platform stats | 60,000+ merchants; 500+ app developers; estimate SAR 4,130 a month for 100 subscriptions at SAR 59 |
| Salla Partners home | https://partners.salla.com/en | 2026-11-05 | platform stats | 1,000+ verified partners; SAR 9,999,700 cumulative partner earnings; 59,700+ active stores |
| Zid Developers FAQ | https://developers.zid.sa/ | 2026-11-05 | platform (terms) | No listing fee; revenue share set in a signed agreement; 11 app categories including Analytics and Reports |
| Week One Labs, Shopify app benchmarks 2026 | https://weekonelabs.com/blog/shopify-app-revenue-benchmarks-2026 | 2026-11-02 | survey (context from the comparable Shopify market) | Median listed app under USD 1,000/month; install-to-paid 8-18% with strong onboarding; first 50 reviews decide discovery |

## Why it works now
Both platforms publish partner numbers that show a paid-app habit
(71% of Zid merchants pay for at least one app) and a small developer
pool (500 on Salla against 11,000 on Shopify), so a focused single-feature
app faces far less competition than on Shopify, where the same idea was
rejected last cycle. Profit-per-order is the first question the
reporting-service prospects ask, and the app is the same calculation run
automatically. Zid pays non-Saudi partners in USD by monthly invoice, and
the app can be marketed to merchants by the studio's existing email
channel and through the partner's own ad packages.

## What would kill it
- Payout route for a Qatar partner: Zid's page confirms USD invoicing for non-Saudi partners but not the transfer method; Salla's is unverified. Both need an owner ticket to open the partner accounts.
- Review and approval time on both markets (weeks) and a signed partner agreement per app.
- Shopify's lesson: the median app earns under USD 1,000 a month and discovery needs reviews; the email channel must carry the first installs.
- Platform-native profit reports could arrive at any time.

## Platform and payout check (from research/platform-rules.md and management/payments.md)
- Platform usable by a Qatar-resident seller: partner sign-up open to non-Saudi developers (Zid: USD invoices for non-Saudi partners); Salla unverified
- Payout route: Zid partner payout in USD (bank transfer method unverified); Salla unverified; neither is Gumroad or PayPal, so a new row in payments.md is needed before launch
- Published volume caps and disclosure duties that apply: partner agreements and quality standards per platform; merchant data under written terms

## Capital needed (itemised)
| Item | USD | One-off / monthly |
|------|-----|-------------------|
| Partner accounts (free), development stores (free) | 0 | |
| Hosting for the app backend (free tier to start) | 0 | 0-5 later |
**Total start:** USD 0  **Monthly run:** USD 0  **Funding tier:** 0

## Time
- Time to first dollar (typical, from evidence): 2-3 months (build 3-4 weeks, review and agreement 2-6 weeks, 14-day trial), so a presale test by email comes first
- Monthly range at 6 months (typical small operator, from evidence; name the median if known): USD 0 - 650 (0-50 stores at USD 13); the Shopify median for a listed app is under USD 1,000; median unknown for Zid and Salla
- Owner time per week after launch: 0 h after two partner accounts are opened

## Distribution
Channel 1: studio-domain email to 20 then 30 Zid and Salla merchants
(store contact addresses) offering a free profit statement for last
month built from an order export, with the app's trial as the follow-on;
the reporting-service prospect list is shared. First ten customers: those
stores. Second channel: the Zid and Salla app markets themselves and the
reporting service's deliveries, which carry the app link.

## Automatability
| Step | Agent / Owner / Either | Note |
|------|------------------------|------|
| Build the app, listing copy, screenshots | Agent | Zid and Salla APIs |
| Partner accounts, agreements, identity checks | Owner, via tickets | |
| Submission, review fixes, support | Agent | |
| Merchant outreach and presale test | Agent | business addresses only |
| Billing and payouts | Platform | reconciled in the ledger monthly |

## Legal / platform notes
Partner agreements signed by the owner; merchant order data processed
under written terms and never shared; VAT on Saudi sales handled by the
platform where the agreement says so. Income legal basis per ticket
20261025-studio-1.

## Research confidence
Medium: platform-level numbers are strong, but no first-person developer
income report for Zid or Salla was found, the payout transfer method is
unverified, and the comparable Shopify median is low.

## Score

| # | Criterion | Score | Weight | Points | Justification |
|---|---|---|---|---|---|
| 1 | Evidence strength | 3 | 4 | 12 | platform-level numbers from Zid and Salla, but no first-person developer income and the only comparable median (Shopify) is under USD 1,000 |
| 2 | Capital to first dollar | 5 | 3 | 15 | USD 0, partner accounts and development stores are free |
| 3 | Time to first dollar | 2 | 4 | 8 | 2-3 months: build, market review and a signed agreement before any subscription can bill |
| 4 | Automatability | 4 | 3 | 12 | agent builds, submits and supports, owner opens two partner accounts, signs agreements and passes identity checks |
| 5 | Owner time per week | 5 | 2 | 10 | 0 h after set-up |
| 6 | Earnings ceiling at 6 months | 2 (+1 edge) | 2 | 6 | USD 0-650 at 0-50 stores, no evidence of small-developer earnings on these markets |
| 7 | Durability | 3 (+1 edge) | 1 | 4 | two app markets plus studio email and the reporting service |
| 8 | Legal / platform clarity | 2 | 1 | 2 | Zid pays non-Saudi partners in USD but the transfer method is unverified and Salla eligibility is unverified |

**Total:** 69/100 — REJECTED (threshold 70); owner-edge bonus applied


## Rejected: 69/100, below the 70 threshold
Lowest criteria: time to first dollar (2, a 2-3 month build and review before any subscription bills), legal and platform clarity (2, Zid's transfer method to a non-Saudi partner and Salla's eligibility are unverified) and earnings ceiling (2, no small-developer income evidence on either market). Research may resubmit once a Zid or Salla partner payout route to Qatar is verified in management/payments.md and the merchant-reporting service (20261029-salla-zid-merchant-reporting) has passed its validation, which would supply the first installs and the missing demand evidence.
