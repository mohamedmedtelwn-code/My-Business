# Live dashboard feed — Management team

The owner's live dashboard is the artifact **Venture Studio Control Room**
(URL in `management/dashboard-url.txt`). Its page reads a small database;
Management writes to it with the `ArtifactData` tool (load it with
ToolSearch `select:ArtifactData`). Every write takes the artifact `url`.
Documents already present carry a `version`; pass it as `if_version` on
updates. Prefer one `batch` per refresh.

## Collections and shapes

**studio / summary** (one doc, `set` each refresh)
```json
{"updated":"YYYY-MM-DD HH:MM",
 "capital":{"ceiling":1000,"released":0,"spent":0,"revenue":0,"pool":0},
 "pipeline":{"inbox":0,"assessed":0,"planned":0,"tickets_open":0},
 "businesses":{"live":0,"paused":0,"stopped":0}}
```

**teams / {research|planning|preparation|work|management}** (`update` after each team's run)
```json
{"status":"idle|running|ok|warn|bad","summary":"one line on the last run",
 "last_run":"YYYY-MM-DD HH:MM","next_run":"text"}
```

**businesses / <slug>** (`set` on launch, `update` each refresh)
```json
{"name":"...","category":"...","status":"live|paused|stopped","rag":"green|amber|red",
 "days_live":0,"spent":0,"revenue":0,"last_run":"YYYY-MM-DD HH:MM","flag":false,
 "metrics":[{"name":"...","value":0,"kill":0,"scale":0}]}
```

**tickets / <ticket-id>** (`set` when raised, `update` status when closed)
```json
{"title":"...","business":"<slug>","type":"approval|investment","amount":0,
 "raised":"YYYY-MM-DD","status":"open|closed"}
```

**ledger / <YYYYMMDD-slug-n>** (`set` once per ledger line; never edit history)
```json
{"date":"YYYY-MM-DD","business":"<slug>","item":"...","out":0,"in":0,"tier":"0|1|2"}
```

**activity / <YYYYMMDD-HHMM-team>** (`set` one line per finished run; keep the
collection under 200 docs by deleting the oldest when it grows past that)
```json
{"ts":"YYYY-MM-DD HH:MM","team":"research","text":"one sentence"}
```

## When to write
- Every team: one `activity` line and its own `teams` doc at the end of a run.
- Preparation: `tickets` on raise/close, `ledger` on Tier 0 spend, `businesses` on launch.
- Work: `businesses/<slug>` metrics and `ledger` lines for that business.
- Management nightly: `studio/summary` recomputed from the markdown ledger
  and all business folders, then every `businesses` doc.

The markdown files in `management/` remain the source of truth; the
database mirrors them for the live view.
