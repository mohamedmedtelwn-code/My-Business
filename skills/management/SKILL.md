---
name: management
description: Management team — refresh the portfolio dashboard, keep the ledger reconciled, read the run log, write the weekly review, and recommend stop / hold / scale for each business with the owner signing every decision. Use for the nightly dashboard task and the weekly review task.
---

# Management Team

Goal: the owner opens one file, `management/dashboard.md` (or the live
dashboard), and knows in 60 seconds what is running, what it is earning, what
it is costing, which runs failed, and what needs a decision.

## Start and end of every run
- Start: `python tools/check.py` (Management records ERRORs under "Issues"
  rather than fixing other teams' files), then
  `python tools/runlog.py start --team management`; keep the RUN_ID.
- End: `python tools/check.py`, then
  `python tools/runlog.py end --id <RUN_ID> --outcome ok|warn|bad --summary "<dashboard refreshed; n issues; n decisions pending>" --commit`.

## Rules
- Follow CLAUDE.md hard rules. Task-only context.
- Read-only across businesses. Management never edits a business folder; it
  writes to `management/` and raises tickets.
- Numbers only from `python tools/ledger.py report`, `metrics.md` rows with a
  Source, logbooks and `python tools/runlog.py status`. No estimates presented
  as facts; mark estimates as such.
- A stop, hold, scale or pause is a recommendation until the owner signs it in
  `management/decisions.md`.
- Management may reset a team's circuit breaker (`python tools/runlog.py reset
  --team <team>`) once a week after writing the cause in the review; a second
  trip in the same week is an owner decision.

## Nightly: dashboard
1. Run `python tools/check.py --json`, `python tools/ledger.py reconcile`,
   `python tools/ledger.py report`, `python tools/runlog.py status`. Read every
   `businesses/*/metrics.md` last row, the last logbook entry and any `FLAG.md`.
2. Rebuild `management/dashboard.md`:
   - Capital: ceiling, released, released unspent, spent, revenue, pool (from the report)
   - Pipeline counts: inbox, assessed, validating (passed / parked), planned, open tickets
   - Runs: per team, last run, outcome, consecutive failures, breaker state; crashed runs
   - Table per business: status, days live, spend to date, revenue to date,
     the three plan metrics vs kill / scale thresholds, last run, flag, RAG
   - "Needs owner": open tickets with age (older than 3 days first), items in
     any `for-owner/` folder, pending decisions
   - "Issues": check.py ERRORs and WARNs, ledger mismatches
3. Push the live dashboard with the procedure in `DASHBOARD.md` (list with
   out_dir, `python tools/dashboard_push.py --versions-dir ...`, send batches).

## Weekly: review and decisions
1. Write `management/reviews/YYYY-WW.md` from `templates/weekly-review.md`:
   per business, what happened, trend over 4 weeks, cost per unit of result,
   weeks below kill or above scale, and a recommendation.
2. Recommendation rules (plan thresholds override these defaults; the numbers
   live in `management/config.json`):
   - **Stop**: below the kill threshold for `kill_weeks` (2) consecutive weeks,
     or spend exceeds the approved budget, or a compliance problem, or
     `zero_revenue_weeks_to_stop` (4) consecutive weeks with zero revenue and
     no growth in the lead metric.
   - **Pause**: a ticket for the business older than `ticket_pause_days` (7),
     or the team's circuit breaker tripped twice in a month. Pause is logged as
     a decision; the Work agent skips runs while the pause warning stands.
   - **Monthly cull** (Phase 1): rank live businesses by revenue, then
     lead-metric growth; if a plan waiting in `20-planned/` outscores the bottom
     one, propose stop for the bottom one and launch for the plan.
   - **Phase 2 cutover** (day 90 from `studio_start`): propose keeping the 3
     best and stopping the rest; the pool concentrates on the survivors.
   - **Scale**: above the scale threshold for `scale_weeks` (2) consecutive
     weeks and a clear next investment with expected return; attach an
     Investment Ticket funded from the pool first.
   - **Hold**: everything else; state what would change it.
3. Append each recommendation to `management/decisions.md` with status
   `pending-owner`. The owner replaces it with `signed-stop`, `signed-scale`,
   `signed-hold` or `signed-pause` and the date.
4. Reinvestment: if the pool balance (`ledger.py report`) covers a scale step
   or a planned business's capital ask, write the Investment Ticket funded from
   the pool and say so in the review. Bigger follow-on ideas get priority when
   the pool can fund them.
5. Portfolio view: total revenue, total spend, runway at current burn,
   concentration (is one business most of the money), whether the pipeline is
   feeding enough, and run health (ok / warn / bad / crashed counts).
6. Write three lessons to `research/feedback.md` so Research and Planning
   improve targeting; include validation outcomes by test type.

## Dashboard tone
Short. Red/amber/green per business. Numbers with dates. Nothing the owner has
to interpret.
