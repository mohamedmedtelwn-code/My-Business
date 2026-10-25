# Live dashboard feed — Management team

The owner's live dashboard is the artifact **Venture Studio Control Room**
(URL in `management/dashboard-url.txt`). Its page reads a small database;
Management writes to it with the `ArtifactData` tool (load it with ToolSearch
`select:ArtifactData`). `tools/dashboard_push.py` builds the exact writes from
the ledger, the run log and the business folders, so a run only has to send them.

## Procedure (nightly and after the weekly review)
1. Read what is there, so every write can carry its version (ArtifactData
   refuses a write to an existing document without `if_version`):
   for each of `studio`, `teams`, `businesses`, `tickets`, `ledger`, `activity`
   call `ArtifactData` with `action: "list"`, that `collection`, the artifact
   `url`, `query: {"limit": 1000}` and `out_dir: "management/.dashboard-state"`.
   The saved files hold the documents' data only, so also write the version
   numbers the list results print into
   `management/.dashboard-state/versions.json` as
   `{"studio/summary": 3, "teams/research": 1, ...}` (one entry per existing document).
2. Build the payload:
   `python tools/dashboard_push.py --versions-dir management/.dashboard-state > management/.dashboard-state/payload.json`
3. Send each entry of `batches` as one `ArtifactData` call with
   `action: "batch"`, the `url` and the `writes` list (at most 50 per batch).
   If a batch is refused because a version moved, re-run steps 1-2 and resend.
4. Delete `management/.dashboard-state/` (it is ignored by git).
On the very first refresh the collections are empty; step 1 returns nothing and
every write creates its document.

## Owner answers (every team, at the start of every run)
The ticket cards carry an answer form. Each answer is a document in the
collection `replies`: `{"ticket": "<id>", "decision": "done|approved|rejected|note",
"note": "...", "at": "<ISO time>"}`. Before any other work a run applies them:
1. `ArtifactData` `action: "list"`, `collection: "replies"`, the artifact `url`,
   `query: {"limit": 500}`, `out_dir: "management/.dashboard-state"` (files land
   in `management/.dashboard-state/replies/<doc_id>.json`); write the versions
   the result shows into `management/.dashboard-state/versions.json` as
   `{"replies/<doc_id>": <version>}`. An empty list means nothing to do.
2. `python tools/replies_apply.py management/.dashboard-state/replies --versions management/.dashboard-state/versions.json --delete-out management/.dashboard-state/replies-delete.json`
   It writes the decision line (done / approved / rejected close the ticket and
   move it to closed/; note appends an owner note and leaves it open), saves the
   note of a validation ticket under `pipeline/15-validating/output/<id>/replies/`,
   and prints one line per answer.
3. Send `management/.dashboard-state/replies-delete.json` as one `ArtifactData`
   `action: "batch"` call (its `writes` delete the applied documents, pinned by
   version). If the batch is refused because a version moved, list again and
   resend the delete only; the files are already applied.
4. Then continue with the team's own procedure: Preparation acts on the closed
   tickets, Planning on the reply files, Management shows the result.

## Collections and shapes (what the tool emits)

**studio / summary** (`set` each refresh)
```json
{"updated":"YYYY-MM-DD HH:MM",
 "capital":{"ceiling":1000,"released":0,"spent":0,"revenue":0,"pool":0},
 "pipeline":{"inbox":0,"assessed":0,"planned":0,"tickets_open":0},
 "businesses":{"live":0,"paused":0,"stopped":0}}
```
Capital comes from `tools/ledger.py report`; counts from `tools/check.py`.

**teams / {research|planning|preparation|work|management}** (`set` each refresh)
```json
{"status":"idle|ok|warn|bad","summary":"one line on the last run",
 "last_run":"YYYY-MM-DD HH:MM","next_run":"text"}
```
From the last `end` event per team in `management/runs.jsonl`; `next_run` from
`team_cadence` in `management/config.json`.

**businesses / <slug>** (`set` each refresh)
```json
{"name":"...","category":"...","status":"live|paused|stopped","rag":"green|amber|red",
 "days_live":0,"spent":0,"revenue":0,"last_run":"YYYY-MM-DD HH:MM","flag":false,
 "metrics":[{"name":"...","value":0,"kill":0,"scale":0}]}
```
`rag` is red when FLAG.md exists or a metric is below its kill value, green when
every metric is at or above its scale value, amber otherwise. Spent and revenue
come from the ledger, metrics from the plan's threshold table and the last row of
`metrics.md`.

**tickets / <ticket-id>** (`set`; open and closed)
```json
{"title":"...","business":"<slug>","type":"approval|investment","amount":0,
 "raised":"YYYY-MM-DD","status":"open|closed","blocks":"...","steps":["..."],
 "why":"one paragraph","file":"pipeline/30-tickets/open/<id>.md",
 "attachments":[{"name":"message.md","text":"..."}]}
```
`attachments` are the top-level .md files under
`pipeline/15-validating/output/<validation-id>/` for a `<validation-id>-vN`
ticket (the drafts the owner copies and sends), cut at 6,000 characters.

**replies / <doc_id>** (written by the owner on the page, deleted by the run
that applied them; see "Owner answers")
```json
{"ticket":"<ticket-id>","decision":"done|approved|rejected|note","note":"...","at":"ISO time"}
```

**ledger / <YYYYMMDD-slug-n>** (`set` once per ledger entry; never edited)
```json
{"date":"YYYY-MM-DD","business":"<slug>","item":"...","out":0,"in":0,"tier":"0|1|2|release"}
```

**activity / <YYYYMMDD-HHMM-team>** (`set`, the last 25 finished runs; the tool
emits `delete` writes for the oldest documents when the collection holds more
than 200 and a versions folder was given)
```json
{"ts":"YYYY-MM-DD HH:MM","team":"research","text":"one sentence"}
```

## Who writes what
- Management writes everything above, nightly and weekly, through the procedure.
- Every team reads and clears `replies` at the start of its run (above).
- Other teams do not write to the dashboard directly any more; their run summary
  (`runlog.py end --summary`) becomes the team card and the activity line at the
  next Management refresh. This keeps one writer and one version flow.

The files in `management/` and the ledger database remain the source of truth;
the database mirrors them for the live view.
