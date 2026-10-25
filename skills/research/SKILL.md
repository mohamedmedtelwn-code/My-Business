---
name: research
description: Research team — find ways people are demonstrably making money right now, anywhere in the world, and write idea briefs into pipeline/00-inbox. Use when running a research cycle or when the owner asks for new ideas.
---

# Research Team

Goal: ten new, evidence-backed idea briefs per cycle in Phase 1 (first 90
days), five afterwards. Not inventions.
Observed, working money-making methods with the playbook written down.

## Rules
- Follow CLAUDE.md hard rules. No personal information about the owner.
- Whole world is in scope. Rotate categories across cycles so the inbox
  is not all one type (see category wheel).
- Every earnings claim needs a URL and the date seen. No URL, no claim.
- Prefer primary evidence: creator income breakdowns, marketplace sales
  counts, public revenue dashboards, job-board demand, pricing pages,
  case studies with numbers. Treat "guru" courses and affiliate blogs as
  weak evidence.
- Skip anything illegal, deceptive, or against platform terms. Do not
  write it up as a brief; add one line to `research/rejected-at-source.md`.

## Category wheel (rotate, do not repeat the last cycle's set)
1. Content platforms: YouTube, Shorts, TikTok, podcasts, newsletters
2. Digital products: templates, ebooks, courses, presets, printables, fonts
3. Marketplaces: Etsy, Gumroad, Creative Market, app stores, Shopify apps
4. Services and gigs: Fiverr, Upwork, local B2B services, done-for-you
5. Software: micro-SaaS, browser extensions, bots, APIs, data products
6. Arbitrage and resale: retail, domain, ticket, cross-border, dropship
7. Local physical: vending, rental, cleaning, delivery, events, kiosks
8. Affiliate and lead-gen: niche sites, comparison tools, directories
9. Communities and memberships: Discord, Patreon, paid groups, cohorts
10. Finance-adjacent (legal): staking, cash-back stacking, bank bonuses

Pick 5–6 categories per cycle in Phase 1, 3–4 afterwards. Within each, find the sub-niches where
small operators (not celebrities) report income.

## Procedure
0. Read `OWNER-EDGE.md`. At least one brief this cycle must build on it;
   in the first two cycles, at least three.
1. Read `research/sources.md` and `research/playbooks/` so you do not
   duplicate a method already documented.
2. For each chosen category, search for: "how much I made", income
   report, case study, revenue screenshot, marketplace bestseller lists,
   demand signals (job posts, search volume, sold counts).
3. For each promising method, dig until you can fill every field of
   `templates/idea-brief.md`. If you cannot fill "evidence" with at least
   two independent sources, drop it.
4. Write the playbook: exact steps a small operator follows, tools used,
   time per week, typical ramp to first dollar, typical monthly range at
   6 months. Save as `research/playbooks/<method>.md`.
5. Write the brief to `pipeline/00-inbox/YYYYMMDD-<slug>.md` using the
   template. One idea per file.
6. Append sources to `research/sources.md`.
7. Finish with a 5-line summary in the run log: briefs written, categories
   covered, methods rejected at source and why.

## Quality bar per brief
- Who pays, how much, how often — with numbers
- Why it works now (demand signal), and what would kill it
- Capital needed (itemised), time to first dollar, time per week
- Automatability: which steps an agent can do, which need a human
- At least two independent evidence URLs with dates

## Live dashboard
At the end of every run, write this team's `teams` doc and one `activity`
line to the owner's live dashboard per `skills/management/DASHBOARD.md`.
