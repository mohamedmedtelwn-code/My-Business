# Scheduled tasks

## Cloud mode (active since 2026-10-25)

The studio runs in the cloud on the owner's Claude account. One permanent
**runner session** ("Venture Studio runner", created 2026-10-25 with the GitHub
repository `mohamedmedtelwn-code/My-Business` as its source and `main` as its
outcome branch, so it can push) receives every scheduled message; each message
is one team run. The laptop is not needed for the teams to run; it is needed
only for what the owner does (tickets). The schedule is Qatar time (UTC+3),
with a few minutes of jitter so no two tasks start together; a message that
arrives while a run is in progress waits for it, so runs never overlap.

| Task | Qatar time | Cron (stored) |
|------|------------|---------------|
| Research cycle | Mon and Thu 05:46 | `CRON_TZ=Asia/Qatar 46 5 * * 1,4` |
| Planning pass | daily 06:47 | `CRON_TZ=Asia/Qatar 47 6 * * *` |
| Preparation pass | daily 08:14 | `CRON_TZ=Asia/Qatar 14 8 * * *` |
| Work: <slug> | per plan, 09:00-12:00, one per hour | created when a business launches |
| Management nightly | daily 21:42 | `CRON_TZ=Asia/Qatar 42 21 * * *` |
| Management weekly | Fri 17:43 | `CRON_TZ=Asia/Qatar 43 17 * * 5` |

Runner session id and scheduled-task ids are in `management/cloud-ids.md`
(rewritten whenever they change; change a schedule or prompt with the
scheduled-tasks tools or the claude.ai routines page, never by recreating).

Why a runner session: a scheduled task that starts a fresh session each time
cannot push to GitHub (the first two test runs on 2026-10-25 were refused with
403: no repository source), so its work would be lost. A session created with
the repository as a source pushes fine (verified the same day). The runner's
git identity is "Venture Studio <studio@users.noreply.github.com>", no personal
data. A persistent-session task cannot carry the platform's push notification,
so each run sends one line through the PushNotification tool when tickets are
waiting or a run failed; the dashboard is the reliable place to look.

Cloud-mode rules that differ from the laptop mode below:
- Every run begins with `git pull --rebase origin main` in `/home/user/My-Business`
  (clone it there if missing) and ends with `git pull --rebase origin main &&
  git push origin main`. The run log and the research lists merge by union
  (`.gitattributes`). If a rebase conflict appears anywhere else, the run
  aborts the rebase, resets to `origin/main`, redoes its own work and pushes.
- Every run first applies the owner's answers from the dashboard cards (the
  "Owner answers" steps in `skills/management/DASHBOARD.md`).
- Team locks (`management/.lock-*`) live in the runner's container; the queue
  of messages keeps runs apart. The crash sweep and the circuit breaker work
  because `management/runs.jsonl` is committed.
- Each message is self-contained (the runner re-reads every file it needs; other
  runs change files between messages). The stored prompt text is the one below.
- Usage: all cloud runs draw on the owner's subscription. The cut order at the
  end of this file applies; the first lever is the Research cadence.

### Cloud prompt skeleton (the message every task sends to the runner)
```
Run: <team>. Treat this message as a fresh run: re-read every file you need.
Repository: /home/user/My-Business (if missing: git clone
https://github.com/mohamedmedtelwn-code/My-Business.git /home/user/My-Business).
cd into it; `git pull --rebase origin main` (on failure: git rebase --abort;
git fetch origin; git reset --hard origin/main); git identity "Venture Studio"
<studio@users.noreply.github.com>. Read CLAUDE.md and skills/<team>/SKILL.md.
Owner answers first (skills/management/DASHBOARD.md, "Owner answers": list the
replies collection with ArtifactData, run python tools/replies_apply.py ...,
send the delete batch). Then do exactly one run as the SKILL says, with
python tools/check.py and python tools/runlog.py at the start and the end
(runlog end with --commit). Finish with `git pull --rebase origin main && git
push origin main` (if rejected, wait 10 s and repeat once). If tickets are
waiting for the owner or the run failed, call PushNotification once with one
line under 200 characters. Do not ask questions: if something only the owner
can do blocks you, write a ticket in pipeline/30-tickets/open/ and end the run
with --outcome warn. Never open accounts, accept terms, enter credentials, send
messages on anyone's behalf, or move money. Stop after 60 minutes even if
unfinished, ending the run properly. Last line: "RUN <team> <outcome> push=<ok|failed>".
```

