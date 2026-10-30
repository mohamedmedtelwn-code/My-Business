# Validation Brief: Fixed-fee CRM and mailing-list cleaning for GCC SMEs

- **Id:** 20261029-crm-list-cleaning-service
- **Started:** 2026-11-19  **Deadline:** 2026-11-26 (7 days; replies count to day 9)
- **Test:** outreach
- **Extended:** no
- **Cost:** USD 0

## The test
The agents email 20 marketing or sales leads at GCC SMEs that visibly email
customers (newsletter form, Mailchimp or HubSpot footer, CRM-driven
campaigns), from the studio domain, offering a free 48-hour quality report on
a 500-row sample of their list (duplicate rate, bad formats, bilingual name
clashes) and a fixed clean-up at USD 290 (QAR 1,050) for up to 5,000 records.
If the first 20 bring no signal, 30 more follow. A sample sent for the free
report counts as intent (1); a paid clean-up counts 3. Data-processing terms
go with every reply. The email is in `output/20261029-crm-list-cleaning-service/message.md`;
list rules in `prospect-criteria.md`. Runs alongside the translation test.
Starts when the studio email sender exists; Planning shifts the date if not.

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
1. Build the prospect list from public business sources per prospect-criteria.md; business addresses only; keep it in output/20261029-crm-list-cleaning-service/prospects.csv (company, role, address, source URL).
2. Send 20 personalised emails from the studio domain over the first 3 days (studio-wide cap 20 a day), each with the opt-out line.
3. Day 3: one follow-up to anyone silent; never after a "no" or an opt-out.
4. Save every reply as a file in output/20261029-crm-list-cleaning-service/replies/ (first name, company type, what they said, date) and add a Signals row citing it.
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
**Reason:** Deadline 2026-11-26 not reached; 0 SU so far.  
**Counted on:** 2026-10-30 by tools/signals.py
