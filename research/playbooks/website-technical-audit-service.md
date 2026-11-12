# Playbook: fixed-fee website technical audit

Checked 2026-11-02. Sources in the brief 20261102-website-technical-audit-service.

## What is sold
A crawl-based technical audit (indexing, Core Web Vitals, broken links,
mobile layout, hreflang and RTL faults on bilingual sites, structured
data) delivered as a prioritised fix list with the exact changes; USD 240
up to 100 pages, USD 390 up to 500 pages; fixes quoted separately.

## Steps a small operator follows
1. Build the crawler: Playwright plus Lighthouse, link checker, hreflang
   and schema validators, a scoring sheet; output a 10-point mini report.
2. Prospect GCC SMEs whose sites earn leads; pre-crawl each site; keep
   only those with measurable faults.
3. Email 20 then 30 marketing managers or owners (company addresses) with
   three faults found on their own site and the fixed price; opt-out line.
4. Deliver the full audit in 3 days; offer the fix package with the
   client inviting the studio email into their CMS.
5. Landing page with a self-serve URL score; Gumroad package; re-audit
   after redesigns.

## Prices observed
Upwork basic technical audits USD 300-800; technical audit projects
USD 500-2,000; a top-rated seller at USD 200/300/400 by site size;
freelancer manual audits USD 500-2,000; 43% of US businesses pay
USD 101-750 per audit (WebFX via Foundgrove).

## Tools
Playwright and Chromium in the runner, Lighthouse, Python, Screaming Frog
free tier, Google PageSpeed Insights API (free), the studio email sender.

## Time per week
Owner 0 h.

## Ramp
First dollar 2-4 weeks. At 6 months: USD 250-1,600 a month. Median unknown.

## Add-on: accessibility module (added 2026-11-12)
An automated WCAG 2.2 pass (axe-core via Playwright: contrast, alt text,
form labels, empty links, document language) is sold as a USD 90 add-on
to the audit, not as a separate business: the WebAIM Million 2026 found
detectable failures on 95.9% of the top million home pages, and published
manual-audit prices run USD 100-250 a page (Accessible.org) and USD 499-
2,750 per small site; the GCC has no private-sector mandate, so the buyer
is the same site owner the audit already reaches, with the European
Accessibility Act (June 2025) as the hook for GCC firms selling into the EU.

## Risks
Free tools cover the basics; buyers expect rankings, not fix lists; CMS
access for fixes; USD 5-15/h marketplace tier.
