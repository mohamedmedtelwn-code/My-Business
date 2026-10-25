# Business folder skeleton: businesses/<slug>/

```
plan.md        the execution plan (moved here by Preparation)
WORK.md        standing instruction for the Work agent (below)
logbook.md     append-only run log
metrics.md     three plan metrics, dated rows
ledger.md      every USD in and out for this business
FLAG.md        created only when a kill/scale threshold is crossed
output/        YYYYMMDD/ folders of produced work
for-owner/     items waiting for the owner to press a button
```

## WORK.md template
```
# WORK — <slug>
Run cadence: <e.g. daily 08:00>
Time budget per run: <e.g. 30 min>
Each run:
1. <action>
2. <action>
3. Update metrics.md, append logbook.md
Stop and ticket if: <conditions>
Platform rules to re-check monthly: <URLs>
```

## logbook.md entry format
```
## YYYY-MM-DD HH:MM
- Did:
- Outputs: output/YYYYMMDD/...
- Metrics: m1 __ (Δ__), m2 __ (Δ__), m3 __ (Δ__)
- Problems:
- Next run:
```

## metrics.md format
| Date | Metric 1 | Metric 2 | Metric 3 | Source | Note |
|------|----------|----------|----------|--------|------|

## ledger.md format
| Date | Item | USD out | USD in | Ticket / tier | Balance |
|------|------|---------|--------|---------------|---------|
