# Reliable agent pipelines on one laptop (checked 2026-10-25)

Scope: file-based multi-agent pipeline, one Windows laptop, Claude Code + Claude desktop scheduled tasks, Pro/Max subscription, no API keys, Python 3.11+ stdlib only.

Source quality note: Anthropic/Claude domains (code.claude.com, support.claude.com, anthropic.com) were fetched directly this session. Third-party domains (docs.python.org, learn.microsoft.com, camel.apache.org, martinfowler.com, git-scm.com, conventionalcommits.org, jsonlines.org, community blogs) did NOT resolve for fetch (DNS error), and the web search budget ran out mid-task. Python/Microsoft/community facts therefore come from search-result excerpts only (marked "search excerpt"). Items marked [design] are my synthesis, not sourced.

## Recommendations table

| # | Practice | Why | How on Windows + Python stdlib | Source |
|---|---|---|---|---|
| 1 | One owner per folder (single-writer rule): each team writes only its own stage folders; others read only | Atomic replace stops torn files but not lost updates; separate dirs stop agents overwriting each other | Folder map in a tiny `OWNERS.md`; scripts refuse writes outside the team's folders [design] | [4], [20] |
| 2 | Publish files atomically: write temp file in the SAME directory, flush+fsync, then `os.replace` | Readers see old or new file, never half-written; temp on another volume becomes copy+delete (not atomic) | `tempfile.mkstemp(dir=target_dir)`; `os.replace`; retry 3-5x with short sleep on `PermissionError` (AV/indexer/open handle); skip dir-fsync on Windows | [6], [7], [8] |
| 3 | Claim work by atomic move into `in-progress/<run_id>/` | Exactly one runner owns a file; crash leaves evidence | On Windows `os.rename` raises `FileExistsError` if dest exists, `os.replace` overwrites silently: use `rename` for claims, `replace` for publish | [6] (search excerpt), [design] |
| 4 | Run lock via `os.open(path, O_CREAT\|O_EXCL\|O_WRONLY)` holding JSON (run_id, team, pid, started_at, heartbeat) | Prevents two sessions of the same team overlapping; Desktop may skip/overlap runs | Stale if heartbeat older than 2x max run time AND owner not alive. Do NOT probe pid with `os.kill(pid, 0)` on Windows (it terminates the process); use `ctypes` OpenProcess/GetExitCodeProcess or just age | [design]; Python os.kill Windows caveat from memory, UNVERIFIED this session |
| 5 | `msvcrt.locking` only for short critical sections (append to JSONL, update index) | Byte-range, advisory-ish; `LK_LOCK` retries 10x at 1 s then `OSError` | Open file, `msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)` in your own retry loop with jitter; unlock in `finally` | [5] (search excerpt) |
| 6 | Level-triggered jobs: "process whatever is in inbox" not "process today's item" | Desktop gives ONE catch-up run after a missed window (7-day lookback), older misses discarded | Each run scans its input folder, does bounded N files, exits | [1] |
| 7 | Done-markers + content hash: `<file>.done.json` with sha256 of input and output, run_id | Re-run becomes no-op if input hash unchanged; Anthropic's cron-guide advice: sentinel files / exit conditions | `hashlib.sha256`; write marker AFTER output is published (marker last) | [18] (secondary), [design] |
| 8 | Let deterministic scripts do state changes; the agent calls `pipeline.py begin/claim/finish/fail` | CLAUDE.md text is advisory, hooks/scripts are deterministic; poka-yoke: make mistakes hard | Small `pipeline.py` CLI with `argparse`; agent prompt says "never move files by hand" | [3], [9] |
| 9 | JSONL run log, append-only: `start` event then `end` event per run | Crash = start without end; one line per event survives partial failure | Fields: run_id, team, event, ts_utc, host, model, files_in, files_out, outcome, attempts, error, tokens/cost if known, prompt_version | [design]; claude -p JSON has session_id/total_cost_usd [10] |
| 10 | Crash sweep at start of every run: find `start` without `end` older than max runtime, mark `crashed`, move claimed files back to inbox (attempt+1) or to `dead-letter/` | Desktop run can die (sleep, app close, usage limit) leaving work half-claimed | Sweep reads last N lines of JSONL; do it before taking new work | [1], [design] |
| 11 | Retry budget per file: 2-3 attempts with growing delay (next scheduled run counts as the backoff), then `dead-letter/` + ticket in `needs-owner/` | Claude Code already retries transient API errors 10x with exponential backoff; do not stack more loops in the agent | Attempt counter in sidecar JSON; no in-agent retry loops | [11], [3] |
| 12 | Circuit breaker per team: after K (e.g. 3) consecutive failed runs write `state/circuit-<team>.json` open; runs exit immediately until owner or cooldown clears it | Stops burning scarce subscription usage on a broken stage | First action of every run: read breaker; close on first success after cooldown (half-open) | [design]; generic pattern in vendor sources [19] (low confidence) |
| 13 | Hard caps in the prompt AND mechanically: max files/run, max wall time, `--max-turns`/`max_turns` if using `claude -p`, Stop-hook loops auto-capped at 8 | "Include stopping conditions such as a max number of iterations" (Anthropic); SDK has no session timeout | Prompt: "process at most 5 files then stop"; checker script refuses 6th claim | [3], [12], [13] |
| 14 | Deterministic verification gate before a file advances a stage (schema/front-matter/required sections/links) | "Give Claude a way to verify its work"; agents declare victory early (Anthropic harness article) | `validate.py` returns exit code; failing file goes to `rework/` with reason | [9], [14] |
| 15 | Pre-approve tools and deny the rest in unattended runs | Manual mode stalls until you answer a prompt; `dontAsk` denies instead of waiting | Run "Run now" once, "always allow" each prompt; or allow rules in settings; consider `--permission-prompts none` for `claude -p` | [1], [10] |
| 16 | Keep context small: CLAUDE.md < 200 lines, per-team prompt, read index files not whole folders, `/clear` between tasks, one task type per session | Subscription usage scales with context; each request resends the conversation | Per-team `INDEX.md` listing path+1-line summary+hash; skills for rarely used rules | [15], [9] |
| 17 | Stagger the five teams; avoid overlapping runs | Shared 5-hour and weekly pool across all surfaces; Desktop skips runs if another task is running | Different offsets; Desktop adds a deterministic delay of a few minutes anyway | [1], [16] |
| 18 | Git as audit log: init repo in the pipeline root; the wrapper script (not the agent) commits once per run after `finish` | Diffable history, revert path; Anthropic harness: commit per session with descriptive message | Message: `run(<team>): <run_id> <outcome> in=N out=M`; `.gitignore` locks/tmp; pre-commit runs `validate.py`; never skip hooks | [14], [9]; conventions [design] |
| 19 | Owner dashboard from JSONL: generated `STATUS.md`, one row per team, RED/AMBER/GREEN, plus `needs-owner/` queue | Desktop "Succeeded" only means session ended OK, not that the work was done | `status.py` reads last events; green = last run ok and recent; amber = late or retries; red = crashed/breaker open/dead-letter non-empty | [17], [design] |
| 20 | Keep laptop awake and Desktop open during windows | Local scheduled tasks only fire while app open AND computer awake; lid close sleeps | Settings > This computer > System > Keep computer awake; Windows power plan "never sleep on AC" | [1] |

