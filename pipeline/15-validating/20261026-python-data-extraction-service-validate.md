# Validation Brief: Python data-extraction and automation service for small firms

- **Id:** 20261026-python-data-extraction-service
- **Started:** 2026-11-02  **Deadline:** 2026-11-09 (7 days; replies count to day 9)
- **Test:** outreach
- **Extended:** no
- **Cost:** USD 0

## The test
The owner sends the message in
`output/20261026-python-data-extraction-service/message.md` to 20 owners or
operations staff of small GCC firms that copy web data by hand (resellers
tracking competitor prices, recruiters building lists from public
directories, brokers tracking listings, researchers), offering a free 50-row
sample extraction from one public site they name and a fixed first script at
QAR 730 (USD 200), delivered in 5 days. If the first 20 bring no signal, 30
more follow. The prospect criteria are in `prospect-criteria.md`. Agents never
send the messages and never collect personal data. Starts 2026-11-02, the day
the owner's two cycle-2 tests have closed.

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
1. On 2026-11-02 read prospect-criteria.md and list 20 people who match (business contacts, not family or close friends).
2. Send message.md to each with the one personal line filled in. Update **Messages sent:** above.
3. When someone names a site: tell the agents on the dashboard card; they build the 50-row sample within 24 hours for you to forward.
4. Day 3: send the follow-up line from message.md to anyone silent.
5. Record every reply on the dashboard card (write what they said, press Send) or as a file in output/20261026-python-data-extraction-service/replies/.
6. Nothing else. Planning counts the signals with tools/signals.py on 2026-11-09.

## Signals
| Date | Type | Who / what | Source |
|------|------|-----------|--------|

Type is one of: payment, call, intent, signup. Source is a file path under
output/ (screenshot, export) or a URL. Rows without a source do not count.

## Verdict

**Verdict:** RUNNING  
**Signal units:** 0 (payments 0 x3, calls 0, intent replies 0, sign-ups 0 -> 0 SU)  
**Denominator:** 0 of 50 messages (not reached)  
**Reason:** Deadline 2026-11-09 not reached; 0 SU so far.  
**Counted on:** 2026-10-26 by tools/signals.py
