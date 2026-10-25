# Idea Brief: XER to DCMA-14 schedule health report (local desktop tool)

- **Id:** 20261025-xer-dcma-health-report
- **Category:** 10 Professional tooling and expertise products
- **Method playbook:** research/playbooks/gumroad-desktop-utility.md
- **Date:** 2026-10-25

## What it is
A Windows script that reads a Primavera P6 XER file on the user's own machine
and writes a DCMA 14-point health report plus a two-file comparison
(as-planned vs update) to Excel. No upload of confidential programmes. Sold on
Gumroad to freelance planners and small contractors who cannot justify
enterprise tools.

## Who pays, how much, how often
Freelance planners, small and mid contractors, junior consultants. USD 39
one-off for the health report, USD 79 for the comparison module; or USD 9 per
report run through a pay-per-report option later.

## Evidence (minimum two independent sources, at least one platform-level or first-person with numbers)
| Source | URL | Date seen | Type | What it shows (numbers) |
|--------|-----|-----------|------|-------------------------|
| ScheduleLens pricing on Capterra | https://www.capterra.com/p/10053722/ScheduleLens/pricing/ | 2026-10-25 | marketplace price page | USD 29 per health check, USD 79 per comparison, subscriptions from USD 79/month: buyers pay per report |
| Softedemy shop | https://admin.softedemy.com/shop/ | 2026-10-25 | vendor shop | DCMA analyzer, XER-to-Excel and comparison utilities sold at USD 15-90 each |
| ScheduleReader licence page | https://www.schedulereader.com/?p=23117 | 2026-10-25 | vendor price page | USD 344/year (PRO USD 440): the ceiling for a viewer-class tool |
| Steelray Analyzer for P6 | https://steelray.com/AnalyzerP6/AnalyzerForP6.php | 2026-10-25 | vendor price page | USD 990 per user per year for schedule analysis |
| PyP6Xer on PyPI | https://pypi.org/project/PyP6Xer/ | 2026-10-25 | registry (primary) | LGPL-2.1 parser, v1.16.0 (Jul 2025): the build can be closed-source |

## Why it works now
Enterprise tools (SmartPM USD 12,000-25,000/year, Steelray USD 990) are out of
reach for freelancers; free converters cap what plain conversion can charge, so
the value is the report and the privacy. The owner already has XER processing
and schedule-QA tooling that can be productised (OWNER-EDGE.md).

## What would kill it
- A free DCMA workbook spreading in the planner community (several exist already: price pressure, not a kill)
- Oracle changing the XER format (slow, versioned)
- Licence problems if a GPL parser is used (avoid: PyP6Xer is LGPL)

## Platform and payout check (from research/platform-rules.md and management/payments.md)
- Platform usable by a Qatar-resident seller: yes (Gumroad)
- Payout route: Gumroad
- Published volume caps and disclosure duties that apply: none

## Capital needed (itemised)
| Item | USD | One-off / monthly |
|------|-----|-------------------|
| none (Python, open-source parser, Gumroad) | 0 | |
**Total start:** USD 0  **Monthly run:** USD 0  **Funding tier:** 0

## Time
- Time to first dollar (typical, from evidence): 1-3 months (build and test, then outreach); no distribution data, anchors are utility price points
- Monthly range at 6 months (typical small operator, from evidence; name the median if known): USD 50-400; no median exists for this niche
- Owner time per week after launch: 1 h (support questions, test on real XER files)

## Distribution
Channel 1: 50 personalised messages to freelance planners on LinkedIn and
Upwork offering a free run on one of their files. Channel 2: a free "5-check
lite" version posted in planner forums and Arabic P6 groups that links to the
full tool. Second channel: Upwork profile as a delivery vehicle.

## Automatability
| Step | Agent / Owner / Either | Note |
|------|------------------------|------|
| Build and test the script | Agent | PyP6Xer (LGPL), stdlib Excel writer or openpyxl |
| Test on real project files | Owner | confidentiality |
| Listing, docs, outreach messages | Agent drafts, owner publishes and sends | |

## Legal / platform notes
Use the LGPL parser; do not redistribute GPL code in a closed product. No
customer data leaves the customer's machine.

## Research confidence
Medium-low: price anchors are solid, free substitutes are many; validation
must show that privacy and the report format are worth paying for.

## Score

| # | Criterion | Score | Weight | Points | Justification |
|---|---|---|---|---|---|
| 1 | Evidence strength | 3 | 4 | 12 | four vendor price pages and a primary registry; no sales distribution |
| 2 | Capital to first dollar | 5 | 3 | 15 | USD 0: Python, LGPL parser, Gumroad |
| 3 | Time to first dollar | 3 | 4 | 12 | build then outreach: 1-3 months |
| 4 | Automatability | 4 | 3 | 12 | agent builds, documents and lists; owner tests on real files |
| 5 | Owner time per week | 4 | 2 | 8 | about 1 h a week |
| 6 | Earnings ceiling at 6 months | 3 (+1 edge) | 2 | 8 | USD 50-400 anchored on Softedemy and ScheduleLens prices |
| 7 | Durability | 2 (+1 edge) | 1 | 3 | outreach plus a free lite version; Upwork later |
| 8 | Legal / platform clarity | 4 | 1 | 4 | Gumroad allowed; LGPL licence respected |

**Total:** 74/100 — APPROVED (threshold 70); owner-edge bonus applied
