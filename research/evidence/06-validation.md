# Zero-cost validation benchmarks (checked 2026-10-25)

Method note: two limits applied to this run. (1) The page-fetch tool could not resolve any host (ENOTFOUND on unbounce.com, lemlist.com, woodpecker.co, belkins.io, kickstarter.com, indiehackers.com), and direct curl was refused by the egress proxy, so NO primary page was read. (2) The shared web-search budget ran out after 12 searches. Every figure below is therefore taken from search-result summaries of the named pages and is secondary unless stated. Confidence is capped at M for that reason. Arithmetic is mine (Python, binomial, scripts in /tmp/claude-0/-home-user/ec294943-3007-54b7-bb44-949b2f3654da/scratchpad/calc/).

## Benchmarks table (test type | metric | median/typical | best-case | source | date)

| Test type | Metric | Median / typical | Best-case | Source | Date |
|---|---|---|---|---|---|
| Landing page, all industries | Median visitor-to-conversion (any page goal) | 6.6% | n/a | Unbounce [1][3] | 2024 report (visits Jul 2023-Jul 2024), ~41,000 pages, 57M conversions |
| Landing page, SaaS | Median conversion | 3.8% (42% below all-industry) | one secondary site says top-quartile SaaS ~11.6% (unconfirmed) | Unbounce [1] | 2024 |
| Landing page, ecommerce | Median conversion | 4.2% in page header vs 5.2% in body text (internal conflict) | food and beverage 7.1% | Unbounce [4] | 2024 |
| Landing page, professional services (closest to lead gen) | Median / top 25% | 6.1% | top 25% starts at 14.1% | Unbounce via search summary [3] | 2024 |
| Landing page, financial services | Median | 8.3% (another summary says 8.4%) | insurance 18.2% | Unbounce [3] | 2024 |
| Search-ad traffic (not a page benchmark) | Average conversion, Google/Microsoft ads | 7.52% (prior year 6.96%) | automotive 14.67% | WordStream/LocaliQ [5] | June 2025 |
| Free-launch traffic: Product Hunt, not featured | Visitors / signups on launch day | 100-500 visitors, 1-15 signups | n/a | Awesome Directories analysis via [17] | Nov 2025 |
| Free-launch traffic: Product Hunt, rank 31+ | Visitors / signups | under 300 visitors, under 10 signups | n/a | [18] | 2026 |
| Free-launch traffic: Product Hunt, rank 4-10 / top 3 | Visitors / signups | 1,000-3,000 / 30-100; top 3: 5,000-15,000 / 100-400 | n/a | [18] | 2026 |
| Product Hunt founder examples | Visitors to signups | #13: 323 visitors, 26 signups; #2: 570 launch-day visitors, 1,317 week-1 visitors, 85 users (6.45%) | n/a | founder posts [19][20][21] (attribution of each figure unconfirmed) | 2022-2026 |
| Product Hunt visitor-to-signup | Rate | 2-4% healthy B2C, 1-2% other (vendor guide) | 8-15% (another vendor guide, weight lightly) | [17][21] | 2026 |
| Show HN | Visits to signups | 45 signups from ~5,000 visits (<1%) in one write-up | Warp: 11K visits, 1,800 signups (16%) | [23][22] | undated / 2026 |
| Reddit | Visits to signups | niche subreddit 3-10% (vendor blog, UNVERIFIED) | Warp r/programming: 34K visits, 8,900 signups (26%) | [22][24] | 2026 |
| Cold email, strict method | Reply rate (auto-replies excluded) | 0.45% (7,530,489 sends, 34,393 replies) | n/a | Belkins [11][12] | 2025 data, published 2026 |
| Cold email, platform data | Average reply rate | 3.43% (Instantly); 2.09% (Mailshake, 1.37M emails); 3.1% (Cleanlist) | top quartile 5.5%+, top 10% 10.7%+ (Instantly) | [13][7][9][6] | 2025-2026 |
| Cold email, small lists | Reply rate | under 50 recipients 5.8% vs 500+ 2.1% (Belkins via Woodpecker, via search summary); under 100: 5.5% | 1-2 contacts per company 7.8% vs 3.8% at 10+ | [6][8][11] | 2024-2025 data |
| Cold email, positive replies | Positive reply rate | 1.4% of sends (Cleanlist); 1-2% (Thakkar) | top 4-6% | [9][10] | 2026 |
| Cold email, meetings | Meeting-booked rate per send | 0.5% (Thakkar), 0.7% (Cleanlist), 0.5-2.5% range (Lemlist) | top 2-3% | [10][9][6] | 2026 |
| Cold email, sequence | Share of replies from first email | 58% first email, 42% follow-ups | n/a | Instantly [13][41] | 2026 |
| LinkedIn DM | Message reply rate | 10.4% of outbound messages | warm/inbound-primed 25-40% (vendor claim) | Expandi [14] | H1 2026 |
| LinkedIn connection note | Reply to note | 3.0% (fell from 3.5% May 2025 to 2.2% Apr 2026) | n/a | Expandi [14] | 2026 |
| LinkedIn personalisation | Personalised note vs none | 25.3% accept / 8.2% reply vs 27.6% / 5.3% (attributed to Belkins) | n/a | [14][15] | 2025-2026 |
| LinkedIn acceptance | Connection acceptance | 25-35% baseline | n/a | [15][16] | 2026 |
| Kickstarter | Launched-project success rate | 41.39% (platform page, undated); 42.74% (2026 stats site) | games ~49%, tech ~23% | Kickstarter [25], [29] | undated / 2026 |
| Kickstarter | Successful project size | mean backers 255; median raised $5,050 (2017); median successful goal $3,838 (331K-project analysis) | wearables median 402 backers | [26][27] | 2017 / analysis undated |
| Waitlist to paid | Conversion | 5-25%, ~20% if onboarded within a month, under 10% after 3 months (Indie Hackers post); open waitlists 2-3% (vendor, attributed to Lenny Rachitsky 2022) | cohort launch 8-15% vs single blast 1-4% (vendor claim) | [31][32][33] | 2022-2026 |
| Waitlist false positive anecdote | Signups to payers | 4,500 signups to 5 payers = 0.11% (unnamed founder) | n/a | [34] | undated |

