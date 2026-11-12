# Validation Brief: Bilingual website privacy-and-consent pack for Saudi and UAE businesses (PDPL)

- **Id:** 20261112-gcc-website-privacy-compliance-pack
- **Started:** 2027-01-14  **Deadline:** 2027-01-21 (7 days; replies count to day 9)
- **Test:** outreach
- **Extended:** no
- **Cost:** USD 0

## The test
The agents run a headless-browser scan of the public websites of 5-50-staff firms in Saudi Arabia and the UAE, keep only the sites that load advertising or analytics tags before any consent or carry no privacy notice, and email 20 owners or marketing managers from the studio mailbox quoting the tags found and the missing notice on their own site, with the offer of the bilingual pack (privacy notice, cookie notice, banner wording, developer sheet) at USD 190 (QAR 690) per website plus an optional USD 19 monthly re-scan. A reply asking for the pack or the quote counts 1 (intent); a paid pack counts 3; a thank-you for the scan alone counts 0. If the first 20 bring no signal, 30 more follow. The email is in output/20261112-gcc-website-privacy-compliance-pack/message.md; list rules in prospect-criteria.md. Scheduled for the first free slot after the email-authentication test (2027-01-14); it moves with the queue if the mailbox ticket studio-7 is still open. Planning may run it on the same 50 domains as the website-audit, Google-listing and email-authentication tests so one scan feeds four hooks (feedback 2026-11-12).

## Denominator (update as the test runs)
- **Messages sent:** 0   (outreach: 20 first, then 30 more unless 0 signals; pass needs 50)
- **Visitors:** 0        (not used)
- **Asks:** 0            (presale: at least 20 direct asks)

## What counts (signal units, pass at 3)
payment / pre-order / deposit from a stranger 3 · booked call with a qualified
stranger 1 (void if not held within 14 days) · reply with explicit intent 1
(a "yes, send the pack" or a request for the quote counts) ·
likes, follows, friends and family 0.

## Owner steps (ticket raised if any)
None for this test. The owner only completes the studio set-up tickets
(free studio mailbox, Gumroad, legal basis). Agent steps:
1. Build the prospect list from public business sources per prospect-criteria.md; run the scan on every site; business addresses only; keep it in output/20261112-gcc-website-privacy-compliance-pack/prospects.csv (company, role, address, source URL, tags found, notice present).
2. Send 20 personalised emails from the studio mailbox over the first 3 days (studio-wide cap 20 a day), each with the opt-out line.
3. Day 3: one follow-up to anyone silent; never after a "no" or an opt-out.
4. Save every reply as a file in output/20261112-gcc-website-privacy-compliance-pack/replies/ (first name, company type, what they said, date) and add a Signals row citing it.
5. If the first 20 bring no signal by day 5, send 30 more.
6. Planning counts the signals with tools/signals.py at the deadline.

## Signals
| Date | Type | Who / what | Source |
|------|------|-----------|--------|

Type is one of: payment, call, intent, signup. Source is a file path under
output/ (screenshot, export) or a URL. Rows without a source do not count.

## Verdict

**Verdict:** RUNNING  
**Signal units:** 0 (payments 0 x3, calls 0, intent replies 0, sign-ups 0 -> 0 SU)  
**Denominator:** 0 of 50 messages (not reached)  
**Reason:** Deadline 2027-01-21 not reached; 0 SU so far.  
**Counted on:** 2026-11-12 by tools/signals.py
