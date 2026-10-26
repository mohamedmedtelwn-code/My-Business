# Idea Brief: Arabic amount-in-words (tafqeet) and bilingual invoice add-on for Google Sheets and Excel

- **Id:** 20261026-tafqeet-invoice-sheets-addon
- **Category:** 5 Software (micro-SaaS through a merchant of record)
- **Method playbook:** research/playbooks/workspace-addon-micro-saas.md
- **Date:** 2026-10-26

## What it is
A Google Sheets add-on (Workspace Marketplace) and an Excel add-in that add
=TAFQEET() and =NUM2WORDS_EN() functions with correct Arabic grammar and
currency forms (QAR, SAR, AED, KWD, BHD, OMR, EGP, USD) plus a bilingual
invoice, quotation and receipt-voucher template that fills the words line
automatically. Free tier for 20 conversions a month; Pro licence key sold
on Gumroad (USD 19 one-off per seat or USD 4 a month).

## Who pays, how much, how often
Accountants, bookkeepers and small-business owners in the GCC and Egypt who
issue invoices, cheques and vouchers with the amount written in Arabic words
("فقط ... لا غير"). Comparable Sheets utilities: Email-to-Sheets add-on,
USD 1,500/month from 60 customers on subscriptions and lifetime deals
(IndieExit, verified listing); Sync2Sheets USD 9,000 MRR from 400+ paying
users out of 40,000 installs (first-person). Base rate: ForecastSheets,
3,000 users and USD 0 after two years. Frequency: one-off licence or
monthly subscription.

## Evidence (minimum two independent sources, at least one platform-level or first-person with numbers)
| Source | URL | Date seen | Type | What it shows (numbers) |
|--------|-----|-----------|------|-------------------------|
| Sync2Sheets revenue on Indie Hackers | https://www.indiehackers.com/product/notion2sheets/revenue | 2026-10-26 | first-person (self-reported revenue) | USD 9,000/month; Indie Hustle interview: 400+ paying customers, ~40,000 installs, MVP built in 2 weeks |
| Email to Google Sheets add-on listing | https://indieexit.com/listing/email-to-google-sheets-add-on/ | 2026-10-26 | platform-level (revenue-verified sale listing) | USD 18,000/year, 60 customers, 2,000 monthly users, started Nov 2023, subscriptions and lifetime deals |
| ForecastSheets postmortem | https://developerwithacat.com/blog/202606/google-sheets-forecasting/ | 2026-10-26 | first-person (base rate) | 3,000 users, USD 0 revenue in two years; ranked top of Google and third in Marketplace search |
| Odoo app, Arabic Amount in Words (Tafqeet) | https://apps.odoo.com/apps/modules/19.0/arabic_amount_in_words | 2026-10-26 | vendor (demand signal) | Paid Odoo module for bilingual invoices "as required on bilingual invoices in Saudi Arabia and the Gulf" |
| DEV Community, the four rules behind tafqeet | https://dev.to/support_confileo_ce7442eb/spelling-numbers-in-arabic-is-harder-than-it-looks-the-four-rules-behind-tafqeet-3pgp | 2026-10-26 | first-person (maintainer of a converter used for invoices and cheques) | Naive libraries fail Arabic grammar; free web converter and MIT library exist |
| Dynamics Community blog, Arabic and English amount in words for Excel | https://community.dynamics.com/blogs/post?postid=91b69185-7c71-4c20-8e10-6c11df635f08 | 2026-10-26 | first-person (demand signal) | Author reports "many requests across the years" for an Excel version; free VBA shared in 2014 |
| With Jhinna, why build for Google Workspace | https://www.withjhinna.com/blog/why-google-workspace-addons/ | 2026-10-26 | first-person (context) | Marketplace fee 0%; Stripe ~3%; "relatively uncrowded" |

