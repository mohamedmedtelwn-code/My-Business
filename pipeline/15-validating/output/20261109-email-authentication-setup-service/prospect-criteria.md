# Prospect list rules (agent-built, 20 first, 30 more if needed)

Count a firm only if all four hold:
1. A trading, contracting-supply, clinic, agency, logistics or
   professional-services firm in Qatar, the UAE or KSA with 5-50 staff
   that sends quotes or invoices from its own domain (the domain has MX
   records). Not construction contractors or planning consultancies
   until 2026-11-25 (owner hold).
2. The agent's public DNS check shows at least one fault: no SPF record,
   an SPF record over the 10-lookup limit or ending in +all, no DMARC
   record, or a DMARC record with no rua= report address.
3. An owner, office manager, finance or IT contact with a published
   business address on the firm's own site, or a role address (info@,
   admin@, accounts@) on the site.
4. The address comes from the firm's own site or a public directory; no
   scraped private lists, no personal addresses.

Good sources: Qatar and UAE chamber and business directories, trade-fair
exhibitor lists, the website-audit and automation prospect lists (shared
audience; reuse their domains).

Agents save the list as prospects.csv in this folder (firm, role, address,
source URL, records found). Replies are saved in replies/ with a first
name and firm type only. Only public DNS is queried; nothing is sent to
the prospect's mail server.
