# Changelog — hardening pass, 2026-10-25

The folder arrived as a Markdown specification. Two passes were made: a sourced
research pass (`research/STUDIO-RESEARCH.md`) and a hardening pass that turned
the rules into tools and updated the spec to match the evidence. The five-team
structure, the funding rules (USD 0 default, USD 1,000 ceiling released per
ticket, pool before ceiling) and the owner-only actions were not changed.

## Pass 1: research (what was learned)
- Nine research questions, each with a claim ledger and URLs (`research/evidence/`),
  consolidated in `research/STUDIO-RESEARCH.md`. Confidence is marked per claim;
  anything unconfirmed is labelled UNVERIFIED.
- `research/platform-rules.md`: monetisation thresholds, fees, AI-content rules
  and Qatar eligibility for YouTube, TikTok, Etsy, Gumroad, Lemon Squeezy,
  Paddle, Fiverr, Upwork, Amazon Associates, KDP, Apple and Google Play, with
  the date checked.
- `management/payments.md`: eight payout routes ranked for a Qatar resident,
  the legal status of side income (Law 9/2026, MOCI e-commerce licence, 10%
  tax on Qatar-source business income), and step-by-step owner instructions for
  Gumroad and PayPal via QNB.
- Headline findings: Etsy shops, TikTok Creator Rewards and Amazon Associates
  (US bank payout) are not usable from Qatar; Gumroad pays QAR to a Qatar bank;
  the median small operator earns about USD 0 at month 6 on content platforms
  and under USD 150 a month on apps and indie SaaS; the old "3 signals from 20
  messages" rule parks two thirds of genuinely good ideas; AI-run business
  experiments failed on distribution, hallucinated progress, platform
  enforcement and unguarded autonomy.

## Pass 2: what changed and why

| Area | Change | Why (section of STUDIO-RESEARCH.md) |
|------|--------|-------------------------------------|
| `templates/scoring-rubric.md` | Weights Evidence 3 to 4, Capital 5 to 3, Time to first dollar 3 to 4; anchors rewritten; eight gates (Qatar platform and payout, no mass-produced content, two channels); two worked examples; change log filled | 1, 2, 7 |
| Category wheel (`skills/research/SKILL.md`) | Etsy and TikTok Rewards removed; finance-adjacent replaced by professional tooling and expertise products; categories 6, 7, 8 downgraded with conditions | 1, 2, 5 |
| Validation (`CLAUDE.md` rule 10, `templates/validation-brief.md`, `tools/signals.py`) | Denominators (50 messages sequential, 100 visitors at 8%, 20 asks), weighted signal units, 48-hour reply tail, one extension when inconclusive | 4 |
| Kill, scale and pause defaults (`CLAUDE.md` rule 11, `management/config.json`) | Kept 4-week zero-revenue stop and 2-week kill/scale; added 7-day ticket pause, 10-ticket studio cap, monthly platform-rules re-check, payout route verified before money | 6, 7 |
| `tools/ledger.py` + `management/ledger.sqlite` | Ledger as code; `ledger.md` and each `businesses/<slug>/ledger.md` are generated views; refuses spend from an unreleased ceiling, beyond a ticket's release, or from an empty pool; `reconcile` and `report` commands | 7 (failure modes 3, 8) |
| `tools/check.py` | Validates stage placement, blocking tickets, Phase caps, deadlines, stale tickets, metric sources, platform-rules age, payout flag, crashed runs, breakers, ledger agreement | 6 |
| `tools/runlog.py` + `management/runs.jsonl` | Start and end events per run, files touched, tickets raised, per-team lock, crash sweep, circuit breaker after 3 failures, optional git commit per run | 6 |
| `tools/dashboard_push.py` | Prints the ArtifactData batch payload from ledger, run log and folders; versions folder adds `if_version`; prunes activity beyond 200 docs | DASHBOARD.md |
| `tools/rubric.py`, `tools/signals.py` | Deterministic score block and validation verdict; the agent pastes, it does not total by hand | 6, 7 |
| `management/config.json` | Single source of every enforced number (caps, thresholds, denominators, weights, cadence) | 6 |
| Five `skills/*/SKILL.md` | Each run starts and ends with `check.py` and `runlog.py`; money only via `ledger.py`; read lists are explicit; Work has outbound, price and volume guards; Management reads the run log and pushes the dashboard | 6, 7 |
| `skills/management/DASHBOARD.md` | One writer (Management), version-pinned batch procedure | tool constraints |
| `templates/*` | Idea brief gets a platform-and-payout check and evidence types; plan gets Launched, price guard, channel mix, metric sources; tickets name the ledger commands; WORK.md template carries the run commands | 1, 2, 7 |
| `tests/` | 104 unit tests plus `tests/dry_run.py`, which walks three fixture briefs (strong, gate-fail, borderline) through Planning, Validation, Preparation, Work and Management with the tools and ends with the checker passing and a sample dashboard payload | brief item 6 |
| `SCHEDULE.md` | Final prompts and cadence per task, Work task template, usage-limit facts and the order in which to cut | 6 |
| `README.md` | Setup and first cycle from the README alone, including the self-checks and the GitHub clone command | brief item 8 |
| Removed | `CLAUDE-CODE-PROMPT.md` (the brief that drove this pass; it stays in git history) | a fresh session must not re-run the hardening |