## Why it works now
Every invoice, cheque and voucher in the Gulf carries the amount in Arabic
words, and the free VBA scripts in circulation get the grammar and the
fractions wrong (user complaints on the 2008 and 2014 scripts). Saudi
e-invoicing and GCC VAT pushed small firms into Sheets and Excel templates.
The Workspace Marketplace takes no fee and is thinly populated; Gumroad
handles licence keys and pays to a Qatar bank. The owner's Excel skill and
an agent that writes and tests the grammar engine make the build a week.

## What would kill it
- Free tools (web converters, VBA, the MIT library) are good enough for most users; conversion to paid stays under 1-2% (Sync2Sheets ~1%, Chrome-extension reports 2-5%).
- Google OAuth verification for a Sheets add-on takes weeks and needs a privacy policy and a verified domain (USD 12/yr).
- Microsoft AppSource listing needs a Partner Center account; Excel side may stay a downloadable .xlam sold on Gumroad.
- Accounting software (Odoo, Zoho, QuickBooks) adds the feature natively.

## Platform and payout check (from research/platform-rules.md and management/payments.md)
- Platform usable by a Qatar-resident seller: Gumroad yes (route 1); Google Workspace Marketplace publishing from Qatar UNVERIFIED (Google Cloud project, OAuth verification); Lemon Squeezy UNVERIFIED for new Qatar sellers
- Payout route: Gumroad (bank payout in QAR); needs ticket 20261025-studio-2
- Published volume caps and disclosure duties that apply: Marketplace listing review and OAuth scopes; Gumroad 10% + USD 0.50 per direct sale; privacy policy required

## Capital needed (itemised)
| Item | USD | One-off / monthly |
|------|-----|-------------------|
| Domain for privacy policy and docs | 12 | yearly |
| Google Cloud project, Apps Script (free) | 0 | monthly |
| Gumroad (no fixed fee) | 0 | monthly |
**Total start:** USD 12  **Monthly run:** USD 0  **Funding tier:** 0

## Time
- Time to first dollar (typical, from evidence): 4-8 weeks (build 1-2 weeks, Marketplace review 2-4 weeks; Gumroad .xlam can sell from week 2)
- Monthly range at 6 months (typical small operator, from evidence; name the median if known): USD 0 - 300; the base rate for Sheets utilities is near zero (ForecastSheets), the median indie app is under USD 50/month (Froxi 2026)
- Owner time per week after launch: 1-2 h (support, publishing)

## Distribution
Channel 1: Arabic accounting and bookkeeping groups (Facebook, Telegram,
LinkedIn) where tafqeet questions recur, posting the free converter and the
template; and direct messages to 20 small accounting firms and freelance
bookkeepers in Qatar, Saudi and Egypt offering the Pro licence free for a
testimonial. First ten customers: those bookkeepers plus buyers of the
studio's finance-tracker templates (same Gumroad store). Second channel:
Workspace Marketplace search ("Arabic", "number to words", "invoice") and a
free web converter page that links to the add-on; Google organic is not
counted as a channel on its own.

## Automatability
| Step | Agent / Owner / Either | Note |
|------|------------------------|------|
| Grammar engine, tests against known cases | Agent | 8 currencies, fractions, masculine/feminine |
| Apps Script add-on and .xlam add-in | Agent | |
| Templates (invoice, quote, voucher) | Agent | bilingual |
| Google Cloud project, OAuth consent, Marketplace listing | Owner | identity-gated |
| Gumroad product and licence keys | Owner publishes, Agent drafts | |
| Group posts and outreach | Agent drafts, Owner sends | |
| Support replies | Agent drafts, Owner sends | |

## Legal / platform notes
No financial advice; templates are not tax-compliant e-invoices (Saudi
ZATCA requires certified solutions; say so). Privacy policy and minimal
OAuth scopes. Gumroad account per ticket 20261025-studio-2; income basis
per ticket 20261025-studio-1.

## Research confidence
Medium-Low. The add-on monetisation model is documented with numbers, but
no sales data exists for this specific niche; demand is shown by requests
and free tools, not by purchases.
