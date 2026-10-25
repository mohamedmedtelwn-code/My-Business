# Platform rules that affect monetisation

- **Checked:** 2026-10-25
- **Re-check:** monthly. `tools/check.py` warns when this file is older than 30 days.
- **How to read confidence:** H = official page fetched and read; M = official page seen
  as a search excerpt; L = secondary source only. "UNVERIFIED" means do not rely on it.
- **Owner location assumed:** Qatar resident (expatriate), Qatari bank account, no foreign entity.

## Summary

| Platform | Monetisation threshold | Fees | AI-content rule | Qatar: can sell? | Qatar: can get paid? | Conf. |
|---|---|---|---|---|---|---|
| YouTube Partner Program | 1,000 subs + 4,000 public watch hours (12 mo) or 10M Shorts views (90 d). **From 1 Feb 2027 new applicants: 8,000 hours or 20M Shorts views**, still 1,000 subs. Fan funding / Shopping tier: 500 subs + 3,000 h or 3M Shorts views. | Revenue share 55% long-form / 45% Shorts (vendor sources) | "Inauthentic content" policy (15 Jul 2025): mass-produced, repetitive or templated content is not monetisable "regardless of how it was made"; AI allowed if original. Realistic synthetic content must be flagged in Studio "AI use". | Yes, Qatar is on the YPP country list | AdSense: USD 100 threshold; Qatar payout by wire or check (old table), not EFT | M |
| TikTok Creator Rewards | 10,000 followers + 100,000 views in 30 d, 18+, videos >= 1 min | n/a | Realistic AI content must be labelled; C2PA auto-labels cannot be removed | **No.** Programme open only in US, UK, DE, JP, KR, FR, MX, BR (Creator Academy, updated 10 Sep 2026) | n/a | M |
| Etsy | none | USD 0.20 listing; 6.5% transaction; processing varies by bank country; Offsite Ads 12-15% (cap USD 100); one-time shop set-up fee (~USD 15, secondary) | Creativity Standards: AI work is "Designed by" the seller and AI use must be stated in the listing; no bot-generated listings | **No.** Etsy Payments country list (fetched) does not include Qatar; a shop can only open where Etsy Payments is available | n/a | H |
| Gumroad | none | 10% + USD 0.50 per direct sale, plus card processing 2.9% + USD 0.30; 30% flat on Discover sales; 5% + 0.50 above USD 20k/month | No seller AI policy found | Yes | **Yes: bank payout to Qatar in QAR** (official list); weekly payouts; identity verification via Stripe; no Payoneer/Wise payouts | M |
| Lemon Squeezy | none | 5% + USD 0.50; payout fee 1% outside US (bank) or 3% capped USD 30 (PayPal); USD 50 minimum payout; paid 14th and 28th | Not retrieved | Yes (Qatar on supported list, per subagent excerpt) | Bank or PayPal; moving onto Stripe Managed Payments in 2026, new-seller eligibility for Qatar UNVERIFIED | M/L |
| Paddle | software and SaaS only | ~5% + USD 0.50 (secondary) | Not retrieved | Qatar not on the unsupported list | Wire or Payoneer, monthly; USD 15 SWIFT fee for some countries; individuals UNVERIFIED | L/M |
| Fiverr | none; 14-day clearance after order completion | Seller commission 20% (long-standing rule; not in retrieved excerpts, verify); buyer order fee USD 5 | Community Standards bar bulk AI output delivered to several clients; infringing AI content removed, account may be suspended (snippet) | No exclusion found; UNVERIFIED | PayPal (USD 0 fee, USD 1 min), Bank transfer via Payoneer (USD 20 min), Payoneer account (USD 10 min), Fiverr Revenue Card. "Payoneer availability depends on your country" | M |
| Upwork | none; Connects USD 0.15 each to bid | Freelancer service fee **0-15% per contract**, fixed when the proposal is sent; Freelancer Plus USD 19.99/mo | Not retrieved | No exclusion found; UNVERIFIED | Direct to Local Bank (USD 0.99; QAR UNVERIFIED), Payoneer, PayPal, wire | M |
| Amazon Associates | 3 qualifying sales within 180 days or the application is closed | n/a; US rates 1-10% by category | Not retrieved (disclosure statement required, from memory, UNVERIFIED) | Joining from Qatar UNVERIFIED | **Bank transfer only to US, UK and EUR countries (52).** Qatar bank cannot receive direct deposit; alternatives: Amazon gift card (USD 10 min) or check (USD 100 min) | H (payout), L (join) |
| Amazon KDP | none; 2 new titles per format per week (since 21 Sep 2026, secondary) | 35% or 70% royalty options | Must disclose AI-generated text, images, translations; AI-assisted editing need not be disclosed | Yes | Direct deposit where the bank country is supported (Qatar UNVERIFIED); wire/check USD 100 threshold; since 1 Aug 2026 Payoneer/Wise payouts need completed KYC | M |
| Apple App Store | none | USD 99/yr; Small Business Program 15% under USD 1M; standard 30% (memory) | No generative-AI rule; spam (4.3) and template-app (4.2.6) rules apply | Enrolment regions not published; Qatar storefront exists | Payout within 45 days; unlisted bank countries need > USD 40 balance; **whether a Qatari bank can receive payouts: UNVERIFIED** | H (fees), L (payout) |
| Google Play | none | USD 25 one-off; service fee tiers now "10/20/25% + 5% billing fee" style (page partial; read before pricing) | Not retrieved | **Yes: Qatar supports developer AND merchant registration (USD)** | Yes (merchant country) | M |

