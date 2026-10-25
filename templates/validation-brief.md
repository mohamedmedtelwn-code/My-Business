# Validation Brief: <title>

- **Id:** YYYYMMDD-<slug>
- **Started:** YYYY-MM-DD  **Deadline:** YYYY-MM-DD (7 days; replies count to day 9)
- **Test:** outreach | landing | presale
- **Extended:** no
- **Cost:** USD 0

## The test
One paragraph: who is contacted or who sees the page, with what offer, at what
price. The first-ten-customers list and the exact message or page draft live in
`pipeline/15-validating/output/<id>/` (owner publishes or sends via a ticket if
the agent cannot).

## Denominator (update as the test runs)
- **Messages sent:** 0   (outreach: 20 first, then 30 more unless 0 signals; pass needs 50)
- **Visitors:** 0        (landing: at least 100 qualified visitors; sign-ups count only above 8%)
- **Asks:** 0            (presale: at least 20 direct asks)

## What counts (signal units, pass at 3)
payment / pre-order / deposit from a stranger 3 · booked call with a qualified
stranger 1 (void if not held within 14 days) · reply with explicit intent 1 ·
email sign-up 1/3 (landing test only, above the rate and visitor minimums; at most
2 SU in total, so a second step is always needed) · likes, follows, upvotes,
views, friends and family 0.

## Owner steps (ticket raised if any)
1.

## Signals
| Date | Type | Who / what | Source |
|------|------|-----------|--------|

Type is one of: payment, call, intent, signup. Source is a file path under
output/ (screenshot, export) or a URL. Rows without a source do not count.

## Verdict
Written by `python tools/signals.py <this file> --write` at the deadline:
PASSED (move to passed/, write the plan), PARKED (move to parked/, one line in
research/feedback.md), INCONCLUSIVE (deadline extended once, keep going) or
RUNNING.
