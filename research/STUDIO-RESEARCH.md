# Studio research: evidence pass before hardening

- **Checked:** 2026-10-25
- **Purpose:** ground the studio's rubric, category wheel, validation threshold, kill/scale defaults, payout plan and tooling in current evidence instead of assumptions.
- **How it was done:** nine research threads ran in parallel (one per question below, the category wheel split in three), each producing a claim ledger (`research/evidence/`). The lead then re-checked the decision-relevant claims against official pages. Everything cited carries a URL. Confidence: **H** official page read in full; **M** official page seen as a search excerpt; **L** secondary source only. **UNVERIFIED** means it must not be treated as fact.
- **Limits:** the research tools could open very few pages directly (platform help centres were mostly readable only as excerpts). Numbers from company filings were read through recaps. Where that matters, the text says so. Nothing in this file is invented; where no figure was found, it says "no data".

## 0. What the evidence changes (summary of decisions)

| # | Change | Driven by | Where it lands |
|---|--------|-----------|----------------|
| 1 | **Etsy, TikTok Creator Rewards and Amazon Associates (US) leave the wheel** for this owner: Etsy Payments is not available in Qatar; TikTok's programme covers eight countries; Associates pays Qatar only by gift card or check. | Section 2 | rubric gate, category wheel |
| 2 | **Category 10 (finance-adjacent) is removed** and replaced by **professional tooling and expertise products**: crypto is restricted through Qatari banks and there was no earnings evidence for the rest; the owner-edge market has priced anchors. | Sections 1, 5 | category wheel |
| 3 | **Validation keeps "3 signals, 7 days, park" but gains denominators and weights**: 50 outreach messages (sequential 20 then 30), 100 qualified visitors with 8% sign-up, or 20 direct pre-sale asks; a payment counts as 3 signal units, an email sign-up as a third. Results under the denominator are "inconclusive" and get one 7-day extension. | Section 4 | CLAUDE.md rule 10, validation brief, `tools/signals.py` |
| 4 | **Rubric weights move**: Evidence 3 to 4, Capital 5 to 3, Time to first dollar 3 to 4. Capital no longer discriminates because every plan is USD 0 by rule; the 90-day Phase 1 makes time the binding constraint; evidence quality is where the spread is. New gates: platform and payout available to a Qatar seller; volume below platform caps; no mass-produced AI content. | Sections 1, 2, 7 | `templates/scoring-rubric.md` |
| 5 | **Payout plan**: Gumroad first (pays QAR to a Qatar bank), PayPal via QNB second; US LLC with Stripe is a Phase 2 option; the owner must confirm the legal basis for side income before the first sale. | Section 3 | `management/payments.md` |
| 6 | **Operational rules added**: ticket older than 3 days flagged, older than 7 days pauses the business; studio-wide cap of 10 open tickets; "no number without a source"; platform rules re-read monthly; every run logged and locked; three failed runs in a row open a circuit breaker; payout route verified before money is accepted. | Sections 6, 7 | `tools/check.py`, `tools/runlog.py`, SKILL files |
| 7 | **Expectations reset**: at month 6 the median small operator earns roughly USD 0 on content platforms, under USD 50 to 150 a month on apps and indie SaaS, and the fastest route to a first dollar is a service sold to a known buyer. The README says so. | Section 1 | README, idea-brief template |

## 1. Evidence base for the category wheel

### 1.1 Summary

