"""Shared helpers of the lab kit: Markdown sections, sentences, numbers and the report lines."""
from __future__ import annotations

import re
import sys
from pathlib import Path

LABS = Path(__file__).resolve().parents[1]
FILES = LABS / "files"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

NUMBER = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*(?:\.\d+)?%?(?![\w])")
DECIMAL = re.compile(r"(?<![\w.])\d+\.\d+(?![\w])")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")


def read(path: str | Path) -> str:
    p = Path(path)
    if not p.exists():
        sys.exit(f"error: {p.as_posix()} not found")
    return p.read_text(encoding="utf-8")


def strip_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def sections(text: str) -> dict[str, str]:
    """Map each heading (lower case, without #) to the text under it."""
    out: dict[str, list[str]] = {"": []}
    cur = ""
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            cur = m.group(2).strip().lower()
            out.setdefault(cur, [])
        else:
            out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def find_section(secs: dict[str, str], *keywords: str) -> str | None:
    for name in secs:
        if any(k in name for k in keywords):
            return name
    return None


def paragraphs(text: str) -> list[str]:
    body = [p.strip() for p in re.split(r"\n\s*\n", strip_code(text))]
    return [p for p in body if p and not HEADING.match(p.splitlines()[0])]


def sentences(text: str) -> list[str]:
    flat = re.sub(r"\s+", " ", strip_code(text))
    parts = re.split(r"(?<=[.!?؟])\s+(?=[A-Z؀-ۿ\d(])", flat)
    return [s.strip() for s in parts if s.strip()]


def words(text: str) -> list[str]:
    return re.findall(r"[\w'%.-]+", strip_code(text))


def decimals(text: str) -> list[str]:
    return DECIMAL.findall(text)


class Report:
    """Collects findings and prints PASS or the list, like the solution scripts expect."""

    def __init__(self, title: str):
        self.title = title
        self.problems: list[str] = []
        self.notes: list[str] = []

    def need(self, ok: bool, problem: str) -> None:
        if not ok:
            self.problems.append(problem)

    def note(self, text: str) -> None:
        self.notes.append(text)

    def finish(self) -> int:
        print(f"== {self.title}")
        for n in self.notes:
            print(f"   {n}")
        for p in self.problems:
            print(f"   FIX: {p}")
        print("PASS" if not self.problems else f"{len(self.problems)} to fix")
        return 0 if not self.problems else 1
