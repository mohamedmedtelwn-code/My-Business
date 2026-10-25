# Venture Studio — Owner Guide

An always-on Claude agent on a dedicated laptop that researches, plans,
prepares, executes, and reports on small businesses. You approve
funding and account creation; the teams do the rest.

## 1. Laptop setup (one-time)

1. Fresh Windows user account dedicated to the studio. Auto-login, never
   lock, never sleep on AC power.
2. Install the Claude desktop app, sign in with your subscription, set
   it to start with Windows.
3. Install Claude Code (needs Node.js). Verify with `claude --version`.
4. Copy this `venture-studio` folder to `Documents\venture-studio`.
5. In the Claude desktop app, connect the folder `Documents\venture-studio`.
6. Windows Update: set active hours so it never reboots mid-task.
7. Optional but recommended: a separate email address and browser
   profile used only for studio businesses.

## 2. First run (manual, together)

Before anything, open `OWNER-EDGE.md` and correct it. It is the only
file about you the teams read; it holds skills and markets, no personal
data.

Open Claude Code in `Documents\venture-studio` and run:

```
Read CLAUDE.md and skills/research/SKILL.md, then run one Research cycle.
Produce five idea briefs in pipeline/00-inbox.
```

Then:

```
Run Planning on everything in pipeline/00-inbox.
```

Review the five scores with me in chat. We tune the rubric weights
until the ranking matches your judgement. Only then automate.

## 3. Scheduled tasks (after tuning)

Create these as scheduled tasks that require this computer:

| Task | Schedule | Prompt |
|------|----------|--------|
| Research cycle | Mon & Thu 06:00 | "Run the Research team per skills/research/SKILL.md. Target 5 new briefs." |
| Planning pass | daily 07:00 | "Run Planning on all files in pipeline/00-inbox and close any validation past its deadline in pipeline/15-validating." |
| Preparation pass | daily 07:30 | "Run Preparation on pipeline/20-planned and any closed tickets." |
| Work: <business> | per plan | "Run Work for businesses/<slug> per its plan.md." |
| Management nightly | daily 22:00 | "Refresh management/dashboard.md." |
| Management weekly | Fri 18:00 | "Write the weekly review and any stop/hold/scale decisions." |

Add one Work task per business when Preparation creates it.

## 4. Your role

You'll receive tickets in `pipeline/30-tickets/open/` (and a push
notification if the scheduled task is set to notify). Each ticket is
one page: what, why, cost, what you must do. You act, write
`APPROVED`, `REJECTED`, or `DONE` at the bottom with the date, and move
it to `closed/`. That's the whole approval process.

Budget: nothing is deposited. USD 1,000 is a ceiling you release only
when a ticket earns it; every spend, however small, is a ticket you pay
yourself at that moment. The teams plan every business to start at USD 0.

## 5. What the agents never do

Open accounts, accept terms, type passwords or card numbers, move money,
sign anything, use any personal information about you, or run anything
illegal or against platform rules. If a step needs one of these, you get
a ticket.

## 6. Honest expectations

- Phase 1 (first 90 days) is deliberately wide: ~20 briefs a week, many
  validations in parallel, up to 8 businesses live. Expect 8–15 tickets a
  week in this phase, mostly accounts and publishes. Phase 2 narrows to
  the 3 best.
- Most ideas get rejected at Planning. That is the system working.
- Platform businesses (YouTube, TikTok, Etsy, affiliate) usually take
  months to first revenue. Services and digital products are faster.
- Agents run when scheduled or messaged, not in a continuous loop.
  "Always on" means every few hours, which is enough.
- Losses are normal. The ledger and weekly review exist so losses are
  small, visible, and stopped early.
