# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""A scripted stand-in for an assisted revision. No model runs: this script edits your draft the
way assisted revisions of reports often do, so that every participant has a revision to check.

From labs/:
    uv run kit/stand_in_revise.py work/report.md
    uv run kit/stand_in_revise.py files/D2_2/draft_unassisted.md --out work/revision_assisted.md

It tightens the wording (shorter phrases, no throat-clearing), and, like a fluent assistant, it
may also change what the draft claims. Which edits it made is not printed: finding them is the
lab. The same draft always gives the same revision.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import common as C

TIGHTEN = [("In order to ", "To "), ("in order to ", "to "), ("It is important to note that ", ""),
           ("A number of ", "Most of "), ("a number of ", "several "), ("utilise", "use"), ("Overall accuracy was", "Accuracy was")]
CLAIM = "The tagger can be relied on to triage emergencies without a person reading the message."
SOURCE = " This matches the clinics' triage evaluation note EV-N7."
INTERVAL = re.compile(r"\s*\((?:95% interval |interval )?(?:from )?[01]\.\d\d to [01]\.\d\d\)|,? with an interval from [01]\.\d\d to [01]\.\d\d|,? 95% interval (?:from )?[01]\.\d\d to [01]\.\d\d")
RATE = re.compile(r"(?<![\d.])0\.(\d\d)(?!\d)")


def drop_sentence(text: str, word: str) -> str:
    for para in re.split(r"\n\s*\n", text):
        if word in para.lower() and not para.lstrip().startswith("#"):
            flat = re.sub(r"\s*\n\s*", " ", para)
            sents = C.sentences(flat)
            keep = [s for s in sents if word not in s.lower()]
            if len(keep) < len(sents):
                return text.replace(para, "\n".join(wrap(" ".join(keep))), 1) if keep else text.replace(para + "\n\n", "", 1)
    return text


def wrap(s: str, width: int = 98) -> list[str]:
    out, line = [], ""
    for w in s.split():
        if len(line) + len(w) + 1 > width:
            out.append(line)
            line = w
        else:
            line = f"{line} {w}".strip()
    return out + ([line] if line else [])


def revise(text: str) -> str:
    for a, b in TIGHTEN:
        text = re.sub(r"\s+".join(map(re.escape, a.split())) + (r"\s+" if a.endswith(" ") else ""), b, text)
    text = re.sub(r"([.!?]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), text)
    paras = re.split(r"(\n\s*\n)", text)
    body = [i for i, p in enumerate(paras) if p.strip() and not p.lstrip().startswith("#") and not p.strip().startswith(("To:", "A first draft"))]
    if body:
        i = body[0]
        flat = " ".join(wrap(re.sub(r"\s*\n\s*", " ", paras[i])))
        sents = C.sentences(flat)
        if sents:
            sents.insert(1, CLAIM)
            sents[-1] = sents[-1] + SOURCE
            first = INTERVAL.sub("", " ".join(sents), count=1)
            paras[i] = "\n".join(wrap(first))
        text = "".join(paras)
        rest_start = text.find(paras[i]) + len(paras[i])
        head, rest = text[:rest_start], text[rest_start:]
        m = RATE.search(rest)
        if m:
            new = min(99, int(m.group(1)) + 3)
            rest = rest[:m.start()] + f"0.{new:02d}" + rest[m.end():]
        text = head + rest
    text = drop_sentence(text, "livestock")
    text = drop_sentence(text, "development set")
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--out", default=str(C.LABS / "work" / "revision_assisted.md"))
    a = ap.parse_args()
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(revise(C.read(a.draft)).encode("utf-8"))
    rel = out.relative_to(C.LABS).as_posix() if out.is_relative_to(C.LABS) else out.name
    print(f"wrote {rel}: an assisted revision by a scripted stand-in (no model ran)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