## Detail per topic

### 1. Idempotent runs
- Reruns of the same prompt do NOT give the same actions; defuse by stating an exit condition in the prompt, a sentinel file with timestamp after each successful run, or tracking state externally (search excerpt of a cron guide) [18].
- Anthropic harness pattern (Nov 26, 2025): progress file read at session start, JSON feature list (JSON chosen because models overwrite it less than Markdown), one item at a time, commit and update progress at end of every session, quick sanity check at start of next [14]. Direct fit for stage folders + done-markers.
- Atomic write: temp file in same directory, flush+fsync, `os.replace`. Windows: dir fsync unavailable, `os.replace` can fail with `PermissionError` if another process (AV, indexer) holds the file, so retry; atomic replace prevents torn files but NOT lost updates (search excerpts) [7]. Python docs: `os.replace` silently replaces an existing file; `os.rename` raises `FileExistsError` on Windows if dest exists; success implies atomic rename; may fail across filesystems (search excerpt) [6].
- Microsoft docs (search excerpt): MoveFileEx WRITE_THROUGH only affects copy+delete moves; cross-volume moves are copy+delete (non-atomic); docs do not promise atomic same-volume rename; keep temp on same volume [8].
- Content hashes: [design] use sha256 of input in the done-marker; marker written last.

### 2. File locks, single-writer, hot folders
- `msvcrt.locking`: `LK_LOCK`/`LK_RLCK` retry after 1 s, up to 10 attempts then `OSError`; `LK_NBLCK`/`LK_NBRLCK` single attempt; locks bytes from current file position; regions cannot overlap and must be unlocked individually (search excerpt of docs.python.org, Python 3.15 docs) [5].
- Lock file with `O_EXCL`: standard create-if-absent; [design] store JSON owner info and heartbeat; stale timeout > longest legitimate run. Windows pitfall: `os.kill(pid, 0)` terminates the process on Windows (from memory of Python docs, UNVERIFIED this session).
- Watch/hot folder lessons (search excerpts, 2026 .NET guide and forum threads) [21]: producer writes `name.tmp` then renames to final name on same volume = only race-free pattern; if producer is not under your control: poll size+mtime until stable, then try exclusive open; stable-but-incomplete happens if writer crashed, so use a trailer/checksum; watchers that only listen for "modified" miss save-via-rename, handle create+move events. For this pipeline you control all producers, so use temp+rename plus claim-by-move.
- Anthropic: in a multi-agent setup "give each agent its own working directory so they do not overwrite each other's files" [20]; parallel sessions can use worktrees [9] (not suited to a shared-state pipeline folder).

