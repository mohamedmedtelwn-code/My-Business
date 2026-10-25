# Scoring Rubric

Score each criterion 1-5. Multiply by the weight. Sum. Maximum 100.
Threshold to approve: 70. Run the arithmetic with
`python tools/rubric.py score --scores a,b,c,d,e,f,g,h [--edge]` and paste the
block it prints under `## Score`. The weights and threshold the tool uses live
in `management/config.json` (`rubric_weights`, `rubric_threshold`); change
them there and in this table together, and log the change at the bottom.

| # | Criterion | Weight | 1 | 3 | 5 |
|---|-----------|--------|---|---|---|
| 1 | Evidence strength | 4 | one source, or only vendor / course-seller / affiliate pages | two independent sources with numbers, at least one platform-level (filing, payout page, platform statistics) or first-person with screenshots | three or more primary sources with hard numbers, including a distribution (a median, not a top earner), none of them selling a course or tool |
| 2 | Capital to first dollar | 3 | over USD 500 | USD 50-200 | USD 0 (free tools only) |
| 3 | Time to first dollar | 4 | over 6 months (ad-revenue content, SEO sites, apps without an audience) | 1-3 months (digital product via a merchant of record with an outreach list; micro-SaaS with a validated waitlist) | under 2 weeks (a service or product sold directly to named buyers the owner can reach today) |
| 4 | Automatability | 3 | mostly owner work | half agent | agent runs it, owner presses buttons |
| 5 | Owner time per week | 2 | over 5 h | 2-5 h | under 1 h |
| 6 | Earnings ceiling at 6 months | 2 | under USD 100/mo (the evidence median for most categories) | USD 300-1,000/mo with a source showing small operators there | over USD 2,000/mo with a source showing small operators there |
| 7 | Durability | 1 | one platform, or Google organic search, is the only channel | two channels, one of them owned (email list, direct clients, repeat buyers) | diversified and defensible: owned audience, repeat buyers, no channel above 60% of leads |
| 8 | Legal / platform clarity | 1 | grey area, or disclosure duties unclear | mostly clear | clearly allowed, documented in `research/platform-rules.md`, volume plan under every published cap |

Weights sum to 20; max score 100. Evidence and time to first dollar carry the
largest weights on purpose: Phase 1 lasts 90 days, and the research pass found
that the typical small operator earns about USD 0 at month 6 on content
platforms and under USD 150 a month on apps and indie SaaS. Capital carries less
weight than before because every plan is USD 0 by rule 4, so it rarely
separates ideas.

## Bonuses
- +1 Durability and +1 Earnings ceiling (each capped at 5) when the idea uses an
  item in `OWNER-EDGE.md`. State which item. `rubric.py --edge` applies it.

## Gate checks (fail any -> reject before scoring, write `## Rejected: <gate>`)
1. Illegal in the operating jurisdiction or the target market.
2. Against platform terms, or relies on deception, spam, fake reviews, bought
   engagement or impersonation.
3. Evidence is a single source, or only course / guru / vendor sales pages.
4. **Platform or payout not available to a Qatar-resident seller** (see
   `research/platform-rules.md` and `management/payments.md`). Today that
   excludes Etsy shops, TikTok Creator Rewards, Amazon Associates paid to a
   Qatar bank, and Stripe accounts in the owner's name.
5. **Relies on mass-produced or templated content** on a platform that
   penalises it (YouTube inauthentic content, KDP title caps, Fiverr bulk AI
   delivery, Apple 4.3 spam), or plans volume above a published cap.
6. Requires a licence or physical presence the studio cannot provide (for
   example a Qatar commercial registration the owner does not hold).
7. No named channel and first-ten-customers path ("post and wait").
8. Google organic search is the only acquisition channel.
9. Relates to the owner's construction-planning profession while the owner
   hold in `management/config.json` (`edge_hold_until`) is in force.

## Worked example A (rejected)
Faceless YouTube Shorts channel, history facts niche. Gate 5 fails: templated
AI-narrated Shorts are the profile YouTube's inauthentic-content policy names
(15 Jul 2025). Scored anyway to show the arithmetic:
1 Evidence 2x4=8 (vendor RPM pages, no small-operator distribution) · 2 Capital 5x3=15
· 3 Time 1x4=4 (YPP needs 1,000 subs and 10M Shorts views; Shorts RPM USD 0.03-0.06)
· 4 Automatability 4x3=12 · 5 Owner time 4x2=8 · 6 Ceiling 2x2=4 · 7 Durability 1x1=1
· 8 Legal 2x1=2 -> **54, rejected** (and gated).

## Worked example B (approved, owner edge)
Bilingual Gulf FIDIC claim pack (notice letters, time-bar tracker, register,
worked example) sold on Gumroad to planners at small GCC contractors, reached by
50 personalised LinkedIn messages. Edge: EOT claim preparation.
1 Evidence 3x4=12 (price anchors: Etsy USD 6, ARMACO USD 11.99, Claims Class USD 645;
Upwork delay analysts USD 35-65/h; no sales distribution) · 2 Capital 5x3=15
· 3 Time 4x4=16 (direct outreach, Gumroad pays QAR) · 4 Automatability 4x3=12
· 5 Owner time 3x2=6 (legal review of drafts) · 6 Ceiling 3+1=4x2=8 · 7 Durability 2+1=3x1=3
· 8 Legal 4x1=4 -> **76, approve**, flagged "owner reviews every legal statement; not legal advice".

## Weight change log
| Date | Change | Reason and source |
|------|--------|-------------------|
| 2026-10-25 | Weights: Evidence 3 to 4, Capital 5 to 3, Time to first dollar 3 to 4 | Every plan is USD 0 by rule 4, so capital stopped discriminating; Phase 1 is 90 days, so time to first dollar binds; evidence quality had the widest spread in the research pass (course-seller content dominates categories 2, 6, 7, 8). `research/STUDIO-RESEARCH.md` section 1. |
| 2026-10-25 | New gate 4: platform and payout available to a Qatar seller | Etsy Payments country list excludes Qatar (help.etsy.com, fetched); TikTok Creator Rewards covers eight countries (Creator Academy, 10 Sep 2026); Amazon Associates bank transfer covers 52 US/UK/EUR countries only. Section 2. |
| 2026-10-25 | New gate 5: no mass-produced content, volume under caps | YouTube inauthentic-content policy (15 Jul 2025); KDP 2 titles per format per week; Fiverr bulk-AI ban; Apple 4.3. Sections 2 and 7. |
| 2026-10-25 | New gate 8 and Durability anchors rewritten around channel mix | Ahrefs: 58% lower position-1 CTR where AI Overviews appear; niche sites losing over 90% of traffic. Section 7, failure mode 6. |
| 2026-10-25 | Time and Ceiling anchors tied to the evidence medians | Month-6 medians: content ~USD 0, apps under USD 50, indie SaaS USD 145 MRR, KDP 44% at or under USD 100. Section 1. |
| 2026-10-25 | Worked example A now fails; example B added | Shorts RPM and policy evidence; owner-edge price anchors from section 5. |
