# Idea Brief: Email authentication (SPF, DKIM, DMARC) set-up and monitoring for GCC SMEs

- **Id:** 20261109-email-authentication-setup-service
- **Category:** 4 Services and gigs
- **Method playbook:** research/playbooks/email-authentication-service.md
- **Date:** 2026-11-09

## What it is
A fixed-fee set-up of a business domain's email authentication: inventory
of every service that sends as the domain (mail host, invoicing,
newsletter, CRM, booking tool), a correct SPF record, DKIM switched on at
each sender, a DMARC record pointed at a studio-run report address, and a
staged move from monitor to quarantine to reject over 4-8 weeks, delivered
as exact DNS records the client pastes (or lets the studio paste via a
delegated DNS login). USD 190 (QAR 690) per domain for the set-up, then
USD 19 a month per domain for report parsing, new-sender alerts and a
one-page monthly pass-rate report. Sold by studio-domain email to owners
and office managers of 5-50-staff firms in Qatar and the GCC whose public
DNS already shows the fault: the first email names the missing or broken
record on their own domain and what it does to their quotes and invoices.

## Who pays, how much, how often
Trading, contracting, clinic, agency and professional-services firms that
send quotes and invoices from their own domain and have no IT provider
watching DNS. Upwork's published project band for a deliverability audit
and set-up (SPF, DKIM, DMARC, reputation review, action plan) is USD
300-800; the Instantly-experts page puts deliverability set-up and
warm-up at USD 200-800. The MSP pricing guide at dmarc.ai prices the
smallest clients at USD 20-25 a month per domain and under-25-staff
rollouts at USD 3-5K (with a free audit as the sales tool). Monitoring
software sells at USD 8-24 a month per small business (PowerDMARC Basic
USD 8, dmarcian Basic USD 24, trustyourinbox Lite USD 9). One set-up fee
per domain, then monthly for as long as the domain sends mail.

## Evidence (minimum two independent sources, at least one platform-level or first-person with numbers)
| Source | URL | Date seen | Type | What it shows (numbers) |
|--------|-----|-----------|------|-------------------------|
| Upwork, email marketing consultants hire page (project ranges) | https://www.upwork.com/hire/email-marketing-consultants | 2026-11-09 | platform stats | "Deliverability audit and setup" (SPF, DKIM, DMARC, list hygiene, action plan) USD 300-800 per project, experienced tier |
| Upwork, Instantly experts hire page | https://www.upwork.com/hire/instantly-experts | 2026-11-09 | platform stats | Deliverability set-up and warm-up USD 200-800 per project; hourly USD 15-40 |
| dmarc.ai, how to price DMARC services as an MSP | https://dmarc.ai/academy/how-to-price-dmarc-services-as-an-msp | 2026-08-09 | vendor (provider-side pricing guide) | Under-25-staff clients: audit free, rollout USD 3-5K, monthly USD 50-100 per domain; micro clients deliverable at USD 20-25 a month per domain; "the audit is the sales tool" |
| DEV Community, audit of 1,728 local business domains | https://dev.to/ashtech52/dmarc-for-small-business-we-checked-1728-local-business-domains-and-46-had-no-dmarc-record-22ii | 2026-10-26 | first-person study (public DNS, incl. five Gulf countries) | 46% of mail-receiving local business domains had no DMARC record; only 28% of DMARC records request reports; 71% not at enforcement; "about an hour of work spread over a few weeks" |
| dmarcian, pricing | https://dmarcian.com/pricing | 2026-01-13 | platform price | Basic USD 24/month (2 domains); Plus USD 240/month; small-business plan positioning |
| PowerDMARC, DMARC pricing 2026 | https://powerdmarc.com/dmarc-cost-pricing | 2026-10-26 | vendor (price survey) | SMB tools USD 8-75 a month; managed rollouts quote-based; Basic from USD 8 |
| trustyourinbox, pricing | https://trustyourinbox.com/pricing | 2026-11-09 | platform price | Free for 1 domain; Lite USD 9/month (5 domains); Pro USD 19/month (25 domains); "small-business tools typically run USD 10-40/month" |
| TRENET (Finland), SPF/DKIM/DMARC service page | https://www.trenet.eu/en/services/spf-dkim-dmarc | 2026-11-09 | marketplace listing (competitor price) | Managed service from EUR 250 a month; "meaningful cleanup in about one month" |
| Christoph Olivier Consulting, email agency rate cards 2026 | https://christopholivierconsulting.com/email-marketing-agency/ | 2026-11-01 | vendor round-up (cites Upwork) | Deliverability audit and set-up USD 300-800; Gmail, Yahoo and Outlook bulk-sender rules since 2024-2025 require SPF, DKIM and DMARC |
| Sales.co cold email benchmark 2026 | https://sales.co/research/cold-email-statistics | 2026-10-29 | survey (2M+ emails) | Reply rate 2.09%, positive 14.1% of replies |