## Per-platform notes

### YouTube
- Current thresholds and the 1 Feb 2027 increase: https://support.google.com/youtube/answer/72851 ; https://support.google.com/youtube/answer/12843009
- Inauthentic content (15 Jul 2025): https://support.google.com/youtube/answer/1311392 ; YouTube's own FAQ: https://support.google.com/youtube/thread/356734251
- AI disclosure field: https://support.google.com/youtube/answer/14328491
- Country availability (Qatar listed): https://support.google.com/youtube/answer/7101720
- AdSense threshold and Qatar payout methods (old table): https://support.google.com/adsense/answer/1709871 ; https://support.google.com/adsense/answer/7164701
- Implication: a faceless, templated, AI-narrated channel is the exact profile the policy names. Only channels with an original editorial point of view should be planned, and first ad revenue is months away. Shorts RPM is USD 0.03-0.06 per 1,000 views (vendor data).

### TikTok
- Programme page: https://www.tiktok.com/creator-academy/article/creator-rewards-program ; terms: https://www.tiktok.com/legal/page/global/tiktok-creator-rewards-program-br/en
- AI labels: https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content
- Implication: TikTok is a distribution channel only for this studio. Plans may use it to drive traffic to a product or service but may not count on TikTok payouts.

### Etsy
- Eligible countries (fetched in full; Qatar absent): https://help.etsy.com/hc/en-us/articles/115015710408-Countries-Eligible-for-Etsy-Payments
- Why a shop cannot open: https://help.etsy.com/hc/en-us/articles/1500006519562-Why-Can-t-I-Open-a-Shop-in-My-Country
- Fees: https://www.etsy.com/legal/fees/ ; Creativity Standards: https://www.etsy.com/legal/creativity
- Implication: Etsy is removed from the studio's wheel until the owner has a residential address and bank account in an eligible country.

### Gumroad
- Getting paid (Qatar | QAR in bank-payout table): https://gumroad.com/help/article/13-getting-paid
- Fees: https://gumroad.com/help/article/66-gumroads-fees ; merchant of record: https://gumroad.com/pricing
- No Payoneer or Wise payouts: https://gumroad.com/help/article/223-payoneer-and-gumroad.html
- Payout settings and identity verification (via Stripe): https://gumroad.com/help/article/260-your-payout-settings-page.html

### Lemon Squeezy and Paddle
- Lemon Squeezy fees and payouts: https://docs.lemonsqueezy.com/help/getting-started/fees ; https://docs.lemonsqueezy.com/help/getting-started/getting-paid ; 2026 move to Stripe Managed Payments: https://www.lemonsqueezy.com/blog/2026-update ; supported countries: https://docs.lemonsqueezy.com/help/getting-started/supported-countries
- Paddle supported countries: https://paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle ; payouts: https://paddle.com/help/manage/get-paid/when-and-how-do-i-get-paid

