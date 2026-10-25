# Getting paid from Qatar

- **Checked:** 2026-10-25 (research pass; sources in `research/STUDIO-RESEARCH.md`, section 3)
- **Status of the studio's payout route:** `not verified` (the owner sets this to `verified` in `management/config.json` after the first test payout lands)
- **Assumption:** the owner is an expatriate resident of Qatar with a personal account at a Qatari bank and no foreign company.

## The short version
1. **Gumroad** for digital products: pays to a Qatar bank in QAR, acts as merchant of record, no monthly fee. Start here.
2. **PayPal withdrawn through QNB** for services, invoices and marketplace payouts (Fiverr and Upwork both pay to PayPal). QNB has an official PayPal withdrawal service (QAR 18.20 per withdrawal, QAR 10,000 limit per transaction).
3. **Lemon Squeezy** or **Paddle** when a product is software or a subscription; **Payoneer** when a marketplace only pays that way. Each has an unverified point for Qatar; verify before building on it.
4. **A US LLC with Stripe** is a Phase 2 option, only when revenue justifies roughly USD 500 up front and USD 400 a year plus a US tax filing.
5. **Local gateways** (Dibsy, SkipCash, Sadad) need a commercial registration. Not for Phase 1.

## Ranked options

| # | Route | Available to a Qatar resident? | Merchant of record? | Fees | Payout to Qatar bank | KYC | Main blocker | Conf. |
|---|---|---|---|---|---|---|---|---|
| 1 | Gumroad | Yes (Qatar on bank-payout list, paid in QAR) | Yes, since 1 Jan 2025 | 10% + USD 0.50 + card processing 2.9% + 0.30 per direct sale; 30% on Discover sales | Direct deposit, weekly; 2-7 business days | Identity verification via Stripe; details tied to country | No Payoneer/Wise payouts; minimum payout amount not confirmed | M |
| 2 | PayPal + QNB | PayPal operates in Qatar (paypal.com/qa); QNB withdrawal service is official | No | PayPal receiving fees apply; 3% to withdraw to a US bank; QAR 18.20 per QNB withdrawal | Yes via QNB only (other banks: reported not to work); up to 7 business days | PayPal account verification | Needs a QNB account; PayPal holds/limits on new accounts are common | M |
| 3 | Lemon Squeezy | Qatar on supported list (excerpt) | Yes | 5% + USD 0.50; payout fee 1% (bank outside US) or 3% capped USD 30 (PayPal); USD 50 minimum; paid 14th and 28th | Bank or PayPal | Standard | Moving to Stripe Managed Payments in 2026; new-seller onboarding for Qatar unverified | M/L |
| 4 | Paddle | Qatar not on unsupported list | Yes | ~5% + USD 0.50 (secondary) | Wire or Payoneer, monthly; USD 15 SWIFT fee for some countries | Business verification | Software/SaaS only; acceptance of individuals and payout minimum unverified | L/M |
| 5 | Payoneer | Third-party sites say yes; no official Qatar page found | No | USD 29.95/yr if under USD 6,000 received; up to 2% to withdraw to bank | Yes (190+ countries claimed) | ID + address | Qatar availability unverified; needed for Fiverr bank transfer and Upwork wallet | L |
| 6 | Wise | Qatar on the "hold money" list, no extra restriction | No | Low FX; business account needs a business tax ID | Yes | ID | No Wise card in Qatar; receiving account details need a business account; not a sales channel | M/L |
| 7 | US LLC + Stripe + Mercury | Legal; Stripe does not serve Qatar businesses directly | Stripe is not MoR (Managed Payments is) | Atlas USD 500 one-off (Delaware, includes year-1 agent); Delaware LLC tax USD 400/yr; registered agent after year 1; Stripe 2.9% + 0.30 | Via Mercury (accepts non-resident founders) then wire to Qatar | US LLC, EIN, passport | Form 5472 + pro-forma 1120 every year (USD 25,000 penalty if missed); BOI reporting no longer required for US companies (FinCEN, Aug 2026) | M |
| 8 | Qatar bank + local gateway (Dibsy, SkipCash, Sadad, QPay) | Requires a commercial registration (CR) or the new MOCI e-commerce licence | No | Not retrieved | Yes | CR / licence | Licence eligibility for an expatriate individual unverified | L |

