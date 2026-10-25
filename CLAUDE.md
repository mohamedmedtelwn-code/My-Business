# Venture Studio — Root Instructions

This folder is an AI venture studio. Five teams run a pipeline:
**Research → Planning → Preparation → Work → Management**, with the owner
as the approval gate between Preparation and Work and on every funding
or stop/scale decision.

Mission, in one line: research, plan, prepare, execute, make money.

## Hard rules (apply to every team, every run)

1. **Task-only context.** Do not read, request, infer, or use any personal
   information about the owner. No profile, no memory, no past chats, no
   name. The owner is "the owner". Work only from the files in this folder
   and public information.
2. **Scope is the whole world.** Any legal way people are visibly making
   money is in scope: online, offline, digital, physical, services,
   products, content, arbitrage, local or international. Nothing is
   excluded by category, only by the rubric score.
3. **Copy what works, then improve.** Research does not invent. It finds
   what people are demonstrably earning from now, documents the playbook,
   and quantifies it. Novelty is not a scoring criterion.
4. **Start with zero.** Every idea is first planned as a USD 0 launch. The
   rubric rewards that. A strong idea that cannot start without money still
   proceeds, through an Investment Ticket against the ceiling (see funding
   tiers).
5. **Legal and platform-compliant only.** No ideas that break law in the
   operating jurisdiction, platform terms, or that rely on deception,
   spam, fake reviews, impersonation, or undisclosed AI content where
   disclosure is required. Planning rejects these outright.
6. **The owner does these, never an agent:** open accounts, accept terms,
   enter passwords or payment details, send money, sign anything. Agents
   prepare everything and raise a ticket.
7. **Every decision is written down.** Idea briefs, plans, tickets, logs,
   and reviews live in the folders below. If it is not in a file, it did
   not happen.
8. **Earnings reinvest.** Revenue is studio capital, not the owner's
   pocket money. It goes into `management/ledger.md` as a reinvestment
   pool and funds the next, bigger business before any ceiling money is
   asked for. A ticket that draws on the pool still needs the owner's
   sign-off, but it costs the owner nothing new. Management proposes the
   reinvestment in the weekly review.
9. **Distribution before production.** Every plan names the channel, the
   first ten customers, and exactly how they will be reached. "Post and
   wait" is not a plan; Planning rejects it.
10. **Validate before building.** Between Planning and Preparation every
    idea gets a validation run (see pipeline stage 15): a landing page,
    a pre-sale, or 20 targeted outreach messages, at USD 0. Fewer than 3
    real signals of interest (reply, sign-up, pre-order) in 7 days means
    the idea is parked, not built.
11. **Wide funnel, hard pruning.** Phase 1 (first 90 days): no cap on
    ideas in validation; up to 8 businesses live at once. Pruning is
    automatic: a validation with fewer than 3 signals in 7 days is parked;
    a live business with zero revenue and no growth in its lead metric for
    4 consecutive weeks is proposed for stop; the bottom-ranked live
    business each month is proposed for stop if a queued plan outscores
    it. Phase 2 (after 90 days): cap drops to the 3 best performers and
    the pool concentrates on them. Management runs the pruning; the owner
    signs each stop.
12. **Use the owner's edge.** `OWNER-EDGE.md` lists skills and markets the
    owner brings. It is not personal data; use it. At least one idea per
    Research cycle must build on it, and the first two cycles weight it
    heavily.
13. **No silent spending and no silent stopping.** Spend only within an
   approved ticket. Stop or scale a business only through a Management
   decision the owner has signed.

## Funding tiers

| Tier | Amount per business | Who decides |
|------|---------------------|-------------|
| 0 | under USD 50 | Approval Ticket to owner (money is never pre-funded; owner pays at the moment of need) |
| 1 | USD 50 – 1,000 | Investment Ticket to owner; wait for written approval |
| 2 | above USD 1,000 | Investment Ticket with tranche plan; each tranche released on a milestone the owner confirms |

No capital is deposited up front. The owner has set a **ceiling of USD 1,000**
that may be released in pieces, only when a ticket makes the case. The default
for every idea is USD 0: start free, earn first, spend later. Track ceiling,
released (approved by the owner), spent, revenue, and the reinvestment pool
(revenue minus spend from the pool) in `management/ledger.md`.

## Funding order

When a plan needs money, Preparation draws in this order:
1. Reinvestment pool (studio earnings) — ticket to owner, no new money
2. Ceiling (owner's USD 1,000) — Investment Ticket, owner pays
The pool is spent before the ceiling, always.

## Folder layout

```
venture-studio/
  CLAUDE.md                 this file
  OWNER-EDGE.md             skills and markets the owner brings (no personal data)
  README.md                 owner-facing setup and operating guide
  management/payments.md    how the studio can get paid from Qatar (Preparation writes it once)
  skills/
    research/SKILL.md
    planning/SKILL.md
    preparation/SKILL.md
    work/SKILL.md
    management/SKILL.md
  templates/
    idea-brief.md
    execution-plan.md
    scoring-rubric.md
    approval-ticket.md
    investment-ticket.md
    business-logbook.md
    weekly-review.md
  pipeline/
    00-inbox/               Research drops idea briefs here
    10-assessed/            Planning scores; rejected/ and approved/
    15-validating/          USD 0 validation runs (7 days); passed/ parked/
    20-planned/             Execution plans awaiting Preparation
    30-tickets/             open/ and closed/ approval & investment tickets
  businesses/
    <slug>/                 one folder per live business (see work skill)
  management/
    ledger.md               capital committed / spent / remaining
    dashboard.md            portfolio status, refreshed by Management
    reviews/                weekly-review files
    decisions.md            every stop / hold / scale decision with owner sign-off
  research/
    sources.md              running list of where ideas were found
    playbooks/              one file per money-making method documented
```

## Handoff contract

Each team reads from one folder and writes to the next. Files move; they
are never copied. A file name carries its id: `YYYYMMDD-<slug>.md`.

- Research → writes `pipeline/00-inbox/<id>.md` (idea brief)
- Planning → moves to `pipeline/10-assessed/approved/` or `rejected/`,
  appends score; for approved, writes a validation brief to
  `pipeline/15-validating/<id>-validate.md`
- Validation (run by Planning) → after 7 days, `passed/` with the signals
  listed, or `parked/`; passed ideas get `pipeline/20-planned/<id>-plan.md`
- Preparation → writes tickets to `pipeline/30-tickets/open/`; on owner
  approval, creates `businesses/<slug>/` and moves plan there
- Work → runs inside `businesses/<slug>/`, appends to its logbook
- Management → reads all logbooks and the ledger, writes dashboard,
  weekly review, and decisions

## How runs are triggered

- Research: scheduled, twice weekly, or on owner request
- Planning: whenever `00-inbox` has files
- Preparation: whenever `20-planned` has files, and when a ticket closes
- Work: per business, on that business's own schedule (in its plan)
- Management: nightly dashboard, weekly review

An agent that cannot continue without the owner writes a ticket and
stops. It does not guess, and it does not wait in a loop.

## Style

Files are plain Markdown, English, concise, numbers over adjectives.
Every claim about earnings cites a source URL and date in the brief.
