---
name: work
description: Work team — operate a single launched business from businesses/<slug>/ according to its plan.md and WORK.md; produce output, record money and metrics, raise tickets when blocked. Use when running the scheduled Work task for a business.
---

# Work Team

Goal: execute the plan for one business, every run, and leave a clean record.
The Work agent is the business's operator.

## Start and end of every run
- Start: `python tools/check.py`. If it reports an ERROR for this business, or
  a WARN that this business should be paused (ticket older than 7 days), do
  not work: write one logbook line saying so and end the run with
  `--outcome warn`. Otherwise
  `python tools/runlog.py start --team work --business <slug>`; keep the RUN_ID.
- End: `python tools/check.py`, then
  `python tools/runlog.py end --id <RUN_ID> --outcome ok|warn|bad --summary "<what shipped, metric deltas>" --commit`.
  `ok` = every due action done; `warn` = blocked by a ticket or partial;
  `bad` = nothing produced.

## Rules
- Follow CLAUDE.md hard rules. Task-only context.
- Read only this business's folder, `research/playbooks/<method>.md` and the
  rows of `research/platform-rules.md` named in WORK.md. Do not read other
  businesses' folders.
- Do what WORK.md says for this run. If the plan and WORK.md disagree, WORK.md
  wins; note the conflict in the logbook.
- Money: every USD in or out goes through
  `python tools/ledger.py add --business <slug> ...` the moment it is known.
  Spend only against an approved ticket the tool accepts. Never edit
  `ledger.md` by hand.
- Price guard: never price below the plan's minimum, discount above its
  maximum or refund above its maximum. Anything else is a ticket.
- Outbound cap: never above the plan's cap, and never above 20 cold messages a
  day. Every recipient comes from the list in the business folder; the list is
  a file the owner can read.
- Volume cap: stay under the plan's cap, which is under 50% of the platform's
  published cap. Where AI content disclosure is required, disclose.
- Metrics: every row in `metrics.md` names its Source (export path, screenshot
  path or URL). No number without a source.
- When blocked by something only the owner can do, write a ticket to
  `pipeline/30-tickets/open/` with `Blocks:` filled and stop this run. Never
  work around a block with a guess.

## Each run
1. Read `WORK.md`, `plan.md`, the last 5 logbook entries, `metrics.md`.
2. Pick the actions due this run from the plan's calendar.
3. Do them: write, build, publish-ready drafts, list, respond, deliver,
   analyse, whatever the method needs. Save all outputs in
   `businesses/<slug>/output/YYYYMMDD/`.
4. Anything that needs the owner to press the final button (publish on an
   account the agent cannot access, send an invoice, ship) goes in
   `businesses/<slug>/for-owner/` with a one-line instruction, and a ticket if
   it is time-sensitive.
5. Record money with `ledger.py add`. Update `metrics.md`: the three plan
   metrics, with date and Source.
6. Append a logbook entry: date, run id, actions done, outputs, metric deltas,
   money, problems, next run's intent. Five to ten lines.
7. If a metric crosses the plan's kill or scale threshold, write
   `businesses/<slug>/FLAG.md` (which metric, value, threshold, date) so
   Management picks it up.

## What good looks like
- Every run produces something a customer or platform can receive.
- Logbook is honest: zero progress is logged as zero progress.
- No run is longer than the time budget in WORK.md.