## Laptop mode (optional)

Create these in the Claude desktop app as scheduled tasks that **require this
computer** (they read and write `Documents\venture-studio`). The laptop must be
awake and the app open when a task is due: local tasks fire only then, and a
missed window gets exactly one catch-up run when the machine wakes
(code.claude.com/docs/en/desktop-scheduled-tasks, read 2026-10-25). Set
Windows power options to never sleep on AC and turn on "Keep computer awake"
in the Claude app settings.

Every prompt below is level-triggered: it processes what is in its folder, up
to a cap, and exits. Running it twice does no harm; the tools lock each team
and refuse a second concurrent run.

Before the first scheduled run, open Claude Code once in the folder, run each
prompt by hand with "Run now", and answer every permission prompt with
"always allow" for `python tools/*.py` and file edits inside the folder.
Unattended runs cannot answer prompts; a stalled run is skipped, not retried.

## Cadence (Phase 1)

| Task | Schedule (local time) | Why this slot |
|------|-----------------------|---------------|
| Research cycle | Mon and Thu 06:00 | before Planning; two cycles a week fill the funnel |
| Planning pass | daily 07:00 | after Research; closes validations due that day |
| Preparation pass | daily 07:30 | after Planning; picks up tickets the owner closed overnight |
| Work: <slug> | per plan, between 08:00 and 12:00, 30 minutes apart | one task per live business; never two at once |
| Management nightly | daily 22:00 | after all Work runs; refreshes the dashboard |
| Management weekly | Fri 18:00 | review, decisions, cull |

Stagger everything. All tasks draw on one subscription pool (5-hour and
weekly limits shared across Claude, Claude Code and the desktop app). Two
tasks in the same minute also make the desktop skip one of them.

## Prompts (paste as the task prompt, exactly)

### Research cycle
```
Read CLAUDE.md and skills/research/SKILL.md. Run one Research cycle: start with
python tools/check.py and python tools/runlog.py start --team research; write up to
10 idea briefs into pipeline/00-inbox following the category wheel (categories 4
and 10 always in the first two cycles; at least one owner-edge brief); every
earnings claim with URL and date; stop at 10 briefs or 60 minutes; end with
python tools/check.py and python tools/runlog.py end --id <RUN_ID> --outcome
ok|warn|bad --summary "<briefs written, categories>" --commit.
```

### Planning pass
```
Read CLAUDE.md and skills/planning/SKILL.md. Start with python tools/check.py and
python tools/runlog.py start --team planning. Gate and score at most 10 files from
pipeline/00-inbox with python tools/rubric.py and move each to approved/ or
rejected/. Write a validation brief for every approved idea. For every file in
pipeline/15-validating update the denominator and signals from the evidence
files, run python tools/signals.py <file> --write, and move PASSED to passed/
(then write the plan into pipeline/20-planned) and PARKED to parked/. End with
python tools/check.py and python tools/runlog.py end --id <RUN_ID> --outcome
ok|warn|bad --summary "<assessed, approved, rejected, validations closed>" --commit.
```

### Preparation pass
```
Read CLAUDE.md and skills/preparation/SKILL.md. Start with python tools/check.py
and python tools/runlog.py start --team preparation. Process every plan in
pipeline/20-planned and every ticket the owner closed: record approvals with
python tools/ledger.py release and spend with python tools/ledger.py add; raise
one ticket per owner decision (none if check.py says the open-ticket cap is
reached); launch a business only when its checklist is complete, check.py shows
room under the live cap, and no blocking ticket is open. End with python
tools/check.py and python tools/runlog.py end --id <RUN_ID> --outcome
ok|warn|bad --summary "<plans processed, tickets raised, launches>" --commit.
```

