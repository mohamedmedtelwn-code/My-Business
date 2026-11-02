# Playbook: scanned-document digitisation to Excel

Checked 2026-11-02. Sources in the brief 20261102-arabic-document-digitisation-service.

## What is sold
Scanned or paper records (invoices, ledgers, statements, forms) in Arabic
and English converted to verified Excel or CSV in the client's column
layout: USD 59 up to 50 pages, USD 169 up to 200, USD 390 up to 500;
72-hour turnaround; confidence log per field.

## Steps a small operator follows
1. Build the pipeline: OCR and vision models, table reconstruction,
   Arabic and English normalisation, totals and date checks, confidence
   scoring, column mapping.
2. Prospect finance and admin managers at trading, logistics, clinic and
   school firms; email 20 then 30 offering a free 5-page sample in their
   own layout; data terms attached; opt-out line.
3. Convert the sample in 24 hours; quote the flat tier.
4. Deliver the file and the confidence log; delete after 30 days.
5. Landing page with three Gumroad tiers and sample upload; monthly
   batches for firms with ongoing paper flow.

## Prices observed
DataConvertPro USD 49/149/349 flat tiers; GoTranscript from USD 3.00 per
page; Upwork catalog gigs from USD 10-65 with 100-1,200 reviews;
XHTMLTEAM USD 12-25 per hour.

## Tools
Open-source OCR and vision models in the runner, Python (pandas,
openpyxl), a paid OCR API only as a ticketed pass-through, the studio
email sender, Gumroad.

## Time per week
Owner 0 h; the owner signs the data-processing terms template once
(shared with the list-cleaning service).

## Ramp
First dollar 2-3 weeks. At 6 months: USD 300-1,500 a month. Median unknown.

## Risks
Free invoice capture in accounting tools; confidentiality; handwriting
accuracy disputes; overlap with the Python data-extraction service.
