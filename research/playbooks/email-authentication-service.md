# Playbook: email authentication set-up and monitoring (SPF, DKIM, DMARC)

Checked 2026-11-09. Sources in the brief 20261109-email-authentication-setup-service.

## What is sold
A per-domain set-up: sender inventory, SPF record, DKIM at each sending
service, DMARC record with reports to a studio address, staged move to
p=reject over 4-8 weeks; USD 190 per domain. Then USD 19 a month per
domain for report parsing, new-sender alerts and a monthly pass-rate page.

## Steps a small operator follows
1. Build the checker: one script that queries MX, SPF and DMARC for a list
   of domains and flags no SPF, no DMARC, DMARC without a report address,
   and SPF records over the 10-lookup limit.
2. Prospect GCC firms of 5-50 staff from public directories; run the
   checker; keep only domains with a fault.
3. Email 20 then 30 owners or office managers (company addresses) naming
   the record found or missing on their own domain and the fixed price;
   opt-out line.
4. On reply: inventory the senders from the client's own list of tools,
   draft the exact records with a rollback line, give the DKIM steps per
   service, verify within an hour of each paste.
5. Point DMARC reports at a studio mailbox; parse the XML weekly; move
   the policy to quarantine then reject once every legitimate sender
   passes; send the monthly page and invoice the retainer.
6. Landing page with a self-serve domain check; Gumroad set-up product and
   monitoring subscription.

## Prices observed
Upwork deliverability audit and set-up USD 300-800 per project; set-up
and warm-up USD 200-800; MSP guide USD 20-25 a month per micro domain,
USD 3-5K rollouts for under-25-staff firms; software USD 8-24 a month
(PowerDMARC, trustyourinbox, dmarcian); managed service from EUR 250 a
month (TRENET).

## Tools
Python (stdlib DNS over a resolver call, zipfile and XML parsing for the
reports), the studio email sender, a report mailbox on the studio
domain, the free checkers for cross-verification.

## Time per week
Owner 0 h.

## Ramp
First dollar 2-3 weeks. At 6 months: USD 400-1,500 a month. Median unknown.

## Risks
DNS held by third parties; free wizards cover the SPF step; a wrong
record blocks the client's mail (rollback line, hourly verification);
low retainer ticket until 20+ domains.
