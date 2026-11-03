# Validation Brief: Arabic-ready software directory with paid featured listings

- **Id:** 20261102-arabic-saas-directory
- **Started:** 2026-12-21  **Deadline:** 2026-12-28 (7 days; replies count to day 9)
- **Test:** outreach
- **Extended:** no
- **Cost:** USD 0

## The test
Before the test the agents publish the directory on a studio sub-domain with at least 50 tools verified against the Arabic-ready checklist on vendor free trials. Then they email 20 marketing managers at SaaS vendors selling into the GCC (company addresses only) from the studio domain: their free verified listing is live, here is the link and the badge; a featured placement in their category costs USD 79 a month or USD 790 a year on Gumroad. A reply claiming the listing with corrections or asking for the featured terms counts 1 (intent); a paid featured listing counts 3; a bare thank-you counts 0. If the first 20 bring no signal, 30 more follow. The email is in output/20261102-arabic-saas-directory/message.md; list rules in prospect-criteria.md. Runs with the automation test from 2026-12-21; the sub-domain DNS record needs one owner ticket before 2026-12-14.

## Denominator (update as the test runs)
- **Messages sent:** 0   (outreach: 20 first, then 30 more unless 0 signals; pass needs 50)
- **Visitors:** 0        (not used)
- **Asks:** 0            (presale: at least 20 direct asks)

## What counts (signal units, pass at 3)
payment / pre-order / deposit from a stranger 3 · booked call with a qualified
stranger 1 (void if not held within 14 days) · reply with explicit intent 1
(a "yes, send the quote" or a sample file sent for the free step counts) ·
likes, follows, friends and family 0.

## Owner steps (ticket raised if any)
None for this test. The owner only completes the studio set-up tickets
(brand domain, email-sending account and API key, Gumroad, legal basis). Agent steps:
1. Build the prospect list from public business sources per prospect-criteria.md; business addresses only; keep it in output/20261102-arabic-saas-directory/prospects.csv (company, role, address, source URL).
2. Send 20 personalised emails from the studio domain over the first 3 days (studio-wide cap 20 a day), each with the opt-out line.
3. Day 3: one follow-up to anyone silent; never after a "no" or an opt-out.
4. Save every reply as a file in output/20261102-arabic-saas-directory/replies/ (first name, company type, what they said, date) and add a Signals row citing it.
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
**Reason:** Deadline 2026-12-28 not reached; 0 SU so far.  
**Counted on:** 2026-11-03 by tools/signals.py
