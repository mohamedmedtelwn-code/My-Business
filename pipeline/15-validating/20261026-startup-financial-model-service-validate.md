# Validation Brief: Fixed-fee financial models for GCC startups and SMEs

- **Id:** 20261026-startup-financial-model-service
- **Started:** 2026-11-11  **Deadline:** 2026-11-18 (7 days; replies count to day 9)
- **Test:** presale
- **Extended:** no
- **Cost:** USD 0

## The test
The agents email 20 founders of early-stage startups and SME owners in Qatar
and the GCC who are raising money or applying to QDB, QSTP or an incubator
(found on public cohort pages and funding announcements, company addresses
only), from the studio domain, asking them to buy an investor-ready
three-statement Excel model at the test price of USD 900 (QAR 3,280), with a
free written review of their current numbers first (they send a sheet, the
agents reply with the three things an investor will question). A deposit
counts 3; "yes, start" or a booked review call counts 1. The email is in
`output/20261026-startup-financial-model-service/message.md`; list rules in
`prospect-criteria.md`. The owner does nothing. Starts when the studio email
sender exists; Planning shifts the date if not.

## Denominator (update as the test runs)
- **Messages sent:** 0   (not used)
- **Visitors:** 0        (not used)
- **Asks:** 0            (presale: at least 20 direct asks)

## What counts (signal units, pass at 3)
payment / pre-order / deposit from a stranger 3 · booked call with a qualified
stranger 1 (void if not held within 14 days) · reply with explicit intent 1 ·
likes, follows, friends and family 0.

## Owner steps (ticket raised if any)
None for this test. The owner only completes the studio set-up tickets
(brand domain, email-sending account and API key, legal basis). Agent steps:
1. Build the prospect list from public business sources per prospect-criteria.md; business addresses only; keep the list in output/<id>/prospects.csv (company, role, address, source URL).
2. Send 20 personalised emails from the studio domain over the first 3 days (studio-wide cap 20 a day), each with the opt-out line.
3. Day 3: one follow-up to anyone silent; never after a "no" or an opt-out.
4. Save every reply as a file in output/<id>/replies/ (first name, company type, what they said, date) and add a Signals row citing it.
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
**Denominator:** 0 of 20 asks (not reached)  
**Reason:** Deadline 2026-11-18 not reached; 0 SU so far.  
**Counted on:** 2026-10-31 by tools/signals.py