## Why it works now
Gmail, Yahoo and Outlook have required SPF, DKIM and a DMARC record for
bulk senders since 2024-2025, and quotes and invoices from a domain with
no SPF or DMARC land in spam more often; yet 46% of local business
domains checked in October 2026 (including five Gulf countries) had no
DMARC record at all. The fault is visible from outside: one public DNS
query per domain tells the agent exactly what is missing, so the first
email is a true finding about the prospect's own domain, not a pitch.
Delivery is text (DNS records, a sender inventory, a monthly report) and
report parsing is a Python job over the DMARC XML, which fits the runner
and the owner's Python edge. The software vendors charge USD 8-24 a month
but leave the set-up to the customer; the service sells the set-up and
keeps the monitoring.

## What would kill it
- Clients whose DNS is held by a web agency or a telecom that will not give access or paste records; the set-up then stalls on a third party.
- Free checkers and the mailbox providers' own wizards (Google Workspace, Microsoft 365) make the SPF step a two-minute job; the sale rests on the sender inventory, DKIM at every service and the staged move to reject.
- A record pasted wrongly can block the client's own mail; every change ships with a rollback line and is verified by the agent within an hour.
- Low ticket (USD 19 a month) means the retainer only matters at 20+ domains; the set-up fee carries the first months.

## Platform and payout check (from research/platform-rules.md and management/payments.md)
- Platform usable by a Qatar-resident seller: direct invoicing yes; Gumroad product for the set-up and subscription for the monitoring
- Payout route: Gumroad (QAR) or PayPal via QNB
- Published volume caps and disclosure duties that apply: email rule 15 (20 cold emails a day, business addresses, opt-out line); DNS queries of public records only; no login held by the agents beyond a delegated DNS editor the client can revoke

## Capital needed (itemised)
| Item | USD | One-off / monthly |
|------|-----|-------------------|
| DNS lookups, DMARC report mailbox on the studio domain, Python parser | 0 | |
**Total start:** USD 0  **Monthly run:** USD 0  **Funding tier:** 0

## Time
- Time to first dollar (typical, from evidence): 2-3 weeks (finding in the first email, fixed fee on reply, records delivered within 2 days, DKIM and DMARC staged over the following weeks)
- Monthly range at 6 months (typical small operator, from evidence; name the median if known): USD 400 - 1,500 (2-5 set-ups a month at USD 190 plus 10-30 domains on the USD 19 retainer); median unknown
- Owner time per week after launch: 0 h

## Distribution
Channel 1: studio-domain email to 20 then 30 owners or office managers of
5-50-staff GCC firms whose domain shows no SPF, no DMARC or a DMARC with
no report address (checked by the agent before sending), each email
quoting the record found or missing on their own domain. First ten
customers: those firms. Second channel: a landing page with a self-serve
"type your domain, see your three records" check and a Gumroad set-up
product; cross-sell to every client of the website-audit and automation
services, whose domains the studio already knows.

## Automatability
| Step | Agent / Owner / Either | Note |
|------|------------------------|------|
| Prospect list from public directories, DNS check of each domain, outreach | Agent | business addresses only; public DNS only |
| Sender inventory, SPF and DMARC record drafting, DKIM instructions per service | Agent | client pastes records or delegates a DNS editor role |
| Verification within an hour of each change, staged policy moves | Agent | scheduled checks |
| DMARC XML report parsing, new-sender alerts, monthly report, invoice | Agent | Python over the report mailbox |

## Legal / platform notes
Only public DNS records are read; DMARC aggregate reports contain sending
IPs and counts, not message content or personal data. The studio never
holds the client's mailbox password; DNS changes go through the client or
a revocable delegated role. Income legal basis per ticket 20261025-studio-1.

## Research confidence
High on price (two Upwork project bands, a provider-side pricing guide,
three vendor price pages, one competitor service page) and on the size of
the fault (a 1,728-domain public study); Medium on GCC conversion by email.
