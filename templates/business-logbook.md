# Business folder skeleton: businesses/<slug>/

```
plan.md        the execution plan (moved here by Preparation; Status and Launched filled)
WORK.md        standing instruction for the Work agent (below)
logbook.md     append-only run log
metrics.md     plan metrics, dated rows, every row with a Source
ledger.md      every USD in and out for this business (tools/ledger.py appends; never hand-edit)
FLAG.md        created only when a kill/scale threshold is crossed
output/        YYYYMMDD/ folders of produced work
for-owner/     items waiting for the owner to press a button
```

## WORK.md template
```
# WORK — <slug>
Run cadence: <e.g. daily 08:00>
Time budget per run: <e.g. 30 min>
Outbound cap: <e.g. 10 messages per run, never above 20 cold messages a day>
Platform rules to re-check monthly: <rows in research/platform-rules.md>
Price guard: min price USD __, max discount __%, max refund USD __ (anything else is a ticket)

Each run:
0. python tools/check.py  (fix ERRORs first); python tools/runlog.py start --team work --business <slug>
1. <action>
2. <action>
3. Record money: python tools/ledger.py add --business <slug> --item "..." --in X  (or --out X --source ... --ticket ...)
4. Update metrics.md (with Source), append logbook.md
5. python tools/check.py; python tools/runlog.py end --id <RUN_ID> --outcome ok|warn|bad --summary "..." --commit
Stop and ticket if: <conditions>
```

## logbook.md entry format
```
## YYYY-MM-DD HH:MM (run <RUN_ID>)
- Did:
- Outputs: output/YYYYMMDD/...
- Metrics: m1 __ (Δ__), m2 __ (Δ__), m3 __ (Δ__)
- Money: USD in __ / out __ (ledger entries #__)
- Problems:
- Next run:
```

## metrics.md format
| Date | Metric 1 | Metric 2 | Metric 3 | Source | Note |
|------|----------|----------|----------|--------|------|
Source is the export, screenshot path or URL the number was read from. A row
without a Source is flagged by tools/check.py ("no number without a source").

## ledger.md format (written by tools/ledger.py)
| Date | Item | USD out | USD in | Ticket / tier | Balance |
|------|------|---------|--------|---------------|---------|