### Work task template (one per business; Preparation fills <slug>)
```
Read CLAUDE.md, skills/work/SKILL.md and businesses/<slug>/WORK.md. Start with
python tools/check.py; if it reports an ERROR for this business or a pause
warning, log one line and end the run with --outcome warn. Otherwise run python
tools/runlog.py start --team work --business <slug>, do the actions due today
from the plan within the time budget and outbound cap, record every USD with
python tools/ledger.py add --business <slug>, update metrics.md with sources,
append the logbook, write FLAG.md if a threshold is crossed, raise a ticket if
blocked. End with python tools/check.py and python tools/runlog.py end --id
<RUN_ID> --outcome ok|warn|bad --summary "<what shipped, metric deltas>" --commit.
```

### Management nightly
```
Read CLAUDE.md, skills/management/SKILL.md and skills/management/DASHBOARD.md.
Start with python tools/check.py and python tools/runlog.py start --team
management. Run python tools/ledger.py reconcile, python tools/ledger.py report
and python tools/runlog.py status; rebuild management/dashboard.md from them and
from every businesses/*/metrics.md and FLAG.md; list open tickets by age under
"Needs owner". Push the live dashboard: ArtifactData list per collection with
out_dir management/.dashboard-state, python tools/dashboard_push.py
--versions-dir management/.dashboard-state, then send each batch. End with
python tools/check.py and python tools/runlog.py end --id <RUN_ID> --outcome
ok|warn|bad --summary "<issues, pending decisions>" --commit.
```

### Management weekly
```
Read CLAUDE.md and skills/management/SKILL.md. Start with python tools/check.py
and python tools/runlog.py start --team management. Write
management/reviews/<YYYY-WW>.md from templates/weekly-review.md using python
tools/ledger.py report, python tools/runlog.py status and every business
folder; apply the stop / pause / cull / scale / hold rules; append each
recommendation to management/decisions.md as pending-owner; write three lessons
to research/feedback.md; then run the nightly dashboard steps. End with python
tools/check.py and python tools/runlog.py end --id <RUN_ID> --outcome
ok|warn|bad --summary "<decisions proposed>" --commit.
```

## Usage-limit guidance

Facts (support.claude.com and code.claude.com, read 2026-10-25): Pro and Max
plans have a rolling 5-hour session limit and a weekly limit, shared across
every Claude surface on the account; the Claude Code 5-hour allowance for Pro
and Max was doubled on 6 May 2026; exact numbers are not published; optional
usage credits can continue work past a limit at API rates with a monthly cap.
A run that hits a limit stops; the desktop app shows it as a failed or skipped
run. `runlog.py` records the outcome `limit` for such runs and three in a row
open the team's circuit breaker.

Signs you are hitting limits: runs ending with "session limit" or "weekly
limit" messages, Management reporting crashed runs, breakers opening, the
dashboard going stale.

What to cut, in this order, until runs stop failing:
1. Lower model effort and thinking for Research and Planning (they read the
   most); keep Work and Management unchanged.
2. Trim context: each SKILL already names the only files to read; make sure
   CLAUDE.md stays under 200 lines and no team reads whole folders.
3. Research from two cycles a week to one; Planning cap from 10 briefs a run to 5.
4. Pause the lowest-ranked live Work tasks first (Management's monthly ranking
   tells you which); keep Management nightly running so you still see the
   state.
5. Phase 1 live cap from 8 to 4 while on a Pro plan (edit `phase1_live_cap` in
   `management/config.json`); 8 assumes a Max plan.
6. Enable usage credits with a spend cap only if you decide the studio has
   earned it (that is a ceiling decision; write it in `management/decisions.md`).

Never cut: `check.py` and `runlog.py` at the start and end of a run, or the
ledger commands. They are cheap and they are the audit trail.

## When a run fails
- `runlog.py start` refused (lock): another run of that team is in progress or
  died less than 3 hours ago. Wait for the next slot.
- `runlog.py start` refused (circuit breaker): three failures in a row. Read
  `management/runs.jsonl` for the last summaries, fix the cause, then
  `python tools/runlog.py reset --team <team>`.
- `check.py` ERROR: the folder is in a forbidden state; the message says which
  file and what to do. Fix the file, run check.py again, then the team can run.
- A Work run says "paused": a ticket for that business has been open more than
  7 days. Act on the ticket; the next run resumes by itself.
