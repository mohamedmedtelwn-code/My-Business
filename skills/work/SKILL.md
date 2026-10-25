---
name: work
description: Work team — operate a single launched business from businesses/<slug>/ according to its plan.md and WORK.md; produce output, log results, raise tickets when blocked. Use when running the scheduled Work task for a business.
---

# Work Team

Goal: execute the plan for one business, every run, and leave a clean
record. The Work agent is the business's operator.

## Rules
- Follow CLAUDE.md hard rules. Task-only context.
- Read only this business's folder plus `research/playbooks/<method>.md`.
  Do not read other businesses' folders.
- Do what `WORK.md` says for this run. If the plan and WORK.md disagree,
  WORK.md wins; note the conflict in the logbook.
- Spend nothing outside the business's approved ledger lines.
- When blocked by something only the owner can do, write a ticket to
  `pipeline/30-tickets/open/` and stop this run. Never work around a
  block with a guess.
- Platform rules are read fresh each month and followed. Where AI
  content disclosure is required, disclose.

## Each run
1. Read `WORK.md`, `plan.md`, the last 5 logbook entries, `metrics.md`.
2. Pick the actions due this run from the plan's calendar.
3. Do them: write, build, publish-ready drafts, list, respond, deliver,
   analyse — whatever the method needs. Save all outputs in
   `businesses/<slug>/output/YYYYMMDD/`.
4. Anything that needs the owner to press the final button (publish on
   an account the agent cannot access, send an invoice, ship) goes in
   `businesses/<slug>/for-owner/` with a one-line instruction, and a
   ticket if it is time-sensitive.
5. Update `metrics.md`: the three plan metrics, with date and source.
6. Append a logbook entry: date, actions done, outputs, metric deltas,
   problems, next run's intent. Five to ten lines.
7. If a metric crosses the plan's kill or scale threshold, add a line
   to `businesses/<slug>/FLAG.md` so Management picks it up.

## What good looks like
- Every run produces something a customer or platform can receive.
- Logbook is honest: zero progress is logged as zero progress.
- No run is longer than the time budget in WORK.md.

## Live dashboard
At the end of every run, write this team's `teams` doc and one `activity`
line to the owner's live dashboard per `skills/management/DASHBOARD.md`.
