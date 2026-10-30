# Validation Brief: Automated weekly sales and stock reports for Salla and Zid merchants

- **Id:** 20261029-salla-zid-merchant-reporting
- **Started:** 2026-11-27  **Deadline:** 2026-12-04 (7 days; replies count to day 9)
- **Test:** outreach
- **Extended:** no
- **Cost:** USD 0

## The test
The agents email 20 owners of Salla and Zid stores whose store site publishes
a business address, in repeat-purchase categories (coffee, beauty, abayas,
perfume, supplements), from the studio domain, with a sample weekly report
attached and the offer of a free two-week pilot on their own store data,
then USD 49 (SAR 185) a month. A "yes, connect my store" with the store
URL counts as intent (1); a paid first month counts 3. The pilot app is
built only after three yeses, so no developer account is needed for the
test. If the first 20 bring no signal, 30 more follow. The email is in
`output/20261029-salla-zid-merchant-reporting/message.md`; list rules in
`prospect-criteria.md`. Starts when the two 2026-11-19 tests close.

## Denominator (update as the test runs)
- **Messages sent:** 0   (outreach: 20 first, then 30 more unless 0 signals; pass needs 50)
- **Visitors:** 0        (not used)
- **Asks:** 0            (presale: at least 20 direct asks)

## What counts (signal units, pass at 3)
payment / pre-order / deposit from a stranger 3 · booked call with a qualified
stranger 1 (void if not held within 14 days) · reply with explicit intent 1
(a "yes, start" with the details asked for counts) · likes, follows, friends
and family 0.

## Owner steps (ticket raised if any)
None for this test. The owner only completes the studio set-up tickets
(brand domain, email-sending account and API key, Gumroad, legal basis). Agent steps:
1. Build the prospect list from public business sources per prospect-criteria.md; business addresses only; keep it in output/20261029-salla-zid-merchant-reporting/prospects.csv (company, role, address, source URL).
2. Send 20 personalised emails from the studio domain over the first 3 days (studio-wide cap 20 a day), each with the opt-out line.
3. Day 3: one follow-up to anyone silent; never after a "no" or an opt-out.
4. Save every reply as a file in output/20261029-salla-zid-merchant-reporting/replies/ (first name, company type, what they said, date) and add a Signals row citing it.
5. Outreach tests: if the first 20 bring no signal by day 5, send 30 more. Presale tests: 20 asks.
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
**Reason:** Deadline 2026-12-04 not reached; 0 SU so far.  
**Counted on:** 2026-10-30 by tools/signals.py