## Detail per test type with [n] citations

**Landing pages.** Unbounce's latest edition I could confirm is the 2024 report (about 41,000 pages, 57M conversions). All-industry median 6.6%, SaaS 3.8% [1][3]. A "conversion" is any page goal (ebook download counts), so it overstates demand-signal quality for a waitlist. One site cites a 4.02% "2026" Unbounce median [40]; I found no corroboration, so I did not use it. HubSpot was not retrieved. WordStream's 7.52% is a paid-search conversion rate, not a landing-page benchmark [5]. Traffic source changes the number heavily: one source cites 5.1% for SaaS search-ad traffic vs 0.3% for display [1 summary].

**Realistic $0 traffic in 7 days.** All data are founder anecdotes or vendor blogs; none is a controlled study. A non-featured Product Hunt launch gives about 100-500 visitors and 1-15 signups; rank 31+ gives under 300 visitors and under 10 signups [17][18]. A #13 launch reported 323 visitors and 26 signups [19-21]. A five-founder roundup found 7-day signups from 71 to about 450, with the spread driven mainly by pre-existing audience [19]. Show HN can give thousands of visits but one write-up got under 1% conversion [23]; HN also discourages "coming soon" or waitlist-only links [24]. Reddit and LinkedIn communities: no neutral data found (UNVERIFIED). Working assumption for a founder with no audience: 100-500 qualified visitors in 7 days from one free launch plus a few community posts.

**Cold email.** Reported reply rates range 0.45% to 3.4% depending on method. Belkins excludes auto-replies and counts unique replies per send [11]; platform vendors (Instantly 3.43%, Mailshake 2.09%, Cleanlist 3.1%) include more [13][7][9]. One guide says published benchmarks vary up to 7.6x by method [41 summary]. Positive reply is about 1-2% of sends and meetings about 0.5-0.7% [9][10]. Small, tightly targeted lists do much better (5.5-5.8% reply under 50-100 recipients) [6][8]. Follow-ups matter: about 42% of replies come from sequence steps after the first email [13]. B2B vs B2C split: no clean data found; Mailshake only says a 3% reply rate reads differently by segment [7] (UNVERIFIED for B2C). Gong benchmark was not retrieved (UNVERIFIED).

**LinkedIn.** About 10% of outbound DMs get any reply; connection-note replies are about 3% and falling [14]. Personalised connection notes lifted replies from 5.3% to 8.2% (attributed to Belkins) [14][15]. LinkedIn publishes no official figures [16]. The share of replies that show intent is not reported; I use the cold-email ratio (1.4/3.1 = 45%, derived) as a stand-in.

