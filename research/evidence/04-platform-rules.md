# Platform rules (checked 2026-10-25)

Researcher: sub-agent D. All "checked" dates = 2026-10-25.

## Evidence-quality caveat (read first)
- The WebSearch budget for this session ran out mid-task (platforms 6-10 only partly covered). WebFetch could only resolve developer.apple.com, developer.android.com and github.com; support.google.com, help.etsy.com, kdp.amazon.com, affiliate-program.amazon.com, gumroad.com, fiverr.com, upwork.com, tiktok.com, blog.youtube all failed (DNS ENOTFOUND for WebFetch, HTTP 403 policy denial for curl). I did not route around these blocks.
- Source tiers used below:
  - **O-F** = official page fetched and read this session (Apple, Android dev, GitHub repo).
  - **O-S** = official page URL returned by search, content seen only as a search-tool excerpt/summary (page itself NOT read). Treat as medium confidence.
  - **S** = third-party/secondary.
  - **MEM** = model memory only, no source retrieved. NOT citable; listed only as a prior to check.
- NOT RESEARCHED at all (no evidence): Fiverr (#7), Upwork (#8), Gumroad payout countries/ownership detail (#6, partly), Google Play (#10).

## Summary table
| Platform | Monetisation threshold | Fees | AI-content rule | Qatar eligibility (sell / get paid) | Official URL | Page date |
|---|---|---|---|---|---|---|
| YouTube Partner Program | Today: 1,000 subs + 4,000 qualified watch hrs (12 mo) OR 10M qualified Shorts views (90 d). From 2027-02-01 for NEW applicants: 8,000 hrs (365 d) OR 20M Shorts views (90 d), still 1,000 subs. Lite tier: 500 subs + 3,000 hrs/3M Shorts views (fan funding, Shopping only). Also 2-step verification, 18+, no active strikes, AdSense linked [1][2][3] | YPP revenue share not re-verified (UNVERIFIED) | "Inauthentic content" (renamed 2025-07-15 from repetitious): mass-produced/templated/interchangeable content is not monetisable; AI allowed only if original value; disclose realistic synthetic content via Studio "AI use" [4][7] | YPP: Qatar listed as eligible (M-H) [6]. Payout: AdSense; $100 threshold; Qatar = wire/check yes, EFT no (older table, M) [8] | https://support.google.com/youtube/answer/72851?hl=en | Not shown in excerpts; policy note dated 2025-07-15; YPP 2027 blog ~2026-08-10 |
| TikTok Creator Rewards | 10,000 followers + 100,000 views in last 30 d; 18+; personal account; videos >1 min (secondary) [10] | n/a (payout program) | Must label realistic AI/significantly edited content; C2PA auto-labels cannot be removed; fake crisis/authority AI banned [11] | NOT eligible per official list (US, UK, DE, JP, KR, FR, MX, BR); list ~18 months old [10]. TikTok Shop: no evidence Qatar supported (S, L) [12] | https://www.tiktok.com/creator-academy/en/article/creator-rewards-program | ~Apr 2025 (age metadata) |
| Etsy | none (open marketplace) | $0.20/listing (4-month); 6.5% transaction; payment processing varies by bank location (US 3% + $0.25); Offsite Ads 15% (12% if >= $10k sales/365d; cap $100/order); possible one-time $15 set-up fee for some new shops [13][16] | Creativity Standards: AI items = "Designed by" seller with AI use stated in listing description; no bot-generated listings with no human involvement; real unedited finished-item photos [14] | Qatar NOT found on Etsy Payments eligible list (only UAE via Payoneer seen among Gulf); likely cannot open shop (M) [15] | https://www.etsy.com/legal/fees/ | Fees policy updated ~2026-10-05 (search metadata) |
| Amazon Associates | 3 qualifying sales within 180 days of applying or application withdrawn/rejected [17] | n/a | not verified | Payout: direct deposit (local bank in 52 listed countries; Qatar NOT confirmed), gift card, or check ($100 min, $15 fee waived outside US). [17] | https://affiliate-program.amazon.com/help/operating/agreement | Operating Agreement changes eff. 2026-04-14 (O-S) |
| Amazon KDP | none | royalty rates not re-verified | Disclose AI-GENERATED text/images/translations at publish; AI-ASSISTED (you wrote, AI polished/brainstorm) not disclosed [18] | Qatar EFT: NOT confirmed (old EFT list; PSP route via Payoneer/Wise, KYC required since 2026-08-01) [19] | https://kdp.amazon.com/en_US/help/topic/G200672390 | Limits eff. 2026-09-21 (S + O-S) |
| Gumroad | none | 10% + $0.50 direct; 30% via Discover; card processing 2.9% + $0.30 is separate on older help page (conflict); MoR change announced [20] | No seller-AI policy found; repo requires AI disclosure for contributors [21] | UNVERIFIED (not found) | https://gumroad.com/pricing | 3 yrs old per metadata |
| Fiverr | NOT RESEARCHED | NOT RESEARCHED | NOT RESEARCHED | NOT RESEARCHED | - | - |
| Upwork | NOT RESEARCHED | NOT RESEARCHED | NOT RESEARCHED | NOT RESEARCHED | - | - |
| Apple App Store | none | $99/yr individual or org (USD; local currency shown); 15% Small Business Program (<= $1M prior-year proceeds); standard rate not stated on fetched page (MEM: 30%) [22] | No dedicated generative-AI rule in first 100k chars of guidelines; 1.2 covers AI content-creation apps; 5.1.2(i) third-party AI data sharing; 4.3 spam, 4.2.6 template apps rejected [22] | Enroll: page lists no regions; "may not be supported in certain regions" (sanctions). Payout: bank-country list NOT published on fetched pages; Qatar not in threshold table so $40 USD min applies to unlisted bank countries (inference) [22] | https://developer.apple.com/support/enrollment/ | Guidelines last updated 2026-10-16 |
| Google Play | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED (see gaps) | https://support.google.com/googleplay/android-developer/answer/10788890 | - |

## Per-platform detail

### 1. YouTube Partner Program
- Eligibility today (2026-10-25): 1,000 subscribers AND (4,000 qualified public watch hours in past 12 months OR 10M qualified Shorts views in past 90 days). Shorts-feed watch hours do not count toward the 4,000. Also: no active Community Guidelines strikes, 2-Step Verification on the Google Account, AdSense for YouTube account linked, age 18+ (or guardian handles payments). Every channel passes a standard review even after meeting thresholds [1] (O-S).
- Lower tier: 500 subs + 3,000 watch hours or 3M Shorts views unlocks fan funding and Shopping, not ad revenue share [1][2] (O-S).
- Announced change: from 2027-02-01, new applicants for ads/Premium revenue share need 8,000 qualified watch hours (365 d) OR 20M qualified Shorts views (90 d), plus 1,000 subs. Existing YPP members unaffected. Creators must accept updated terms in Studio by 2027-01-31 or lose earnings from affected features (stay in YPP). Shorts Creator Pool: 10M qualified Shorts views per 90 days to earn monthly from the pool; missing it does not remove the channel from YPP [2][3] (O-S) ; corroborated by Gulf News/RouteNote/NewscastStudio [9] (S). Conflict: SwitcherStudio says the Shorts rule applies to existing members too; others say grandfathered. The Help page 72851 was reported as still showing old 4,000/10M numbers alongside a Feb-2027 banner (consistent, since the change is not yet live).
- Inauthentic content: policy renamed 2025-07-15 from "repetitious content"; YouTube says this content was already ineligible; covers repetitive/mass-produced content; channels whose videos are interchangeable cannot monetise; shared intro/outro OK if substance differs; templated AI content lacking creator perspective is a violation; AI scripts/voiceover/visuals are allowed if channel otherwise complies and content is clearly original; monetisation can be removed from the whole channel [4] (O-S). Spam policy separately bans using automation/AI to churn out high volumes of similar content with minimal changes [5] (O-S).
- AI disclosure: in Studio upload > Attributes > "AI use": answer Yes for realistic content that makes a real person appear to say/do something they did not, alters real events/places, or generates a realistic scene. Not required: clearly unrealistic/animation, minor aesthetic edits, AI scripts/outlines/production assistance. Content made with YouTube's own gen-AI tools is auto-labelled. Repeated non-disclosure can lead to manual labels, content removal, or YPP suspension [7] (O-S).
- Qatar: YPP availability pages list Qatar as an eligible country/region (search summary of [6], O-S). Not read directly.
- Payout: via AdSense. Payment threshold table shows USD $100; payment issued between the 21st and 26th if balance >= threshold and no holds; payment-method selection threshold lower ($10 USD). Qatar row: Check yes, EFT no, Wire yes, Hyperwallet no (from a table whose metadata is >3 yrs old) [8] (O-S, M).
- Account verification: AdSense account (identity/address) is needed; exact PIN/ID steps not retrieved.

### 2. TikTok Creator Rewards Program
- Official Creator Academy article (age ~18 months per metadata): 10,000 followers and 100,000 video views in last 30 days; age 18+ (19 in South Korea per secondary); business accounts excluded; account must be registered in an eligible country [10] (O-S). Videos >1 minute and original per secondary sources (S, [10] blogs: Buffer, Brandwatch, Metricool).
- Eligible countries per the official article: United States, United Kingdom, Germany, Japan, South Korea, France, Mexico, Brazil. Qatar not listed. Secondary sources add Canada, Italy, Spain, Australia (conflict, unverified); Toptal says TikTok publishes no official live country list [10].
- AI labelling: creators must label AI-generated or significantly edited content depicting realistic scenes/people; unlabeled content may be removed, restricted, or labelled by TikTok; creators can use AIGC toggle/caption/sticker; TikTok auto-labels via C2PA Content Credentials and auto-labels cannot be removed; banned: fake authoritative sources/crisis events, AI likeness of minors and private adults without permission. TikTok Shop has stricter AI rules (no AI impersonation of celebrities/doctors for promotion) [11] (O-S).
- TikTok Shop: no evidence that Qatar (or any GCC state) has a local seller center. Saudi reportedly eyed for early 2027, unconfirmed [12] (S, L).

### 3. Etsy
- Fees (official fees policy, search excerpt): listing $0.20 per item (expires after 4 months); transaction 6.5% of price + shipping/gift wrap; payment processing separate and varies by bank location (US 3% + $0.25); Offsite Ads 15% on attributed orders, 12% once a shop has >= $10,000 sales in prior 365 days (permanent), max $100 per order [13] (O-S). Older Etsy Fee Basics help pages are ~1,700 days old.
- Creativity Standards (2024): categories Made by / Designed by / Handpicked by / Sourced by. AI-generated work belongs under "Designed by" the seller with the seller's own prompt; AI use must be stated in listing description; cannot present AI output as handmade; newer AI update bars AI-generated patterns/recipes/instructions (as reported) and bot-generated listings with no human involvement; finished-item photos must be real [14] (O-S, M). California SB 1050 (eff. 2027-01-01) may require disclosure of AI synthetic performers (S, L).
- Etsy Payments: help article "Countries Eligible for Etsy Payments" lists UAE with an asterisk (Payoneer Payment Account route). Qatar, Bahrain, Kuwait, Saudi not found in any Etsy list returned. Etsy's "What is Etsy Payments" says where Etsy Payments is unavailable you generally cannot open a shop [15] (O-S). Alura guides on "unsupported countries" are third-party (S).
- Onboarding: government ID + selfie checked by Persona; ID name must match bank account name; unexpired ID; failing repeatedly can block onboarding; 2FA required for new shops; outside US bank details can be verified after first sale; business accounts need entity details and 25%+ owners; some new shops may face a one-time $15 set-up fee (2024 announcement, status unchecked) [16] (O-S).

### 4. Amazon Associates
- Application/acceptance: after applying you have 180 days to refer a sale; once 3 qualifying sales are referred, Amazon reviews and decides; application withdrawn if not enough qualifying sales within 180 days; rejected accounts cannot be reinstated [17] (O-S, Associates Central help G7MJTPEP9NC3YKMG).
- Dormancy: no commission income for 3 years can trigger a maintenance fee and closure. Either party may terminate on 7 calendar days notice. Closed-account appeal within 5 business days [17] (O-S).
- Operating Agreement changes effective 2026-04-14 reportedly added a 180-day requirement to purchase rules (product must be shipped/streamed/downloaded and paid for to qualify). Details unverified [17] (O-S, L).
- Payout methods: direct deposit ($10 min), Amazon gift card ($10-$2,000), check ($100 min outside US; $15 fee waived outside the US where direct deposit is unavailable). Local-bank payout ("52 selected countries") available for US, UK, DE, FR, IT, ES, CA programs; country list not captured, Qatar not confirmed [17] (O-S). Amazon.ae programme appears to pay by direct deposit only to UAE banks (Geniuslink, S) [17].
- Commission rates (US, Table 1 fixed standard rates; page ~495 days old): Luxury Beauty / Luxury Stores Beauty / Amazon Explore 10%; apparel-type 4%; grocery and health & personal care 1% [17] (O-S). Amazon.ae: 8% baseline, 7% tier incl. beauty/automotive/baby/health [17] (O-S). The "Amazon Games 20%" figure could not be confirmed (UNVERIFIED).
- Disclosure requirement: not retrieved (MEM prior: operating agreement requires the statement "As an Amazon Associate I earn from qualifying purchases"; UNVERIFIED).

### 5. Amazon KDP
- AI content: must disclose AI-generated text, images or translations when publishing or republishing an edited book; AI-assisted content (you created it, AI only edited/refined or brainstormed) needn't be disclosed; if an AI tool produced the content it counts as AI-generated even after substantial editing [18] (O-S, KDP Content Guidelines).
- Volume limits: creation limit and submission limit of 2 new titles per book format per week (ebook, paperback, hardcover counted separately); resets Sundays 00:00 UTC; updates to already-submitted titles don't count; effective 2026-09-21 per secondary; previous cap reported as 10/week [18] (KDP "Create a Book" excerpt O-S; selfpublishingadvice.org, vappingo S). The user's "3 per day" figure appears outdated.
- Payouts: KDP supports EFT to local bank for listed countries (Countries w/ EFT page; ~2017-era list; Qatar not seen), wire/check with thresholds, EFT no minimum. As of 2026-08-01 KDP stops paying accounts using a non-participating payment service provider or without completed KYC; Payoneer and Wise are participating PSPs; authors not eligible for PSP must use a bank account at a deposit-taking bank; 45 days to finish KYC after notice [19] (O-S). Whether a Qatar resident can use PSP/bank: UNVERIFIED.

### 6. Gumroad
- Fees: 10% + $0.50 per direct sale (profile/direct link); 30% flat via Discover (includes processing); older help page lists card processing 2.9% + $0.30 as additional on direct sales and a 40% fee on in-app purchases (conflict/outdated; pricing page title says "10% + 50c direct, 30% via Discover") [20] (O-S, page ~3 yrs old by metadata).
- Merchant of Record: Gumroad blog post "Gumroad is becoming a Merchant of Record (+ more updates!)" exists [20] (title only; content not read).
- Open source: github.com/antiwork/gumroad is public, MIT licence, ~5,143 commits, under the "antiwork" org, has TRADEMARK_GUIDELINES.md; contributors must fork/PR and email support@gumroad.com, and disclose AI model used [21] (O-F). The README does not describe hosted terms, fees or payouts. Ownership change/2025 details: not verified.
- AI-content stance for sellers; payout countries (bank vs PayPal); Qatar: NOT FOUND.

### 7. Fiverr - NOT RESEARCHED
(MEM prior only, uncheckable: 20% seller commission; levels; Qatar payout methods. Do not rely.)

### 8. Upwork - NOT RESEARCHED
(MEM prior only: flat 10% fee since 2023, Connects ~$0.15; may have changed in 2025-26. Do not rely.)

### 9. Apple App Store (all O-F, fetched 2026-10-25)
- Program fee: USD 99/yr (individual and organization); Enterprise USD 299/yr; local-currency pricing where available [22].
- Individual: Apple Account with two-factor authentication, legal age of majority, legal name as seller name; government photo ID only requested in some card-payment cases. Sole proprietors enrol as individuals [22].
- Organization: legal entity able to contract with Apple (no DBAs/trade names), D-U-N-S number (free in most jurisdictions), legal binding authority, work email on org domain, public functioning website; may need notarized docs; membership purchasable only after Apple verification [22].
- Regions: enrolment page lists no regions; says enrolment may not be supported in certain regions (e.g., sanctions); India only via Developer app [22]. No Qatar statement found.
- Getting paid: need Paid Apps Agreement in effect (Account Holder signs), banking info in App Store Connect (one bank only; bank country chosen from menu; additional docs in some regions), tax forms, minimum monthly payment threshold met, invoicing where required. Payment within 45 days of fiscal month end by EFT/direct deposit [22].
- Minimum payment threshold: table lists specific bank countries (most 0.02 USD; Colombia 100, Hong Kong 27, Nicaragua 90, Korea 1, Sri Lanka 5, Thailand 10, Uganda 20). Qatar not listed; "all other bank countries or regions and currencies must exceed 40 USD" [22].
- Qatar facts: financial report regions page has a Qatar row (QAR, code QA) i.e. Qatar storefront exists; Apple Distribution International Limited is the paying entity for QAR. This shows Qatar as a sales territory; does NOT prove a Qatari bank account can receive payouts [22].
- Commission: Small Business Program 15% on paid apps and IAP for developers with <= $1M proceeds in prior calendar year (or new developers); falls back to standard rate if proceeds exceed $1M in current year; 10% reduced rate for some EU alternative terms/subscriptions after year 1; standard rate (30%) not stated on fetched page (MEM) [22].
- Guidelines (last updated 2026-10-16): 4.3(a) no multiple Bundle IDs for same app; 4.3(b) no copycat apps in saturated categories; 4.2.6 commercial template/app-generator apps rejected unless submitted by content provider; 5.6.2 developer identity must be accurate; 5.6.3 discovery fraud (reviews/charts) bannable; repeated manipulative conduct = removal from program [22].

### 10. Google Play - NOT VERIFIED
- Fetched only developer.android.com pages: Android developer verification begins 2026-09-30 for participating stores in Brazil, Indonesia, Singapore, Thailand; "2027 and beyond" global expansion; Play Console path; limited distribution accounts (up to 20 devices, no government ID or fee) [23] (O-F). Verified identity required; existing Play verified identity meets it for most Play developers.
- $25 fee, tester requirement, merchant countries, 2025-26 service-fee rates: the official support.google.com pages were unreachable. MEM prior (not citable): $25 one-time; personal accounts created after Nov 2023 need closed test with 12 testers (reduced from 20) opted in for 14 days; merchant-country list unknown. The brief's "20 testers" figure is probably outdated; UNVERIFIED.

## Rules that affect an AI agent operating the account
- Human identity gates (cannot be delegated to an agent): Etsy Persona ID + selfie, 2FA, name-matches-bank [16]; Apple 2FA Apple Account, legal name, Account Holder must sign Paid Apps Agreement, org needs D-U-N-S/website/authority [22]; YouTube 2-Step Verification, 18+, AdSense [1]; Android developer identity verification [23]; KDP PSP KYC [19].
- Mass-production/automation bans: YouTube inauthentic content + spam policy on automated/AI mass production [4][5]; Etsy bans bot-generated listings with no human involvement [14]; Apple 4.3 spam and 4.2.6 template apps [22]; KDP weekly cap 2 titles/format [18].
- Disclosure duties: YouTube "AI use" [7]; TikTok AIGC label + C2PA [11]; Etsy listing-description AI statement [14]; KDP AI-generated disclosure [18].
- Engagement manipulation (bots for views/subs) can remove YPP/channel [4]; Apple 5.6.3 discovery fraud [22].
- Account sharing / multiple-account prohibitions: NOT verified on any platform this session.
- Gumroad repo contributions require AI-model disclosure (code contributions only) [21].

## Claim ledger
| claim | URL | source type | date | confidence | corroborated by |
|---|---|---|---|---|---|
| YPP current: 1,000 subs + 4,000 hrs/12mo or 10M Shorts views/90d | https://support.google.com/youtube/answer/72851?hl=en | O-S | checked 2026-10-25 | M-H | support.google.com/youtube/answer/13429240; Gulf News |
| YPP new-applicant thresholds from 2027-02-01: 8,000 hrs/365d or 20M Shorts/90d + 1,000 subs | https://support.google.com/youtube/answer/12843009?hl=en | O-S | announced ~2026-08-10 | M-H | blog.youtube post; Gulf News, RouteNote, NewscastStudio |
| Terms acceptance deadline 2027-01-31 | https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/ | O-S | 2026-08 | M | single search summary |
| Inauthentic content rename 2025-07-15 | https://support.google.com/youtube/answer/1311392?hl=en | O-S | 2025-07-15 | M-H | YouTube community FAQ |
| AI disclosure via Studio "AI use" attribute | https://support.google.com/youtube/answer/14328491?hl=en | O-S | checked 2026-10-25 | M-H | YouTube Community update thread |
| Qatar eligible for YPP | https://support.google.com/youtube/answer/7101720?hl=en | O-S | checked 2026-10-25 | M | https://support.google.com/youtube/answer/13429240 |
| AdSense threshold USD $100, paid 21st-26th | https://support.google.com/adsense/answer/1709871?hl=en | O-S | checked 2026-10-25 | M-H | https://support.google.com/youtube/answer/14727140 |
| Qatar AdSense payout: wire/check yes, EFT no | https://support.google.com/adsense/answer/7164701?hl=en-GB | O-S (old table) | >3 yrs old | L-M | none |
| TikTok Creator Rewards: 10k followers/100k views 30d, 18+ | https://www.tiktok.com/creator-academy/en/article/creator-rewards-program | O-S | ~2025-04 | M | Buffer, Brandwatch, Metricool (S) |
| TikTok eligible countries (8, no Qatar) | https://www.tiktok.com/creator-academy/en/article/creator-rewards-program | O-S | ~2025-04 | M | partial agreement w/ blogs (conflict on adds) |
| TikTok AIGC labeling + C2PA | https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content | O-S | checked 2026-10-25 | M-H | https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-content?lang=en |
| TikTok Shop not in GCC (Saudi eyed 2027) | https://www.ecomcrew.com/tiktok-shop-is-reportedly-eyeing-saudi-arabia-south-korea-and-australia-for-early-2027/ | S | 2026 | L | photonpay, echotik |
| Etsy listing $0.20, transaction 6.5%, offsite ads 15%/12% cap $100 | https://www.etsy.com/legal/fees/ | O-S | policy updated ~2026-10-05 | M-H | https://help.etsy.com/hc/en-us/articles/115014483627-What-are-the-Fees-and-Taxes-for-Selling-on-Etsy |
| Etsy processing 3% + $0.25 (US) | https://www.etsy.com/sell | O-S (old page) | ~2022 | L-M | fees policy says varies by bank location |
| Etsy AI = "Designed by", disclose in description | https://www.etsy.com/legal/creativity | O-S | ~2024 | M | https://www.etsy.com/legal/sellers/ ; https://www.etsy.com/seller-handbook/article/1522733284810 |
| Etsy Payments list has UAE (Payoneer) not Qatar | https://help.etsy.com/hc/en-us/articles/115015710408-Countries-Eligible-for-Etsy-Payments | O-S | old page | M | https://help.etsy.com/hc/en-us/articles/16999319005207-How-Do-I-Use-a-Payoneer-Account-With-Etsy-Payments |
| Etsy Persona ID + selfie, 2FA | https://help.etsy.com/hc/en-us/articles/22481159004567-How-to-Verify-Your-Identity-on-Etsy | O-S | checked 2026-10-25 | M | https://www.etsy.com/seller-handbook/article/1241780194948 |
| Associates: 180 days, 3 qualifying sales | https://affiliate-program.amazon.com/help/node/topic/G7MJTPEP9NC3YKMG | O-S | checked 2026-10-25 | M-H | operating agreement page |
| Associates payout: DD $10 / gift card $10-2,000 / check $100 | https://affiliate-program.amazon.com/help/node/topic/GGD9H76RMDDNEWAE | O-S | checked 2026-10-25 | M | https://affiliate-program.amazon.com/help/operating/policies |
| Associates local-bank payout 52 countries (Qatar unconfirmed) | https://affiliate-program.amazon.com/resource-center/receive-your-international-affiliate-earnings-in-your-local-bank | O-S | checked 2026-10-25 | M | Amazon FX FAQ G8VUMS6GTBCR9RGV |
| Associates US luxury beauty 10%, apparel 4%, grocery/health 1% | https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ | O-S | page ~495 days old | M | none |
| Associates Amazon.ae baseline 8% | https://affiliate-program.amazon.ae/help/node/topic/GRXPHT8U84RAYDXZ | O-S | old | L-M | none |
| KDP AI-generated must be disclosed; AI-assisted not | https://kdp.amazon.com/en_US/help/topic/G200672390 | O-S | checked 2026-10-25 | M-H | none |
| KDP 2 new titles/format/week | https://kdp.amazon.com/en_US/help/topic/G202172740 | O-S | eff. 2026-09-21 | M | https://selfpublishingadvice.org/amazon-cuts-kdp-weekly-upload-limit/ ; https://www.vappingo.com/word-blog/kdp-publishing-limit/ |
| KDP PSP cutoff 2026-08-01; Payoneer & Wise participating | https://kdp.amazon.com/en_US/help/topic/G6GLVRHVQZY4V4FX | O-S | 2026-08-01 | M | KDP PSP FAQ GD9NN4LS8ZDU8XZ7 |
| Gumroad 10% + $0.50 direct, 30% Discover | https://gumroad.com/pricing | O-S | page ~3 yrs old | M | https://help.gumroad.com/article/66-gumroads-fees ; sign-up page |
| Gumroad repo public, MIT licence | https://github.com/antiwork/gumroad | O-F | fetched 2026-10-25 | H | none |
| Apple $99/yr; Enterprise $299; D-U-N-S for orgs | https://developer.apple.com/support/enrollment/ | O-F | fetched 2026-10-25 | H | https://developer.apple.com/programs/ |
| Apple Small Business Program 15%, <= $1M | https://developer.apple.com/app-store/small-business-program/ | O-F | (c) 2026, no update date | H | none |
| Apple payment within 45 days; Paid Apps Agreement; one bank | https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments/ | O-F | fetched 2026-10-25 | H | enter-banking-information page |
| Apple min payment: unlisted bank countries $40 USD; Qatar not listed | https://developer.apple.com/help/app-store-connect/reference/reporting/minimum-payment-threshold | O-F | fetched 2026-10-25 | H | none |
| Apple Qatar QAR financial region exists | https://developer.apple.com/help/app-store-connect/reference/reporting/financial-report-regions-and-currencies | O-F | fetched 2026-10-25 | H | https://developer.apple.com/help/app-store-connect/reference/reporting/apple-legal-entities |
| Apple guidelines last updated 2026-10-16 | https://developer.apple.com/app-store/review/guidelines/ | O-F | 2026-10-16 | H | none |
| Android developer verification from 2026-09-30 (BR/ID/SG/TH), global 2027 | https://developer.android.com/developer-verification | O-F | fetched 2026-10-25 | H | https://developer.android.com/distribute/play-policies |

## Unverified / gaps
- Fiverr (commission, levels, AI policy, Qatar payout/availability): not researched.
- Upwork (fee, Connects, AI rules, Qatar payout/availability): not researched.
- Google Play: $25 fee, tester count (brief says 20; memory suggests 12) and 14 days, Qatar as merchant country, 2025-26 fee rates: unverified.
- Gumroad: payout countries (bank vs PayPal) and Qatar; 2025 open-source/ownership changes and MoR detail beyond repo; AI stance for sellers.
- TikTok: current (2026) eligible country list; Qatar; TikTok Shop in Qatar.
- Etsy: full Etsy Payments country list (Qatar absence inferred from search summary); current $15 set-up fee status; Etsy account-sharing rules.
- Amazon Associates: whether a Qatar resident can join (Amazon.com vs Amazon.ae/.sa), Qatar in 52-country bank list, disclosure wording, current category rate table, "Amazon Games 20%".
- KDP: Qatar EFT/PSP eligibility; royalty rates.
- Apple: whether Qatari bank accounts can receive payouts; standard 30% rate not on fetched page; Qatar Developer Program enrolment list not published on fetched pages.
- YouTube: exact current wording on support.google.com pages (page not read); Qatar AdSense payout table is old; YPP fan-funding/Shopping eligibility in Qatar.
- Account-sharing/multi-account/bot prohibitions per platform: not verified.

## Sources
[1] https://support.google.com/youtube/answer/72851?hl=en
[2] https://support.google.com/youtube/answer/12843009?hl=en ; https://support.google.com/youtube/answer/13429240?hl=en&co=GENIE.Platform%3DAndroid
[3] https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/
[4] https://support.google.com/youtube/answer/1311392?hl=en
[5] https://support.google.com/youtube/answer/2801973?hl=en
[6] https://support.google.com/youtube/answer/7101720?hl=en
[7] https://support.google.com/youtube/answer/14328491?hl=en
[8] https://support.google.com/adsense/answer/1709871?hl=en ; https://support.google.com/adsense/answer/7164701?hl=en-GB ; https://support.google.com/youtube/answer/14732067?hl=en
[9] https://gulfnews.com/technology/youtube-raises-monetisation-requirements-for-new-creators-from-2027-1.500637658 ; https://routenote.com/blog/youtube-partner-program-changes-2027/ ; https://www.newscaststudio.com/2026/08/10/youtube-partner-program-monetization-changes-2027/
[10] https://www.tiktok.com/creator-academy/en/article/creator-rewards-program ; https://buffer.com/resources/tiktok-creativity-program/ ; https://www.brandwatch.com/blog/tiktok-creator-program/
[11] https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content ; https://www.tiktok.com/community-guidelines/en/integrity-authenticity ; https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-content?lang=en
[12] https://www.ecomcrew.com/tiktok-shop-is-reportedly-eyeing-saudi-arabia-south-korea-and-australia-for-early-2027/ ; https://www.photonpay.com/en/blog/article/335
[13] https://www.etsy.com/legal/fees/ ; https://help.etsy.com/hc/en-us/articles/115014483627-What-are-the-Fees-and-Taxes-for-Selling-on-Etsy
[14] https://www.etsy.com/legal/creativity ; https://www.etsy.com/legal/sellers/ ; https://www.etsy.com/seller-handbook/article/1522733284810
[15] https://help.etsy.com/hc/en-us/articles/115015710408-Countries-Eligible-for-Etsy-Payments ; https://help.etsy.com/hc/en-us/articles/16999319005207-How-Do-I-Use-a-Payoneer-Account-With-Etsy-Payments ; https://help.etsy.com/hc/en-us/articles/360002120927-What-is-Etsy-Payments
[16] https://help.etsy.com/hc/en-us/articles/22481159004567-How-to-Verify-Your-Identity-on-Etsy ; https://www.etsy.com/seller-handbook/article/1241780194948
[17] https://affiliate-program.amazon.com/help/node/topic/G7MJTPEP9NC3YKMG ; https://affiliate-program.amazon.com/help/operating/agreement ; https://affiliate-program.amazon.com/help/operating/policies ; https://affiliate-program.amazon.com/help/node/topic/GGD9H76RMDDNEWAE ; https://affiliate-program.amazon.com/resource-center/receive-your-international-affiliate-earnings-in-your-local-bank ; https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ ; https://affiliate-program.amazon.ae/help/node/topic/GRXPHT8U84RAYDXZ ; https://geniuslink.com/blog/?p=1284
[18] https://kdp.amazon.com/en_US/help/topic/G200672390 ; https://kdp.amazon.com/en_US/help/topic/G202172740 ; https://selfpublishingadvice.org/amazon-cuts-kdp-weekly-upload-limit/ ; https://www.vappingo.com/word-blog/kdp-publishing-limit/
[19] https://kdp.amazon.com/en_US/help/topic/GJD7DFFX6X88AK46 ; https://kdp.amazon.com/help?topicId=G201208420 ; https://kdp.amazon.com/en_US/help/topic/G6GLVRHVQZY4V4FX ; https://kdp.amazon.com/help?topicId=A3E24YJK5O82TD
[20] https://gumroad.com/pricing ; https://help.gumroad.com/article/66-gumroads-fees ; https://gumroad.gumroad.com/p/gumroad-is-becoming-a-merchant-of-record-more-updates
[21] https://github.com/antiwork/gumroad
[22] https://developer.apple.com/programs/ ; https://developer.apple.com/support/enrollment/ ; https://developer.apple.com/app-store/small-business-program/ ; https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments/ ; https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information ; https://developer.apple.com/help/app-store-connect/reference/reporting/minimum-payment-threshold ; https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements ; https://developer.apple.com/help/app-store-connect/reference/reporting/financial-report-regions-and-currencies ; https://developer.apple.com/help/app-store-connect/reference/reporting/apple-legal-entities ; https://developer.apple.com/app-store/review/guidelines/
[23] https://developer.android.com/developer-verification ; https://developer.android.com/developer-verification/guides/google-play-console ; https://developer.android.com/distribute/play-policies

---
# SUPPLEMENT (lead session, Parallel Search excerpts + fetches, checked 2026-10-25)

## Fiverr (official help pages, excerpts)
- Payout methods: PayPal (24 h, $0 fee, $1 min); Bank Transfer via Payoneer (1-3 business days local currency or 5-7 USD wire; $1 fee (one table) / $3 (another table), $20 min); Payoneer Account (up to 2 business days, $3 fee, $10 min); Fiverr Revenue Card by Payoneer ($1 within 2 days or $3 within 2 hours). "Payoneer availability depends on your country." https://help.fiverr.com/hc/en-us/articles/360010530058-Withdrawing-your-earnings-managing-payout-methods ; https://help.fiverr.com/hc/en-us/articles/14257019400465-Setting-up-Payoneer-as-a-payout-method
- Earnings clear 14 days after order completion (shorter for Top Rated / Seller Plus / Pro). One account per withdrawal provider per profile. https://help.fiverr.com/hc/en-us/articles/34069565843985-How-Fiverr-works-for-freelancers
- Payment Terms last updated October 2026: buyer Order Initiation Fee US$5; hourly-contract service fee 5.5%. https://www.fiverr.com/legal-portal/legal-terms/payment-terms-of-service
- Seller commission 20% of each order: long-standing Fiverr rule; NOT in the excerpts retrieved (verify on fiverr.com/legal-portal before relying). Fiverr AI-content policy text: not retrieved (UNVERIFIED; subagent I cites a Fiverr ban on bulk AI delivery from snippets).
- Qatar: no page found that excludes Qatar; payout via PayPal or Payoneer would apply. UNVERIFIED for account opening.

## Upwork (official pages, excerpts + fetch)
- Freelancer Service Fee: variable **0% to 15% per contract**, locked when the proposal/offer is sent; applies to all earnings incl. bonuses. https://support.upwork.com/hc/en-us/articles/211062538-Learn-about-the-Freelancer-Service-Fee ; https://www.upwork.com/pricing/freelancer
- Connects **$0.15 each**; free monthly Connects; Freelancer Plus $19.99/month (+70 Connects). https://www.upwork.com/tools/connects-calculator ; https://www.upwork.com/resources/is-upwork-free (Jul 2026)
- Payout methods vary by location: bank transfer (Direct to Local Bank **$0.99 per withdrawal**), PayPal, Payoneer, wire, M-Pesa. https://support.upwork.com/hc/en-us/articles/211063888-How-to-withdraw-earnings-with-Direct-to-Local-Bank (fetched; currency list truncated in the extract, so **QAR availability UNVERIFIED**; Payoneer and wire are documented alternatives)
- Payoneer-Upwork partnership renewed 14 May 2026 (Payoneer Account and Direct to Local Bank for international freelancers). https://investor.payoneer.com/news-releases/news-release-details/payoneer-and-upwork-extend-15-year-partnership-power-global
- Upwork AI-content rules and Qatar account availability: not retrieved (UNVERIFIED).

## Google Play (official Play Console Help, excerpts)
- Supported locations table: **Qatar ✔ developer registration ✔ merchant registration, default currency USD**. https://support.google.com/googleplay/android-developer/answer/9306917
- Registration fee one-off **USD 25**; personal accounts created after 13 Nov 2023 must run a closed test with **at least 12 testers opted in continuously for 14 days** before production access. https://support.google.com/googleplay/android-developer/answer/14151465 ; https://support.google.com/googleplay/android-developer/answer/14659200
- Service fees page now shows tiered structure with a separate billing fee (e.g. "10% + 5% billing fee", "20% + 5%", "25% + 5%", and 15% for external web links), with effective dates 30 Jun 2026 (EEA, UK, US) and 30 Sep 2026 (Australia, Japan). Excerpt is partial; read the page before pricing an app. https://support.google.com/googleplay/android-developer/answer/112622
- Android developer verification: all Play package names must be registered by **30 Sep 2026** or apps are removed. https://support.google.com/googleplay/android-developer/answer/16984799

## Etsy (official, page FETCHED)
- Etsy Payments countries (full list fetched): Argentina*, Australia, Austria, Belgium, Brazil*, Bulgaria, Canada, Chile*, China*, Croatia, Cyprus, Czech Republic, Denmark, Egypt*, Estonia, Finland, France, Georgia*, Germany, Greece, Hong Kong, Hungary, India*, Indonesia, Ireland, Israel, Italy, Japan*, Kazakhstan*, Latvia, Lithuania, Luxembourg, Malaysia, Malta, Mexico, Morocco, Netherlands, New Zealand, Norway, Pakistan*, Peru*, Philippines, Poland, Portugal, Romania, Serbia*, Singapore, Slovakia, Slovenia, South Africa, South Korea*, Spain, Sweden, Switzerland, Thailand*, Türkiye, Ukraine*, United Arab Emirates*, United Kingdom, United States, US territories, Vietnam (* = via Payoneer). **Qatar is not listed.** https://help.etsy.com/hc/en-us/articles/115015710408-Countries-Eligible-for-Etsy-Payments
- "You can only open an Etsy shop in a country where Etsy Payments is available." One-time non-refundable shop set-up fee at onboarding (amount not in excerpt; USD 15 per secondary sources). https://help.etsy.com/hc/en-us/articles/115015672808 ; https://help.etsy.com/hc/en-us/articles/1500006519562-Why-Can-t-I-Open-a-Shop-in-My-Country
- Consequence: a Qatar-resident owner cannot open an Etsy shop. Etsy is OUT of the category wheel for this studio unless the owner has a bank account and residential address in an eligible country.

## TikTok (official, excerpt)
- Creator Rewards Program (Creator Academy, last updated 10 Sep 2026): open to creators in the **United States, United Kingdom, Germany, Japan, South Korea, France, Mexico and Brazil** only; must be based there with an account registered there. **Qatar not eligible.** https://www.tiktok.com/creator-academy/article/creator-rewards-program ; https://support.tiktok.com/en/business-and-creator/creator-rewards-program/creator-rewards-program
- Program terms: legal resident of a program country, 18+, linked payment account in own name; eligible videos >= 1 minute. https://www.tiktok.com/legal/page/global/tiktok-creator-rewards-program-br/en

## YouTube (official, excerpts)
- YPP thresholds today: 1,000 subscribers + 4,000 qualified public watch hours (12 months) OR 1,000 subscribers + 10M qualified Shorts views (90 days). https://support.google.com/youtube/answer/72851
- **From 1 Feb 2027 new creators need 8,000 qualified watch hours (365 days) or 20M qualified Shorts views (90 days), plus 1,000 subscribers**; existing members unaffected; activity requirement (1,000 watch hours/365 d or 1M Shorts views/90 d) to stay in. Fan funding / Shopping entry stays at 500 subs + 3,000 hours or 3M Shorts views. https://support.google.com/youtube/answer/12843009
- Channel monetisation policies, 15 Jul 2025: "repetitious content" renamed **"inauthentic content"**, clarified to include mass-produced or repetitive content; "applies regardless of how the content was made"; channels using AI remain eligible if original and authentic. https://support.google.com/youtube/answer/1311392 ; https://support.google.com/youtube/thread/356734251
- YPP availability list includes **Qatar**. https://support.google.com/youtube/answer/7101720

## Amazon (official, fetch + excerpts)
- Associates international bank transfer covers 52 countries = US, UK and Eurozone/EUR countries only; **Qatar not included**, so a Qatar bank cannot receive Associates direct deposit from the US programme; alternatives: Amazon gift card (min $10) or check (min $100). https://affiliate-program.amazon.com/help/node/topic/G8VUMS6GTBCR9RGV (fetched) ; https://affiliate-program.amazon.com/help/node/topic/GP8Z3AZ27ZFHTEUL
- Amazon has separate Associates programmes for Saudi Arabia (amazon.sa) and UAE (amazon.ae) among its marketplaces; eligibility for Qatar residents not retrieved (UNVERIFIED). https://affiliate-program.amazon.com/help/node/topic/G84KVZ7BTNXHF4UH
- KDP payment options: direct deposit (EFT, no threshold where available), wire and check ($100 threshold); no PayPal; availability depends on bank location (Qatar EFT UNVERIFIED). https://kdp.amazon.com/en_US/help/topic/GJD7DFFX6X88AK46 ; https://kdp.amazon.com/en_US/help/topic/G201207800
- KDP 70% royalty option does not require living in a 70% territory. https://kdp.amazon.com/help/topic/G200644210
