# Validation Brief: GCC startup financial-model Excel templates sold on Gumroad

- **Id:** 20261029-gcc-financial-model-templates
- **Started:** 2026-11-27  **Deadline:** 2026-12-04 (7 days; replies count to day 9)
- **Test:** presale
- **Extended:** no
- **Cost:** USD 0

## The test
The agents email 20 founders of early-stage GCC startups found on public
incubator cohort pages and funding announcements (company addresses only),
from the studio domain, with the free one-page runway calculator attached and
a pre-launch offer: the GCC three-statement model template (QAR, SAR, AED,
VAT, gratuity, incubator outputs) at USD 29 (QAR 105) instead of USD 49,
delivered the day Gumroad goes live. A payment through Gumroad counts 3; a
"yes, send me the link when it is live" counts 1 (intent); a calculator
download alone counts 0. Prospects already emailed for the model service are
excluded unless they declined it. The email is in
`output/20261029-gcc-financial-model-templates/message.md`; list rules in
`prospect-criteria.md`. Needs ticket 20261025-studio-2 (Gumroad) for payments;
intent counts without it.

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
1. Build the prospect list from public business sources per prospect-criteria.md; business addresses only; keep it in output/20261029-gcc-financial-model-templates/prospects.csv (company, role, address, source URL).
2. Send 20 personalised emails from the studio domain over the first 3 days (studio-wide cap 20 a day), each with the opt-out line.
3. Day 3: one follow-up to anyone silent; never after a "no" or an opt-out.
4. Save every reply as a file in output/20261029-gcc-financial-model-templates/replies/ (first name, company type, what they said, date) and add a Signals row citing it.
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
**Reason:** Deadline 2026-12-04 not reached; 0 SU so far.  
**Counted on:** 2026-10-30 by tools/signals.py
