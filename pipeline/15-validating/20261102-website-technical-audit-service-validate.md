# Validation Brief: Fixed-fee website technical audit and fix list for GCC SMEs

- **Id:** 20261102-website-technical-audit-service
- **Started:** 2026-12-05  **Deadline:** 2026-12-12 (7 days; replies count to day 9)
- **Test:** outreach
- **Extended:** no
- **Cost:** USD 0

## The test
The agents pre-crawl the public sites of GCC SMEs that earn leads online (clinics, law and accounting firms, trading companies, schools, hotels, stores), keep those with measurable faults, and email 20 marketing managers or owners from the studio domain. Each email names three faults found on their own site and offers the full audit with a prioritised fix list at USD 240 (QAR 875) up to 100 pages, USD 390 up to 500 pages, delivered in 3 days. A reply asking for the audit or the quote counts 1 (intent); a paid audit counts 3; a thank-you for the free findings alone counts 0. If the first 20 bring no signal, 30 more follow. The email is in output/20261102-website-technical-audit-service/message.md; list rules in prospect-criteria.md. One slot on 2026-12-05 beside the tender-digest test keeps the owner-load rule (fewer than two tests running).

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
1. Build the prospect list from public business sources per prospect-criteria.md; business addresses only; keep it in output/20261102-website-technical-audit-service/prospects.csv (company, role, address, source URL).
2. Send 20 personalised emails from the studio domain over the first 3 days (studio-wide cap 20 a day), each with the opt-out line.
3. Day 3: one follow-up to anyone silent; never after a "no" or an opt-out.
4. Save every reply as a file in output/20261102-website-technical-audit-service/replies/ (first name, company type, what they said, date) and add a Signals row citing it.
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
**Reason:** Deadline 2026-12-12 not reached; 0 SU so far.  
**Counted on:** 2026-11-04 by tools/signals.py
