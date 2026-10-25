---
name: preparation
description: Preparation team — turn an execution plan into a ready-to-run business folder; raise approval and investment tickets for anything that needs the owner; install tools and configure access. Use whenever pipeline/20-planned has files or a ticket has been closed.
---

# Preparation Team

Goal: when Preparation hands over, the Work agent can start on day one
with no missing tool, account, or decision.

## Rules
- Follow CLAUDE.md hard rules. Task-only context.
- The owner does: account creation, accepting terms, passwords, payment
  details, sending money, signing. Everything else, Preparation does.
- Never spend without a closed, approved ticket. Fund from the
  reinvestment pool first, the owner's ceiling second (CLAUDE.md funding
  order).
- One ticket per decision. Do not bundle "open a YouTube account" with
  "approve USD 300 for stock footage".
- Do not start a business that has an open ticket blocking its first
  action.

## Procedure
0. If `management/payments.md` does not exist, write it first: which
   payout platforms (Gumroad, Paddle, Lemon Squeezy, Payoneer, Stripe via
   a non-resident entity, PayPal, local bank) are usable from Qatar, with
   fees, limits and the owner steps to set each one up. Raise one
   Approval Ticket for the owner to set up the first payout route.
1. For each plan in `pipeline/20-planned/`:
   a. Build the readiness checklist: every tool, account, access, file,
      and decision the plan needs, marked `agent` or `owner`.
   b. Do every `agent` item now: install packages, create the business
      folder from `templates/business-logbook.md`, write the Work
      agent's `plan.md` and schedule, prepare content calendars,
      drafts, scripts, listings, briefs — whatever the plan calls for.
   c. For each `owner` item, write a ticket:
      - account/access/terms → `templates/approval-ticket.md`
      - money above Tier 0 → `templates/investment-ticket.md`
      Save to `pipeline/30-tickets/open/<id>-<n>.md`.
   d. Record Tier 0 spend in `management/ledger.md` with the plan id.
2. When a ticket is closed (owner wrote APPROVED/DONE/REJECTED):
   - APPROVED/DONE → complete the dependent `agent` items, tick the
     checklist, move the ticket to `closed/`.
   - REJECTED → write the reason into the plan, mark the plan
     `## Status: blocked` and move it to `pipeline/10-assessed/rejected/`
     unless the plan can proceed without that item.
3. When the checklist is 100% ticked:
   - create `businesses/<slug>/` (if not already), move the plan in as
     `plan.md`, initialise `logbook.md`, `metrics.md`, `ledger.md`
   - write `businesses/<slug>/WORK.md`: the standing instruction for the
     Work agent (what to do each run, what to log, when to stop and ask)
   - add a line to `management/dashboard.md` under "Launched"
   - write a final ticket of type "Schedule Work task" telling the owner
     the exact scheduled-task prompt and cadence to create.
4. Run log: plans processed, tickets raised, businesses launched.

## Ticket discipline
A ticket is one page. The owner must be able to act on it in under five
minutes without opening any other file. It states what, why, cost,
exact steps for the owner, and what happens after.

## Live dashboard
At the end of every run, write this team's `teams` doc and one `activity`
line to the owner's live dashboard per `skills/management/DASHBOARD.md`.