**Pre-sales and crowdfunding.** Kickstarter success is about 41-43% across all launches [25][29]. Average backers for funded projects were 255 and the median raise $5,050 in 2017 [26]. Small campaigns under $1,000 were the most likely to fail to deliver (Mollick) [28]; a Kickstarter-commissioned report said most failures were goals of $1,000 or less [30]. I could not find a median backer count for small campaigns or any Indiegogo figure (UNVERIFIED). Indie-hacker pre-sale case studies with hard numbers: none found within the search limit (UNVERIFIED). Fake door / smoke test: Dropbox's demo video took a waitlist from about 5,000 to about 75,000 [38], but that is a survivor story with a distribution channel (Digg/HN), not a base rate. Fake-door framing in the literature: landing page with a buy or sign-up button, hypothesis form "if we offer X to Y, at least Z% will do W in T" [38]. Savoia XYZ thresholds not retrieved.

## Practitioner minimum-sample guidance

- The Mom Test sets no N. The test is qualitative: a meeting succeeds only if it ends in a commitment or advancement (time, reputation, money); compliments count for nothing [35]. Primary book text was not read.
- Secondary summaries of interview counts: 10-15 as the floor below which signal cannot be told from noise, 30-50 interviews to see patterns [36 Launchrock]; Steve Blank 50-100 across discovery and validation [36 Koji, secondary, UNVERIFIED]; "after about ten, answers tend to repeat" [36 Oregon State]; Fitzpatrick 20-30 structured interviews [36 Koji, UNVERIFIED]. A reader's note puts Hansen's 5-10 interviews at 20-30 hours over 4-6 weeks, and flags it as the note-taker's own estimate [37].
- Eric Ries, Y Combinator, Tiny Seed/MicroConf, Justin Jackson, Arvid Kahl: not retrieved (search limit). UNVERIFIED. None of the above gives a visitor or message N for a smoke test; those must come from the statistics below.

## False positives: signals vs money

- Waitlist to paid: 5-25% with fast onboarding and under 10% after three months [31]; 2-3% for open waitlists [32]; single-blast launches 1-4% vs cohort launches 8-15% [33]. All are vendor or forum claims.
- 4,500 signups to 5 payers (0.11%) is one unnamed-founder anecdote [34]; treat as illustrative of the tail, not a rate.
- Implication (derived): 3 email signups at 2-25% waitlist-to-paid imply 0.06-0.75 expected payers. One payer is worth roughly 4 to 50 signups.
- Stated intent vs purchase: a vendor glossary says intent predicts direction but overstates absolute purchase, most for new, expensive products [39]. No data on startup LOI-to-purchase conversion was found (UNVERIFIED).
- Mom Test: money is the strongest currency; a letter of intent is a weaker form of it [35]. Tesla-reservation argument (deposit turns a soft signal into a costly one) is commentary, not data [34].

## Arithmetic for the studio's threshold (show the calculation)

P(X>=3) with X ~ Binomial(n, p), p = chance one message (or visitor) yields one qualifying signal. P(X>=3) = 1 - sum_{i=0..2} C(n,i) p^i (1-p)^(n-i).

Choice of p for outreach (per message, positive signal = intent reply or booked call): 0.5% (Belkins strict reply 0.45% / meeting rate 0.5%), 1.4% (positive-reply average, Cleanlist), 2.5% (small-list reply 5.5% x ~45% positive, derived), 5% (top-quartile positive 4-6%; or LinkedIn 10.4% x 45% = 4.7%), 10% and 15% (hypothetical strong-fit idea).

| p per message | n=20 | n=50 | n=100 |
|---|---|---|---|
| 0.5% | 0.0% | 0.2% | 1.4% |
| 1.4% (benchmark positive) | 0.3% | 3.3% | 16.5% |
| 2.5% | 1.3% | 12.9% | 45.8% |
| 5% | 7.5% | 45.9% | 88.2% |
| 10% | 32.3% | 88.8% | 99.8% |
| 15% | 59.5% | 98.6% | 100% |

Reading: with 20 messages, three signals need a true rate near 15%+ to pass more than half the time. At the 1.4% benchmark the pass chance is 0.3%, so the rule works as a strong-evidence filter, not a benchmark-calibrated one. An idea with a true 10% intent rate (a very good one) is parked 68% of the time at n=20. Samples to reach 80% chance of >=3: 305 messages at 1.4%, 171 at 2.5%, 85 at 5%, 42 at 10%.

