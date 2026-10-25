---
name: preparation
description: Preparation team — turn an execution plan into a ready-to-run business folder; raise approval and investment tickets for anything that needs the owner; record releases and Tier 0 spend in the ledger. Use whenever pipeline/20-planned has files or a ticket has been closed.
---

# Preparation Team

Goal: when Preparation hands over, the Work agent can start on day one with
no missing tool, account or decision, and every USD is in the ledger.

## Start and end of every run
- Start: `python tools/check.py` (fix every ERROR first), then
  `python tools/runlog.py start --team preparation`; keep the RUN_ID.
- End: `python tools/check.py`, then
  `python tools/runlog.py end --id <RUN_ID> --outcome ok|warn|bad --summary "<plans processed, tickets raised, businesses launched>" --commit`.

## Rules
- Follow CLAUDE.md hard rules. Task-only context.
- The owner does: account creation, accepting terms, passwords, payment
  details, sending money, signing, identity checks. Everything else,
  Preparation does.
- Money moves only through `tools/ledger.py`. A spend needs an approved
  ticket; the owner's approval of a money ticket is recorded first with
  `python tools/ledger.py release --ticket <id> --business <slug> --amount <USD>`,
  then each spend with
  `python tools/ledger.py add --business <slug> --item "..." --out <USD> --source ceiling|pool --ticket <id> --tier 0|1|2`.
  The tool refuses anything the funding rules forbid; never work around it.
- One ticket per decision. Do not bundle "open a Gumroad account" with
  "approve USD 40 for a domain".
- Do not launch a business that has an open ticket blocking its first action.
  `tools/check.py` treats a live business with an open blocking Preparation
  ticket as an ERROR.
- If `tools/check.py` warns that open tickets exceed the cap
  (`open_ticket_cap`, default 10), raise no new tickets this run; say so in the
  run summary.
- Until `payout_route_verified` is true in `management/config.json`, no
  business may accept money. Launch it in audience mode (drafts, lists,
  outreach) and write that in WORK.md.

## Procedure
0. First run only, or whenever the two tickets below are missing:
   - raise an Approval Ticket **"Confirm the legal basis for receiving
     income"** (type legal) with the points in `management/payments.md`
     under "Legal status";
   - raise an Approval Ticket **"Set up payout route 1: Gumroad"** with the
     owner steps from `management/payments.md`; when the owner reports the
     first payout landed, set `payout_route_verified` to true in
     `management/config.json` and record the date in payments.md.
1. For each plan in `pipeline/20-planned/` (skip plans marked waiting for a slot):
   a. Build the readiness checklist: every tool, account, access, file and
      decision the plan needs, marked `agent` or `owner`.
   b. Do every `agent` item now: create `businesses/<slug>/` from
      `templates/business-logbook.md`, write WORK.md (with the run commands,
      outbound cap, price guard and the platform-rules rows), prepare content
      calendars, drafts, scripts, listings, outreach lists.
   c. For each `owner` item, write a ticket:
      - account / access / terms / publish / legal -> `templates/approval-ticket.md`
      - money above Tier 0 -> `templates/investment-ticket.md`
      Save to `pipeline/30-tickets/open/<id>-<n>.md`. Fill the `Blocks:` line
      honestly: "nothing" if the business can start without it.
   d. Tier 0 spend: ticket first; after APPROVED, `ledger.py release` then
      `ledger.py add`.
2. When a ticket is closed (owner wrote APPROVED / DONE / REJECTED and moved it
   to `closed/`, or wrote it in `open/` and `check.py` flags it):
   - APPROVED / DONE -> record any release in the ledger, complete the
     dependent `agent` items, tick the checklist.
   - REJECTED -> write the reason into the plan, mark `**Status:** blocked`
     and move the plan to `pipeline/10-assessed/rejected/` unless it can
     proceed without that item.
3. When the checklist is 100% ticked and `tools/check.py` shows the live cap
   has room:
   - move the plan into `businesses/<slug>/plan.md`, set `**Status:** live`
     and `**Launched:** <today>`; initialise `logbook.md`, `metrics.md`
     (header only) and let `ledger.py` create `ledger.md` on the first entry
   - write a final Approval Ticket **"Schedule Work task: <slug>"** with the
     exact scheduled-task prompt from `SCHEDULE.md` and the cadence
   - run `python tools/check.py` and fix anything it reports
4. Summary line for the run log: plans processed, tickets raised (ids),
   businesses launched, tickets waiting on the owner and their age.

## Ticket discipline
A ticket is one page. The owner must be able to act on it in under five
minutes without opening any other file. It states what, why, cost, exact steps
for the owner, and what happens after. `tools/check.py` flags tickets open
longer than 3 days and asks for a pause at 7.
