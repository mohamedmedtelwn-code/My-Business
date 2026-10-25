"""Shared helpers for the venture-studio tools.

Every tool imports this module. It knows where the studio root is, how to
read the config, and how to parse the small set of Markdown conventions the
templates use (``- **Key:** value`` lines, ISO dates, the owner decision
line). Standard library only. Works on Windows, macOS and Linux.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import re
import tempfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Config: the single source of the numbers the tools enforce.
# management/config.json overrides these defaults. CLAUDE.md quotes them.
# ---------------------------------------------------------------------------
DEFAULT_CONFIG = {
    "studio_start": None,            # YYYY-MM-DD; set by the owner on day one
    "ceiling_usd": 1000,             # owner's ceiling; never deposited
    "phase1_days": 90,               # Phase 1 length
    "phase1_live_cap": 8,            # live businesses allowed in Phase 1
    "phase2_live_cap": 3,            # live businesses allowed in Phase 2
    "validation_days": 7,            # validation window
    "validation_min_signals": 3,     # signals needed to pass
    "validation_min_outreach": 50,   # minimum messages sent for an outreach test (20 first, then 30 more)
    "validation_first_batch": 20,    # outreach: park early if 0 signals after this many messages
    "validation_min_visitors": 100,  # minimum qualified visitors for a landing-page test
    "validation_min_signup_rate": 0.08,  # sign-ups count only above this visitor-to-sign-up rate
    "validation_min_asks": 20,       # minimum direct asks for a pre-sale test
    "ticket_stale_days": 3,          # open ticket older than this is flagged
    "ticket_pause_days": 7,          # open ticket older than this pauses its business
    "open_ticket_cap": 10,           # studio-wide cap on open tickets
    "run_stale_hours": 3,            # a run started and not finished after this is a crash
    "breaker_failures": 3,           # failed runs in a row that stop a team until reset
    "platform_rules_max_age_days": 30,  # research/platform-rules.md must be re-checked within this
    "payout_route_verified": False,  # owner sets true after the first test payout lands
    "rubric_threshold": 70,          # planning approval threshold /100
    "rubric_weights": [4, 3, 4, 3, 2, 2, 1, 1],  # see templates/scoring-rubric.md; sum 20
    "zero_revenue_weeks_to_stop": 4, # live, no revenue, no lead-metric growth
    "kill_weeks": 2,                 # weeks below kill threshold before stop
    "scale_weeks": 2,                # weeks above scale threshold before scale
    "team_cadence": {                # shown on the dashboard as "next run"
        "research": "Mon and Thu 06:00", "planning": "daily 07:00", "preparation": "daily 07:30",
        "work": "per business plan", "management": "nightly 22:00, weekly Fri 18:00"},
}

STAGES = {
    "inbox": "pipeline/00-inbox",
    "approved": "pipeline/10-assessed/approved",
    "rejected": "pipeline/10-assessed/rejected",
    "validating": "pipeline/15-validating",
    "passed": "pipeline/15-validating/passed",
    "parked": "pipeline/15-validating/parked",
    "planned": "pipeline/20-planned",
    "tickets_open": "pipeline/30-tickets/open",
    "tickets_closed": "pipeline/30-tickets/closed",
    "businesses": "businesses",
    "management": "management",
    "reviews": "management/reviews",
    "research": "research",
    "playbooks": "research/playbooks",
}

TEAMS = ("research", "planning", "preparation", "work", "management")

ID_RE = re.compile(r"^\d{8}-[a-z0-9][a-z0-9-]*$")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def find_root(start: Path | str | None = None) -> Path:
    """Walk up from ``start`` (default: this file) to the folder holding CLAUDE.md."""
    p = Path(start or Path(__file__).resolve().parent).resolve()
    for candidate in (p, *p.parents):
        if (candidate / "CLAUDE.md").is_file():
            return candidate
    raise FileNotFoundError("Could not find the studio root (a folder containing CLAUDE.md) above %s" % p)


def load_config(root: Path) -> dict:
    cfg = dict(DEFAULT_CONFIG)
    path = Path(root) / "management" / "config.json"
    if path.is_file():
        cfg.update(json.loads(read_text(path)))
    return cfg


def today() -> str:
    return _dt.date.today().isoformat()


def now() -> str:
    return _dt.datetime.now().strftime("%Y-%m-%d %H:%M")


def now_iso() -> str:
    return _dt.datetime.now().replace(microsecond=0).isoformat()


def parse_date(s: str) -> _dt.date:
    return _dt.date.fromisoformat(s)


def days_between(a: str, b: str) -> int:
    """b - a in days (both YYYY-MM-DD)."""
    return (parse_date(b) - parse_date(a)).days


def phase(cfg: dict, today_s: str | None = None, **kw) -> int:
    """1 during the first ``phase1_days`` after ``studio_start``, else 2.
    With no start date recorded the studio is treated as Phase 1."""
    today_s = kw.get("today", today_s) or today()
    start = cfg.get("studio_start")
    if not start:
        return 1
    return 1 if days_between(start, today_s) < int(cfg["phase1_days"]) else 2


def live_cap(cfg: dict, today_s: str | None = None) -> int:
    return int(cfg["phase1_live_cap"] if phase(cfg, today_s) == 1 else cfg["phase2_live_cap"])


# ---------------------------------------------------------------------------
# File IO: always UTF-8, atomic writes (write temp file, then replace).
# ---------------------------------------------------------------------------
def read_text(path: Path | str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write_text(path: Path | str, text: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".tmp-", suffix=path.suffix, dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def append_text(path: Path | str, text: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def list_md(folder: Path) -> list[Path]:
    """Markdown files directly inside ``folder`` (not recursive), sorted."""
    folder = Path(folder)
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() == ".md")


# ---------------------------------------------------------------------------
# Markdown conventions used by the templates.
# ---------------------------------------------------------------------------
_FIELD_RE = re.compile(r"\*\*([^*\n]+?):\*\*\s*([^*\n]*)")


def parse_fields(text: str) -> dict:
    """Return ``{key_lower: value}`` for every ``**Key:** value`` in the text.
    Several pairs may share a line (``**Started:** d  **Deadline:** d``)."""
    out = {}
    for m in _FIELD_RE.finditer(text):
        key = m.group(1).strip().lower()
        val = m.group(2).strip()
        if key not in out:
            out[key] = val
    return out


def first_date(s: str | None) -> str | None:
    if not s:
        return None
    m = DATE_RE.search(s)
    return m.group(0) if m else None


def owner_decision(text: str) -> str | None:
    """APPROVED / REJECTED / DONE from the ticket's owner-decision line, or None.
    The untouched template line (``APPROVED / REJECTED / DONE``) counts as none."""
    m = re.search(r"\*\*Owner decision:\*\*\s*(.*)", text)
    if not m:
        return None
    val = m.group(1).strip()
    words = re.findall(r"\b(APPROVED|REJECTED|DONE)\b", val)
    if len(set(words)) > 1:
        return None  # still the template placeholder
    return words[0] if words else None


def section(text: str, heading: str) -> str | None:
    """Body of the ``## heading`` section (case-insensitive prefix match), or None."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.lower().startswith("## " + heading.lower()):
            body = []
            for l2 in lines[i + 1:]:
                if l2.startswith("## "):
                    break
                body.append(l2)
            return "\n".join(body).strip()
    return None


def fmt_usd(n: float) -> str:
    n = float(n or 0)
    if abs(n - round(n)) < 0.005:
        return f"{int(round(n)):,}"
    return f"{n:,.2f}"


def slug_of(stem: str) -> str:
    """``20261101-my-idea-plan`` -> ``my-idea``; strips the date and a stage suffix."""
    s = re.sub(r"^\d{8}-", "", stem)
    for suffix in ("-validate", "-plan"):
        if s.endswith(suffix):
            s = s[: -len(suffix)]
    return s


def rel(root: Path, path: Path) -> str:
    try:
        return Path(path).resolve().relative_to(Path(root).resolve()).as_posix()
    except ValueError:
        return str(path)
