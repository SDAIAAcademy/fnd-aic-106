# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check a decision memo's form and trace its numbers to the evidence.

From labs/:
    uv run kit/memocheck.py work/memo.md
    uv run kit/memocheck.py work/memo.md --evidence files/D1_3/comparison.csv --context files/D1_3/context.md

Checks: one page (450 words or fewer, headings and Working lines not counted); the five sections
of the template; a recommendation in the bottom line; every option named in Options and in
Trade-offs; roles for author and reviewer that differ; numbers in "What would change this".
Every number must come from the evidence or the context, or be shown on a "Working:" line. It
does not score the memo: a partner does that with the five-criterion rubric of the lab page.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys

import common as C

OPTIONS = {"rules": ("rules", "keyword"), "model s": ("model s",), "model l": ("model l",)}


def norm(n: str) -> str:
    n = n.replace(",", "").rstrip("%")
    try:
        return f"{float(n):g}"
    except ValueError:
        return n


def allowed_numbers(evidence: str, context: str) -> set[str]:
    ok = set()
    with open(evidence, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for v in row.values():
                ok.add(norm(v))
    for n in C.NUMBER.findall(C.read(context)):
        ok.add(norm(n))
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("memo")
    ap.add_argument("--evidence", default=str(C.FILES / "D1_3" / "comparison.csv"))
    ap.add_argument("--context", default=str(C.FILES / "D1_3" / "context.md"))
    a = ap.parse_args()
    text = C.read(a.memo)
    rep = C.Report(f"decision memo: {a.memo}")
    lines = text.splitlines()
    working = [l for l in lines if l.strip().lower().startswith("working:")]
    prose = "\n".join(re.sub(r"^\s*\d+\.\s", "", l) for l in lines if l not in working and not C.HEADING.match(l))
    n_words = len(C.words(prose))
    rep.note(f"{n_words} words (one page is 450 or fewer)")
    rep.need(n_words <= 450, f"{n_words} words: cut to one page, 450 or fewer")
    secs = C.sections(text)
    names = {}
    for label, keys in (("Bottom line", ("bottom line",)), ("Options", ("option",)), ("Trade-offs", ("trade",)),
                        ("Recommendation", ("recommend",)), ("What would change this", ("change",))):
        names[label] = C.find_section(secs, *keys)
        rep.need(names[label] is not None, f"no section '{label}'")
    if names["Bottom line"]:
        bl = secs[names["Bottom line"]].lower()
        rep.need("recommend" in bl, "the bottom line does not state the recommendation")
        rep.need(len(C.sentences(bl)) <= 3, "the bottom line is longer than three sentences")
    for sec in ("Options", "Trade-offs"):
        if names[sec]:
            body = secs[names[sec]].lower()
            for opt, keys in OPTIONS.items():
                rep.need(any(k in body for k in keys), f"'{sec}' does not mention {opt}")
    if names["What would change this"]:
        rep.need(len(C.NUMBER.findall(secs[names["What would change this"]])) >= 2,
                 "'What would change this' needs conditions with numbers (a threshold, a volume, a price)")
    head = "\n".join(lines[:6]).lower()
    m_from = re.search(r"from:\s*([^·\n]+)", head)
    m_rev = re.search(r"reviewed by:\s*([^·\n]+)", head)
    rep.need(bool(m_from and m_rev), "name the author (From:) and a reviewer (Reviewed by:) by role")
    if m_from and m_rev:
        rep.need(m_from.group(1).strip() != m_rev.group(1).strip(), "the reviewer must be a different person from the author")
    ok = allowed_numbers(a.evidence, a.context)
    shown = set()
    for w in working:
        for n in C.NUMBER.findall(w):
            shown.add(norm(n))
    untraced = sorted({n for n in C.NUMBER.findall(prose) if norm(n) not in ok and norm(n) not in shown})
    rep.note(f"{len(set(C.NUMBER.findall(prose)))} distinct numbers; {len(working)} Working lines")
    for n in untraced:
        rep.need(False, f"{n} is not in the evidence or the context: show how you got it on a Working: line")
    return rep.finish()


if __name__ == "__main__":
    sys.exit(main())
