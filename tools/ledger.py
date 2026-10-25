#!/usr/bin/env python3
"""Studio ledger as code.

The ledger lives in ``management/ledger.sqlite``. ``management/ledger.md`` is
a generated view; never edit it by hand. Every money event is one entry:

* ``release``  the owner approved a ticket that draws USD X from the ceiling
* ``spend``    USD out, funded from ``ceiling`` (needs a released ticket) or
               ``pool`` (needs pool balance and a ticket)
* ``revenue``  USD in, earned by a business; it fills the reinvestment pool

Rules enforced (CLAUDE.md funding rules):
  released total      <= ceiling
  spend from ceiling  <= what the owner released on that ticket
  spend from pool     <= pool balance (revenue minus earlier pool spend)
  every spend names a ticket (pool spend still needs the owner's sign-off)

Usage (run from anywhere inside the studio folder):
  python tools/ledger.py init
  python tools/ledger.py release --ticket 20261101-abc-1 --business abc --amount 40
  python tools/ledger.py add --business abc --item "domain" --out 12 --source ceiling --ticket 20261101-abc-1 --tier 0
  python tools/ledger.py add --business abc --item "first sale" --in 25
  python tools/ledger.py report [--json]
  python tools/ledger.py reconcile [--json]
  python tools/ledger.py render
  python tools/ledger.py list [--business abc]
Exit codes: 0 ok, 1 refused or mismatch, 2 usage error.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import studio  # noqa: E402

SOURCES = ("ceiling", "pool")
EPS = 0.005


class LedgerError(Exception):
    """An entry the rules refuse. The message says why."""


class Ledger:
    def __init__(self, root: Path | None = None):
        self.root = Path(root) if root else studio.find_root()
        self.cfg = studio.load_config(self.root)
        self.db_path = self.root / "management" / "ledger.sqlite"
        self.md_path = self.root / "management" / "ledger.md"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.con = sqlite3.connect(str(self.db_path))
        self.con.row_factory = sqlite3.Row
        self._ensure_schema()

    # -- setup -------------------------------------------------------------
    def _ensure_schema(self) -> None:
        self.con.executescript(
            """
            CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
            CREATE TABLE IF NOT EXISTS entries (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                date     TEXT NOT NULL,
                business TEXT NOT NULL,
                kind     TEXT NOT NULL CHECK (kind IN ('release','spend','revenue')),
                item     TEXT NOT NULL,
                usd_out  REAL NOT NULL DEFAULT 0,
                usd_in   REAL NOT NULL DEFAULT 0,
                amount   REAL NOT NULL DEFAULT 0,
                source   TEXT,
                ticket   TEXT,
                tier     TEXT,
                note     TEXT,
                created  TEXT NOT NULL
            );
            """
        )
        self.con.commit()

    def init(self) -> None:
        """Create the database (idempotent) and render the Markdown view."""
        cur = self.con.execute("SELECT value FROM meta WHERE key='ceiling_usd'")
        if cur.fetchone() is None:
            self.con.execute("INSERT INTO meta(key,value) VALUES('ceiling_usd',?)", (str(self.cfg["ceiling_usd"]),))
            self.con.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('opened',?)", (studio.today(),))
            self.con.commit()
        self.render()

    def close(self) -> None:
        self.con.close()

    @property
    def ceiling(self) -> float:
        row = self.con.execute("SELECT value FROM meta WHERE key='ceiling_usd'").fetchone()
        return float(row["value"]) if row else float(self.cfg["ceiling_usd"])

    # -- sums --------------------------------------------------------------
    def _sum(self, sql: str, *params) -> float:
        v = self.con.execute(sql, params).fetchone()[0]
        return round(float(v or 0), 2)

    def released_total(self) -> float:
        return self._sum("SELECT SUM(amount) FROM entries WHERE kind='release'")

    def released_on(self, ticket: str) -> float:
        return self._sum("SELECT SUM(amount) FROM entries WHERE kind='release' AND ticket=?", ticket)

    def spent_on(self, ticket: str) -> float:
        return self._sum("SELECT SUM(usd_out) FROM entries WHERE kind='spend' AND source='ceiling' AND ticket=?", ticket)

    def spent_total(self) -> float:
        return self._sum("SELECT SUM(usd_out) FROM entries WHERE kind='spend'")

    def spent_from(self, source: str) -> float:
        return self._sum("SELECT SUM(usd_out) FROM entries WHERE kind='spend' AND source=?", source)

    def revenue_total(self) -> float:
        return self._sum("SELECT SUM(usd_in) FROM entries WHERE kind='revenue'")

    def pool_balance(self) -> float:
        return round(self.revenue_total() - self.spent_from("pool"), 2)

    # -- writes ------------------------------------------------------------
    def release(self, ticket: str, business: str, amount: float, date: str | None = None, note: str = "") -> int:
        amount = float(amount)
        if not ticket:
            raise LedgerError("A release needs the approved ticket id.")
        if amount <= 0:
            raise LedgerError("Release amount must be positive.")
        if self.released_total() + amount > self.ceiling + EPS:
            raise LedgerError(
                f"Release of USD {studio.fmt_usd(amount)} would take released total to "
                f"USD {studio.fmt_usd(self.released_total() + amount)}, above the ceiling of USD {studio.fmt_usd(self.ceiling)}.")
        date = date or studio.today()
        studio.parse_date(date)
        cur = self.con.execute(
            "INSERT INTO entries(date,business,kind,item,amount,ticket,note,created) VALUES(?,?,?,?,?,?,?,?)",
            (date, business or "studio", "release", f"Owner released USD {studio.fmt_usd(amount)} on ticket {ticket}",
             amount, ticket, note, studio.now_iso()))
        self.con.commit()
        self.render()
        return cur.lastrowid

    def add(self, business: str, item: str, out: float = 0, inc: float = 0, source: str | None = None,
            ticket: str | None = None, tier: str | None = None, date: str | None = None, note: str = "",
            business_row: bool = True) -> int:
        out = float(out or 0)
        inc = float(inc or 0)
        if not business:
            raise LedgerError("Every entry names a business slug (or 'studio').")
        if not item:
            raise LedgerError("Every entry needs an item description.")
        if out > 0 and inc > 0:
            raise LedgerError("One entry is either USD out or USD in, not both.")
        if out <= 0 and inc <= 0:
            raise LedgerError("Entry has no amount: give --out or --in.")
        date = date or studio.today()
        studio.parse_date(date)

        if out > 0:
            kind = "spend"
            if source not in SOURCES:
                raise LedgerError("A spend names its source: --source ceiling or --source pool.")
            if not ticket:
                raise LedgerError("A spend needs the approved ticket id (pool spend too; the owner signs every spend).")
            if source == "ceiling":
                released = self.released_on(ticket)
                if released <= 0:
                    raise LedgerError(
                        f"Ticket {ticket} has no release recorded: this would spend from an unreleased ceiling. "
                        f"Record the owner's approval first: ledger.py release --ticket {ticket} --amount ...")
                remaining = released - self.spent_on(ticket)
                if out > remaining + EPS:
                    raise LedgerError(
                        f"Ticket {ticket} has USD {studio.fmt_usd(remaining)} unspent of USD {studio.fmt_usd(released)} released; "
                        f"USD {studio.fmt_usd(out)} exceeds it (unreleased ceiling).")
            else:
                pool = self.pool_balance()
                if pool <= EPS:
                    raise LedgerError("The reinvestment pool is empty: nothing can be spent from it.")
                if out > pool + EPS:
                    raise LedgerError(
                        f"Pool balance is USD {studio.fmt_usd(pool)}; USD {studio.fmt_usd(out)} exceeds it.")
        else:
            kind = "revenue"
            source = None

        cur = self.con.execute(
            "INSERT INTO entries(date,business,kind,item,usd_out,usd_in,source,ticket,tier,note,created) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (date, business, kind, item, out, inc, source, ticket or None, str(tier) if tier not in (None, "") else None,
             note, studio.now_iso()))
        self.con.commit()
        if business_row:
            self._append_business_row(business, date, item, out, inc, ticket, tier)
        self.render()
        return cur.lastrowid

    # -- business ledgers --------------------------------------------------
    BIZ_HEADER = "| Date | Item | USD out | USD in | Ticket / tier | Balance |\n|------|------|---------|--------|---------------|---------|\n"

    def _append_business_row(self, business, date, item, out, inc, ticket, tier) -> None:
        folder = self.root / "businesses" / business
        if not folder.is_dir():
            return
        path = folder / "ledger.md"
        if not path.exists():
            studio.write_text(path, f"# Ledger — {business}\n\n{self.BIZ_HEADER}")
        bal = self._sum("SELECT SUM(usd_in) - SUM(usd_out) FROM entries WHERE business=? AND kind IN ('spend','revenue')", business)
        ref = "-"
        if ticket:
            ref = f"{ticket} / T{tier}" if tier not in (None, "") else ticket
        studio.append_text(
            path,
            f"| {date} | {item} | {studio.fmt_usd(out)} | {studio.fmt_usd(inc)} | {ref} | {studio.fmt_usd(bal)} |\n")

    @staticmethod
    def _parse_business_ledger(text: str) -> tuple[float, float, int]:
        out = inc = 0.0
        rows = 0
        for line in text.splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4 or cells[0].lower() == "date" or set(cells[0]) <= set("-: "):
                continue
            try:
                out += _money(cells[2])
                inc += _money(cells[3])
            except ValueError:
                continue
            rows += 1
        return round(out, 2), round(inc, 2), rows

    def reconcile(self) -> tuple[bool, list[str]]:
        """Compare every businesses/<slug>/ledger.md with the studio ledger."""
        issues: list[str] = []
        db = {}
        for r in self.con.execute(
                "SELECT business, SUM(usd_out) o, SUM(usd_in) i, COUNT(*) n FROM entries "
                "WHERE kind IN ('spend','revenue') GROUP BY business"):
            db[r["business"]] = (round(float(r["o"] or 0), 2), round(float(r["i"] or 0), 2), int(r["n"]))
        biz_root = self.root / "businesses"
        folders = [p for p in biz_root.iterdir() if p.is_dir()] if biz_root.is_dir() else []
        for folder in folders:
            slug = folder.name
            md = folder / "ledger.md"
            if not md.exists():
                if slug in db:
                    issues.append(f"{slug}: studio ledger has {db[slug][2]} entries but businesses/{slug}/ledger.md is missing")
                continue
            out, inc, rows = self._parse_business_ledger(studio.read_text(md))
            d_out, d_in, d_n = db.get(slug, (0.0, 0.0, 0))
            if abs(out - d_out) > EPS or abs(inc - d_in) > EPS:
                issues.append(
                    f"{slug}: business ledger out {studio.fmt_usd(out)} / in {studio.fmt_usd(inc)} "
                    f"vs studio ledger out {studio.fmt_usd(d_out)} / in {studio.fmt_usd(d_in)}")
            elif rows != d_n:
                issues.append(f"{slug}: business ledger has {rows} rows, studio ledger has {d_n} entries (totals match)")
        return (not issues), issues

    # -- reads -------------------------------------------------------------
    def report(self) -> dict:
        released = self.released_total()
        spent_c = self.spent_from("ceiling")
        spent_p = self.spent_from("pool")
        rev = self.revenue_total()
        per_biz = {}
        for r in self.con.execute(
                "SELECT business, SUM(usd_out) o, SUM(usd_in) i FROM entries "
                "WHERE kind IN ('spend','revenue') GROUP BY business ORDER BY business"):
            o = round(float(r["o"] or 0), 2)
            i = round(float(r["i"] or 0), 2)
            per_biz[r["business"]] = {"spent": o, "revenue": i, "net": round(i - o, 2)}
        tickets = {}
        for r in self.con.execute("SELECT ticket, SUM(amount) a FROM entries WHERE kind='release' GROUP BY ticket"):
            t = r["ticket"]
            tickets[t] = {"released": round(float(r["a"]), 2), "spent": self.spent_on(t)}
            tickets[t]["remaining"] = round(tickets[t]["released"] - tickets[t]["spent"], 2)
        return {
            "ceiling": self.ceiling,
            "released": released,
            "ceiling_remaining": round(self.ceiling - released, 2),
            "released_unspent": round(released - spent_c, 2),
            "spent": round(spent_c + spent_p, 2),
            "spent_from_ceiling": spent_c,
            "spent_from_pool": spent_p,
            "revenue": rev,
            "pool": round(rev - spent_p, 2),
            "net": round(rev - spent_c - spent_p, 2),
            "entries": int(self.con.execute("SELECT COUNT(*) FROM entries").fetchone()[0]),
            "businesses": per_biz,
            "tickets": tickets,
        }

    def entries(self, business: str | None = None) -> list[dict]:
        sql = "SELECT * FROM entries"
        params: tuple = ()
        if business:
            sql += " WHERE business=?"
            params = (business,)
        sql += " ORDER BY date, id"
        return [dict(r) for r in self.con.execute(sql, params)]

    # -- view --------------------------------------------------------------
    def render(self) -> str:
        r = self.report()
        f = studio.fmt_usd
        lines = [
            "# Studio Ledger",
            "",
            f"Generated by `tools/ledger.py` from `management/ledger.sqlite` on {studio.now()}. "
            "Do not edit by hand; record entries with the tool.",
            "",
            f"Ceiling set by owner: USD {f(r['ceiling'])} (nothing deposited; released per approved ticket)",
            "",
            "| Ceiling | Released | Ceiling remaining | Released unspent | Spent total | Spent from ceiling | Spent from pool | Revenue | Pool balance |",
            "|---|---|---|---|---|---|---|---|---|",
            f"| {f(r['ceiling'])} | {f(r['released'])} | {f(r['ceiling_remaining'])} | {f(r['released_unspent'])} | "
            f"{f(r['spent'])} | {f(r['spent_from_ceiling'])} | {f(r['spent_from_pool'])} | {f(r['revenue'])} | {f(r['pool'])} |",
            "",
            "## Per business",
            "",
            "| Business | Spent | Revenue | Net |",
            "|---|---|---|---|",
        ]
        if r["businesses"]:
            for slug, v in r["businesses"].items():
                lines.append(f"| {slug} | {f(v['spent'])} | {f(v['revenue'])} | {f(v['net'])} |")
        else:
            lines.append("| — | 0 | 0 | 0 |")
        lines += ["", "## Releases by ticket", "", "| Ticket | Released | Spent | Remaining |", "|---|---|---|---|"]
        if r["tickets"]:
            for t, v in sorted(r["tickets"].items()):
                lines.append(f"| {t} | {f(v['released'])} | {f(v['spent'])} | {f(v['remaining'])} |")
        else:
            lines.append("| — | 0 | 0 | 0 |")
        lines += [
            "", "## Entries", "",
            "| # | Date | Business | Kind | Item | USD out | USD in | Source | Ticket | Tier | Released to date | Spent to date | Revenue to date | Pool balance |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
        ]
        rel = spent = rev = pool_spent = 0.0
        rows = self.entries()
        if not rows:
            lines.append(f"| 0 | {self._opened()} | — | — | Ledger opened | 0 | 0 | — | — | — | 0 | 0 | 0 | 0 |")
        for e in rows:
            if e["kind"] == "release":
                rel += e["amount"]
            elif e["kind"] == "spend":
                spent += e["usd_out"]
                if e["source"] == "pool":
                    pool_spent += e["usd_out"]
            else:
                rev += e["usd_in"]
            lines.append(
                f"| {e['id']} | {e['date']} | {e['business']} | {e['kind']} | {_cell(e['item'])} | {f(e['usd_out'])} | {f(e['usd_in'])} | "
                f"{e['source'] or '—'} | {e['ticket'] or '—'} | {e['tier'] or '—'} | {f(rel)} | {f(spent)} | {f(rev)} | {f(rev - pool_spent)} |")
        text = "\n".join(lines) + "\n"
        studio.write_text(self.md_path, text)
        return text

    def _opened(self) -> str:
        row = self.con.execute("SELECT value FROM meta WHERE key='opened'").fetchone()
        return row["value"] if row else studio.today()


def _money(cell: str) -> float:
    s = re.sub(r"[^0-9.\-]", "", cell.replace("—", "0").replace("–", "0"))
    if s in ("", "-", "."):
        return 0.0
    return float(s)


def _cell(s: str) -> str:
    return str(s).replace("|", "/").replace("\n", " ")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ledger.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", help="studio root (default: found from this file's location)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init", help="create the database if needed and render ledger.md")
    a = sub.add_parser("add", help="record a spend (USD out) or revenue (USD in)")
    a.add_argument("--business", required=True)
    a.add_argument("--item", required=True)
    a.add_argument("--out", type=float, default=0)
    a.add_argument("--in", dest="inc", type=float, default=0)
    a.add_argument("--source", choices=SOURCES)
    a.add_argument("--ticket")
    a.add_argument("--tier", choices=["0", "1", "2"])
    a.add_argument("--date")
    a.add_argument("--note", default="")
    a.add_argument("--no-business-row", action="store_true", help="do not append to businesses/<slug>/ledger.md")
    r = sub.add_parser("release", help="record the owner's approval of a ticket drawing on the ceiling")
    r.add_argument("--ticket", required=True)
    r.add_argument("--business", required=True)
    r.add_argument("--amount", type=float, required=True)
    r.add_argument("--date")
    r.add_argument("--note", default="")
    rep = sub.add_parser("report", help="ceiling / released / spent / revenue / pool")
    rep.add_argument("--json", action="store_true")
    rec = sub.add_parser("reconcile", help="compare business ledgers with the studio ledger")
    rec.add_argument("--json", action="store_true")
    sub.add_parser("render", help="regenerate management/ledger.md")
    ls = sub.add_parser("list", help="list entries")
    ls.add_argument("--business")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = Path(args.root) if args.root else studio.find_root(Path.cwd())
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return 2
    led = Ledger(root)
    try:
        if args.cmd == "init":
            led.init()
            print(f"Ledger ready: {led.db_path} (ceiling USD {studio.fmt_usd(led.ceiling)}); view: {led.md_path}")
        elif args.cmd == "add":
            led.init() if not led.con.execute("SELECT 1 FROM meta WHERE key='ceiling_usd'").fetchone() else None
            eid = led.add(args.business, args.item, out=args.out, inc=args.inc, source=args.source, ticket=args.ticket,
                          tier=args.tier, date=args.date, note=args.note, business_row=not args.no_business_row)
            r = led.report()
            print(f"OK entry #{eid}. Released {studio.fmt_usd(r['released'])} · spent {studio.fmt_usd(r['spent'])} · "
                  f"revenue {studio.fmt_usd(r['revenue'])} · pool {studio.fmt_usd(r['pool'])}")
        elif args.cmd == "release":
            led.init() if not led.con.execute("SELECT 1 FROM meta WHERE key='ceiling_usd'").fetchone() else None
            eid = led.release(args.ticket, args.business, args.amount, date=args.date, note=args.note)
            r = led.report()
            print(f"OK release #{eid}. Released {studio.fmt_usd(r['released'])} of ceiling {studio.fmt_usd(r['ceiling'])}; "
                  f"remaining {studio.fmt_usd(r['ceiling_remaining'])}")
        elif args.cmd == "report":
            r = led.report()
            if args.json:
                print(json.dumps(r, indent=2))
            else:
                print(f"Ceiling USD {studio.fmt_usd(r['ceiling'])} · released {studio.fmt_usd(r['released'])} "
                      f"(unspent {studio.fmt_usd(r['released_unspent'])}) · spent {studio.fmt_usd(r['spent'])} "
                      f"(ceiling {studio.fmt_usd(r['spent_from_ceiling'])} / pool {studio.fmt_usd(r['spent_from_pool'])}) · "
                      f"revenue {studio.fmt_usd(r['revenue'])} · pool {studio.fmt_usd(r['pool'])} · net {studio.fmt_usd(r['net'])}")
                for slug, v in r["businesses"].items():
                    print(f"  {slug}: spent {studio.fmt_usd(v['spent'])} · revenue {studio.fmt_usd(v['revenue'])} · net {studio.fmt_usd(v['net'])}")
        elif args.cmd == "reconcile":
            ok, issues = led.reconcile()
            if args.json:
                print(json.dumps({"ok": ok, "issues": issues}, indent=2))
            else:
                print("RECONCILE OK: business ledgers match the studio ledger." if ok else "RECONCILE MISMATCH:")
                for i in issues:
                    print(f"  - {i}")
            return 0 if ok else 1
        elif args.cmd == "render":
            led.render()
            print(f"Rendered {led.md_path}")
        elif args.cmd == "list":
            for e in led.entries(args.business):
                print(f"#{e['id']} {e['date']} {e['business']:<20} {e['kind']:<8} out {studio.fmt_usd(e['usd_out']):>8} "
                      f"in {studio.fmt_usd(e['usd_in']):>8} rel {studio.fmt_usd(e['amount']):>8} {e['source'] or '-':<8} "
                      f"{e['ticket'] or '-'} {e['item']}")
        return 0
    except LedgerError as e:
        print(f"REFUSED: {e}")
        return 1
    except ValueError as e:
        print(f"ERROR: {e}")
        return 2
    finally:
        led.close()


if __name__ == "__main__":
    sys.exit(main())
