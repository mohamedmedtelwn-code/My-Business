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
2. **Scope is the whole world, filtered by Qatar.** Any legal way people are
   visibly making money is in scope, but only on platforms that accept a
   Qatar-resident seller with a payout route in `management/payments.md`.
   `research/platform-rules.md` holds the verified answers.
3. **Copy what works, then improve.** Research does not invent. It finds
   what people are demonstrably earning from now, documents the playbook,
   and quantifies it. Novelty is not a scoring criterion.
4. **Start with zero.** Every idea is first planned as a USD 0 launch. A
   strong idea that cannot start without money still proceeds, through an
   Investment Ticket against the ceiling (see funding tiers).
5. **Legal and platform-compliant only.** No ideas that break law in the
   operating jurisdiction, platform terms, or that rely on deception, spam,
   fake reviews, bought engagement, impersonation, undisclosed AI content
   where disclosure is required, or mass-produced content on a platform that
   penalises it. Planning rejects these outright.
6. **The owner does these, never an agent:** open accounts, accept terms,
   enter passwords or payment details, pass identity checks, send money,
   sign anything. Agents prepare everything and raise a ticket. The owner
   does nothing else: the owner's name, face, personal accounts and personal
   network are never used for marketing, outreach or delivery (owner
   decision 2026-10-27, `management/decisions.md`).
7. **Every decision is written down.** Idea briefs, plans, tickets, logs,
   and reviews live in the folders below. If it is not in a file, it did
   not happen. Every number in a metrics or review file names its source.
8. **Earnings reinvest.** Revenue is studio capital, not the owner's pocket
   money. It goes into the ledger as a reinvestment pool and funds the next,
   bigger business before any ceiling money is asked for. A ticket that
   draws on the pool still needs the owner's sign-off, but it costs the owner
   nothing new. Management proposes the reinvestment in the weekly review.
9. **Distribution before production.** Every plan names two channels, the
   first ten customers, and exactly how they will be reached. "Post and
   wait" is not a plan; Google organic search alone is not a channel.
10. **Validate before building.** Between Planning and Preparation every
    idea gets a USD 0 validation run (stage 15), run by the agents under
    rule 15: 50 personalised outreach emails from the studio domain (20
    first, 30 more unless the first 20 bring nothing), or a landing page
    seen by at least 100 qualified visitors, or 20 direct pre-sale asks by
    email. Pass = 3 signal units within 7 days: a payment or
    pre-order counts 3, a booked call 1, a reply with explicit intent 1, an
    email sign-up one third (only above an 8% sign-up rate), likes and
    follows 0. `tools/signals.py` counts and decides. Under the denominator
    the result is inconclusive and gets one 7-day extension; otherwise the
    idea is parked, not built.
11. **Wide funnel, hard pruning.** Phase 1 (first 90 days from
    `studio_start` in `management/config.json`): no cap on ideas in
    validation; up to 8 businesses live at once. Pruning is automatic: a
    parked validation stays parked; a live business with zero revenue and
    no growth in its lead metric for 4 consecutive weeks is proposed for
    stop; the bottom-ranked live business each month is proposed for stop if
    a queued plan outscores it; a business with a ticket open more than 7
    days is paused. Phase 2 (after 90 days): cap drops to the 3 best
    performers and the pool concentrates on them. Management runs the
    pruning; the owner signs each stop.
12. **Use the owner's edge, within the owner's hold.** `OWNER-EDGE.md` lists
    skills and markets the owner brings. It is not personal data; use it.
    Until `edge_hold_until` in `management/config.json` (set by the owner on
    2026-10-25 to 2026-11-25) no business may relate to the owner's
    construction-planning profession: P6 or scheduling services, EOT and
    claims products, contractor-facing tools, courses for planners. General
    skills in the edge file (Excel modelling, Python tooling, Arabic and
    English) stay usable. After the hold date, at least one idea per Research
    cycle builds on the edge.
13. **No silent spending and no silent stopping.** Spend only within an
    approved ticket, recorded by `tools/ledger.py`, which refuses anything
    the funding rules forbid. Stop, pause or scale a business only through a
    Management decision the owner has signed.
14. **Tools before prose.** Every run starts and ends with `tools/check.py`
    (the folder must be in a legal state) and `tools/runlog.py` (every run is
    logged, locked and, after three failures in a row, stopped until the
    owner resets). The numbers the tools enforce live in
    `management/config.json`; this file quotes them, the config decides.
15. **Agents run everything.** Every business is run end to end by the
    agents: prospecting, outreach, content, delivery, support, reporting.
    Outreach goes out only under the studio brand from studio-owned channels:
    email from the studio domain (personalised, business addresses only,
    at most 20 cold messages a day across the studio, an opt-out line in
    every message, no second follow-up after a "no"), landing pages and
    product pages the agents publish, and marketplace listings under the
    studio brand where the platform's terms allow an account to be operated
    on the holder's behalf. Channels that require a real person to operate
    them (LinkedIn messaging, Upwork, Fiverr, personal social accounts) are
    out of scope. Consumer audiences reachable only through personal social
    accounts or paid ads are out of scope until a studio-owned channel
    exists. The studio brand, domain, email-sending account and API keys
    are set up by the owner through tickets and stored as environment
    secrets of the runner session; agents never see passwords.

