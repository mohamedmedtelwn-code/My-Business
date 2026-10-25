#!/usr/bin/env python3
"""Validation verdict: counts signal units in a validation brief and decides.

Rule 10 v2 (see research/STUDIO-RESEARCH.md section 4):
  pass        3 signal units (SU) within the window, any time
  SU weights  payment / pre-order / deposit from a stranger  3
              booked call with a qualified stranger          1
              reply with explicit intent                     1
              email sign-up                                  1/3, only when visitors >= validation_min_visitors
                                                             and sign-up rate >= validation_min_signup_rate;
                                                             sign-ups together count at most 2 SU (a second
                                                             step is always needed)
              likes, follows, upvotes, views, friends        0
  denominator outreach: validation_min_outreach messages (first batch validation_first_batch; 0 signals
                        after the first batch parks early)
              landing:  validation_min_visitors qualified visitors
              presale:  validation_min_asks direct asks
  verdicts    PASSED        3 SU reached
              RUNNING       deadline not reached, under 3 SU
              PARKED        deadline reached, denominator reached, under 3 SU (or 0 of the first batch)
              INCONCLUSIVE  deadline reached, denominator not reached, not yet extended
                            (--write extends the deadline once by validation_days and sets Extended: yes;
                            an already-extended brief is PARKED instead)

The brief format (templates/validation-brief.md):
  - **Started:** YYYY-MM-DD  **Deadline:** YYYY-MM-DD
  - **Test:** outreach | landing | presale
  - **Extended:** no | yes
  - **Messages sent:** N   - **Visitors:** N   - **Asks:** N
  ## Signals table: | Date | Type | Who / what | Source |   (Type: payment, call, intent, signup)

Usage:
  python tools/signals.py pipeline/15-validating/<id>-validate.md            # print verdict
  python tools/signals.py pipeline/15-validating/<id>-validate.md --write    # also write ## Verdict into the file
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import studio  # noqa: E402

TYPES = {
    "payment": 3.0, "preorder": 3.0, "pre-order": 3.0, "deposit": 3.0, "paid": 3.0,
    "call": 1.0, "booked": 1.0, "meeting": 1.0,
    "intent": 1.0, "reply": 1.0,
    "signup": 1 / 3, "sign-up": 1 / 3, "waitlist": 1 / 3,
}
SIGNUP_CAP = 2.0


class SignalsError(Exception):
    pass


def _int_field(f: dict, key: str) -> int:
    v = f.get(key, "")
    m = re.search(r"\d+", v or "")
    return int(m.group(0)) if m else 0


def parse(text: str) -> dict:
    f = studio.parse_fields(text)
    deadline = studio.first_date(f.get("deadline"))
    if not deadline:
        raise SignalsError("Validation brief has no **Deadline:** YYYY-MM-DD.")
    test = (f.get("test") or "").strip().lower()
    messages = _int_field(f, "messages sent")
    visitors = _int_field(f, "visitors")
    asks = _int_field(f, "asks")
    if test not in ("outreach", "landing", "presale"):
        test = "landing" if visitors else "presale" if asks else "outreach"
    counts = {"payment": 0, "call": 0, "intent": 0, "signup": 0}
    ignored = []
    in_table = False
    for line in text.splitlines():
        if line.startswith("## "):
            in_table = line.lower().startswith("## signals")
            continue
        if not in_table or not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() == "date" or set(cells[0]) <= set("-: "):
            continue
        t = cells[1].strip().lower()
        if t in ("payment", "preorder", "pre-order", "deposit", "paid"):
            counts["payment"] += 1
        elif t in ("call", "booked", "meeting"):
            counts["call"] += 1
        elif t in ("intent", "reply"):
            counts["intent"] += 1
        elif t in ("signup", "sign-up", "waitlist"):
            counts["signup"] += 1
        else:
            ignored.append(t)
    return {"started": studio.first_date(f.get("started")), "deadline": deadline, "test": test,
            "extended": (f.get("extended") or "no").strip().lower().startswith("y"),
            "messages": messages, "visitors": visitors, "asks": asks, "counts": counts, "ignored": ignored}


def verdict(text: str, cfg: dict, today: str | None = None) -> dict:
    p = parse(text)
    today = today or studio.today()
    c = p["counts"]
    su = 3.0 * c["payment"] + 1.0 * c["call"] + 1.0 * c["intent"]
    signup_su = 0.0
    signup_rate = (c["signup"] / p["visitors"]) if p["visitors"] else 0.0
    if p["test"] == "landing" and p["visitors"] >= int(cfg["validation_min_visitors"]) \
            and signup_rate >= float(cfg["validation_min_signup_rate"]):
        signup_su = min(c["signup"] / 3.0, SIGNUP_CAP)
    su += signup_su
    su = round(su, 2)
    due = today >= p["deadline"]
    if p["test"] == "outreach":
        reached = p["messages"] >= int(cfg["validation_min_outreach"])
        early_park = p["messages"] >= int(cfg["validation_first_batch"]) and su == 0
        denominator = f"{p['messages']} of {cfg['validation_min_outreach']} messages"
    elif p["test"] == "landing":
        reached = p["visitors"] >= int(cfg["validation_min_visitors"])
        early_park = False
        denominator = f"{p['visitors']} of {cfg['validation_min_visitors']} visitors, sign-up rate {signup_rate:.1%}"
    else:
        reached = p["asks"] >= int(cfg["validation_min_asks"])
        early_park = False
        denominator = f"{p['asks']} of {cfg['validation_min_asks']} asks"

    if su >= 3:
        v, reason = "PASSED", f"{su:g} signal units (3 needed)."
    elif not due:
        v, reason = "RUNNING", f"Deadline {p['deadline']} not reached; {su:g} SU so far."
    elif early_park:
        v, reason = "PARKED", f"0 signals after the first {cfg['validation_first_batch']} messages."
    elif reached:
        v, reason = "PARKED", f"{su:g} SU from {denominator}; under 3."
    elif p["extended"]:
        v, reason = "PARKED", f"Denominator still not reached after one extension ({denominator}); {su:g} SU."
    else:
        v, reason = "INCONCLUSIVE", f"Deadline reached but denominator not ({denominator}); extend once by {cfg['validation_days']} days."
    return {"verdict": v, "reason": reason, "su": su, "counts": c, "signup_su": round(signup_su, 2),
            "signup_rate": round(signup_rate, 4), "test": p["test"], "deadline": p["deadline"],
            "denominator": denominator, "denominator_reached": reached, "extended": p["extended"],
            "ignored": p["ignored"], "today": today}


def render(v: dict) -> str:
    c = v["counts"]
    lines = ["## Verdict", "",
             f"**Verdict:** {v['verdict']}  ",
             f"**Signal units:** {v['su']:g} (payments {c['payment']} x3, calls {c['call']}, intent replies {c['intent']}, "
             f"sign-ups {c['signup']} -> {v['signup_su']:g} SU)  ",
             f"**Denominator:** {v['denominator']} ({'reached' if v['denominator_reached'] else 'not reached'})  ",
             f"**Reason:** {v['reason']}  ",
             f"**Counted on:** {v['today']} by tools/signals.py"]
    if v["ignored"]:
        lines.append(f"**Ignored rows (count 0):** {', '.join(v['ignored'])}")
    return "\n".join(lines) + "\n"


def write_verdict(path: Path, cfg: dict, today: str | None = None) -> dict:
    path = Path(path)
    text = studio.read_text(path)
    v = verdict(text, cfg, today)
    if v["verdict"] == "INCONCLUSIVE" and not v["extended"]:
        new_deadline = (studio.parse_date(v["today"]) + __import__("datetime").timedelta(days=int(cfg["validation_days"]))).isoformat()
        text = re.sub(r"(\*\*Deadline:\*\*\s*)\d{4}-\d{2}-\d{2}", r"\g<1>" + new_deadline, text, count=1)
        if re.search(r"\*\*Extended:\*\*\s*\w+", text):
            text = re.sub(r"(\*\*Extended:\*\*\s*)\w+", r"\g<1>yes", text, count=1)
        else:
            text = text.replace("- **Cost:**", "- **Extended:** yes\n- **Cost:**", 1)
        v["new_deadline"] = new_deadline
        v["reason"] += f" New deadline {new_deadline}."
    # replace or append the verdict section
    if "## Verdict" in text:
        head, _, tail = text.partition("## Verdict")
        rest = tail.split("\n## ", 1)
        text = head + render(v) + ("\n## " + rest[1] if len(rest) > 1 else "")
    else:
        text = text.rstrip("\n") + "\n\n" + render(v)
    studio.write_text(path, text)
    return v


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="signals.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--root")
    ap.add_argument("--write", action="store_true", help="write the ## Verdict section into the file")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    path = Path(args.file)
    try:
        root = Path(args.root) if args.root else studio.find_root(path.resolve().parent)
    except FileNotFoundError:
        root = Path.cwd()
    cfg = studio.load_config(root)
    try:
        v = write_verdict(path, cfg) if args.write else verdict(studio.read_text(path), cfg)
    except SignalsError as e:
        print(f"ERROR: {e}")
        return 2
    except FileNotFoundError:
        print(f"ERROR: no such file {path}")
        return 2
    if args.json:
        print(json.dumps(v, indent=2))
    else:
        print(render(v))
        if v["verdict"] == "PASSED":
            print("Next: move the file to 15-validating/passed/ and write the execution plan.")
        elif v["verdict"] == "PARKED":
            print("Next: move the file to 15-validating/parked/ and add one line to research/feedback.md.")
        elif v["verdict"] == "INCONCLUSIVE":
            print("Next: keep running; reach the denominator before the new deadline." if args.write else "Run with --write to extend the deadline once.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
