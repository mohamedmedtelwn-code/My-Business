# Validation Brief: Fixed-fee workflow automation builds (Make, Zapier, Python) for GCC SMEs

- **Id:** 20261102-gcc-automation-setup-service
- **Started:** 2026-12-21  **Deadline:** 2026-12-28 (7 days; replies count to day 9)
- **Test:** outreach
- **Extended:** no
- **Cost:** USD 0

## The test
The agents email 20 operations, admin or sales managers at GCC SMEs whose public stack shows a manual gap (a contact form with no auto-reply, a Salla or Zid store with manual invoicing, a careers page that takes applications by email) from the studio domain, proposing one named automation at a fixed USD 390 (QAR 1,420) for a single workflow or USD 990 for a multi-step one, built in the client's own Make or Zapier account or as a scheduled job, runbook included, plus a USD 150 monthly keep-it-running option. A reply asking for the scope questions or the quote counts 1 (intent); a paid build counts 3. If the first 20 bring no signal, 30 more follow. The email is in output/20261102-gcc-automation-setup-service/message.md; list rules in prospect-criteria.md. Runs with the directory test from 2026-12-21.

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
1. Build the prospect list from public business sources per prospect-criteria.md; business addresses only; keep it in output/20261102-gcc-automation-setup-service/prospects.csv (company, role, address, source URL).
2. Send 20 personalised emails from the studio domain over the first 3 days (studio-wide cap 20 a day), each with the opt-out line.
3. Day 3: one follow-up to anyone silent; never after a "no" or an opt-out.
4. Save every reply as a file in output/20261102-gcc-automation-setup-service/replies/ (first name, company type, what they said, date) and add a Signals row citing it.
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
**Counted on:** 2026-11-13 by tools/signals.py