## Funding tiers

| Tier | Amount per business | Who decides |
|------|---------------------|-------------|
| 0 | under USD 50 | Approval Ticket to owner (money is never pre-funded; owner pays at the moment of need) |
| 1 | USD 50 – 1,000 | Investment Ticket to owner; wait for written approval |
| 2 | above USD 1,000 | Investment Ticket with tranche plan; each tranche released on a milestone the owner confirms |

No capital is deposited up front. The owner has set a **ceiling of USD 1,000**
that may be released in pieces, only when a ticket makes the case. The default
for every idea is USD 0: start free, earn first, spend later. The ledger
(`tools/ledger.py`, view in `management/ledger.md`) tracks ceiling, released,
spent, revenue and the reinvestment pool (revenue minus spend from the pool).

## Funding order

When a plan needs money, Preparation draws in this order:
1. Reinvestment pool (studio earnings): ticket to owner, no new money
2. Ceiling (owner's USD 1,000): Investment Ticket, owner pays
The pool is spent before the ceiling, always. The ledger tool enforces both.

## Folder layout

```
venture-studio/
  CLAUDE.md                 this file
  OWNER-EDGE.md             skills and markets the owner brings (no personal data)
  README.md                 owner-facing setup and operating guide
  SCHEDULE.md               scheduled-task prompts, cadence, usage-limit guidance
  CHANGELOG.md              what changed in the hardening pass and why
  skills/<team>/SKILL.md    one per team; management/DASHBOARD.md for the live feed
  templates/                idea-brief, validation-brief, execution-plan, scoring-rubric,
                            approval-ticket, investment-ticket, business-logbook, weekly-review
  tools/                    check.py, runlog.py, ledger.py, signals.py, rubric.py,
                            dashboard_push.py, replies_apply.py, studio.py (shared helpers); stdlib only
  tests/                    unit tests and dry_run.py (walks three fixture briefs end to end)
  pipeline/
    00-inbox/               Research drops idea briefs here
    10-assessed/            Planning scores; approved/ and rejected/
    15-validating/          USD 0 validation runs; output/, passed/, parked/
    20-planned/             execution plans awaiting Preparation
    30-tickets/             open/ and closed/ approval and investment tickets
  businesses/<slug>/        one folder per launched business (see templates/business-logbook.md)
  management/
    config.json             every number the tools enforce (caps, thresholds, cadence)
    ledger.sqlite, ledger.md   the ledger (tool-owned) and its generated view
    runs.jsonl              every run: start, end, outcome, files touched, tickets raised
    payments.md             payout routes from Qatar and the owner's set-up steps
    dashboard.md            portfolio status, rebuilt nightly by Management
    reviews/                weekly-review files
    decisions.md            every stop / hold / scale / pause decision with owner sign-off
    dashboard-url.txt       the live dashboard artifact
  research/
    STUDIO-RESEARCH.md      the evidence behind the rules (read section 1 before a cycle)
    platform-rules.md       monetisation thresholds and Qatar eligibility per platform
    evidence/               claim ledgers with URLs
    sources.md, feedback.md, rejected-at-source.md, playbooks/
```

## Handoff contract

Each team reads from one folder and writes to the next. Files move; they
are never copied. A file name carries its id: `YYYYMMDD-<slug>.md`.

- Research → writes `pipeline/00-inbox/<id>.md` (idea brief)
- Planning → moves to `pipeline/10-assessed/approved/` or `rejected/`,
  appends `## Score` (from `tools/rubric.py`) or `## Rejected`; for approved,
  writes `pipeline/15-validating/<id>-validate.md`
- Validation (run by Planning) → `tools/signals.py --write` decides; PASSED
  moves to `passed/` and gets `pipeline/20-planned/<id>-plan.md`; PARKED
  moves to `parked/`
- Preparation → writes tickets to `pipeline/30-tickets/open/`; records
  releases and spend with `tools/ledger.py`; on a complete checklist creates
  `businesses/<slug>/`, moves the plan in, sets Status live and Launched
- Work → runs inside `businesses/<slug>/`, records money with `tools/ledger.py`,
  appends to its logbook and metrics
- Management → reads all logbooks, the ledger and the run log; writes
  dashboard, weekly review and decisions

## How runs are triggered

See `SCHEDULE.md` for the prompts and cadence.
- Research: scheduled, twice weekly, or on owner request
- Planning: daily; processes whatever is in `00-inbox` and every validation due
- Preparation: daily; processes `20-planned` and closed tickets
- Work: per business, on that business's own schedule (in its plan)
- Management: nightly dashboard, weekly review

Tickets reach the owner on the live dashboard (one card per open ticket, with
the steps and the drafts to copy) and in the push notification each run sends.
The owner answers on the card (Done, Approved, Rejected, or a note); every run
applies those answers first with `tools/replies_apply.py` (see
`skills/management/DASHBOARD.md`). Editing the ticket file by hand still works.

An agent that cannot continue without the owner writes a ticket and stops.
It does not guess, and it does not wait in a loop. Runs are level-triggered:
each run processes what is there, up to its cap, and exits.

## Style

Files are plain Markdown, English, concise, numbers over adjectives. Every
claim about earnings cites a source URL and date in the brief. Every number
in a metrics or review file names where it was read from.
