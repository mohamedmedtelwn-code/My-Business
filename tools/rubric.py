#!/usr/bin/env python3
"""Scoring arithmetic for Planning (templates/scoring-rubric.md).

Eight criteria, each scored 1-5, multiplied by its weight (weights sum to 20,
so the maximum is 100). The owner-edge bonus adds +1 to Durability and
Earnings ceiling (capped at 5). Approve at rubric_threshold (default 70).

Usage:
  python tools/rubric.py score --scores 4,5,2,4,4,3,2,3 [--edge] [--notes "a;b;c;d;e;f;g;h"] [--json]
Prints the ## Score block Planning pastes into the brief. Exit 0 approved, 1 rejected, 2 bad input.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import studio  # noqa: E402

CRITERIA = [
    "Evidence strength",
    "Capital to first dollar",
    "Time to first dollar",
    "Automatability",
    "Owner time per week",
    "Earnings ceiling at 6 months",
    "Durability",
    "Legal / platform clarity",
]
EDGE_BONUS = {5: 1, 6: 1}  # index -> bonus (Earnings ceiling, Durability)


class RubricError(Exception):
    pass


def score(scores, cfg: dict, edge: bool = False, notes=None) -> dict:
    weights = list(cfg.get("rubric_weights", studio.DEFAULT_CONFIG["rubric_weights"]))
    thr = float(cfg.get("rubric_threshold", 70))
    if len(scores) != len(CRITERIA):
        raise RubricError(f"Need {len(CRITERIA)} scores, got {len(scores)}.")
    if len(weights) != len(CRITERIA) or sum(weights) != 20:
        raise RubricError("rubric_weights must have 8 entries summing to 20.")
    rows = []
    total = 0
    notes = list(notes or [])
    for i, (name, w) in enumerate(zip(CRITERIA, weights)):
        try:
            s = int(scores[i])
        except (TypeError, ValueError):
            raise RubricError(f"Score for '{name}' is not an integer: {scores[i]!r}")
        if not 1 <= s <= 5:
            raise RubricError(f"Score for '{name}' must be 1-5, got {s}.")
        bonus = EDGE_BONUS.get(i, 0) if edge else 0
        eff = min(5, s + bonus)
        pts = eff * w
        total += pts
        rows.append({"n": i + 1, "criterion": name, "score": s, "bonus": eff - s, "weight": w, "points": pts,
                     "note": notes[i] if i < len(notes) else ""})
    return {"rows": rows, "total": total, "threshold": thr, "approved": total >= thr, "edge": edge}


def render(r: dict) -> str:
    lines = ["## Score", "", "| # | Criterion | Score | Weight | Points | Justification |", "|---|---|---|---|---|---|"]
    for row in r["rows"]:
        sc = f"{row['score']}" + (f" (+{row['bonus']} edge)" if row["bonus"] else "")
        lines.append(f"| {row['n']} | {row['criterion']} | {sc} | {row['weight']} | {row['points']} | {row['note']} |")
    lines.append("")
    lines.append(f"**Total:** {r['total']}/100 — {'APPROVED' if r['approved'] else 'REJECTED'} (threshold {r['threshold']:g})"
                 + ("; owner-edge bonus applied" if r["edge"] else ""))
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="rubric.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("score")
    s.add_argument("--scores", required=True, help="eight comma-separated integers 1-5, in rubric order")
    s.add_argument("--edge", action="store_true", help="apply the OWNER-EDGE.md bonus")
    s.add_argument("--notes", default="", help="eight justifications separated by ';'")
    s.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    try:
        root = Path(args.root) if args.root else studio.find_root(Path.cwd())
        cfg = studio.load_config(root)
    except FileNotFoundError:
        cfg = dict(studio.DEFAULT_CONFIG)
    try:
        scores = [x.strip() for x in args.scores.split(",")]
        notes = [n.strip() for n in args.notes.split(";")] if args.notes else []
        r = score(scores, cfg, edge=args.edge, notes=notes)
    except RubricError as e:
        print(f"ERROR: {e}")
        return 2
    print(json.dumps(r, indent=2) if args.json else render(r))
    return 0 if r["approved"] else 1


if __name__ == "__main__":
    sys.exit(main())