Landing page, sign-ups as the signal, c = visitor-to-signup (Unbounce SaaS median 3.8%, all-industry 6.6%):

P(>=3 sign-ups), n=100 visitors / n=300 visitors:
- c=0.5%: 1.4% / 19.1%
- c=1%: 7.9% / 57.8%
- c=2%: 32.3% / 94.0%
- c=3.8% (SaaS median): 73.7% / 99.9%
- c=6.6% (all-industry median): 96.4% / 100%
- c=10%: 99.8% / 100%

Reading: three email sign-ups from 100 visitors is what a median SaaS page produces about three times in four, so it is not evidence of demand. Three sign-ups from 300 visitors passes 58% of the time even at a 1% rate.

Pre-order path (sign-up rate x waitlist-to-paid): 3.8% x 3% = 0.11% per visitor; 3.8% x 20% = 0.76%; 6.6% x 20% = 1.3%. P(>=1 payment) from 100 / 300 visitors: 10% / 28% at 0.11%; 53% / 90% at 0.76%; 73% / 98% at 1.3%. So 300 visitors are needed to get a meaningful chance of even one payment.

Confidence intervals (Wilson 95%): 3/20 = 5.2-36%; 3/50 = 2.1-16%; 3/100 = 1.0-8.5%; 5/100 = 2.2-11%. Zero signals: upper bound 13.9% at n=20, 5.8% at n=50, 3.0% at n=100, 1.0% at n=300 (rule of three style).

Sequential outreach design (pass if >=3 in first 20; if 1-2, send 30 more and need >=3 cumulative in 50; 0 in 20 = park): overall pass chance 2.7% at p=1.4%, 10.6% at 2.5%, 39.2% at 5%, 81.7% at 10%, 95.3% at 15% (vs fixed n=50: 3.3%, 12.9%, 45.9%, 88.8%, 98.6%).

Fixed thresholds k of n=50 / 100 (false pass at 1.4%, power at 5% and 10%): n=50,k=3: 3.3% / 45.9% / 88.8%. n=100,k=5: 1.4% / 56.4% / 97.6%. n=100,k=4: 5.2% / 74.2% / 99.2%.

Landing page rate bars, P(pass) at c=3.8% / 6.6% / 10% / 15%: >=8 of 100: 3.7% / 34% / 79% / 99%. >=10 of 100: 0.5% / 12% / 55% / 95%.

## Recommended threshold and why (and what to keep from the current rule)

Keep: the "3 signals in 7 days, else park" shape; three entry routes; $0 only; "parked" not "killed"; booked calls and pre-orders as qualifying signals.

Change:
1. **Denominator is the missing piece.** 3 signals means different things at n=20 and n=100. Minimum denominators: outreach 50 personalised ICP messages (sequential: first 20, extend to 50 if 1-2 signals so far; 0 of 20 = park); landing page 100 qualified unique visitors (non-network, ICP-matching); pre-sale offer 20 direct asks to qualified prospects. If the denominator is not reached by day 7, the result is "inconclusive", not "failed".
2. **Window:** 7 days of exposure plus a mandatory day-3 follow-up, with replies counted until day 9 (48h tail). Reason: about 42% of replies come from follow-ups [13].
3. **Weights (signal units, SU).** Pass = 3 SU within window.
   - Payment, deposit or pre-order from a stranger: 3 SU (passes alone). Reason: one payer is worth roughly 4-50 sign-ups [31][32].
   - Booked call with ICP who is not in the founder's network: 1 SU (drops to 0 if not held within 14 days).
   - Reply with explicit intent (names the problem, asks for next step, price or access): 1 SU. "Sounds cool" or "send info": 0.
   - Email sign-up from non-network ICP visitor: 1/3 SU each, and only if >=100 visitors and conversion >=8%.
   - Likes, follows, upvotes, views, shares, friend or family sign-ups: 0.
