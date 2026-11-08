# Validation Brief: Google Business Profile set-up and review-reply retainer for GCC clinics, restaurants and salons

- **Id:** 20261105-gbp-review-management-service
- **Started:** 2026-12-29  **Deadline:** 2027-01-05 (7 days; replies count to day 9)
- **Test:** outreach
- **Extended:** no
- **Cost:** USD 0

## The test
The agents audit the public Google Business Profiles of clinics, restaurants, salons, gyms and car services in Qatar and the GCC, keep those with unanswered reviews or missing fields, and email 20 owners or managers from the studio domain with the 10-point audit of their own listing and the offer of a bilingual set-up at USD 190 (QAR 690) per location plus an optional USD 120 monthly retainer (every review answered within 24 hours, four posts, edit monitoring, a monthly report). A reply asking for the set-up or granting Manager access counts 1 (intent); a paid set-up or first retainer month counts 3; a thank-you for the audit alone counts 0. If the first 20 bring no signal, 30 more follow. The email is in output/20261105-gbp-review-management-service/message.md; list rules in prospect-criteria.md. Runs with the bid-writing test from 2026-12-29, the first free slot after the cycle-5 tests.

## Denominator (update as the test runs)
- **Messages sent:** 0   (outreach: 20 first, then 30 more unless 0 signals; pass needs 50)
- **Visitors:** 0        (not used)
- **Asks:** 0            (presale: at least 20 direct asks)

## What counts (signal units, pass at 3)
payment / pre-order / deposit from a stranger 3 · booked call with a qualified
stranger 1 (void if not held within 14 days) · reply with explicit intent 1
(a "yes, send the quote" or access granted for the free step counts) ·
likes, follows, friends and family 0.

## Owner steps (ticket raised if any)
None for this test. The owner only completes the studio set-up tickets
(brand domain, email-sending account and API key, Gumroad, legal basis). Agent steps:
1. Build the prospect list from public business sources per prospect-criteria.md; business addresses only; keep it in output/20261105-gbp-review-management-service/prospects.csv (company, role, address, source URL).
2. Send 20 personalised emails from the studio domain over the first 3 days (studio-wide cap 20 a day), each with the opt-out line.
3. Day 3: one follow-up to anyone silent; never after a "no" or an opt-out.
4. Save every reply as a file in output/20261105-gbp-review-management-service/replies/ (first name, company type, what they said, date) and add a Signals row citing it.
5. If the first 20 bring no signal by day 5, send 30 more.
6. Planning counts the signals with tools/signals.py at the deadline.

## Signals
| Date | Type | Who / what | Source |
|------|------|-----------|--------|

Type is one of: payment, call, intent, signup. Source is a file path under
output/ (screenshot, export) or a URL. Rows without a source do not count.

## Verdict

**Verdict:** RUNNING  
**Signal units:** 0 (payments 0 x3, calls 0, intent replies 0, sign-ups 0 -> 0 SU)  
**Denominator:** 0 of 50 messages (not reached)  
**Reason:** Deadline 2027-01-05 not reached; 0 SU so far.  
**Counted on:** 2026-11-08 by tools/signals.py
