# Idea Brief: XER to DCMA-14 health report (local tool)

- **Id:** 20261101-p6-dcma-health-report
- **Category:** 10 Professional tooling and expertise products
- **Method playbook:** research/playbooks/gumroad-professional-utility.md
- **Date:** 2026-11-01

## What it is
A Windows script that reads a Primavera P6 XER file on the user's machine and
writes a DCMA 14-point health report to Excel, sold on Gumroad to small
contractors and freelance planners who cannot afford enterprise tools.

## Who pays, how much, how often
Freelance planners and small contractors. USD 39 one-off, or USD 9 per report.

## Evidence (minimum two independent sources, at least one platform-level or first-person with numbers)
| Source | URL | Date seen | Type | What it shows (numbers) |
|--------|-----|-----------|------|-------------------------|
| ScheduleLens pricing | https://www.capterra.com/p/10053722/ScheduleLens/pricing/ | 2026-10-25 | marketplace price page | USD 29 per health check, USD 79 per comparison |
| Softedemy shop | https://admin.softedemy.com/shop/ | 2026-10-25 | vendor shop | DCMA analyzer and XER-to-Excel utilities at USD 15-90 |
| PyP6Xer on PyPI | https://pypi.org/project/PyP6Xer/ | 2026-10-25 | registry (primary) | LGPL parser, v1.16.0, Jul 2025 |

## Why it works now
Free converters cap the price of plain conversion, so the value is the
report and the privacy (no upload). Enterprise tools cost USD 344-990 a year.

## What would kill it
- A free DCMA workbook spreading in the planner community (several exist)
- Licence risk if a GPL parser is used

## Platform and payout check (from research/platform-rules.md and management/payments.md)
- Platform usable by a Qatar-resident seller: yes (Gumroad)
- Payout route: Gumroad
- Published volume caps and disclosure duties that apply: none

## Capital needed (itemised)
| Item | USD | One-off / monthly |
|------|-----|-------------------|
| none | 0 | |
**Total start:** USD 0  **Monthly run:** USD 0  **Funding tier:** 0

## Time
- Time to first dollar (typical, from evidence): 1-3 months (build, then outreach)
- Monthly range at 6 months: USD 50 - 400 (no median; price anchors only)
- Owner time per week after launch: 1 h

## Distribution
Channel 1: 50 personalised messages to freelance planners on LinkedIn and Upwork. Channel 2: a free "5-check lite" version shared in planner forums.

## Automatability
| Step | Agent / Owner / Either | Note |
|------|------------------------|------|
| Build and test the script | Agent | PyP6Xer (LGPL) |
| Listing | Agent drafts, owner publishes | |

## Legal / platform notes
Use the LGPL parser; do not redistribute GPL code in a closed product.

## Research confidence
Medium-low: price anchors exist, free substitutes are many.