### Fiverr and Upwork
- Fiverr payouts: https://help.fiverr.com/hc/en-us/articles/360010530058-Withdrawing-your-earnings-managing-payout-methods ; Payoneer set-up: https://help.fiverr.com/hc/en-us/articles/14257019400465-Setting-up-Payoneer-as-a-payout-method ; AI content standards: https://help.fiverr.com/hc/en-us/articles/37333179414289-Community-Standards-AI-generated-content ; payment terms (Oct 2026): https://www.fiverr.com/legal-portal/legal-terms/payment-terms-of-service
- Upwork fee: https://support.upwork.com/hc/en-us/articles/211062538-Learn-about-the-Freelancer-Service-Fee ; https://www.upwork.com/pricing/freelancer ; Connects: https://www.upwork.com/tools/connects-calculator ; Direct to Local Bank: https://support.upwork.com/hc/en-us/articles/211063888-How-to-withdraw-earnings-with-Direct-to-Local-Bank ; Payoneer partnership renewed May 2026: https://investor.payoneer.com/news-releases/news-release-details/payoneer-and-upwork-extend-15-year-partnership-power-global
- Market context (company filings via recaps): Fiverr active buyers fell 21.9% YoY to 2.7M (Q2 2026) as AI absorbs low-value gigs; Upwork active clients -4%. The entry-level gig segment is the shrinking one. Plans should sell outcomes, not tasks.

### Amazon
- Associates 180-day rule: https://affiliate-program.amazon.com/help/node/topic/G7MJTPEP9NC3YKMG ; payout methods: https://affiliate-program.amazon.com/help/node/topic/GGD9H76RMDDNEWAE ; 52-country bank list (fetched): https://affiliate-program.amazon.com/help/node/topic/G8VUMS6GTBCR9RGV
- KDP AI disclosure: https://kdp.amazon.com/en_US/help/topic/G200672390 ; payment options: https://kdp.amazon.com/en_US/help/topic/GJD7DFFX6X88AK46 ; thresholds: https://kdp.amazon.com/en_US/help/topic/G201207800 ; royalties: https://kdp.amazon.com/help/topic/G200644210
- Implication: Amazon Associates (US) pays a Qatar resident only in gift cards or checks. Only plan it if the owner accepts gift-card income or an amazon.sa/.ae programme is verified.

### Apple and Google
- Apple enrolment: https://developer.apple.com/support/enrollment/ ; Small Business Program: https://developer.apple.com/app-store/small-business-program/ ; minimum payment threshold: https://developer.apple.com/help/app-store-connect/reference/reporting/minimum-payment-threshold ; guidelines (updated 16 Oct 2026): https://developer.apple.com/app-store/review/guidelines/
- Google Play supported locations (Qatar: developer and merchant): https://support.google.com/googleplay/android-developer/answer/9306917 ; testing requirement for personal accounts (12 testers, 14 days): https://support.google.com/googleplay/android-developer/answer/14151465 ; service fees: https://support.google.com/googleplay/android-developer/answer/112622 ; package registration deadline 30 Sep 2026: https://support.google.com/googleplay/android-developer/answer/16984799

## Rules that bind an AI agent operating an account
- **Identity gates are owner-only:** Etsy (ID + selfie), Apple (two-factor Apple Account, Paid Apps Agreement), YouTube (2-Step Verification, AdSense), Google Play (developer identity verification), KDP (KYC for Payoneer/Wise), Gumroad (identity verification for bank payouts), Fiverr/Upwork (one account per person; verified name must match bank). Agents never do these.
- **Mass production is penalised everywhere it is visible:** YouTube inauthentic content; Etsy bot listings; KDP 2 titles per format per week; Fiverr bulk AI delivery; Apple 4.3 spam and 4.2.6 template apps. Plans must state a volume cap below the platform's published cap.
- **Disclosure duties:** YouTube AI-use field, TikTok AIGC label, Etsy listing statement, KDP AI-generated disclosure. Work agents disclose by default.
- **One account per person** (Fiverr explicit; others implied). The studio never runs two accounts on one platform.
- **Engagement manipulation** (bought views, fake reviews) is a bannable offence on every platform checked. Gate check in the rubric.

## Unverified items to confirm before relying on them
- Fiverr 20% commission text and AI policy wording; Fiverr and Upwork account availability for Qatar residents; Upwork Direct to Local Bank in QAR.
- Apple payouts to Qatari banks; Apple enrolment from Qatar.
- KDP direct deposit to a Qatar bank; Amazon Associates via amazon.sa or amazon.ae for Qatar residents.
- Lemon Squeezy new-seller onboarding for Qatar under Stripe Managed Payments; Paddle acceptance of individuals and its payout minimum.
- Gumroad minimum payout amount and KYC document list.
