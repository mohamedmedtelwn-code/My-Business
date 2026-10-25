---
name: planning
description: Planning team — score idea briefs against the rubric, reject most, run the USD 0 validation, and write an execution plan for the ones that pass. Use whenever pipeline/00-inbox has files or a validation is due.
---

# Planning Team

Goal: protect the owner's time and money. Most ideas get rejected here. The
ones that pass leave with a validated demand signal and a plan that
Preparation can execute without asking questions.

## Start and end of every run
- Start: `python tools/check.py` (fix every ERROR first), then
  `python tools/runlog.py start --team planning`; keep the RUN_ID.
- End: `python tools/check.py`, then
  `python tools/runlog.py end --id <RUN_ID> --outcome ok|warn|bad --summary "<ideas assessed, approved, rejected, validations closed>" --commit`.
- Process at most 10 inbox files per run; leave the rest for the next run.

## Rules
- Follow CLAUDE.md hard rules. Task-only context.
- Gate first, score second. The gates and anchors are in
  `templates/scoring-rubric.md`; the arithmetic is done by
  `python tools/rubric.py score --scores a,b,c,d,e,f,g,h [--edge] --notes "..."`
  and its output is pasted as the `## Score` section. Never total by hand.
- Every plan must include a zero-capital launch path. If none exists, the
  plan says so and the Investment Ticket explains why.
- Capital is a preference, not a cap: a high-capital idea with a strong score
  proceeds, flagged with its funding tier.
- Do not pad plans. If a plan needs more than two pages, the idea is probably
  too complex for a first run; say so.
- Validation verdicts come from `python tools/signals.py <file> --write`, not
  from judgement. A signal without a Source cell does not exist.

## Procedure
1. For each file in `pipeline/00-inbox/`:
   a. Gate check (the eight gates in the rubric). Fail -> move to
      `pipeline/10-assessed/rejected/`, append `## Rejected: <gate and reason>`.
   b. Score each criterion 1-5 with one line of justification; run
      `tools/rubric.py`; append its `## Score` block to the brief.
   c. Approved (total at or above the threshold in `management/config.json`)
      -> move to `approved/`; else -> `rejected/` with the lowest-scoring
      criteria named so Research learns.
2. For each approved brief, write `pipeline/15-validating/<id>-validate.md`
   from `templates/validation-brief.md`: the USD 0 test (outreach, landing or
   presale), the first-ten-customers list and the exact message or page draft
   under `pipeline/15-validating/output/<id>/`, the denominator plan (20 then
   30 messages; 100 visitors; 20 asks), and the 7-day deadline. Raise a ticket
   if the owner must publish or send anything.
3. On every run, for each file in `pipeline/15-validating/`: update the
   denominator lines and the Signals table from the evidence files, then run
   `python tools/signals.py <file> --write`.
   - PASSED -> move to `passed/` and continue to step 4.
   - PARKED -> move to `parked/`; one line in `research/feedback.md`.
   - INCONCLUSIVE -> the tool extended the deadline once; keep working the
     denominator. A second inconclusive result parks.
   - RUNNING -> nothing to do yet. If the brief's **Started** date has arrived
     and its owner ticket (`<id>-v1`) has not been raised, raise it now.
4. For each passed idea, write `pipeline/20-planned/<id>-plan.md` from
   `templates/execution-plan.md`. Fill every field. The plan must name:
   - exact tools, accounts and access needed (and which need the owner)
   - itemised capital with funding tier, and the zero-capital path
   - the first 14 days as concrete daily or weekly actions
   - the three metrics Management will judge it on, each with a Source the
     Work agent can read, and kill and scale thresholds
   - the Work schedule (cadence, time budget, outbound cap under 20 cold
     messages a day)
   - distribution: two channels, first ten customers, exact outreach method,
     neither channel above 60%
   - the price guard (minimum price, maximum discount, maximum refund)
   - the platform rules that apply and the plan's own volume cap
   - whether it uses an owner edge (OWNER-EDGE.md) and the rubric bonus
5. Portfolio check: if `tools/check.py` reports the live cap reached, hold the
   plan in `20-planned/` with `**Status:** waiting for a slot`, so Management
   can compare it with the weakest live business. If the new idea competes
   with a live business for the same audience, owner time or capital, note it
   under "Portfolio conflicts".
6. Summary line for the run log: ideas assessed, approved, rejected, top
   reasons for rejection, validations passed, parked, extended.

## Rejection feedback loop
Once a week, append to `research/feedback.md` the three most common rejection
reasons and the validation outcomes (passed, parked, inconclusive) so Research
adjusts its targeting.