### 3. Run logs and crash detection
- `claude -p --output-format json` returns session_id, result, and `total_cost_usd` plus per-model breakdown; `stream-json` ends with a `result` message including cost; exit code 0 on success, non-zero on failure; SIGTERM gives exit 143 and no result recorded for the in-progress turn; `system/api_retry` events carry attempt, max_retries, retry_delay_ms, error category (`rate_limit`, `overloaded`, ...) [10]. Cost figures are client-side estimates.
- Desktop scheduled-task sessions do not hand you that JSON; log from inside the run via `pipeline.py` and treat cost/tokens as optional ("unknown") [design]. `/usage` and Settings > Usage show plan consumption [15][16].
- OpenTelemetry export exists (`CLAUDE_CODE_ENABLE_TELEMETRY=1`, console exporter, `api_request` events with `cost_usd`, `session.id`) [22]; page does not say whether it works for Pro/Max logins: UNVERIFIED. Not needed for stdlib-only design.
- Session transcripts are JSONL on local disk under `~/.claude/projects/` [20]; could be mined for tokens but field names not verified.
- JSONL schema [design]: `{"run_id","team","event":"start|end|heartbeat|claim|fail","ts","outcome":"ok|partial|fail|skipped|crashed","files_in":[],"files_out":[],"attempt","error","model","tokens","cost_usd"}`.
- Crashed run = `start` without `end` after max runtime. Desktop itself shows skipped runs with reasons (asleep, previous run in progress, other scheduled tasks running) [1].

### 4. Failure handling and guardrails
- Anthropic "Building effective agents" (Dec 19, 2024): simplest solution first; stopping conditions such as max iterations; pause for human feedback at checkpoints/blockers; test in sandboxes; ground truth from environment each step; poka-yoke tool design [3].
- Claude Code best practices: give a verifiable check; Stop hook can gate completion; `/clear` after two failed corrections; failure patterns: kitchen-sink session, over-long CLAUDE.md, trust-then-verify gap, infinite exploration [9].
- Auto-retry: Claude Code retries transient failures up to 10 times with exponential backoff (`CLAUDE_CODE_MAX_RETRIES`); `CLAUDE_CODE_RETRY_WATCHDOG=1` retries 429/529 indefinitely in unattended runs but spend-limit 429s fail at once [11].
- Stop-hook loop protection: `stop_hook_active` input and an 8-consecutive-continuation cap [13].
- Auto mode: 3 consecutive or 20 total blocks pause auto mode; in `-p` runs the action simply doesn't run and the run continues [23].
- Agent SDK: no top-level session timeout, set `max_turns`; hitting it returns `error_max_turns` [12].
- Vendor guardrail articles (low confidence, search excerpt): layered caps (token budgets, concurrency, recursion depth, bounded retries with jitter), breaker that keeps session state for review, enforcement outside agent logic [19].

### 5. Cost and usage control: see next section.

### 6. Git as audit log
- Sourced: commit per session with descriptive message lets agent revert (Anthropic harness) [14]; Claude Code checkpoints do NOT track Bash/external changes and are "not a replacement for git" [9]; Desktop local tasks can run in an isolated worktree if folder is a git repo (off by default) [1].
- Not sourced this session (third-party docs unreachable): Conventional Commits format, git pre-commit semantics. [design] one commit per run by wrapper script; message `run(team): run_id outcome in=N out=M`; pre-commit runs `validate.py`.

