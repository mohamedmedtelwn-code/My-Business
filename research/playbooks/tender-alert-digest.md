# Playbook: keyword-filtered public-tender alert digest

Checked 2026-10-29. Sources in the brief 20261029-gcc-tender-alert-digest.

## What is sold
A daily email of new public tenders matching a subscriber's keywords and
sector from official GCC portals, with buyer, deadline and document link;
a free weekly digest as the lead magnet; paid alerts on a Gumroad
membership at USD 29 a month.

## Steps a small operator follows
1. Read the public listing pages of each portal (Qatar Monaqasat, Saudi
   Etimad public search, UAE and Oman portals) once a day with a polite
   scraper: robots.txt, rate limits, public pages only.
2. Normalise title, buyer, category, deadline, link; translate titles both
   ways; store in a small database.
3. Publish a weekly "tenders this week" page and newsletter (free) for the
   country, excluding construction works during the owner hold.
4. Build the prospect list from public award notices and supplier
   registers in non-construction categories (company addresses only).
5. Email 20 then 30 prospects: the free weekly digest plus a 14-day trial
   of keyword alerts; opt-out line; one follow-up on day 3.
6. Paid tier on Gumroad membership; the alert job reads the subscriber's
   keywords from a form and sends daily.
7. Weekly: dedupe sources, fix parsers, report subscriber counts.

## Prices observed
Incumbents: USD 97 a month for a Gulf bundle (USD 1,260 per 13 months),
USD 60-154 for other bundles; TendersInfo sells daily alerts by
subscription against 8,157 live Qatar and 83,420 Saudi tenders.

## Tools
Python (requests, BeautifulSoup), SQLite, GitHub Actions schedule, the
studio email sender, Gumroad memberships, an agent-published landing page.

## Time per week
Owner 0 h; agents run the scrape, digest and outreach.

## Ramp
First dollar 3-5 weeks. At 6 months: USD 150-900 a month (5-30 subscribers).
Median unknown.

## Risks
Portal blocks, incumbents cutting price, low willingness to pay among
small suppliers, construction dominance of tender volume.
