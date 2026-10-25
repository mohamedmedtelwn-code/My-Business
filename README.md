# Venture Studio — Owner Guide

An always-on Claude agent on a dedicated Windows laptop that researches,
plans, validates, prepares, executes and reports on small businesses. You
approve tickets, open accounts, and sign decisions; the teams do the rest.
Everything the teams know is in this folder. The rules are in `CLAUDE.md`;
the evidence behind them is in `research/STUDIO-RESEARCH.md`.

## 0. How it runs today

Since 2026-10-25 the studio runs in **cloud mode**: scheduled tasks on your
Claude account start a fresh cloud session for each team run, clone this
repository, do the run, and push the result back (see `SCHEDULE.md`, "Cloud
mode"). Nothing has to be installed on a laptop for the teams to run. You
need a laptop or phone only to read the dashboard and act on tickets.

- Live dashboard: the URL in `management/dashboard-url.txt` (your private
  artifact). The "Your queue" panel lists every ticket with its steps.
- Tickets: `pipeline/30-tickets/open/` in this repository. Edit the file on
  GitHub or on a laptop clone, write `APPROVED`, `REJECTED` or `DONE` with the
  date at the bottom, move it to `closed/`, commit. The next run picks it up.
- Validation evidence (replies, screenshots, sign-up counts) goes into
  `pipeline/15-validating/output/<id>/` the same way.

The laptop setup below is optional: use it if you prefer local scheduled
tasks in the Claude desktop app, or want a local clone to edit tickets.

## 1. Laptop setup (optional, about an hour)

1. Create a fresh Windows user account for the studio. Auto-login, never
   lock, never sleep on AC power (Settings > System > Power).
2. Install **Python 3.11 or newer** from python.org. Tick "Add python.exe to
   PATH". Verify in a terminal: `python --version`. The tools use only the
   standard library; nothing else to install.
3. Install **Git for Windows** (git-scm.com). Verify: `git --version`.
4. Install the **Claude desktop app**, sign in with your subscription, set it
   to start with Windows. In its settings turn on "Keep computer awake".
5. Install **Claude Code** (needs Node.js). Verify: `claude --version`.
6. Get this folder onto the laptop as `Documents\venture-studio`:
   `git clone https://github.com/mohamedmedtelwn-code/My-Business.git Documents\venture-studio`
   (or unzip the folder there and run `git init` inside it).
7. In the Claude desktop app, connect the folder `Documents\venture-studio`.
8. Windows Update: set active hours so it never reboots mid-task.
9. Recommended: a separate email address and browser profile used only for
   studio businesses.

## 2. First cycle (manual, together, about two hours)

1. Open `OWNER-EDGE.md` and correct it. It is the only file about you the
   teams read; it holds skills and markets, no personal data.
2. `management/config.json` already has `"studio_start": "2026-10-25"`, the
   day the studio was handed over, so Phase 1 runs to 2027-01-23. If you begin
   later, change it to your real first-run date. Leave the other numbers
   unless you have read the rubric and the research.
3. Open a terminal in `Documents\venture-studio` and run the self-checks:
   ```
   python -m unittest discover -s tests
   python tests\dry_run.py
   python tools\check.py
   python tools\ledger.py init
   ```
   The first walks three fake ideas through the whole pipeline in a scratch
   folder and must end with `DRY RUN PASSED`. The checker must say
   `CHECK OK`. The ledger command creates `management\ledger.sqlite`.
4. Read `management/payments.md`. Two tickets will ask you to (a) confirm the
   legal basis for receiving income in Qatar and (b) set up Gumroad. Nothing
   sells until the Gumroad payout is verified; the teams can still research,
   validate and build in the meantime.
5. Open Claude Code in the folder and run the Research prompt from
   `SCHEDULE.md` by hand ("Run now" in the desktop app, or paste it). Answer
   every permission prompt with "always allow" for the Python tools and file
   edits inside the folder; unattended runs cannot answer prompts.
6. Run the Planning prompt. Review the scores with Claude in chat. Tune
   `rubric_weights` in `management/config.json` and the matching table in
   `templates/scoring-rubric.md` until the ranking matches your judgement;
   write the change in the rubric's log. Only then automate.
7. Create the scheduled tasks exactly as written in `SCHEDULE.md`.

## 3. Your daily five minutes

- Open `management/dashboard.md` (or the live dashboard at the URL in
  `management/dashboard-url.txt`). Red means act today.
- Open `pipeline/30-tickets/open/`. Each ticket is one page: what, why, cost,
  exact steps. Do the steps, write `APPROVED`, `REJECTED` or `DONE` with the
  date at the bottom, and move the file to `closed/`. That is the whole
  approval process. A ticket older than 3 days shows on the dashboard; older
  than 7 days pauses that business.
- Once a week, read `management/reviews/` and sign the decisions in
  `management/decisions.md` (`signed-stop`, `signed-hold`, `signed-scale`,
  `signed-pause`).

## 4. Money

Nothing is deposited. USD 1,000 is a ceiling you release only when a ticket
earns it; every spend, however small, is a ticket you pay yourself at that
moment. Revenue goes into a reinvestment pool that is spent before any ceiling
money. The ledger is a database the tools keep (`management/ledger.sqlite`,
readable view `management/ledger.md`); it refuses any spend without a released
ticket or from an empty pool. Check it any time with
`python tools\ledger.py report`.

## 5. What the agents never do

Open accounts, accept terms, type passwords or card numbers, pass identity
checks, move money, sign anything, use personal information about you, run
two accounts on one platform, send more than 20 cold messages a day per
business, or run anything illegal or against platform rules. If a step needs
one of these, you get a ticket.

## 6. Honest expectations (from the research pass, October 2026)

- Most small operators earn about USD 0 at month 6 on YouTube, TikTok and
  podcasts; under USD 50 a month on apps; about USD 145 a month in indie
  SaaS; 44% of engaged indie authors earn USD 100 or less. The studio's
  fastest route to a first dollar is a service or product sold directly to
  named buyers, which is why outreach is the default validation test.
- Etsy, TikTok Creator Rewards and Amazon Associates (US) are not usable from
  Qatar. Gumroad, PayPal via QNB, Lemon Squeezy and Google Play are.
- Phase 1 (90 days) is deliberately wide: up to 20 briefs a week, several
  validations in parallel, up to 8 businesses live. Expect 8-15 tickets a
  week, mostly accounts and publishes. Most ideas get rejected at Planning or
  parked at validation. That is the system working.
- Runs happen when scheduled, not in a loop. "Always on" means a few runs a
  day, within your subscription's limits (see `SCHEDULE.md` for what to cut
  first if runs start failing).
- Losses stay small because every USD is in the ledger, every run is logged,
  and the weekly review stops what does not work.

## 7. When something looks wrong

```
python tools\check.py          what state the folder is in and what to fix
python tools\runlog.py status  last run per team, failures, circuit breakers
python tools\ledger.py report  ceiling, released, spent, revenue, pool
python tools\ledger.py reconcile
git log --oneline              every run commits its changes
```
A team whose last three runs failed stops until you run
`python tools\runlog.py reset --team <team>`. `CHANGELOG.md` lists the five
decisions you should review before the first automated cycle.