Stripe direct from Qatar: not available (Stripe's supported-country list excludes Qatar; a January 2026 Stripe change added QAR SWIFT as a payout *destination*, which does not create a Qatar merchant account). A reported "Stripe GCC pilot" (May 2026) rests on one secondary source: UNVERIFIED.

## Legal status of side income (read before the first sale)
- **Labour law.** Law No. 9 of 2026 (Official Gazette, 25 June 2026) amends Labour Law 14/2004. Part-time and freelance workers are placed outside the Labour Law, and the Council of Ministers may issue separate regulations for them. As of October 2026 those regulations have not been published (K&L Gates, DLA Piper, Crowell; QatarSteps). Qatar has no freelance visa. An expatriate employee may work part-time for another employer only through the Ministry of Labour's process, and the QFC asks sponsored individuals for a no-objection certificate from their sponsor.
- **Commercial registration.** MOCI launched an **E-Commerce Licence** (Decision No. 25 of 2026): online-only activities, 194 approved activities, QAR 500. A Home Licence costs QAR 1,020. Whether a non-Qatari individual (not a company) can hold either is not stated on the pages retrieved: **UNVERIFIED**. Sole proprietorships are described by secondary sources as limited to Qatari and GCC nationals.
- **Tax.** Income Tax Law 24/2018: salaries are not taxed; business income sourced in Qatar is taxed at 10% and "a self-employed individual may be subject to income tax if one derives qualifying income from sources in Qatar" (PwC, Sep 2026). Every taxpayer carrying on an activity must register with the General Tax Authority (Dhareeba).
- **What the studio does about it.** The first owner ticket of the studio is *"Confirm the legal basis for receiving income"*: employer consent, whether an e-commerce licence is needed and available, and GTA registration. Until that ticket is closed, Preparation may launch USD 0 businesses that produce drafts and audiences but may not accept money. This is an owner decision (see `CHANGELOG.md`).

## Owner steps: route 1, Gumroad (about 20 minutes)
1. Go to https://gumroad.com/signup and create an account with the studio email. Choose **Qatar** as your country. Do not change the country later; it clears your payout details.
2. Settings > Payments: add your Qatari bank account (IBAN, account name exactly as on your bank record, SWIFT). Gumroad pays in QAR.
3. Complete identity verification when prompted (government ID, date of birth, address). This is processed by Stripe on Gumroad's behalf.
4. Settings > Profile: set the studio's display name and a short bio (no personal data beyond what Gumroad requires).
5. Read https://gumroad.com/help/article/13-getting-paid and note your payout day and minimum payout threshold shown on the Payouts page. Record both in this file under "Verified details" below.
6. Tell the agent the account exists by closing the ticket with `DONE`. The agent will then upload the first product draft to your account only through a ticket (you press publish).
7. After the first sale, wait for the first payout to land in your bank. Set `"payout_route_verified": true` in `management/config.json` and add the date under "Verified details".

## Owner steps: route 2, PayPal withdrawn via QNB (about 30 minutes plus bank visit if you have no QNB account)
1. If you do not have a QNB account, open one (QNB is the only Qatari bank with an official PayPal withdrawal service: https://www.qnb.com.qa/sites/qnb/qnbqatar/page/en/enpaypalservices.html).
2. Go to https://www.paypal.com/qa/home and open a **Business** account in your own name, with the studio email and your Qatar address. Confirm the email and phone.
3. Verify the account by linking your bank card as PayPal asks. Keep a copy of PayPal's fee page for Qatar in `management/` (export to PDF) so Planning can price services correctly.
4. In QNB Internet Banking, enable the PayPal service and link your PayPal account (follow QNB's steps). Fee: QAR 18.20 per withdrawal; limit QAR 10,000 per transaction (QNB fee table).
5. Make one test: receive a small payment (for example from a friend's PayPal or a USD 1 test invoice), withdraw it to QNB, and note the time taken and fees in "Verified details".
6. Close the ticket with `DONE`. Fiverr and Upwork payouts can then be set to this PayPal account when those accounts exist.

## Verified details (owner fills in)
| Date | Route | What was verified | Fee observed | Days to arrive |
|------|-------|-------------------|--------------|----------------|
| | | | | |

## Sources (checked 2026-10-25)
- Gumroad: https://gumroad.com/help/article/13-getting-paid ; https://gumroad.com/help/article/66-gumroads-fees ; https://gumroad.com/pricing ; https://gumroad.com/help/article/223-payoneer-and-gumroad.html ; https://gumroad.com/help/article/260-your-payout-settings-page.html
- PayPal Qatar: https://www.paypal.com/qa/home ; https://www.paypal.com/mt/cshelp/article/how-do-i-withdraw-money-from-my-paypal-account-help394 (Qatar transfers up to 7 business days) ; https://www.paypal.com/is/legalhub/paypal/archive-policies-full (3% to US bank for Qatar residents) ; QNB service page: https://www.qnb.com.qa/sites/qnb/qnbqatar/page/en/enpaypalservices.html
- Lemon Squeezy: https://docs.lemonsqueezy.com/help/getting-started/fees ; https://docs.lemonsqueezy.com/help/getting-started/getting-paid ; https://docs.lemonsqueezy.com/help/getting-started/supported-countries ; https://www.lemonsqueezy.com/blog/2026-update
- Paddle: https://paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle ; https://paddle.com/help/manage/get-paid/when-and-how-do-i-get-paid
- Payoneer: https://payoneer.com/pricing/ ; https://payoneer.custhelp.com/app/answers/detail/a_id/18605/~/withdraw-to-bank---faq ; third-party availability claims: https://www.digitalbanknetworks.com/partners/payoneer/doha
- Wise: https://wise.com/help/articles/2813542/where-do-i-need-to-live-to-hold-money-with-wise ; https://wise.com/help/articles/2897226/what-is-a-wise-account
- Stripe and US LLC: https://stripe.com/global ; https://docs.stripe.com/changelog/clover/2026-01-28/cross-border-payouts-new-countries ; https://stripe.com/atlas ; https://www.nonresidentfounder.com/vendors/stripe-atlas ; https://corp.delaware.gov/alt-entitytaxinstructions ; https://www.irs.gov/pub/irs-pdf/i5472.pdf ; https://home.treasury.gov/news/press-releases/sb0603 ; https://support.mercury.com/hc/en-us/articles/28770467511060-Eligibility-and-requirements-for-opening-a-Mercury-account
- Qatar law and tax: https://www.klgates.com/thought-leadership/Qatar-Introduces-Significant-Amendments-to-the-Labour-Law-9-1-2026 ; https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/qatar-overhauls-labour-law-to-support-flexible-work-and-strengthen-worker-protections ; https://www.crowell.com/en/insights/client-alerts/qatar-labor-law-key-amendments-introduced-by-law-no-9-of-2026 ; https://qatarsteps.com/en/guides/freelance-self-sponsored-visa ; https://www.qatarliving.com/en/article/side-hustles-freelancing-qatar-young-people ; https://www.moci.gov.qa/en/news/554 (E-Commerce Licence) ; https://hukoomi.gov.qa/en/services/apply-for-a-home-license-ministry-of-commerce-and-industry ; https://www.moci.gov.qa/en/our-services/investor/commerce-faq/establishing-companies ; https://taxsummaries.pwc.com/Qatar/Individual/Taxes-on-personal-income ; https://gta.gov.qa/en/laws
