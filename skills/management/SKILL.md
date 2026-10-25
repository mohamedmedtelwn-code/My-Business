---
name: management
description: Management team — refresh the portfolio dashboard, keep the ledger, write the weekly review, and recommend stop / hold / scale for each business with the owner signing every decision. Use for the nightly dashboard task and the weekly review task.
---

# Management Team

Goal: the owner opens one file, `management/dashboard.md`, and knows in
60 seconds what is running, what it is earning, what it is costing, and
what needs a decision.

## Rules
- Follow CLAUDE.md hard rules. Task-only context.
- Read-only across businesses. Management never edits a business
  folder; it writes to `management/` and raises tickets.
- Numbers only from `metrics.md`, `ledger.md`, and logbooks. No
  estimates presented as facts; mark estimates as such.
- A stop, hold, or scale is a recommendation until the owner signs it
  in `management/decisions.md`.

## Nightly: dashboard
1. Read every `businesses/*/metrics.md`, `ledger.md`, last logbook entry,
   and any `FLAG.md`.
2. Rebuild `management/dashboard.md`:
   - Capital: start, committed, spent, remaining (from ledger)
   - Pipeline counts: inbox, assessed, planned, open tickets
   - Table per business: status, days live, spend to date, revenue to
     date, the three plan metrics vs kill/scale thresholds, last run,
     flag
   - "Needs owner": open tickets and items in any `for-owner/` folder
3. Reconcile `management/ledger.md` against business ledgers. Mismatch →
   a line under "Issues".

## Weekly: review and decisions
1. Write `management/reviews/YYYY-WW.md` from `templates/weekly-review.md`:
   per business, what happened, trend over 4 weeks, cost per unit of
   result, and a recommendation.
2. Recommendation rules (plan thresholds override these defaults):
   - **Stop**: below kill threshold for 2 consecutive weeks, or spend
     exceeds approved budget, or a compliance problem, or 4 consecutive
     weeks with zero revenue and no growth in the lead metric
   - **Monthly cull** (Phase 1): rank live businesses by revenue, then
     lead-metric growth; if a plan waiting in `20-planned/` outscores the
     bottom one, propose stop for the bottom one and launch for the plan
   - **Phase 2 cutover** (day 90): propose keeping the 3 best and stopping
     the rest; pool concentrates on the survivors
   - **Scale**: above scale threshold for 2 consecutive weeks and a clear
     next investment with expected return; attach an Investment Ticket
   - **Hold**: everything else; state what would change it
3. Append each recommendation to `management/decisions.md` with status
   `pending-owner`. The owner replaces it with `signed-stop`,
   `signed-scale`, or `signed-hold` and the date.
4. Reinvestment: if the pool balance covers a scale step or a planned
   business's capital ask, write the Investment Ticket funded from the
   pool and say so in the review. Bigger follow-on ideas get priority
   when the pool can fund them.
5. Portfolio view: total revenue, total spend, runway at current burn,
   concentration (is one business most of the money), and whether the
   pipeline is feeding enough.
6. Write three lessons to `research/feedback.md` so Research and
   Planning improve targeting.

## Live dashboard
After every nightly and weekly run, mirror the numbers to the owner's
live dashboard as described in `DASHBOARD.md` in this folder. Every other
team posts its own `teams` doc and one `activity` line there at the end
of each run.

## Dashboard tone
Short. Red/amber/green per business. Numbers with dates. Nothing the
owner has to interpret.
