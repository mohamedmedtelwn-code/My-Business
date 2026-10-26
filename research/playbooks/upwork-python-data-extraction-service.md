# Playbook: Python data-extraction and automation service

Checked 2026-10-26. Sources in the brief 20261026-python-data-extraction-service.

## What is sold
A fixed-price Python script that collects public web data into a clean
spreadsheet, plus an optional monthly refresh. Typical units: one site, up
to 5,000 rows, delivered in 3-5 days.

## Steps a small operator follows
1. Pick three buyer types that copy-paste data today (resellers tracking
   competitor prices, recruiters building candidate lists from public
   directories, brokers tracking listings).
2. Build two sample outputs (50 rows each) from public sites and screenshot
   them; these are the proof in every message.
3. Outreach: 20 personalised messages a week offering the free 50-row
   sample, then a fixed quote. Follow up on day 3.
4. Upwork in parallel: profile with the samples; bid only on fixed-price
   posts above USD 150 that name the site; attach a 20-row sample from that
   site in the proposal.
5. Scope every job in writing: site, fields, row count, refresh schedule,
   legal check (public pages only, robots.txt, no personal data).
6. Build with requests/Playwright plus pandas; deliver .xlsx and a
   one-page readme; keep the script for the refresh retainer.
7. Offer the monthly refresh at the delivery call (GitHub Actions schedule).

## Prices observed
USD 100-250 one-off script (most Upwork fixed posts); USD 1,000-1,500
multi-site or expert; USD 1,500 catalogue tier (3 days); median Python
fixed budget USD 170; median hourly USD 30.

## Tools
Python (requests, Playwright, pandas, openpyxl), GitHub Actions for schedules,
Upwork, WhatsApp, LinkedIn.

## Time per week
Owner 3-5 h; agent does drafting, building and testing.

## Ramp
First dollar 1-3 weeks by outreach, 3-6 weeks on Upwork. At 6 months a
small operator with 2-8 jobs a month: USD 300-1,500. Median unknown.

## Risks
Site changes break scripts; personal-data requests must be refused; the
low end of the market is being absorbed by no-code and AI agents.