4. **Landing-page bar:** >=100 qualified visitors, >=8 sign-ups (>=8%), and >=3 of them take a second step (reply with a use case, book a call, or pre-order). The 8% bar sits above the SaaS median (3.8%) and the all-industry median (6.6%) [1][3]; a median page passes it 3.7% of the time (SaaS) and 34% (all-industry), while a 10% page passes 79%.
5. **Outreach bar:** >=3 SU from >=50 messages (>=6%). False pass 3.3% at the 1.4% benchmark; 89% pass for a true 10% idea; 46% for a true 5% idea. Using the sequential variant lowers cost with little loss (81.7% vs 88.8% at 10%).
6. **Pre-sale bar:** >=1 payment from >=20 asks. 0 of 20 leaves a true rate up to ~14% plausible, so do not treat 0 of 20 as proof of no demand; treat it as "not strong enough to proceed".

What the evidence does not support: using the current 20-message rule as a sole kill rule (it parks ~68% of true-10% ideas), or counting raw email sign-ups as intent (median pages pass the 3-in-100 bar 74% of the time).

## Claim ledger (claim | URL | source type | date | confidence | corroborated by)

| Claim | URL | Source type | Date | Confidence | Corroborated by |
|---|---|---|---|---|---|
| Unbounce SaaS median 3.8%; all-industry 6.6%; ~41,000 pages, 57M conversions | https://unbounce.com/conversion-benchmark-report/saas-conversion-rate/ | vendor report (search summary) | 2024 | M | [3], webtonic, foundrycro |
| Professional services median 6.1%, top 25% 14.1%; financial 8.3% | https://unbounce.com/conversion-benchmark-report/ | vendor report (search summary) | 2024 | M | single |
| Ecommerce 4.2% vs 5.2% (page conflicts) | https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/ | vendor report | 2024 | L | none |
| WordStream average ad conversion 7.52% | https://www.wordstream.com/blog/conversion-rate-benchmarks | vendor | Jun 2025 | M | segwise |
| Belkins reply 0.45%, 7,530,489 emails, 34,393 replies | https://belkins.io/blog/cold-email-response-rates | vendor study (search summary) | 2026 (2025 data) | M | somethinginc.com |
| Instantly avg 3.43%, top quartile 5.5%, top 10% 10.7% | https://instantly.ai/blog/email-sequence-benchmarks-2026-whats-a-good-open-rate-reply-rate-and-cost-per-meeting/ | vendor | 2026 | M | lemlist, woodpecker |
| 58% of replies from first email, 42% from follow-ups | https://instantly.ai/blog/email-sequence-benchmarks-2026-whats-a-good-open-rate-reply-rate-and-cost-per-meeting/ | vendor | 2026 | M | single |
| Mailshake 2.09% over 1.37M emails | https://mailshake.com/blog/cold-email-benchmarks-2026/ | vendor | 2026 | M | single |
| Positive reply 1.4% avg, 4-6% top; meeting 0.7% avg, 2-3% top | https://www.cleanlist.ai/blog/2026-02-18-cold-email-response-rate-statistics | vendor blog | Feb 2026 | L-M | thakkar |
| Meeting-booked 0.5% avg; positive reply 1-2% | https://priyeshthakkar.com/blog/cold-email-benchmarks-2026 | consultant blog | 2026 | L-M | cleanlist |
| Meeting-booked range 0.5-2.5% | https://www.lemlist.com/blog/cold-email-benchmarks | vendor | 2026 | M | cleanlist |
| Lists under 50 recipients 5.8% vs 500+ 2.1% | https://woodpecker.co/blog/cold-email-statistics/ | vendor (citing Belkins, older data) | undated | L-M | lemlist summary |
| LinkedIn DM reply 10.4%; connection-note reply 3.0%, falling to 2.2% | https://expandi.io/blog/state-of-li-outreach-h1-2026/ | vendor data | H1 2026 | M | joinvalley, linkmagnet (approx) |
| Personalised LinkedIn note: 8.2% reply vs 5.3% (attributed to Belkins) | https://www.joinvalley.co/blog/linkedin-reply-rate-benchmarks-2026 | vendor (attribution unconfirmed) | 2026 | L | expandi |
| PH non-featured 100-500 visitors, 1-15 signups | https://www.shno.co/marketing-statistics/product-hunt-launch-statistics | stats aggregator | 2025-2026 | L-M | causo |
| PH rank 31+ under 300 visitors, under 10 signups | https://hub.causo.ai/guides/product-hunt-traffic-data-2026 | vendor guide | 2026 | L-M | shno |
| Five-founder roundup: 7-day signups 71-450 | https://happysupport.ai/blog/product-hunt-launch-roundup-2026 | blog | 2026 | L | none |
| Show HN: 45 signups from ~5,000 visits | https://www.grizzlypeaksoftware.com/articles/p/zero-budget-launch-how-i-got-500-signups-without-ads-BU5g8t | founder blog | undated | L | none |
| Warp r/programming 34K visits, 8,900 signups; Show HN 11K / 1,800 | https://www.teract.ai/resources/reddit-vs-hackernews-tech-marketing-2026 | vendor blog | 2026 | L | none |
| Kickstarter success 41.39% | https://www.kickstarter.com/help/stats?ref= | primary (search summary only) | undated | M | expandedramblings 42.74% |
| Avg backers 255; median raised $5,050 (successful) | https://www.crowdfundinsider.com/2017/07/119902-kickstarter-milestone-100000-independent-creators-funded-projects-crowdfunding-platform/ | news (attribution of search summary not confirmed) | 2017 | L-M | none |
| Median successful goal $3,838 (331K projects) | https://medium.com/@daniel.kupka/we-analyzed-331-000-kickstarter-projects-here-s-what-we-learned-about-crowdfunding-success-63b341b025ac | analyst blog | undated | L | none |
| Under-$1,000 campaigns most likely to fail to deliver | https://www.cnbc.com/2015/12/10/9-percent-kickstarter-projects-fail-to-deliver.html | news on Mollick study | 2015 | M | hypebot |
| Waitlist to paid 5-25%, ~20% if <1 month, <10% after 3 months | https://www.indiehackers.com/post/how-many-waiting-list-signups-should-we-have-before-building-mvp-05ea06e9ca | forum post | undated | L | mean.ceo |
| Open waitlists 2-3% convert; attributed to Lenny Rachitsky 2022 | https://blog.mean.ceo/?p=11219 | vendor blog | 2026 | L | none |
| Cohort launch 8-15% vs blast 1-4% | https://blog.getlaunchlist.com/blog/convert-waitlist-to-paying-customers | vendor blog | 2026 | L | none |
| 4,500 signups to 5 payers | https://echai.ventures/startingup/validate-idea/is-a-waitlist-with-a-lot-of-signups-actual-proof-of-demand | blog (which blog unconfirmed; also possible: https://xartup.substack.com/p/why-most-startup-waitlists-suck-and) | undated | L | none |
| Mom Test: commitment = time, reputation, money; compliments worthless | https://mtlynch.io/book-reports/the-mom-test/ | book report | 2023 area | M | ybrikman.com, sachinrekhi.com |
| 10-15 floor; 30-50 for patterns | https://www.launchrock.com/library/expert-advice/customer-discovery | vendor blog | undated | L | koji.so |
| Blank 50-100; Fitzpatrick 20-30 | https://www.koji.so/docs/startup-idea-validation-guide | vendor blog | undated | L | none |
| Dropbox waitlist ~5,000 to ~75,000 after demo video | https://yourstory.com/2026/02/dropbox-fake-demo-video-75k-signups-mvp | media | Feb 2026 | M | alexanderjarvis.com |
| Intent overstates purchase, most for new products | https://ballparkhq.com/research-glossary/purchase-intent | vendor glossary | undated | L | none |

