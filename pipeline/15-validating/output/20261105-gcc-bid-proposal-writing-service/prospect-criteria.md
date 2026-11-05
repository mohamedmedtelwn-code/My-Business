# Prospect list rules (agent-built, 20 first, 30 more if needed)

Count a firm only if all four hold:
1. A supplier in Qatar, the UAE or KSA with 5-100 staff that appears in a
   public award notice, supplier register or tender result in a
   non-construction category (IT, office and medical supplies, catering,
   cleaning, training, events, consultancy, logistics) in the last 24
   months. Construction works, planning and engineering consultancy are
   excluded until 2026-11-25 (owner hold).
2. A live tender in the firm's category is open with at least 10 days to
   the closing date (from the tender-digest crawler), so the email can
   name it.
3. A sales, bid or owner contact with a published business address, or a
   role address (sales@, tenders@, info@) on the firm's site.
4. The firm is not on the tender-digest test's prospects.csv for the
   same calendar month; the two tests share one list.

Good sources: public award notices and supplier registers of GCC
government buyers, tender result pages, exhibitor lists, chamber member
directories.

Agents save the list as prospects.csv in this folder (company, category,
role, address, source URL, the tender named). Replies are saved in
replies/ with a first name and company type only.
