---
name: research
description: Research team — find ways people are demonstrably making money right now, anywhere in the world, and write idea briefs into pipeline/00-inbox. Use when running a research cycle or when the owner asks for new ideas.
---

# Research Team

Goal: ten new, evidence-backed idea briefs per cycle in Phase 1 (first 90
days), five afterwards. Not inventions. Observed, working money-making
methods with the playbook written down.

## Start and end of every run
- Start: `python tools/check.py` (fix every ERROR before anything else), then
  `python tools/runlog.py start --team research` and keep the RUN_ID.
- End: `python tools/check.py`, then
  `python tools/runlog.py end --id <RUN_ID> --outcome ok|warn|bad --summary "<one line>" --commit`.
  `warn` = fewer briefs than target or a source could not be verified; `bad` =
  nothing written. If `runlog.py start` refuses (lock or circuit breaker), stop
  and write nothing.
- Read only: `CLAUDE.md`, this file, `OWNER-EDGE.md`, `research/feedback.md`,
  `research/sources.md`, the playbook index, `research/platform-rules.md`, and
  section 1 of `research/STUDIO-RESEARCH.md` once per cycle.

## Rules
- Follow CLAUDE.md hard rules. No personal information about the owner.
- **Owner hold (CLAUDE.md rule 12):** until `edge_hold_until` in
  `management/config.json`, write no brief that relates to the owner's
  construction-planning profession (Primavera P6, schedules, EOT or claims,
  contractor-facing tools, courses for planners, category 10 as a whole).
  Excel, Python, data and language skills from OWNER-EDGE.md may still be
  used on other audiences. Step 0 below is suspended during the hold.
- Whole world is in scope, but every brief must pass the Qatar check: the
  platform accepts a Qatar-resident seller and a payout route in
  `management/payments.md` exists (`research/platform-rules.md` lists the
  verified answers). Etsy shops, TikTok Creator Rewards and Amazon Associates
  paid to a Qatar bank fail it today.
- Every earnings claim needs a URL and the date seen. No URL, no claim.
- Evidence quality: platform-level data (filings, payout pages, platform
  statistics), first-person reports with screenshots, and surveys with a stated
  sample count as evidence. Course-seller, tool-vendor and affiliate pages may
  be cited for context but do not count toward the two-source minimum. Name
  the median where one exists; a top earner is not a range.
- Skip anything illegal, deceptive, against platform terms, or that depends on
  mass-produced AI content on a platform that penalises it. Add one line to
  `research/rejected-at-source.md`.
- If `tools/check.py` warns that `research/platform-rules.md` is older than 30
  days, this cycle re-verifies each row against its URL and updates the
  **Checked** date before writing briefs.

## Category wheel (rotate; do not repeat the last cycle's set)
1. Content platforms: YouTube long-form, newsletters, podcasts. Shorts and
   TikTok only as distribution (TikTok Creator Rewards is not open in Qatar;
   Shorts RPM is cents). Slow: most channels earn USD 0 at month 6.
2. Digital products: templates, ebooks (KDP with AI disclosure and the
   2-titles-per-format-per-week cap), courses, presets, printables, sold
   through Gumroad or Lemon Squeezy, not Etsy.
3. Marketplaces and app stores: Gumroad, Google Play (Qatar is a merchant
   country), Apple App Store (payout to Qatar unverified), Shopify App Store,
   Udemy. Etsy is excluded for this owner.
4. Services and gigs: direct outreach to named B2B buyers first; Upwork; Fiverr
   only for outcome-priced offers (its entry-level gig segment is shrinking).
   The fastest route to a first dollar.
5. Software: micro-SaaS, browser extensions, bots, APIs, data products, sold
   through a merchant of record (Lemon Squeezy, Paddle, Polar).
6. Arbitrage and resale: retail, domain, cross-border, dropship. Only with a
   verified payout rail and seller registration; usually fails the USD 0 rule.
7. Local physical in Qatar: vending, rental, cleaning, events, kiosks. Only
   when the owner already holds the licence the activity needs.
8. Affiliate and lead-gen: comparison tools, directories, lead-gen into a
   service. Two acquisition channels required; no Amazon Associates paid to a
   Qatar bank; Google organic cannot be the only channel.
9. Communities and memberships: Patreon, Skool, paid groups, cohorts. A second
   step once an audience exists, not a first business.
10. Professional tooling and expertise products: Excel and Python tools,
    checkers, templates, audits and courses for construction planners and
    adjacent professions (owner-edge lane; price anchors in
    `research/STUDIO-RESEARCH.md` section 5).

Pick 5-6 categories per cycle in Phase 1, 3-4 afterwards. Categories 4 and 10
are in every one of the first two cycles. Within each, find the sub-niches
where small operators (not celebrities) report income.

## Procedure
0. Read `OWNER-EDGE.md`. At least one brief this cycle must build on it; in the
   first two cycles, at least three.
1. Read `research/sources.md`, `research/feedback.md` and the playbook titles so
   you do not duplicate a method already documented or rejected.
2. For each chosen category, search for: income report, case study, revenue
   screenshot, marketplace bestseller lists, platform payout statistics,
   demand signals (job posts, search volume, sold counts).
3. For each promising method, dig until you can fill every field of
   `templates/idea-brief.md`, including the platform and payout check. If you
   cannot fill "Evidence" with two qualifying independent sources, drop it.
4. Write the playbook: exact steps a small operator follows, tools used, time
   per week, typical ramp to first dollar, typical monthly range at 6 months
   (median where known). Save as `research/playbooks/<method>.md`.
5. Write the brief to `pipeline/00-inbox/YYYYMMDD-<slug>.md` using the
   template. One idea per file. Lower-case slug, hyphens only.
6. Append sources to `research/sources.md`.
7. End the run with a summary line: briefs written, categories covered,
   methods rejected at source and why.

## Quality bar per brief
- Who pays, how much, how often, with numbers.
- Why it works now (demand signal), and what would kill it.
- Capital needed (itemised), time to first dollar, time per week.
- Automatability: which steps an agent can do, which need a human.
- Two qualifying evidence URLs with dates and source types.
- Platform usable from Qatar, payout route named, volume caps and disclosure
  duties listed.
