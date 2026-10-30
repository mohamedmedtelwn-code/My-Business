# Validation Brief: Python data-extraction and automation service for small firms

- **Id:** 20261026-python-data-extraction-service
- **Started:** 2026-11-03  **Deadline:** 2026-11-10 (7 days; replies count to day 9)
- **Test:** outreach
- **Extended:** no
- **Cost:** USD 0

## The test
The agents email 20 owners or operations staff of small GCC firms that copy
web data by hand (e-commerce resellers, recruitment agencies, brokerages,
market-research firms), from the studio domain, offering a free 50-row sample
extraction from one public site they name and a first script at a fixed
USD 200 (QAR 730), delivered in 5 days. If the first 20 bring no signal, 30
more follow. Prospects come from public company websites and directories;
business addresses only, opt-out line in every email. The email is in
`output/20261026-python-data-extraction-service/message.md`; list-building
rules in `prospect-criteria.md`. The owner does nothing. Starts when the studio
email sender exists; Planning shifts the date if not.

## Denominator (update as the test runs)
- **Messages sent:** 0   (outreach: 20 first, then 30 more unless 0 signals; pass needs 50)
- **Visitors:** 0        (not used)
- **Asks:** 0            (not used)

## What counts (signal units, pass at 3)
payment / pre-order / deposit from a stranger 3 · booked call with a qualified
stranger 1 (void if not held within 14 days) · reply with explicit intent 1
(a site named and "yes, send the sample" counts) · likes, follows, friends and
family 0.

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
**Denominator:** 0 of 50 messages (not reached)  
**Reason:** Deadline 2026-11-10 not reached; 0 SU so far.  
**Counted on:** 2026-10-30 by tools/signals.py