## Unverified / gaps

- No primary page was read; fetch tool failed on every host and search budget ran out. Every figure is from search-result summaries.
- Unbounce lead-gen median and any 2025/2026 edition: not found; 2024 is the latest I can confirm. HubSpot landing-page benchmark: not retrieved.
- Free-channel 7-day traffic for Reddit, LinkedIn posts, and communities: no neutral data. Product Hunt data are anecdotes and vendor guides.
- Gong, Woodpecker follow-up/personalisation splits, B2B vs B2C reply rates: not retrieved. The FlowStrata "Belkins 8.5%, personalisation 4-22%" figures conflicted with other Belkins reports and were excluded.
- Share of cold replies that show real intent for founder-led outreach: only vendor ratios (positive/reply about 45%, derived); no study.
- Kickstarter/Indiegogo median backers for small campaigns; Indiegogo success rate; indie-hacker pre-sale case studies with numbers: not found.
- Eric Ries, Y Combinator, Tiny Seed/MicroConf, Justin Jackson, Arvid Kahl minimum-N guidance: not retrieved. Mom Test has no stated N in any source seen.
- Startup LOI-to-purchase conversion: no data. Waitlist-to-paid ranges are vendor/forum claims and the 4,500-to-5 case is unnamed.
- True intent-rate p1 that justifies building is not in the literature; the 5-10% target is my judgement, not a benchmark.