### 7. Observability for a non-engineer
- Not sourced beyond Anthropic UI facts: Desktop task detail shows History incl. skipped runs and reasons; "Succeeded" only means session ended without failure, open transcript to see whether work completed [1][24]; OS notification when a Code session finishes and you aren't viewing it [25].
- [design] `STATUS.md` rebuilt by `status.py` after every run: table team | last run | outcome | files waiting | RAG. `needs-owner/` = one Markdown ticket per blocked item with: what happened, what is needed, how to resume. Dead-letter non-empty = RED.

## Claude subscription limits and scheduled-task behaviour (with page dates)

Most support/docs pages show no absolute date ("Updated over a week ago"); all fetched 2026-10-25.

Limits
- Pro and Max both have a 5-hour session limit (resets every five hours) and a weekly limit across all models; weekly resets at a fixed per-account time shown in Settings > Usage [16][26][27]. Support pages "Updated over a week ago", no absolute date.
- Usage is shared across claude.ai, Claude Code and Claude Desktop [16]. Cowork inclusion for Pro/Max not stated on that page (UNVERIFIED); for Team/Enterprise the Claude Code costs page says the seat allowance is shared with chat and Cowork [15].
- Max 5x = $100/mo, Max 20x = $200/mo; Max gives 5x/20x Pro's per-session allowance [26]. Pro $20/mo ($17/mo annual, $200 upfront) [28]. No numeric message/token allowances published (page undated).
- May 6, 2026: Anthropic doubled Claude Code 5-hour limits for Pro, Max, Team, seat-based Enterprise and removed the peak-hours reduction for Pro/Max; weekly limits not mentioned [29].
- Conflict: Claude Code Pro/Max page [30] and usage-credits page [31] mention a separate weekly limit for "Fable" on Max; the Max plan page [26] says weekly limit applies across all models and lists no model-specific limit. Unresolved.
- Heavy bursts can exhaust the weekly allowance before the session window resets; error text examples: "You've hit your session limit", "weekly limit"; Opus/Sonnet family limits exist separately [32].
- Wrap-up allowance (rolling out gradually): Claude Code may finish the current step after hitting the 5-hour limit; Pro once per weekly period, Max each 5-hour limit [30].
- Usage credits (opt-in; pay-as-you-go at API rates; monthly spend cap) continue work after limits [31]. Without them, runs are rejected until the window resets [24].
- If `ANTHROPIC_API_KEY` is set Claude Code bills the API instead of the subscription [30]; `claude --bare` does not use subscription login [10]; `/schedule` cloud tasks require claude.ai login [24].
- Auto-continue at usage limit: interactive subscription sessions wait and continue after reset (v2.1.234+); Desktop Code tab has an "Auto-continue when limits reset" checkbox on the session-limit card [32][33]. For `claude -p`: retry watchdog env vars [11].
- Usage-saving guidance: CLAUDE.md under 200 lines, `/clear` between tasks, `/compact <focus>`, Sonnet by default, Haiku for simple subagents, lower effort/thinking for simple tasks, prefer CLI tools over MCP, preprocess with hooks, agent teams ~7x tokens, long sessions resend full context, first message after cache expiry reprocesses everything [15]. Usage-limit best-practices page dated Sept 22, 2026: batch requests, cached project files cost less, caches expire after inactivity [34].
- `/usage` shows plan bars and attribution to skills/subagents/plugins/MCP servers plus recommendations (since week of May 18-22, 2026) [15][35].
- What to cut first when limits hit [design, grounded in 15]: (1) lower effort/thinking and use Sonnet/Haiku, (2) trim context (CLAUDE.md, index files), (3) reduce frequency of research/preparation runs, (4) pause breadth work, keep work-stage and management/status runs, (5) enable usage credits with spend cap only if owner agrees.

