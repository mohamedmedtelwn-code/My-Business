# Playbook: fixed-fee CRM and mailing-list cleaning

Checked 2026-10-29. Sources in the brief 20261029-crm-list-cleaning-service.

## What is sold
Deduplication, standardisation (bilingual names, phones, addresses),
format validation and company matching of a customer or lead list, with a
one-page quality report; USD 290 up to 5,000 records, USD 0.05 per record
above, optional USD 60 monthly hygiene retainer; email verification as a
pass-through extra.

## Steps a small operator follows
1. Build the pipeline: parsing, Arabic and English transliteration map,
   phone and email normalisation, fuzzy matching with flagged (never
   automatic) merges, quality metrics.
2. Prospect SMEs that visibly email customers (newsletter forms, Mailchimp
   or HubSpot footers); company addresses only.
3. Email 20 then 30: a free quality report on a 500-row sample within
   48 hours; data-processing terms attached; opt-out line.
4. Deliver the report; quote the fixed fee; clean; deliver the file and
   the merge log; delete after 30 days and confirm.
5. Offer the retainer and a quarterly re-check; ask for a referral.
6. Landing page with a self-serve duplicate score for 50 pasted rows.

## Prices observed
Upwork data-cleaning projects USD 500-1,500; managed services USD 0.05-0.50
per record and USD 500-3,000 flat; Implisense from EUR 299 with a free
48-hour report; verification credits USD 5.30-9.90 per 1,000 addresses.

## Tools
Python (pandas, rapidfuzz), a transliteration table, an email verification
API when ordered, the studio email sender, Gumroad for the package.

## Time per week
Owner 0 h; the owner signs the data-processing terms template once.

## Ramp
First dollar 2-4 weeks. At 6 months: USD 300-1,500 a month. Median unknown.

## Risks
Personal-data obligations, free native deduplication for simple cases,
low-cost freelancers for basic work.
