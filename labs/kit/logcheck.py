# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check a revision log and the final version it led to.

From labs/:
    uv run kit/logcheck.py work/revision_log.csv work/final.md
    uv run kit/logcheck.py work/revision_log.csv work/final.md --log files/capstone/eval_log_v2.jsonl

The log: every row has a verdict (kept, corrected, removed or restored), and every row the claim
diff flagged says what it was checked against and how. The final version: a disclosure line
("Disclosure:" or "AI assistance:"); no document code that exists nowhere in the course files;
no stronger claim than the evidence ("relied on", "without a person", "always"); and every rate
and count is one the evaluation log gives.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys

import common as C
import evalstats as E

VERDICTS = {"kept", "corrected", "removed", "restored"}
CODE = re.compile(r"\b[A-Z]{2,}-[A-Z]?\d+\b")
CERTAIN = ("always", "never misses", "relied on", "guarantee", "without a person", "without review", "certainly", "all cases")


def course_codes() -> set[str]:
    codes = set()
    for p in C.FILES.rglob("*"):
        if p.is_file() and p.suffix in {".md", ".csv", ".jsonl", ".json", ".txt", ".toml", ".py"}:
            codes |= set(CODE.findall(p.read_text(encoding="utf-8", errors="replace")))
    return codes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("revlog")
    ap.add_argument("final")
    ap.add_argument("--log", default=str(C.FILES / "D2_1" / "eval_log.jsonl"))
    a = ap.parse_args()
    rep = C.Report(f"revision log {a.revlog} and final {a.final}")
    with open(a.revlog, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    rep.need(bool(rows), "the revision log has no rows: run kit/claimdiff.py first")
    for r in rows:
        cid = r.get("claim_id", "?")
        v = (r.get("verdict") or "").strip().lower()
        rep.need(v in VERDICTS, f"{cid}: verdict must be one of {', '.join(sorted(VERDICTS))}")
        if (r.get("flags") or "").strip():
            rep.need(bool((r.get("checked_against") or "").strip()), f"{cid} [{r['flags']}]: say what you checked it against")
            rep.need(bool((r.get("how_checked") or "").strip()), f"{cid} [{r['flags']}]: say how you checked it")
    flagged = sum(1 for r in rows if (r.get("flags") or "").strip())
    rep.note(f"{len(rows)} rows, {flagged} flagged")
    final = C.read(a.final)
    rep.need(re.search(r"^\W*(disclosure|ai assistance)\s*:", final, flags=re.I | re.M) is not None,
             "add a disclosure line: 'Disclosure:' or 'AI assistance:', saying what the assistant did and what you checked")
    known = course_codes()
    for code in sorted(set(CODE.findall(final))):
        rep.need(code in known, f"{code} is cited but exists nowhere in the course files: an invented source")
    low = final.lower()
    for w in CERTAIN:
        rep.need(w not in low, f"'{w}': a stronger claim than the evaluation supports")
    records = [json.loads(l) for l in C.read(a.log).splitlines() if l.strip()]
    items = [r for r in records if r.get("type") == "item"]
    vals, counts = set(), set()
    groups = [items] + [[i for i in items if str(i[f]).lower() == v] for f in E.FIELDS for v in {str(i[f]).lower() for i in items}]
    for g in groups:
        s = E.stats(g)
        for k in ("accuracy", "urgent_recall", "urgent_low", "urgent_high"):
            if s[k] is not None:
                vals.add(f"{s[k]:.2f}")
        counts |= {f"{s['urgent_found']}/{s['urgent_total']}", f"{s['urgent_found']} of {s['urgent_total']}"}
    body = re.sub(r"^\W*(disclosure|ai assistance)\s*:.*$", "", final, flags=re.I | re.M)
    for r in sorted(set(re.findall(r"(?<![\d.])[01]\.\d{2}(?!\d)", body))):
        rep.need(r in vals or r == "0.90", f"{r} is not a rate in the evaluation log")
    for c in sorted(set(re.findall(r"\b\d+/\d+\b|\b\d+ of \d+\b", body))):
        rep.need(c in counts, f"{c} is not a count in the evaluation log")
    return rep.finish()


if __name__ == "__main__":
    sys.exit(main())