Desktop local scheduled tasks (code.claude.com page, undated, needs Desktop 1.1.5368+) [1]
- Fire only while the app is open and computer awake; asleep = run skipped; Keep computer awake in Settings > This computer > System; closing laptop lid still sleeps.
- Missed runs: on wake/app start checks last 7 days, starts exactly ONE catch-up run for most recently missed time, discards older; notification shown when catch-up starts. A 9am task may run at 11pm.
- Checks schedule every minute; each task gets a deterministic start delay of a few minutes. Form minimum interval 1 hour (Hourly/Daily/Weekdays/Weekly/Manual/Custom cron in local time); Claude itself can set shorter.
- History shows skipped runs and why: computer asleep, previous run still in progress, or other scheduled tasks already running.
- Manual permission mode stalls until approved; run "Run now" once and "always allow"; allow rules in `~/.claude/settings.json` apply. Prompt lives at `~/.claude/scheduled-tasks/<task-name>/SKILL.md`, changes apply next run. Optional Worktree isolation if folder is a git repo. Each run is a fresh session.
- Session-scoped `/loop` tasks expire after 7 days and stop when the session closes [36]; not suitable for the pipeline.

Cowork scheduled tasks (support article "Schedule recurring tasks in Cowork", "Updated yesterday", fetched 2026-10-25) [2]
- Says runs happen remotely and fire even when computer asleep or Desktop closed; tasks that need local files/apps "will only run locally"; Pro/Max tasks created before Oct 6 that run on the computer keep running there. Missed-run behaviour and notifications are not documented on that page.
- Earlier search-excerpt summary claimed "only run while computer awake and app open; skipped then run on wake with notification": conflicts with the current article text; treat as an older version. For a local-folder pipeline assume the local Desktop rules above apply.
- Cloud tasks (routines) get a fresh clone, no local files; run on subscription usage; 100 scheduled runs/hour per account cap [24].

## Lessons from people running scheduled Claude Code / agent pipelines

All from search excerpts or Anthropic pages; no first-hand postmortems found (confidence low-medium).
- Re-runs duplicate work (second refactor, duplicate PR); fix with exit condition in prompt, sentinel file, external state [18].
- Caps: example crontabs use `--max-turns 10 --max-budget-usd 0.50 --output-format json`; headless needs `--allowedTools` with narrow `Bash(...)` patterns because nobody can approve [18].
- Cron + headless is fine to ~3 concurrent jobs (one guide) [18]; public-repo scheduled GitHub workflows auto-disable after 60 days of repo inactivity [18].
- GitHub Actions guides: check for existing open PR before nightly run, concurrency group, opt-in variable guard, `--max-turns` 5-15 [37].
- Obsidian: a community read-only "vault health check" routine runs headless, never granted Edit/mv, rm denied by Claude Code permissions; writes one report note: keep scheduled write access narrow [38].
- Anthropic's long-running harness: failures were declaring victory early, trying everything at once, leaving broken state, marking done without end-to-end testing; fixes were a JSON feature list, one feature per session, commit+progress note, start-of-session sanity check [14].
- Routines docs: run "outcomes" describe how the session ended, not whether the prompt's work was done: build your own outcome field [24].

## Claim ledger