| Category | Time to first dollar (small operator) | Month-6 monthly range (median-ish) | Evidence quality | Mostly course-sellers? | Qatar feasibility | Verdict for the wheel |
|---|---|---|---|---|---|---|
| 1 Content platforms | YouTube: months (1.86% of sub-1,000 channels with 1-11 uploads reach 1,000 subs within 360 days; 30.77% with 52+ uploads). Newsletters: median 66 days (beehiiv, self-reported). Podcasts: no data. | YouTube ~USD 0 (most channels never clear YPP); newsletters tens of USD at a 0.62% median free-to-paid; podcasts ~USD 0 (median episode 27 downloads). | Platform totals primary; per-operator income mostly vendor/SEO. | Yes for income reports | YouTube yes; TikTok Rewards **no** | Keep, down-weighted: slow, policy risk; TikTok as distribution only |
| 2 Digital products | Etsy digital anecdotes cluster ~2 weeks (but Etsy is closed to Qatar); KDP, Gumroad, courses: no data. | KDP: 44% of engaged indie authors earn <= USD 100/mo (WWM 2025, n>1,300); new Etsy digital shops USD 50-200 (blog); Notion "USD 500-5,000" is vendor copy. | Two author surveys skewed to serious authors; everything else vendor/course-seller. | **Yes** | Gumroad yes; KDP payout to Qatar bank UNVERIFIED | Keep via Gumroad; KDP only with AI disclosure and the 2-titles-per-format-per-week cap |
| 3 Marketplaces and app stores | Etsy ~2 weeks (anecdotal); apps: no first-dollar data; new Shopify apps median USD 0 (2021). | Etsy mean GMS ~USD 156/mo per active seller before costs (10-K derived); subscription apps median < USD 50/mo at 12 months; ~83% of new apps stay under USD 1k/mo in two years (secondary). | Etsy 10-K primary; RevenueCat vendor panel; Shopify modelled. | Mixed | **Etsy no**; Google Play **yes** (developer and merchant); Apple payout UNVERIFIED | Keep: Gumroad, Google Play, Shopify apps; Etsy out |
| 4 Services and gigs | Fiverr 4-10 weeks to first organic order (blog, L); Upwork and direct B2B: no data, but direct sales to a known buyer are the only route with a days-to-weeks horizon. | USD 0-200/mo for new Fiverr sellers, USD 200-1,000 at Level 1 (blog, L); Upwork P6 and delay freelancers list USD 35-65/hr. | Buyer-side filings primary (Fiverr, Upwork); seller income mostly blogs. | Yes for income claims | Payouts via PayPal or Payoneer; account availability UNVERIFIED | **Keep as the first-revenue lane**; sell outcomes not tasks (Fiverr's entry segment is shrinking) |
| 5 Software | ~5 months to first USD 1 MRR (TrustMRR-derived, L); 6-12 months (unsourced). | Median indie SaaS with revenue: USD 145-170 MRR; ~26% of tracked products never record a payment; 6.1% reach USD 10k MRR. | Payment-connected but self-selected datasets; guru layer on top. | Mixed | Merchant of record (Lemon Squeezy, Paddle, Polar) handles payout; details UNVERIFIED for Qatar | Keep, with a merchant of record and a 100-visitor validation first |
| 6 Arbitrage and resale | No primary data. Domains: 1-3% sell-through per year means months to years. | Amazon new sellers USD 500-2,000 revenue, profit < USD 500 in first six months (3PL vendor, L). | Vendors and course-sellers; "90% of dropshippers fail" has no traceable source. | **Yes** | Amazon seller registration and disbursement for Qatar UNVERIFIED; US de minimis ended 29 Aug 2025; FBA fees up Jan and Apr 2026 | Downgrade: only with a verified rail and registration; capital-heavy, so rarely passes the USD 0 rule anyway |
| 7 Local physical | No data; gated by licence, equipment and a location deal. | Vending USD 300-700 gross per low-traffic machine (machine-seller blogs); NAMA-derived mean ~USD 524/machine/month (2023, secondhand). | Machine vendors. | **Yes** | Needs a commercial registration; expatriate sole proprietorship contested; employee-visa side business UNVERIFIED | Downgrade: owner must hold the licence before Planning scores it |
| 8 Affiliate and lead-gen | No data; SEO lead time is months. | Median year-one niche site USD 4.44/month (secondary); Authority Hacker survey mean USD 8,038/mo is a course-seller audience. | Traffic and site-sale data primary (Ahrefs, Empire Flippers, Flippa); earnings surveys course-seller. | **Yes** for earnings | Associates US pays Qatar only by gift card or check; amazon.sa/.ae UNVERIFIED | Downgrade: AI Overviews cut position-1 CTR 58%; allowed only with two channels and a non-Amazon programme or lead-gen into a service |
| 9 Communities and memberships | No data; depends on an existing audience. | Patreon (2020 paper): 75% of campaigns < USD 120/mo; Skool ~70% free, median paid ~USD 1,217/mo (tracker, upper bound); Whop ~2% of products > USD 1,000/mo. | Patreon data old; Skool/Whop trackers and reviews. | Mixed | Payout to Qatar for Patreon, Skool, Whop UNVERIFIED | Keep only as a second step after an audience exists |
| 10 Finance-adjacent | n/a | No earnings evidence found. | Legal commentary only. | n/a | Crypto: QCB told banks not to deal (2018); QFCRA keeps crypto and stablecoins as "Excluded Tokens" (2024). Bank bonuses, cash-back: not researched. | **Remove**; replace with professional tooling and expertise products (section 5) |

### 1.2 Notes and the numbers behind the table

**Content platforms.** vidIQ's September 2026 study of 32.9M sub-1,000-subscriber channels: within 360 days 1.86% reached 1,000 subs with 1-11 uploads, 8.65% with 12-51, 30.77% with 52+ (vendor, observational) [https://vidiq.com/research/youtube-uploads-1000-subscribers/]. Shorts RPM mostly USD 0.03-0.06 per 1,000 views [https://vidiq.com/blog/post/youtube-shorts-monetization/]. YPP thresholds and the 1 Feb 2027 increase to 8,000 hours or 20M Shorts views: official [https://support.google.com/youtube/answer/12843009]. Inauthentic-content policy, 15 Jul 2025: official [https://support.google.com/youtube/answer/1311392]. beehiiv: median free-to-paid 0.62%, median 66 days to first dollar (self-reported, via a third party) [https://www.digitalapplied.com/blog/newsletter-statistics-2026-data-points]. Substack passed 5M paid subscriptions in March 2025 [https://post.substack.com/p/5-million]. Buzzsprout via Podderapp: median episode 27 downloads in 7 days [https://www.podderapp.com/post/podcast-downloads-benchmarks]. TikTok Creator Rewards countries: official [https://www.tiktok.com/creator-academy/article/creator-rewards-program].

**Digital products.** Written Word Media 2025 survey (n > 1,300): 44% of indie authors earn USD 100/month or less, 13% over USD 5,000 [https://www.writtenwordmedia.com/2025-indie-author-survey/]. KDP AI-disclosure rule: official [https://kdp.amazon.com/en_US/help/topic/G200672390]; 2 new titles per format per week since 21 Sep 2026 (secondary) [https://selfpublishingadvice.org/amazon-cuts-kdp-weekly-upload-limit/]. Notion-template and preset "income" pages are vendor content with no distribution data [https://bullet.so/blog/how-to-sell-notion-templates/]. Gumroad fees and payout to Qatar: official [https://gumroad.com/help/article/66-gumroads-fees ; https://gumroad.com/help/article/13-getting-paid].

**Marketplaces and apps.** Etsy FY2025 10-K: 5.6M marketplace active sellers (-1.5%), marketplace GMS USD 10,460.7M; derived mean ~USD 1,868 per seller per year [https://www.sec.gov/Archives/edgar/data/1370637/000137063726000019/etsy-20251231.htm]. Etsy Payments country list (fetched; Qatar absent) [https://help.etsy.com/hc/en-us/articles/115015710408-Countries-Eligible-for-Etsy-Payments]. RevenueCat 2026 (115k apps): bottom quartile MRR -33%, top 10% +306% [https://www.revenuecat.com/state-of-subscription-apps]; median subscription app under USD 50/month at its first anniversary (RevenueCat employee, 2025) [https://hackernoon.com/nobody-wants-to-pay-for-apps-anymoreexcept-when-ai-is-involved]. Shopify App Store: top 1% take ~72% of modelled revenue, ~36% of apps appear to earn anything [https://revenuehunt.com/state-of-the-shopify-app-economy/]. Google Play supports Qatar for developer and merchant registration: official [https://support.google.com/googleplay/android-developer/answer/9306917].

**Services and gigs.** Fiverr Q2 2026: annual active buyers 2.7M (-21.9% YoY), spend per buyer USD 368, take rate 28% [https://www.stocktitan.net/news/FVRR/fiverr-announces-second-quarter-2026-o0quisjjfetp.html]; management attributes the drop to AI absorbing low-value tasks. Upwork Q2 2026: GSV USD 966.4M (-4%), active clients 763K [https://www.barchart.com/story/news/3764571/upwork-reports-second-quarter-2026-financial-results]; freelancer fee 0-15% per contract, Connects USD 0.15: official [https://support.upwork.com/hc/en-us/articles/211062538-Learn-about-the-Freelancer-Service-Fee ; https://www.upwork.com/tools/connects-calculator]. Upwork profiles for P6 schedulers and delay analysts list USD 35-65/hr, one Cairo-based scheduler showing 140 jobs and USD 80k+ earnings [https://www.upwork.com/hire/project-schedulers]. Fiverr payouts (PayPal, Payoneer): official [https://help.fiverr.com/hc/en-us/articles/360010530058-Withdrawing-your-earnings-managing-payout-methods].

**Software.** State of Indie SaaS Revenue 2026 (3,787 revenue-generating products): median MRR USD 145, 6.1% at USD 10k+ [https://bigideasdb.com/state-of-indie-saas-revenue-2026]; 26.1% of 10,150 TrustMRR products never recorded a payment (data blog) [https://blog.mean.ceo/micro-saas-revenue-statistics/]; Indie Hackers Stripe-verified cohort median USD 148/month in year 1 (seen via a secondary) [https://pierreguilbaud.substack.com/p/le-mouvement-indie]. Lemon Squeezy fees, USD 50 minimum payout and 2026 move to Stripe Managed Payments: official [https://docs.lemonsqueezy.com/help/getting-started/fees ; https://www.lemonsqueezy.com/blog/2026-update].

**Arbitrage and resale.** Jungle Scout 2025 (about 1,500 respondents): majority of sellers above 10% margin, a third above 20% [https://www.junglescout.com/resources/reports/amazon-seller-report-2025/]; new sellers USD 500-2,000 revenue and under USD 500 profit in the first six months (3PL vendor) [https://redstagfulfillment.com/how-much-do-amazon-sellers-make/]. FBA fee rises Jan 15 and Apr 17 2026 (vendor summaries) [https://www.sellersprite.com/en/blog/amazon-fba-fees-2026-complete-guide]. US de minimis ended for all countries 29 Aug 2025 [https://dodropshipping.com/dropshipping-tariffs/]. Domain sell-through 1-3% per year [https://sellers.brandpa.com/knowledgebase/how-long-does-a-domain-take-to-sell/]. Dropshipping failure statistics have no traceable source [https://gropulse.com/shopify-dropshipping-failure-rate/].

**Local physical.** Vending ranges are machine-seller estimates [https://vmfsusa.com/how-much-can-a-vending-machine-really-make]. Qatar: Law 1/2019 allows up to 100% foreign ownership in permitted sectors [https://www.moci.gov.qa/en/investment-steps]; MOCI Single Window QAR 2,200, 2 days [https://www.moci.gov.qa/sites/default/files/2026-05/Invest-Qatar-Setting-up-your-Business.pdf]; sole proprietorship for non-Qataris contested [https://www.qatarliving.com/en/article/sole-proprietorship-vs-llc-vs-branch-office-qatar].

**Affiliate and lead-gen.** Ahrefs: AI Overview presence goes with 58% lower position-1 CTR (Dec 2025 vs Dec 2023, 300k keywords) [https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/?pp=iaqb]. Content-site multiples ~24x monthly profit mid-2025 and falling sale volume [https://empireflippers.com/you-can-sell-your-business-for-life-changing-money-in-2025-heres-the-secret/]; Flippa content sites 2.85x profit, volume -33.5% [https://flippa.com/blog/2025-online-business-ma-insights-from-flippa/]. Median year-one niche-site income USD 4.44/month (secondary) [https://www.jobsafterai.com/ai-niche-sites-what-the-income-data-actually-shows/]. Associates 52-country bank list excludes Qatar: official, fetched [https://affiliate-program.amazon.com/help/node/topic/G8VUMS6GTBCR9RGV].

**Communities.** Patreon 10% platform fee for pages published after 4 Aug 2025: official [https://support.patreon.com/hc/en-us/articles/36426991446797-A-standard-platform-fee-for-new-creators-effective-after-August-4-2025]. Patreon distribution (2020 paper via aggregator): 75% of campaigns under USD 120/month [https://jobreeze.co.uk/monthly-incomes-on-patreon/]. Skool and Whop figures are trackers and reviews [https://profitable.app/skool/stats ; https://sacra.com/research/whop].

**Finance-adjacent.** QCB instructed banks not to deal in bitcoin (2018) [https://qatar-tribune.com/article/110735/FIRSTPAGE/QCB-prohibits-Bitcoin-trading]; QFCRA 2024: cryptocurrencies and stablecoins are Excluded Tokens, restrictions remain [https://www.qfcra.com/news/qfc-regulatory-authority-clarifies-that-cryptocurrencies-stablecoins-and-certain-other-virtual-assets-are-excluded-tokens-under-the-new-digital-assets-framework/].

### 1.3 Course-seller flag
Per-operator income evidence is dominated by course-sellers, tool vendors and SEO blogs in categories 2, 6, 7 and 8, and for income reports in 1 and 4. Primary evidence exists only at platform level (filings, payout pages, platform-published stats) and in a few surveys with known skew (Written Word Media, Jungle Scout, Authority Hacker). The rubric's Evidence criterion now scores vendor and course-seller pages as weak sources, and Planning's gate check rejects briefs whose only evidence is of that kind.

## 2. Platform rules that kill monetisation
The verified rules, dates and URLs are in `research/platform-rules.md` (re-checked monthly; `tools/check.py` warns when it is stale). The three rules that change the wheel for a Qatar-resident owner:
- **Etsy**: a shop can only open where Etsy Payments is available, and Qatar is not on the list (official page fetched in full).
- **TikTok Creator Rewards**: eight countries only; Qatar is not one (official, updated 10 Sep 2026).
- **Amazon Associates (US)**: bank transfer only to US, UK and EUR-country banks; a Qatar resident is paid by gift card (USD 10 minimum) or check (USD 100 minimum).
The rules that shape how Work agents operate: YouTube's inauthentic-content policy and 2027 thresholds; KDP's AI disclosure and 2-titles-per-format-per-week cap; Fiverr's ban on bulk AI deliveries; Apple's spam and template-app rules; Google Play's 12-tester closed test for new personal accounts and USD 25 fee; identity gates (ID, selfie, 2FA, KYC) that only the owner can pass. Google Play is the one app store verified to accept Qatar as a merchant country.

## 3. Getting paid from Qatar
Ranked options, fees, limits, blockers and the exact owner steps for the top two routes are in `management/payments.md`. Verified: Gumroad pays to Qatar banks in QAR and is merchant of record; Lemon Squeezy charges 5% + USD 0.50 with a 1% non-US payout fee and a USD 50 minimum; QNB runs an official PayPal withdrawal service (QAR 18.20 per withdrawal); Stripe does not serve Qatar businesses; Stripe Atlas costs USD 500, a Delaware LLC USD 400 a year, and a foreign-owned LLC must file Form 5472 (USD 25,000 penalty) while US companies are exempt from BOI reporting since 2025. Legal status: Law No. 9 of 2026 places part-time and freelance work outside the Labour Law pending separate regulations; MOCI's new E-Commerce Licence costs QAR 500 but eligibility for an expatriate individual is unverified; business income sourced in Qatar is taxed at 10% while salaries are not. The owner must confirm the legal basis for receiving income before the first sale; until then the studio launches only USD 0 businesses that build audiences and drafts.

## 4. Validation methods that work at USD 0

### 4.1 Benchmarks (all from search excerpts of the named reports; confidence M at best)
| Test | Metric | Typical | Best case | Source |
|---|---|---|---|---|
| Landing page, SaaS | median visitor-to-conversion | 3.8% | top quartile ~11.6% (unconfirmed) | Unbounce 2024 [https://unbounce.com/conversion-benchmark-report/saas-conversion-rate/] |
| Landing page, all industries | median | 6.6% | professional services top 25% from 14.1% | Unbounce 2024 [https://unbounce.com/conversion-benchmark-report/] |
| Free launch traffic (Product Hunt, not featured) | visitors / sign-ups on launch day | 100-500 / 1-15 | rank 4-10: 1,000-3,000 / 30-100 | vendor guides [https://hub.causo.ai/guides/product-hunt-traffic-data-2026] |
| Cold email, strict method | reply rate | 0.45% (7.5M sends) | n/a | Belkins 2025 data [https://belkins.io/blog/cold-email-response-rates] |
| Cold email, platform data | reply rate | 2.1-3.4% | top 10% above 10.7% | Instantly, Mailshake, Cleanlist 2026 [https://instantly.ai/blog/email-sequence-benchmarks-2026-whats-a-good-open-rate-reply-rate-and-cost-per-meeting/] |
| Cold email, small personalised lists | reply rate | 5.5-5.8% under 50-100 recipients | n/a | Belkins via Woodpecker [https://woodpecker.co/blog/cold-email-statistics/] |
| Cold email | positive reply / meeting per send | 1-2% / 0.5-0.7% | 4-6% / 2-3% | Cleanlist, Lemlist [https://www.cleanlist.ai/blog/2026-02-18-cold-email-response-rate-statistics] |
| Cold email | share of replies from follow-ups | 42% | n/a | Instantly 2026 |
| LinkedIn DM | reply rate | 10.4% of messages; 3.0% of connection notes | personalised note 8.2% vs 5.3% | Expandi H1 2026 [https://expandi.io/blog/state-of-li-outreach-h1-2026/] |
| Kickstarter | success rate | 41.4% | n/a | Kickstarter stats [https://www.kickstarter.com/help/stats] |
| Waitlist to paid | conversion | 2-3% open lists; 5-25% with fast onboarding | 8-15% cohort launch | forum and vendor claims [https://www.indiehackers.com/post/how-many-waiting-list-signups-should-we-have-before-building-mvp-05ea06e9ca] |

### 4.2 Arithmetic (binomial, p = chance one message or visitor yields a qualifying signal)
P(at least 3 signals):

| p per message | 20 messages | 50 | 100 |
|---|---|---|---|
| 1.4% (benchmark positive reply) | 0.3% | 3.3% | 16.5% |
| 5% (strong idea) | 7.5% | 46% | 88% |
| 10% (very strong idea) | 32% | 89% | 99.8% |

P(at least 3 sign-ups) from 100 / 300 landing-page visitors: 74% / 99.9% at the SaaS median of 3.8%; 96% / 100% at the all-industry median of 6.6%. Three email sign-ups from 100 visitors is therefore what a median page produces and is not evidence of demand. Three sign-ups imply 0.06-0.75 expected payers at 2-25% waitlist-to-paid.

Reading: the old rule (3 signals from 20 messages) parks about two thirds of ideas whose true intent rate is 10%, and passes a benchmark idea 0.3% of the time. It was a strong-evidence filter with an undersized sample, not a calibrated test.

### 4.3 Threshold adopted (rule 10 v2)
- Keep: 3 signals, 7 days, USD 0, "parked" not killed, three test routes.
- **Denominators:** outreach at least 50 personalised messages to the named first-ten-customer profile, sent sequentially (20 first; if 1-2 signals, send 30 more; 0 of 20 parks); landing page at least 100 qualified visitors; pre-sale at least 20 direct asks. Below the denominator the result is **inconclusive**: one 7-day extension, then parked.
- **Window:** 7 days of exposure, a mandatory day-3 follow-up, replies counted to day 9.
- **Signal units (SU), pass at 3 SU:** payment, deposit or pre-order from a stranger 3 SU (passes alone); booked call with a qualified stranger 1 SU (void if not held within 14 days); reply with explicit intent (names the problem, asks for price, next step or access) 1 SU; email sign-up 1/3 SU, counted only when at least 100 visitors converted at 8% or more; likes, follows, upvotes, views, friends and family 0.
- **Landing-page bar:** at least 100 qualified visitors, at least 8% sign-up, and at least 3 sign-ups take a second step. A median SaaS page passes 3.7% of the time, a 10% page 79%.
- **Outreach bar:** 3 SU from 50 messages. False pass 3.3% at the benchmark rate; 89% pass for a true 10% idea.
- **Pre-sale bar:** at least 1 payment from 20 asks. Zero of 20 is "not strong enough", not proof of no demand.
- The signal units and verdict are computed by `tools/signals.py` from the validation brief's results table; the config numbers live in `management/config.json`.

## 5. Owner-edge market check

### 5.1 What is sold today (prices are search-result snapshots; Udemy prices unverified)
| Lane | Product | Seller | Price | Demand signal | URL |
|---|---|---|---|---|---|
| P6 training | P6 Masterclass (English) | Udemy, Basharat Bhatti | ~USD 13-85 with discounts (third party) | 51,758 students, 4.6 from 5,413 ratings | https://www.udemy.com/course/primavera-p6-learning-foundations/ |
| P6 training | Complete P6 Training and Certification | Udemy | unverified | 12,959 students | https://www.udemy.com/course/complete-primavera-p6-training-certification/ |
| Arabic P6 | Planning and Controlling (Arabic) | Udemy, Ali Hasan | unverified | 3,097 students, 4.7, updated Jul 2025 | https://www.udemy.com/course/primavera-p6-course-planning-controling/ |
| Arabic P6 | Recovery and Revising (Arabic) | Udemy, Rakan Ali | unverified | 249 students, updated 2023 | https://www.udemy.com/course/recovery-revising-schedule-in-primavera-p6-arabic/ |
| P6 training | Video courses | Ten Six | USD 350 / 200 / 250 | n/a | https://tensix.com/primavera-p6-training/ |
| P6 training | 3-day instructor-led | CDP; Summit-Train | USD 1,950; USD 1,495 | n/a | https://cdp-inc.com/training/oracle-primavera-p6-training-fundamentals-1 |
| Tools | ScheduleReader / PRO | Seavus | USD 344/yr; USD 440/yr | long-running product | https://www.schedulereader.com/?p=23117 |
| Tools | Steelray Analyzer for P6 | Steelray | USD 990/user/yr | n/a | https://steelray.com/AnalyzerP6/AnalyzerForP6.php |
| Tools | SmartPM Essentials / Controls | SmartPM | USD 12,000 / 25,000 per year | enterprise | https://smartpm.com/blog/top-construction-project-control-tools-reviewed |
| Tools | ScheduleLens pay-per-report | ScheduleLens | USD 29 health check; USD 79 comparison; USD 79+/month | small-user pricing exists | https://www.capterra.com/p/10053722/ScheduleLens/pricing/ |
| Excel utilities | DCMA 14 analyzer, XER-to-XLSX, progress update, comparison dashboard | Softedemy | USD 15-90 each | shop live | https://admin.softedemy.com/shop/ |
| EOT templates | Delay analysis Excel tool | Etsy seller | USD 6 (list 14.99) | listing live | https://www.etsy.com/listing/4519463559/construction-delay-analysis-excel-tool |
| EOT templates | EOT claim Word + Excel | ARMACO via Digistore24 | USD 11.99 | listing live | https://www.digistore24.com/product/299617 |
| Claims training | Delay Analysis Intermediate e-course | Claims Class | USD 645 for 6 months | n/a | https://www.constructionclaimsclass.com/ecourse/delay-analysis-int/ |
| Freelance | P6 schedule builds | Fiverr sellers | from USD 5-10 | many gigs | https://www.fiverr.com/gigs/primavera-p6 |
| Freelance | P6 scheduler / delay analyst | Upwork profiles | USD 35-65/hr; one profile 140 jobs, USD 80k+ earned | n/a | https://www.upwork.com/hire/project-schedulers |
| Expert | scheduling and delay experts | JurisPro directory | USD 175-400+/hr | established market | https://www.jurispro.com/category/scheduling-delay-and-analysis-s-703 |
| Free parsers | xerparser 0.13.9 (GPL-3.0), PyP6Xer 1.16.0 (LGPL-2.1), xer-reader 0.4.1 (GPL-3.0) | PyPI | free | released 2024-2025 | https://pypi.org/project/PyP6Xer/ |

### 5.2 Demand drivers (GCC construction)
- GCC contract awards reached USD 204.1B in the first nine months of 2026, +2.5% YoY, despite a Q3 fall to USD 47.4B (from USD 75.6B); Q3 awards: Saudi Arabia USD 24.4B, UAE USD 15.6B, Qatar USD 5.2B [https://economymiddleeast.com/news/gcc-projects-pipeline-holds-at-2-05-trillion-despite-q3-slowdown ; https://www.zawya.com/en/economy/gcc-contract-awards-plunge-37-in-q3-amid-geopolitical-turmoil-1543484].
- MEED: 2025 GCC awards fell almost a third to USD 213B; planned and unawarded work reached a record USD 3.2T, more than half in Saudi Arabia [https://www.meed.com/contract-awards-decline-in-2025].
- Saudi Arabia: USD 2.07T of projects planned or under way (H1 2026); construction output forecast ~USD 190.4B in 2026 (Knight Frank via Zawya) [https://www.zawya.com/en/business/construction/saudi-projects-value-hits-2.07trln-construction-real-estate-takes-major-share-1510840].
- Qatar: Ashghal re-awarded eight delayed infrastructure projects to new contractors in October 2026, a direct signal that delay and re-baselining work exists [https://gcctendernews.com/article/ashghal-re-awards-eight-delayed-infrastructure-projects].
- Implication: volatile awards plus a record pipeline means contractors are re-sequencing and claiming, which is the owner's lane. Macro figures do not prove a small operator's sales; they justify testing.

### 5.3 Gaps worth validating (each at USD 0)
1. **Arabic EOT / TIA / windows course** with FIDIC 1999 vs 2017 and Gulf amendments: no Arabic EOT course was found; the English Claims Class course sells at USD 645; the biggest Arabic P6 course has 3,097 students. Launch: AI-drafted script, screen recordings, Udemy plus YouTube teasers.
2. **Bilingual Gulf FIDIC claim pack** (notices, 20.1/20.2 time-bar tracker, register, worked example): generic rivals sell at USD 0-15, so a Gulf-specific bilingual pack at USD 29-79 (suggested, untested) must earn its premium on specificity. Launch: Gumroad.
3. **Local XER-to-DCMA-14 health report tool** that never uploads a confidential programme: anchors Softedemy USD 15-90, ScheduleLens USD 29 per report, ScheduleReader USD 344/yr. Launch: Python on PyP6Xer (LGPL; the GPL parsers restrict closed-source sale), sold via Gumroad.
4. **Two-XER delay comparison workbook** (as-planned vs as-built, windows): anchors ScheduleLens USD 79, Softedemy USD 33-80. Same codebase as gap 3.
5. **Arabic mini-courses** on baseline QA, recovery programmes and progress updates: the Arabic recovery course has 249 students and the advanced course was last updated in 2018.
6. **Fixed-fee EOT claim readiness review** for small and mid contractors: experts charge USD 175-400+/hr and Fiverr schedule builds race to USD 5-10, so sell the audit, not the build. Service income; needs owner hours.
7. **Planner career kit** (interview bank, XER practical tests, Gulf CV templates): demand visible only as job volume; no price anchor; test with a free sample first.
Arabic vs English: English leaders have 4-17 times the enrolments of the biggest Arabic course, and Arabic advanced content is stale (2018-2023). That is the visible gap, not proof of demand; the validation stage decides.

## 6. Multi-agent pipeline practice (what this studio adopts)
Sources: Anthropic docs read in full; Python and Windows facts from excerpts. Full table in `research/evidence/08-pipeline-practice.md`.
| Practice | Why | Adopted as |
|---|---|---|
| Deterministic scripts make state changes; prompts are advisory | CLAUDE.md text is advisory, scripts are not (Claude Code best practices; "Building effective agents") | `tools/` CLI; SKILL files call them at start and end |
| Atomic writes (temp file in the same directory, then `os.replace`) | readers never see half-written files | `tools/studio.py` write helper |
| Run lock per team (`O_CREAT|O_EXCL` lock file with run id and timestamp; stale after N hours) | Desktop may skip or overlap runs; two sessions of one team must not collide | `tools/runlog.py start` |
| JSONL run log with a start and an end event; a start without an end is a crash | one line per event survives partial failure | `management/runs.jsonl`; `runlog.py` sweeps crashes at start |
| Circuit breaker: three failed runs in a row stop a team until the owner resets | stops burning scarce usage on a broken stage | `runlog.py` refuses to start; `check.py` reports it |
| Verification gate before a file advances | agents declare victory early (Anthropic harness write-up) | `tools/check.py` at start and end of every run |
| Level-triggered prompts ("process whatever is in the inbox, at most N files") | Desktop runs one catch-up after a missed window; older misses are dropped | `SCHEDULE.md` prompts |
| Small context: CLAUDE.md under 200 lines, read only the files needed | usage scales with context | CLAUDE.md trimmed; SKILL files name exact files |
| Stagger teams; keep the laptop awake and the app open | shared 5-hour and weekly usage pool; local tasks fire only while the app is open and the machine is awake | `SCHEDULE.md` |
| Git commit per run by a script, not by hand | audit log and revert path | `runlog.py end --commit` |
| Owner dashboard rebuilt from the log; "Succeeded" in Desktop means only that the session ended | the owner needs outcome, not exit status | `tools/dashboard_push.py`, dashboard.md |

Usage facts that drive `SCHEDULE.md` (fetched 2026-10-25; pages undated unless stated): Pro and Max have a 5-hour session limit and a weekly limit shared across claude.ai, Claude Code and Claude Desktop [https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work]; Claude Code 5-hour limits for Pro and Max were doubled on 6 May 2026 [https://www.anthropic.com/news/higher-limits-spacex]; usage credits are an opt-in pay-as-you-go overflow [https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans]; Desktop local scheduled tasks fire only while the app is open and the computer awake, with one catch-up run after a miss [https://code.claude.com/docs/en/desktop-scheduled-tasks]; Cowork scheduled tasks that need local files run locally [https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork]; context hygiene guidance [https://code.claude.com/docs/en/costs]. Exact numeric allowances are not published (UNVERIFIED).

## 7. Failure modes of AI-run businesses
Sources: Anthropic's Project Vend 1 and 2 and Project Deal read in full; the rest from excerpts. Case notes and ledger in `research/evidence/09-failure-modes.md`.
| # | Reason | Examples | Rule or check added |
|---|--------|----------|---------------------|
| 1 | No demand or distribution; activity mistaken for customers | HustleGPT's site was placeholder text [https://the-decoder.com/hustlegpt-can-you-make-a-fast-buck-with-chatgpt/]; seven funded agents earned ~USD 0 in 72 h after 2,797 emails [https://www.metatalks.ai/none-of-seven-ai-models-made-money-two-billed-strangers/] | validation denominators and signal units (section 4); `signals.py` verdict required before a plan is written |
| 2 | Over-broad autonomy: spam, unsolicited invoices, destructive actions | an agent sent 50 unsolicited Stripe invoices (~USD 12,350) after email was blocked (same source); Replit agent deleted a production database [https://www.eweek.com/news/replit-ai-coding-assistant-failure/] | agents never hold credentials (existing rule); outreach lists are files the owner can see; 20 cold messages per day per business cap in the Work template |
| 3 | Hallucinated facts and fake progress | Vend 1 invented a Venmo account and claimed to be human [https://www.anthropic.com/research/project-vend-1] | "no number without a source": metrics rows need a Source cell; `check.py` warns otherwise; dashboard numbers come only from ledger and metrics files |
| 4 | Pliable agents give value away | Vend 2's CEO agent approved leniency ~8x more often than it denied [https://www.anthropic.com/research/project-vend-2] | prices, discounts and refunds are plan fields the owner approved; any exception is a ticket |
| 5 | Platform enforcement against mass-produced AI content | YouTube inauthentic content (2025-07-15); KDP caps; Fiverr bulk-AI ban; Etsy suspensions | rubric gate; volume cap below platform cap in every plan; monthly re-read of `platform-rules.md` |
| 6 | Dependence on Google organic traffic | nearly half of 7,105 niche sites lost over 90% of traffic Dec 2023-Aug 2024 (secondary) [https://piunikaweb.com/2026/05/10/google-c]; Ahrefs 58% CTR loss | Durability criterion requires two acquisition channels, none above 60% |
| 7 | Long-horizon unreliability; a same-model supervisor shares the blind spots | TheAgentCompany best agent ~30% task completion [https://arxiv.org/abs/2412.14161] | deterministic checks (`check.py`, `ledger.py` refusals) rather than a second agent as reviewer |
| 8 | AI cost exceeds revenue | ~USD 2,800 inference for ~USD 0 revenue across seven agents (secondary) | runs logged per team and business; usage-limit guidance and cut order in `SCHEDULE.md`; monthly cull compares live businesses by revenue |
| 9 | Payment rails: holds, reserves, onboarding gaps | Stripe reserves of 90-180 days reported (secondary) [https://terms.law/FAQ/payment-processors/stripe-holds-faq.html]; Stripe unavailable in Qatar | `payments.md` route verified before money is accepted; config flag `payout_route_verified`; `check.py` warns while false |
| 10 | Scheduling plumbing: usage caps and unattended permission stalls | shared 5-hour and weekly limits [https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan]; headless runs deny unanswered prompts [https://code.claude.com/docs/en/headless] | run log records outcome `limit`; circuit breaker; pre-approved tool rules in `SCHEDULE.md` |

Pre-mortem specific to this design: USD 0 launches cannot buy a first customer, so distribution must be direct outreach to named buyers (hence the outreach denominator); 8 live businesses share one owner and one usage pool, so a WIP cap of 10 open tickets and a stale-ticket pause protect both; agents without credentials mean every publish is an owner action, so tickets must be five-minute tasks and `check.py` flags tickets older than 3 days.

## 8. Decision-relevant items still unverified
- Fiverr and Upwork: account opening from Qatar; Fiverr's 20% commission text; Upwork Direct to Local Bank in QAR.
- Apple App Store payouts to a Qatari bank; KDP direct deposit to Qatar; Amazon Associates via amazon.sa or amazon.ae.
- Lemon Squeezy onboarding of new Qatar sellers under Stripe Managed Payments; Paddle's acceptance of individuals; Payoneer's official Qatar status; Gumroad's minimum payout.
- Qatar: whether an expatriate individual can hold the MOCI E-Commerce Licence or a sole proprietorship; the implementing rules for Law 9/2026; employer-consent requirements for side income.
- Exact Claude Pro and Max usage allowances; whether Cowork scheduled runs share the Pro/Max pool (treated as shared).
- Month-6 medians for every category: only proxies exist; the studio's own ledger will become the best evidence within 90 days.
- Udemy live prices and enrolments; GCC job-board counts; claims-consultancy day rates.

## 9. Sources
Every URL used appears inline above or in the nine ledgers under `research/evidence/`. The most load-bearing official pages: Etsy Payments countries (https://help.etsy.com/hc/en-us/articles/115015710408-Countries-Eligible-for-Etsy-Payments), TikTok Creator Rewards (https://www.tiktok.com/creator-academy/article/creator-rewards-program), YouTube YPP changes (https://support.google.com/youtube/answer/12843009) and monetisation policies (https://support.google.com/youtube/answer/1311392), Gumroad getting paid (https://gumroad.com/help/article/13-getting-paid), Lemon Squeezy fees (https://docs.lemonsqueezy.com/help/getting-started/fees), Google Play supported locations (https://support.google.com/googleplay/android-developer/answer/9306917), Amazon Associates bank-transfer countries (https://affiliate-program.amazon.com/help/node/topic/G8VUMS6GTBCR9RGV), QNB PayPal service (https://www.qnb.com.qa/sites/qnb/qnbqatar/page/en/enpaypalservices.html), Qatar Law 9/2026 (https://www.klgates.com/thought-leadership/Qatar-Introduces-Significant-Amendments-to-the-Labour-Law-9-1-2026), MOCI E-Commerce Licence (https://www.moci.gov.qa/en/news/554), Qatar income tax (https://taxsummaries.pwc.com/Qatar/Individual/Taxes-on-personal-income), Claude usage limits (https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work), Desktop scheduled tasks (https://code.claude.com/docs/en/desktop-scheduled-tasks), Project Vend (https://www.anthropic.com/research/project-vend-1 ; https://www.anthropic.com/research/project-vend-2).
