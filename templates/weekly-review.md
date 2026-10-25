# Weekly Review — YYYY-WW

## Portfolio (from `python tools/ledger.py report` and `python tools/check.py`)
| | This week | 4-week trend |
|-|-----------|--------------|
| Revenue (USD) | | |
| Spend (USD) | | |
| Net | | |
| Ceiling released / unspent | | |
| Reinvestment pool | | |
| Businesses live / paused / stopped | | |
| Pipeline: inbox / approved / validating / planned / tickets open | | |
| Runs this week: ok / warn / bad / crashed (from `python tools/runlog.py status`) | | |

## Per business
### <slug> — RED / AMBER / GREEN
- What happened this week (3 lines max)
- Metrics vs thresholds: m1 __ (kill __ / scale __), m2, m3 (weeks below kill: __; weeks above scale: __)
- Cost per unit of result:
- **Recommendation:** stop / hold / scale — and why in one line
- If scale: Investment Ticket <id> attached (funded from the pool first)

(repeat)

## Monthly cull (Phase 1) and Phase 2 cutover (day 90)
Rank live businesses by revenue, then lead-metric growth. Plans waiting in
20-planned/ that outscore the bottom one:

## Decisions for the owner
| Business | Recommendation | Ticket | Status |
|----------|----------------|--------|--------|
| | | | pending-owner |

## Lessons for Research and Planning (append to research/feedback.md)
1.
2.
3.

## Issues
Ledger mismatches (`python tools/ledger.py reconcile`), crashed runs, open
circuit breakers, tickets older than 3 days, compliance notes, platform-rules age.