| claim | URL | source type | date | confidence | corroborated by |
|---|---|---|---|---|---|
| Pro/Max have 5-hour session + weekly limit, shared across Claude, Claude Code, Desktop | https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work | primary | undated (fetched 2026-10-25) | H | [30], [26] |
| Weekly limit resets at fixed per-account time | https://support.claude.com/en/articles/8325606-what-is-the-pro-plan | primary | undated | H | [26] |
| Max 5x $100, 20x $200 | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | primary | undated | H | https://claude.com/pricing ("From $100") |
| Pro $20 monthly / $17 annual | https://claude.com/pricing | primary | undated | M | [Pro plan page: $20] |
| Claude Code 5-hour limits doubled; peak reduction removed (Pro/Max/Team/Ent) | https://www.anthropic.com/news/higher-limits-spacex | primary | 2026-05-06 | H | search summary |
| Max has separate weekly limit for Fable | https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan | primary | undated | M (conflicts with Max page) | usage credits page |
| Wrap-up allowance: Pro once/week, Max each 5h limit; gradual rollout | https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan | primary | undated | M | search summary |
| Usage credits opt-in, API-rate billing, spend cap | https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans | primary | undated ("over 2 weeks ago") | H | costs doc |
| ANTHROPIC_API_KEY set => API billing instead of subscription | https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan | primary | undated | H | routines doc troubleshooting |
| Desktop local tasks need app open + computer awake; skipped if asleep | https://code.claude.com/docs/en/desktop-scheduled-tasks | primary | undated | H | search summary |
| One catch-up run, 7-day lookback, notification | https://code.claude.com/docs/en/desktop-scheduled-tasks | primary | undated | H | search summary |
| Skip reasons: asleep, previous run in progress, other tasks running | https://code.claude.com/docs/en/desktop-scheduled-tasks | primary | undated | H | none |
| Cowork article: runs remote; local-file tasks only run locally; pre-Oct-6 local tasks keep running | https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork | primary | "Updated yesterday" (2026-10-24) | H | second fetch of same article |
| Cloud routines: 100 scheduled runs/hour/account; use subscription usage | https://code.claude.com/docs/en/routines | primary | undated | H | none |
| Claude Code retries 10x exponential backoff; watchdog env vars | https://code.claude.com/docs/en/errors | primary | undated | H | headless doc (api_retry) |
| Session/weekly limits shared across models; Opus/Sonnet family limits separate | https://code.claude.com/docs/en/errors | primary | undated | H | costs doc |
| Auto-continue after usage limit (v2.1.234+) | https://code.claude.com/docs/en/interactive-mode | primary | undated | H | errors doc |
| CLAUDE.md under 200 lines; /clear; /compact; model choice | https://code.claude.com/docs/en/costs | primary | undated | H | best-practices doc |
| claude -p json has total_cost_usd, session_id; exit codes; SIGTERM 143 | https://code.claude.com/docs/en/headless | primary | undated | H | costs doc |
| Stop hook 8-consecutive-continuation cap | https://code.claude.com/docs/en/hooks | primary | undated | H | none |
| Auto mode block thresholds 3/20; -p doesn't stop | https://code.claude.com/docs/en/permission-modes | primary | undated | H | best-practices doc |
| Agent SDK: no session timeout; set max_turns; error_max_turns | https://code.claude.com/docs/en/agent-sdk/hosting | primary | undated | H | none |
| Building effective agents: simplicity, stopping conditions, checkpoints | https://www.anthropic.com/research/building-effective-agents | primary | 2024-12-19 | H | secondary summaries in search |
| Harness: progress file, JSON feature list, commit per session | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | primary (fetched directly; URL not in search results) | 2025-11-26 | H | none |
| os.replace overwrites silently; os.rename FileExistsError on Windows; atomic if successful | https://docs.python.org/3/library/os.html | primary (search excerpt only; fetch failed) | n/a | M | python.org discussion links in search |
| msvcrt.locking LK_LOCK 10 retries/1 s; LK_NBLCK single attempt | https://docs.python.org/3/library/msvcrt.html | primary (search excerpt only) | n/a | M | none |
| MoveFileEx WRITE_THROUGH only for copy+delete; cross-volume not atomic | https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefileexa | primary (search excerpt only) | n/a | M | MS Learn archive thread |
| Atomic write pattern; PermissionError retry; atomic replace != lost-update safety | https://discuss.python.org/t/adding-atomicwrite-in-stdlib/11899 | community (search excerpt) | n/a | M | https://pypi.org/project/safewrite/ |
| Watch folders: temp name + rename is only race-free; stable-size + exclusive open fallback | https://startdebugging.net/2026/04/how-to-detect-when-a-file-finishes-being-written-to-in-dotnet/ | blog (search excerpt) | 2026-04 | M | https://community.ibm.com/community/user/discussion/how-to-avoid-webmethods-scheduler-from-picking-partially-copied-file |
| Cron re-runs not idempotent; sentinel file; --max-turns/--max-budget-usd | https://backgroundclaude.com/scheduled | blog (search excerpt) | n/a | L-M | https://codingwithroby.substack.com/p/claude-code-can-maintain-your-repo |
| Runaway-agent layered caps; breaker preserves state | https://www.getmacha.com/blog/guardrails-autonomous-agents-debounce-caps-auto-disable-loop | vendor blog (search excerpt) | n/a | L | https://www.gravitee.io/ results (Gravitee corpus) |
| Read-only Obsidian routine; Edit/mv not granted, rm denied | https://forum.obsidian.md/t/vault-health-check-a-read-only-claude-code-routine-that-audits-your-vault-free-mit/117831 | forum (search excerpt) | n/a | L-M | none |
| OTel env vars and events for Claude Code | https://code.claude.com/docs/en/monitoring-usage | primary | undated | H | hosting doc |

