# Approval Ticket

- **Ticket:** <plan-id>-<n>
- **Business:** <slug>
- **Type:** account / access / terms / publish / legal / other
- **Raised:** YYYY-MM-DD by <team>
- **Blocks:** <what cannot proceed until this is done; "nothing" if the business can run without it>

## What we need you to do
Numbered steps, exact, under five minutes total. Every link included.
1.
2.
3.

## Why
One paragraph.

## After you're done
What the agent will do next, automatically. If this ticket releases money
(Tier 0), the agent records it with
`python tools/ledger.py release --ticket <id> --business <slug> --amount <USD>`.

---
**Owner decision:** APPROVED / REJECTED / DONE — date — note
