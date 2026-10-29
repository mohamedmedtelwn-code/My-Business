# Playbook: reporting as a service for merchants on a hosted e-commerce platform

Checked 2026-10-29. Sources in the brief 20261029-salla-zid-merchant-reporting.

## What is sold
A weekly automated report (Sheets dashboard plus a one-screen summary) for
merchants on a platform whose cheap plans have basic analytics (here Salla
and Zid), delivered through the platform's API after the merchant
authorises a studio app. USD 49 a month after a free two-week pilot.

## Steps a small operator follows
1. Register a developer account on the platform (owner), build an app with
   read-only order, product and customer scopes, pass review.
2. Build the pipeline: pull orders weekly, compute sales by product, city,
   payment method, repeat share, low stock, refunds; write to the
   merchant's own Google Sheet; render a summary image in Arabic and
   English.
3. Prospect merchants whose store sites publish a business address, in
   repeat-purchase categories; 20 then 30 emails offering the pilot.
4. Onboard in two clicks (OAuth link); run the pilot for two weeks; the
   third email shows a decision the report would have changed.
5. Bill monthly through Gumroad membership or invoice; cancel deletes data.
6. List the app on the platform's app store once approved (second channel).

## Numbers observed
Salla 68,000+ merchants; Zid about 14,000 active stores; 50% of Salla and
41% of Zid stores publish an email; Zid gates detailed reports to a
SAR 18,000-a-year plan; Upwork dashboard projects USD 500-2,500.

## Tools
Platform APIs (OAuth, webhooks), Python, Google Sheets API, GitHub Actions,
Gumroad, the studio email sender.

## Time per week
Owner 0 h after the developer account exists.

## Ramp
First dollar 4-6 weeks. At 6 months: USD 250-1,500 a month (5-30 merchants).
Median unknown.

## Risks
Platform adds the feature, developer-account eligibility from Qatar,
API changes, price sensitivity.
