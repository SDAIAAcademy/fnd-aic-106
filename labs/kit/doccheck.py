# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Prose checks for the labs: a small stand-in for a style linter such as Vale.

From labs/:
    uv run kit/doccheck.py outlines work/outlines.md
    uv run kit/doccheck.py bluf work/rewrite.md
    uv run kit/doccheck.py agents work/AGENTS.md

It checks form, not truth: whether each outline names its reader, purpose and sections; whether
an update puts its bottom line first, uses the glossary's terms and states uncertainty with a
number; whether an agent context file has the parts an agent needs. A person still reads it.
"""
from __future__ import annotations

import csv
import re
import sys

import common as C

HEDGES = ["quite", "fairly", "significantly", "very", "much more", "generally", "somewhat", "rather", "seems", "seem"]
ASK = ["approve", "decide", "choose", "sign", "agree", "confirm", "need your", "we ask", "please"]


def glossary_terms() -> list[tuple[str, list[str]]]:
    with (C.FILES / "D1_1" / "glossary.csv").open(encoding="utf-8") as f:
        return [(r["term_en"], [a for a in r["avoid"].split(";") if a]) for r in csv.DictReader(f)]


def check_outlines(path: str) -> int:
    rep = C.Report(f"outlines: {path}")
    text = C.read(path)
    blocks = re.split(r"^##\s+", text, flags=re.M)[1:]
    rep.need(len(blocks) == 5, f"expected five '## ' outlines, found {len(blocks)}")
    for b in blocks:
        head = b.splitlines()[0].strip()
        low = b.lower()
        for field in ("reader:", "purpose:", "document:", "sections:"):
            rep.need(field in low, f"{head}: no '{field[:-1].capitalize()}:' line")
        items = re.findall(r"^\s*(?:[-*]|\d+\.)\s+\S", b.split("ections:", 1)[-1], flags=re.M)
        rep.need(len(items) >= 4, f"{head}: list at least four sections under Sections: (found {len(items)})")
        rep.note(f"{head}: {len(items)} sections")
    return rep.finish()


def check_bluf(path: str) -> int:
    rep = C.Report(f"bottom line first: {path}")
    text = C.read(path)
    paras = C.paragraphs(text)
    rep.need(bool(paras), "no paragraphs found")
    if not paras:
        return rep.finish()
    first = paras[0]
    fw = C.words(first)
    total = len(C.words("\n\n".join(paras)))
    rep.note(f"first paragraph {len(fw)} words; whole text {total} words")
    rep.need(len(fw) <= 60, f"first paragraph has {len(fw)} words: the bottom line fits in 60")
    rep.need(any(a in first.lower() for a in ASK), "the first paragraph does not say what you ask the reader to do")
    rep.need(bool(C.NUMBER.search(first)), "the first paragraph has no number: say how much, how many or by when")
    rep.need(total <= 250, f"{total} words: an update of this kind fits in 250")
    low = text.lower()
    for term, avoid in glossary_terms():
        for a in avoid:
            if re.search(r"(?<![\w-])" + re.escape(a.lower()) + r"(?![\w-])", low):
                rep.need(False, f"'{a}': the glossary term is '{term}'")
    body = "\n\n".join(paras)
    for s in C.sentences(body):
        hs = [h for h in HEDGES if re.search(r"\b" + re.escape(h) + r"\b", s.lower())]
        if hs and not C.NUMBER.search(s):
            rep.need(False, f"vague without a number ({', '.join(hs)}): \"{s[:70]}\"")
    sl = [len(C.words(s)) for s in C.sentences(body)]
    if sl:
        avg = sum(sl) / len(sl)
        rep.note(f"average sentence {avg:.1f} words")
        rep.need(avg <= 22, f"sentences average {avg:.1f} words: aim for 22 or fewer")
    return rep.finish()


def check_agents(path: str) -> int:
    rep = C.Report(f"agent context file: {path}")
    secs = C.sections(C.read(path))
    for label, keys in (("what the project is", ("overview", "project", "what")),
                        ("setup and run commands", ("setup", "run", "commands", "build")),
                        ("how to test", ("test", "check")),
                        ("conventions", ("convention", "style", "code")),
                        ("data rules", ("data", "privacy", "security"))):
        rep.need(C.find_section(secs, *keys) is not None, f"no section on {label}")
    body = "\n".join(secs.values()).lower()
    rep.need("uv run" in body, "give the exact commands, as typed (uv run ...)")
    rep.need("synthetic" in body or "public" in body, "say which data an agent may read and send")
    return rep.finish()


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] not in ("outlines", "bluf", "agents"):
        print(__doc__)
        return 2
    return {"outlines": check_outlines, "bluf": check_bluf, "agents": check_agents}[sys.argv[1]](sys.argv[2])


if __name__ == "__main__":
    sys.exit(main())
