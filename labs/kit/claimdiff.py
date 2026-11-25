# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""List every sentence an assisted revision removed, added or changed, flagging the claims.

From labs/:
    uv run kit/claimdiff.py work/report.md work/revision_assisted.md

Compares the two documents sentence by sentence (tables row by row) and prints each change with
flags: [number] when a number differs or appears, [source] when a document code or citation
appears, [certainty] when words like "always", "relied on" or "without" make a stronger claim,
[limit] when a sentence about a limit or a slice is removed. Writes work/revision_log.csv with one
row per change and empty columns to fill: verdict (kept, corrected, removed, restored), checked
against (the file or source), and how it was checked.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import re
import sys
from pathlib import Path

import common as C

CODE = re.compile(r"\b[A-Z]{2,}-[A-Z]?\d+\b")
CERTAIN = ("always", "never", "relied on", "guarantee", "without a person", "without review", "certainly", "clearly", "all cases")
LIMIT = ("limit", "weaker", "livestock", "mixed", "development set", "small", "interval", "only")


def units(text: str) -> list[str]:
    out = []
    for block in re.split(r"\n\s*\n", text):
        lines = block.strip().splitlines()
        if not lines:
            continue
        if lines[0].lstrip().startswith("|"):
            out += [l.strip() for l in lines if not re.match(r"^\|[-\s|]+\|$", l.strip())]
        elif lines[0].lstrip().startswith("#"):
            out.append(lines[0].strip())
            if len(lines) > 1:
                out += C.sentences(" ".join(lines[1:]))
        else:
            out += C.sentences(" ".join(l.strip() for l in lines))
    return out


def flags(before: str, after: str) -> list[str]:
    f = []
    if sorted(C.NUMBER.findall(before)) != sorted(C.NUMBER.findall(after)):
        f.append("number")
    if set(CODE.findall(after)) - set(CODE.findall(before)):
        f.append("source")
    if any(w in after.lower() and w not in before.lower() for w in CERTAIN):
        f.append("certainty")
    if before and not after and any(w in before.lower() for w in LIMIT):
        f.append("limit")
    return f


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("revision")
    ap.add_argument("--log", default=str(C.LABS / "work" / "revision_log.csv"))
    a = ap.parse_args()
    d, r = units(C.read(a.draft)), units(C.read(a.revision))
    rows = []
    sm = difflib.SequenceMatcher(a=d, b=r, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        before, after = d[i1:i2], r[j1:j2]
        pairs, used = [], set()
        for b in before:
            best, score = None, 0.5
            for j, x in enumerate(after):
                s = difflib.SequenceMatcher(a=b, b=x).ratio()
                if j not in used and s > score:
                    best, score = j, s
            if best is None:
                pairs.append((before.index(b), b, ""))
            else:
                used.add(best)
                pairs.append((best, b, after[best]))
        pairs += [(j, "", x) for j, x in enumerate(after) if j not in used]
        for _, b, x in sorted(pairs, key=lambda p: p[0]):
            kind = "removed" if not x else "added" if not b else "changed"
            rows.append({"claim_id": "", "change": kind, "before": b, "after": x,
                         "flags": " ".join(flags(b, x)), "verdict": "", "checked_against": "", "how_checked": ""})
    for k, row in enumerate(rows, 1):
        row["claim_id"] = f"C{k:02d}"
    for row in rows:
        tag = f" [{row['flags']}]" if row["flags"] else ""
        print(f"{row['claim_id']} {row['change']}{tag}")
        if row["before"]:
            print(f"   before: {row['before'][:110]}")
        if row["after"]:
            print(f"   after:  {row['after'][:110]}")
    flagged = sum(1 for r_ in rows if r_["flags"])
    print(f"{len(rows)} changes, {flagged} flagged as claims to check")
    log = Path(a.log)
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["claim_id"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    rel = log.relative_to(C.LABS).as_posix() if log.is_relative_to(C.LABS) else log.name
    print(f"wrote {rel}: fill verdict, checked_against and how_checked for every row")
    return 0


if __name__ == "__main__":
    sys.exit(main())
