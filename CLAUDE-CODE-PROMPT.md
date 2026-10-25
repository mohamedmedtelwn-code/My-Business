# Prompt for Claude Code — Venture Studio hardening

Paste everything below the line into Claude Code, started inside
`Documents\venture-studio`.

---

You are working inside a folder called `venture-studio`. Read every file in
it before doing anything: start with `CLAUDE.md`, then `README.md`,
`OWNER-EDGE.md`, every `skills/*/SKILL.md`, every file in `templates/`, and
`skills/management/DASHBOARD.md`.

## What this is

An AI venture studio that runs on this laptop. Five teams work as a
pipeline: Research finds ways people are demonstrably making money
anywhere in the world; Planning scores ideas against a rubric and rejects
most; a 7-day zero-cost Validation stage tests demand; Preparation makes a
business ready to run and raises tickets for anything only the owner can
do; Work operates each live business; Management keeps the ledger, the
dashboard, and proposes stop / hold / scale. The owner approves tickets and
signs decisions. Rules that matter: every idea is planned to launch at
USD 0; the owner's USD 1,000 is a ceiling released only per ticket, never
deposited; earnings go into a reinvestment pool that funds the next bigger
business before any ceiling money; Phase 1 (90 days) is a wide funnel with
automatic pruning, Phase 2 narrows to the best three; agents never open
accounts, accept terms, type credentials, move money, or use personal
information about the owner; `OWNER-EDGE.md` lists skills and markets the
owner brings and is the only owner-related file teams read.

The folder is currently a Markdown specification. Your job is to make it
work as well as it possibly can, in two passes.

## Pass 1 — research (do this first, write findings before changing anything)

Do a deep, sourced research pass and write `research/STUDIO-RESEARCH.md`
with findings and URLs. Cover:

1. **Evidence base for the category wheel.** For each of the ten categories
   in `skills/research/SKILL.md`, find current (last 12 months) primary
   evidence of small operators' earnings: income reports, marketplace
   seller stats, platform payout pages, academic or industry studies. Note
   typical time to first dollar and 6-month monthly range. Flag categories
   where evidence is mostly course-sellers.
2. **Platform rules that kill monetisation.** Current monetisation
   thresholds and AI-content policies for YouTube, TikTok, Etsy, Amazon
   Associates, Gumroad, Fiverr, Upwork, app stores. Put the verified rules
   in `research/platform-rules.md` with the date checked.
3. **Getting paid from Qatar.** Which payout routes a Qatar-resident
   individual can realistically use: Gumroad, Paddle, Lemon Squeezy,
   Payoneer, Wise, PayPal, Stripe (including via a non-resident US LLC),
   local banks. Fees, limits, KYC, known blockers. Write
   `management/payments.md` with the options ranked and the exact owner
   steps for the top two.
4. **Validation methods that work at USD 0.** What the lean-startup and
   indie-hacker literature says about landing-page tests, pre-sales and
   cold outreach: realistic response rates, so our "3 signals in 7 days"
   threshold is calibrated. Adjust the threshold if the evidence says so,
   and record why.
5. **Owner-edge market check.** For the skills in `OWNER-EDGE.md`
   (construction planning, Primavera P6, EOT claims, Gulf construction
   market), find what is already being sold: P6 courses, XER tools, EOT
   templates, claims consultants' pricing, Upwork/Fiverr gig rates, Arabic
   vs English demand. Identify gaps.
6. **Multi-agent pipeline practice.** How other people run autonomous
   agent pipelines reliably: idempotent runs, file locks, run logs,
   failure handling, cost control. Pick what applies to a file-based
   pipeline on one Windows laptop.
7. **Failure modes.** Search for post-mortems of "AI runs my business"
   and automated side-hustle experiments. List the top ten reasons they
   failed and map each to a rule or check we should add.

Use web search for all of this and cite every claim. Mark anything you
could not verify as unverified.

## Pass 2 — harden the studio

Based on Pass 1, improve the folder. Keep the Markdown files as the
human-readable spec and add tooling beside them. Do not change the
five-team structure, the funding rules, or the owner-only actions; those
are decided. Specifically:

1. **Rubric and rules.** Update `templates/scoring-rubric.md`, the category
   wheel, the validation threshold, and the kill/scale defaults to match
   the evidence. Record each change in the rubric's change log with the
   source.
2. **Ledger as code.** Replace the Markdown-only ledger with
   `tools/ledger.py` backed by `management/ledger.sqlite`, and have it
   regenerate `management/ledger.md` as a view. Commands: add entry,
   reconcile business ledgers against the studio ledger, report ceiling /
   released / spent / revenue / pool. Refuse any entry that spends from an
   unreleased ceiling or an empty pool.
3. **Pipeline checker.** `tools/check.py` that validates the folder state:
   every file in the right stage, no business launched with an open
   blocking ticket, live-business count within the Phase cap, validations
   past deadline flagged, tickets older than 3 days flagged. Each team's
   SKILL.md should run it at the start and end of a run.
4. **Run logger.** `tools/runlog.py` that every team calls at start and
   end; appends to `management/runs.jsonl` with team, start, end, files
   touched, tickets raised, outcome. Management reads it for the
   dashboard.
5. **Dashboard feed.** `tools/dashboard_push.py` that reads the ledger,
   runs log and business folders and prints the exact ArtifactData batch
   payload described in `skills/management/DASHBOARD.md`, so the
   Management run only has to send it.
6. **Dry run.** Create `tests/` with three fake idea briefs (one strong,
   one that should fail the gate, one borderline) and a script that
   walks them through Planning → Validation → Preparation → Work → Management
   using the tools above, without touching the web or raising real
   tickets. It should finish with the checker passing and a sample
   dashboard payload.
7. **Scheduled-task prompts.** Write `SCHEDULE.md` with the final prompt
   text and cadence for each scheduled task, including the Work task
   template, with usage-limit guidance: what to cut first if runs start
   failing on subscription limits.
8. **README.** Update it so the owner can set up the laptop and run the
   first cycle from the README alone.

## Constraints

- Windows laptop, Python 3.11+, no paid services, no API keys in the folder.
- Everything must work when a fresh Claude session opens this folder with
  no memory of this conversation; the files are the only context.
- Do not add any personal data about the owner anywhere.
- Keep it simple: a planner should be able to read any file and understand it.
- Commit to git as you go with clear messages; initialise the repo if needed.

When both passes are done, write `CHANGELOG.md` summarising what changed
and why, and list the five decisions you think the owner should review.