## Five decisions for the owner to review

1. **Legal basis for income before the first sale.** Law 9/2026 puts freelance
   work outside the Labour Law pending regulations that had not been issued by
   October 2026; MOCI's new e-commerce licence (QAR 500) may or may not be open
   to an expatriate individual; Qatar-source business income is taxed at 10%.
   The studio now blocks accepting money until you close the "legal basis"
   ticket. Decide how you will confirm this (employer consent, licence, tax
   registration) and whether audience-only launches may run in the meantime.
2. **Payout stack.** Gumroad first (pays QAR to a Qatar bank, merchant of
   record), PayPal withdrawn through QNB second; a US LLC with Stripe (about
   USD 500 up front, USD 400 a year, a US tax filing) only in Phase 2. Confirm
   this order, and whether you hold or will open a QNB account.
3. **What left the wheel.** Etsy, TikTok Creator Rewards and Amazon Associates
   (US) are gated out for Qatar; finance-adjacent methods are replaced by
   professional tooling and expertise products built on your edge. If you
   have, or will have, a bank account and residential address in an eligible
   country, Etsy can come back; say so and the gate changes.
4. **Rubric weights and the validation bar.** Evidence 4, Capital 3, Time to
   first dollar 4; validation needs 50 messages, 100 visitors or 20 asks and
   weighted signals. Both are defaults for your first tuning session; the
   evidence says the old bar was undersized, but the exact numbers are
   judgement. Retune in `management/config.json` and the rubric table together.
5. **Live cap and subscription plan.** The cap stays at 8 live businesses in
   Phase 1, which assumes a Max plan: every run shares one usage pool and each
   live business adds a daily Work run. On a Pro plan set `phase1_live_cap` to
   4 and Research to one cycle a week (`SCHEDULE.md`), and decide whether
   usage credits with a spend cap are acceptable (that is a ceiling decision).

## Known gaps
Section 8 of `research/STUDIO-RESEARCH.md` lists what is still unverified
(Fiverr and Upwork account opening from Qatar, Apple and KDP payouts to a
Qatar bank, Lemon Squeezy onboarding under Stripe Managed Payments, Payoneer's
official Qatar status, exact Claude usage allowances). Research re-verifies the
platform rules monthly; the first 90 days of ledger data will be better
evidence than any page cited here.

## Day 1 operations (2026-10-25)
- First Research cycle run from the cloud session: 8 briefs, 6 playbooks, 7 methods rejected at source.
- First Planning run: 7 approved (71-78), 1 rejected (newsletter, 69); 7 validation briefs; batch 1 (EOT readiness review, claim pack, P6 baseline QA) started with owner tickets; batch 2 starts 2026-11-01.
- First Preparation run: two studio tickets (legal basis for income; Gumroad payout route).
- First Management nightly: dashboard.md rebuilt; live dashboard pushed (15 writes); ticket cards now show the owner's steps.
- Cloud mode switched on: five scheduled tasks on the owner's account (see SCHEDULE.md); `.gitattributes` merges the run log and research lists by union so concurrent runs do not conflict.