## Unverified / gaps
- Exact numeric usage allowances (messages/tokens per 5-hour window or week) for Pro/Max: not published on any fetched page; UNVERIFIED.
- Date weekly limits were introduced in 2025: no fetched page states it. From memory (announced July 2025, effective late Aug 2025): UNVERIFIED.
- Whether Cowork scheduled runs share the same Pro/Max pool: not stated on fetched Pro/Max pages (Team/Enterprise docs say yes). Treat as shared.
- Cowork local-run behaviour on sleep/missed runs: Cowork article silent; Desktop (Code tab) page documents it. Unclear if Cowork-created local tasks follow identical rules.
- Fable weekly limit on Max: pages conflict.
- Which weekday/time the weekly reset falls on: per-account, visible in Settings > Usage; error example shows "resets Mon 12:00am" but that is only an example.
- Whether OpenTelemetry works with Pro/Max logins; token fields inside local transcript JSONL.
- Python `os.kill(pid, 0)` termination on Windows, `O_EXCL` semantics on Windows: from memory, not re-fetched.
- Conventional Commits, git pre-commit specifics, JSONL spec, circuit-breaker canonical sources, Camel/NiFi hot-folder docs: third-party sites unreachable; recommendations marked [design].
- Whether Desktop limits concurrent scheduled tasks (skip reason implies it); exact limit unknown.
- No first-hand postmortems of scheduled Claude Code failures found; lessons are tutorial-grade.
- Web search budget was exhausted mid-task; the dead-letter-queue, Obsidian+Claude pipelines, and "what broke" searches had one pass each.

## Sources
1. https://code.claude.com/docs/en/desktop-scheduled-tasks
2. https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork
3. https://www.anthropic.com/research/building-effective-agents
4. https://code.claude.com/docs/en/agent-sdk/hosting (multi-agent container: own working directory)
5. https://docs.python.org/3/library/msvcrt.html (search excerpt)
6. https://docs.python.org/3/library/os.html (search excerpt)
7. https://discuss.python.org/t/adding-atomicwrite-in-stdlib/11899 and https://pypi.org/project/safewrite/ (search excerpts)
8. https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefileexa (search excerpt)
9. https://code.claude.com/docs/en/best-practices
10. https://code.claude.com/docs/en/headless
11. https://code.claude.com/docs/en/errors
12. https://code.claude.com/docs/en/agent-sdk/hosting
13. https://code.claude.com/docs/en/hooks
14. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (fetched directly; not in search results)
15. https://code.claude.com/docs/en/costs
16. https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
17. https://code.claude.com/docs/en/routines (History outcome semantics)
18. https://backgroundclaude.com/scheduled and https://codingwithroby.substack.com/p/claude-code-can-maintain-your-repo (search excerpts)
19. https://www.getmacha.com/blog/guardrails-autonomous-agents-debounce-caps-auto-disable-loop and https://gravitee.io/corpus/gen-971/winter-was-hard/agent-runaway-prevention-and-safe-termination-controls-for-autonomous-workflows.html (search excerpts)
20. https://code.claude.com/docs/en/agent-sdk/hosting
21. https://startdebugging.net/2026/04/how-to-detect-when-a-file-finishes-being-written-to-in-dotnet/ ; https://community.ibm.com/community/user/discussion/how-to-avoid-webmethods-scheduler-from-picking-partially-copied-file (search excerpts)
22. https://code.claude.com/docs/en/monitoring-usage
23. https://code.claude.com/docs/en/permission-modes
24. https://code.claude.com/docs/en/routines
25. https://code.claude.com/docs/en/desktop
26. https://support.claude.com/en/articles/11049741-what-is-the-max-plan
27. https://support.claude.com/en/articles/8325606-what-is-the-pro-plan
28. https://claude.com/pricing
29. https://www.anthropic.com/news/higher-limits-spacex (2026-05-06)
30. https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan
31. https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans
32. https://code.claude.com/docs/en/errors (usage limits section)
33. https://code.claude.com/docs/en/interactive-mode
34. https://support.claude.com/en/articles/9797557-usage-limit-best-practices (dated Sept 22, 2026)
35. https://code.claude.com/docs/en/whats-new/2026-w21 (May 18-22, 2026)
36. https://code.claude.com/docs/en/scheduled-tasks
37. https://www.morphllm.com/claude-code-github-actions ; https://playbooks.com/skills/codyswanngt/lisa/claude-code-action (search excerpts)
38. https://forum.obsidian.md/t/vault-health-check-a-read-only-claude-code-routine-that-audits-your-vault-free-mit/117831 (search excerpt)