## Sources

[1] https://unbounce.com/conversion-benchmark-report/saas-conversion-rate/
[2] https://unbounce.com/landing-pages/whats-a-good-conversion-rate/
[3] https://unbounce.com/conversion-benchmark-report/
[4] https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/
[5] https://www.wordstream.com/blog/conversion-rate-benchmarks
[6] https://www.lemlist.com/blog/cold-email-benchmarks
[7] https://mailshake.com/blog/cold-email-benchmarks-2026/
[8] https://woodpecker.co/blog/cold-email-statistics/
[9] https://www.cleanlist.ai/blog/2026-02-18-cold-email-response-rate-statistics
[10] https://priyeshthakkar.com/blog/cold-email-benchmarks-2026
[11] https://belkins.io/blog/cold-email-response-rates
[12] https://somethinginc.com/blog/cold-email-response-rates-2026-data/
[13] https://instantly.ai/blog/email-sequence-benchmarks-2026-whats-a-good-open-rate-reply-rate-and-cost-per-meeting/
[14] https://expandi.io/blog/state-of-li-outreach-h1-2026/
[15] https://www.joinvalley.co/blog/linkedin-reply-rate-benchmarks-2026
[16] https://linkmagnet.gg/blog/statistiques-messagerie-dm-linkedin-2026
[17] https://www.shno.co/marketing-statistics/product-hunt-launch-statistics
[18] https://hub.causo.ai/guides/product-hunt-traffic-data-2026
[19] https://happysupport.ai/blog/product-hunt-launch-roundup-2026
[20] https://www.producthunt.com/p/rolyai/3-days-after-my-first-product-hunt-launch-traffic-learnings-next-steps
[21] https://edwardsturm.com/articles/product-hunt-results/
[22] https://www.teract.ai/resources/reddit-vs-hackernews-tech-marketing-2026
[23] https://www.grizzlypeaksoftware.com/articles/p/zero-budget-launch-how-i-got-500-signups-without-ads-BU5g8t
[24] https://getlaunchlist.com/blog/first-100-waitlist-signups
[25] https://www.kickstarter.com/help/stats?ref=
[26] https://www.crowdfundinsider.com/2017/07/119902-kickstarter-milestone-100000-independent-creators-funded-projects-crowdfunding-platform/
[27] https://medium.com/@daniel.kupka/we-analyzed-331-000-kickstarter-projects-here-s-what-we-learned-about-crowdfunding-success-63b341b025ac
[28] https://www.cnbc.com/2015/12/10/9-percent-kickstarter-projects-fail-to-deliver.html
[29] https://expandedramblings.com/index.php/kickstarter-statistics/
[30] https://www.hypebot.com/?p=10227
[31] https://www.indiehackers.com/post/how-many-waiting-list-signups-should-we-have-before-building-mvp-05ea06e9ca
[32] https://blog.mean.ceo/?p=11219
[33] https://blog.getlaunchlist.com/blog/convert-waitlist-to-paying-customers
[34] https://echai.ventures/startingup/validate-idea/is-a-waitlist-with-a-lot-of-signups-actual-proof-of-demand
[35] https://mtlynch.io/book-reports/the-mom-test/ ; https://www.ybrikman.com/blog/2023/03/29/the-mom-test/ ; https://www.sachinrekhi.com/the-mom-test-rob-fitzpatrick
[36] https://www.launchrock.com/library/expert-advice/customer-discovery ; https://www.koji.so/docs/startup-idea-validation-guide ; https://blogs.oregonstate.edu/thestartupadvantage/?p=204
[37] https://www.indiehackers.com/post/deploy-empathy-how-to-talk-so-people-will-talk-2ea4e2a5c5 ; https://www.intercom.com/blog/podcasts/geocodios-michele-hansen-on-interviewing-customers
[38] https://yourstory.com/2026/02/dropbox-fake-demo-video-75k-signups-mvp ; https://abitgamey.substack.com/p/before-building-it-test-if-anyone
[39] https://ballparkhq.com/research-glossary/purchase-intent
[40] https://www.digitalapplied.com/blog/landing-page-statistics-2026-conversion-data-points
[41] https://instantly.ai/blog/ai-sales-agent-benchmarks-2026-the-complete-performance-report/ ; https://emailbison.com/blogs/cold-email-saas-startup
