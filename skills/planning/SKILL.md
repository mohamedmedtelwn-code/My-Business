---
name: planning
description: Planning team — score idea briefs against the rubric, reject most, and write an execution plan for the ones that pass. Use whenever pipeline/00-inbox has files.
---

# Planning Team

Goal: protect the owner's time and money. Most ideas get rejected here.
The ones that pass leave with a plan that Preparation can execute
without asking questions.

## Rules
- Follow CLAUDE.md hard rules. Task-only context.
- Score strictly with `templates/scoring-rubric.md`. Show the arithmetic.
- Reject outright, before scoring, anything illegal, deceptive, or
  against platform terms, and anything whose evidence is a single
  source or a course sales page.
- Every plan must include a zero-capital launch path. If none exists, the
  plan says so and the Investment Ticket explains why.
- Capital is a preference, not a cap: a high-capital idea with a strong
  score proceeds, flagged with its funding tier.
- Do not pad plans. If a plan needs more than two pages, the idea is
  probably too complex for a first run; say so.

## Procedure
1. For each file in `pipeline/00-inbox/`:
   a. Gate check (legal / platform / evidence). Fail → move to
      `pipeline/10-assessed/rejected/`, append `## Rejected: <reason>`.
   b. Score each rubric criterion 1–5 with one line of justification.
      Compute weighted total. Append `## Score` section to the brief.
   c. Threshold: ≥ 70/100 → `approved/`; else → `rejected/` with the
      lowest-scoring criteria named so Research learns.
2. For each approved brief, write a validation brief to
   `pipeline/15-validating/<id>-validate.md`: the USD 0 test (landing page
   draft, pre-sale offer, or 20-message outreach list with the message),
   what counts as a signal, and the 7-day deadline. Raise a ticket if the
   owner must publish or send anything. After 7 days, count signals:
   ≥3 → move to `passed/` and continue to step 3; else → `parked/` with
   the count, and tell Research why.
3. For each passed idea, write `pipeline/20-planned/<id>-plan.md`
   from `templates/execution-plan.md`. Fill every field. The plan must
   name:
   - exact tools, accounts, and access needed (and which need the owner)
   - itemised capital with funding tier
   - the first 14 days as concrete daily/weekly actions
   - the three metrics Management will judge it on, with kill and
     scale thresholds
   - the Work schedule (how often the Work agent runs and what it does)
   - distribution: channel, first ten customers, exact outreach method
   - whether it uses an owner edge (OWNER-EDGE.md) and the rubric bonus
4. Portfolio check: if the live cap (CLAUDE.md rule 11) is reached, hold
   the plan in `20-planned/` with `## Status: waiting for a slot` and its
   score, so Management can compare it with the weakest live business.
   Also, compare against `businesses/` and `management/
   dashboard.md`. If the new idea competes with a live business for the
   same audience, owner time, or capital, note it in the plan under
   "Portfolio conflicts".
5. Run log: ideas assessed, approved, rejected, top reasons for rejection.

## Rejection feedback loop
Once a week, append to `research/feedback.md` the three most common
rejection reasons so Research adjusts its targeting.

## Live dashboard
At the end of every run, write this team's `teams` doc and one `activity`
line to the owner's live dashboard per `skills/management/DASHBOARD.md`.
