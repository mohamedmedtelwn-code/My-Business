# Validation Brief: Excel and Google Sheets automation for small businesses

- **Id:** 20261025-sme-excel-automation-service
- **Started:** 2026-10-25  **Deadline:** 2026-11-01 (7 days; replies count to day 9)
- **Test:** outreach
- **Extended:** no
- **Cost:** USD 0

## The test
The owner sends the message in `output/20261025-sme-excel-automation-service/message.md`
to 20 owners or operations and finance staff of small firms (trading, clinics,
agencies, e-commerce, services) in Qatar and the GCC who run part of the
business on spreadsheets, offering a free 15-minute look at one painful
spreadsheet and a first automation at a fixed USD 290 (QAR 1,050). If the
first 20 bring no signal, 30 more follow. The prospect criteria are in
`prospect-criteria.md`. Agents never send the messages.

## Denominator (update as the test runs)
- **Messages sent:** 0   (outreach: 20 first, then 30 more unless 0 signals; pass needs 50)
- **Visitors:** 0        (not used)
- **Asks:** 0            (not used)

## What counts (signal units, pass at 3)
payment / pre-order / deposit from a stranger 3 · booked call with a qualified
stranger 1 (void if not held within 14 days) · reply with explicit intent 1 ·
email sign-up 1/3 (landing test only) · likes, follows, friends and family 0.

## Owner steps (ticket raised if any)
1. Read prospect-criteria.md and list 20 people who match (business contacts, not family or close friends).
2. Send message.md to each, with the one personal line filled in. Update **Messages sent:** above.
3. Day 3: send the follow-up line from message.md to anyone who has not answered.
4. Record every reply: on the dashboard card (write what they said, press Send) or as a file in output/20261025-sme-excel-automation-service/replies/.
5. Nothing else. Planning counts the signals with tools/signals.py on 2026-11-01.

## Signals
| Date | Type | Who / what | Source |
|------|------|-----------|--------|

Type is one of: payment, call, intent, signup. Source is a file path under
output/ (screenshot, export) or a URL. Rows without a source do not count.

## Verdict

**Verdict:** RUNNING  
**Signal units:** 0 (payments 0 x3, calls 0, intent replies 0, sign-ups 0 -> 0 SU)  
**Denominator:** 0 of 50 messages (not reached)  
**Reason:** Deadline 2026-11-01 not reached; 0 SU so far.  
**Counted on:** 2026-10-26 by tools/signals.py
