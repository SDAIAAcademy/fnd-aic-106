# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check an experiment report or a model card against the evaluation statistics.

From labs/ (run kit/evalstats.py first: it writes work/stats.json):
    uv run kit/cardcheck.py report work/report.md
    uv run kit/cardcheck.py card work/card.md
    uv run kit/cardcheck.py card work/card.md --stats work/stats_v2.json

Checks the sections each document needs; that every rate (a number such as 0.94) and every count
(such as 8/12) is one the statistics contain; that each rate in the results comes with its count;
that the document names every slice the statistics show as weaker (an interval wholly below the
overall rate, or accuracy ten points below) and any overlap with development data; and, for a
card, that owner, reviewer and approver are three different roles. It is a peer's first pass,
not the peer checklist.
"""
from __future__ import annotations

import argparse
import json
import re
import sys

import common as C

REPORT = {"question or summary": ("question", "summary", "result in brief"), "setup": ("setup", "method", "data"),
          "results": ("result",), "uncertainty": ("uncertain", "confidence", "interval"),
          "limits": ("limit", "threat", "caveat"), "next steps": ("next", "repeat")}
CARD = {"intended use": ("intended use", "what it is for", "use"), "out of scope": ("out of scope", "not for"),
        "evaluation data": ("evaluation data", "data"), "results by slice": ("result",),
        "known limits": ("limit",), "ethical considerations": ("ethic",)}
SLICE_WORDS = {"lang=mixed": ("mixed",), "lang=ar": ("arabic",), "lang=en": ("english",), "species_group=livestock": ("livestock",),
               "species_group=other": ("other animals", "birds", "small animals", "other species"),
               "species_group=companion": ("cats and dogs", "companion"), "length=short": ("short",), "length=long": ("long",)}


def known_numbers(stats: dict) -> tuple[set[str], set[str]]:
    rates, counts = set(), set()
    for s in stats["slices"].values():
        for k in ("accuracy", "urgent_recall", "urgent_low", "urgent_high"):
            if s.get(k) is not None:
                rates.add(f"{s[k]:.2f}")
        counts.add(f"{s['urgent_found']}/{s['urgent_total']}")
        counts.add(str(s["n"]))
        counts.add(str(s["urgent_total"]))
        counts.add(str(s["urgent_found"]))
        counts.add(str(s["false_urgent"]))
    rates.add(f"{stats['latency_median_s']:.2f}")
    rates.add(f"{stats['latency_p95_s']:.2f}")
    return rates, counts


def weak_slices(stats: dict) -> list[str]:
    allv = stats["slices"]["all"]
    out = []
    for name, s in stats["slices"].items():
        if name == "all" or name.startswith("in_dev_set"):
            continue
        if (s["urgent_total"] and s["urgent_high"] < allv["urgent_recall"]) or s["accuracy"] <= allv["accuracy"] - 0.10:
            out.append(name)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["report", "card"])
    ap.add_argument("doc")
    ap.add_argument("--stats", default=str(C.LABS / "work" / "stats.json"))
    a = ap.parse_args()
    stats = json.loads(C.read(a.stats))
    text = C.read(a.doc)
    low = text.lower()
    rep = C.Report(f"{a.kind}: {a.doc}")
    secs = C.sections(text)
    for label, keys in (REPORT if a.kind == "report" else CARD).items():
        rep.need(C.find_section(secs, *keys) is not None, f"no section on {label}")
    rates, counts = known_numbers(stats)
    for r in sorted(set(re.findall(r"(?<![\d.])[01]\.\d{2}(?!\d)", text))):
        rep.need(r in rates, f"{r} is not a rate in the statistics: copy it from the stats table")
    for c in sorted(set(re.findall(r"(?<![\d/])\d+/\d+(?![\d/])", text))):
        rep.need(c in counts, f"{c} is not a count in the statistics")
    res = next((n for n in secs if n.startswith("result") and "brief" not in n), None)
    if res:
        for line in secs[res].splitlines():
            if re.search(r"(?<![\d.])0\.\d{2}", line) and not re.search(r"\d+/\d+|\b\d+ of \d+\b|\|\s*\d+\s*\|", line):
                rep.need(False, f"a rate without its count: \"{line.strip()[:70]}\"")
    for name in weak_slices(stats):
        words = SLICE_WORDS.get(name, (name.split("=")[-1],))
        rep.need(any(w in low for w in words), f"the statistics show {name} as weaker: say so, with its count")
    dev = stats["slices"].get("in_dev_set=true")
    if dev and dev["n"]:
        rep.need("development" in low or "dev set" in low, f"{dev['n']} test messages are also in the development set: report it")
    rep.need("interval" in low, "state the uncertainty: give the 95% intervals")
    if a.kind == "card":
        roles = {}
        for key in ("owner", "reviewed by", "approved by"):
            m = re.search(rf"^\W*{key}\W*:\s*(.+)$", text, flags=re.I | re.M)
            rep.need(bool(m), f"no '{key.capitalize()}:' line")
            if m:
                roles[key] = m.group(1).strip().lower()
        rep.need(len(set(roles.values())) == len(roles), "owner, reviewer and approver must be three different roles")
    rep.note(f"{len(weak_slices(stats))} weaker slices in the statistics: {', '.join(weak_slices(stats)) or 'none'}")
    return rep.finish()


if __name__ == "__main__":
    sys.exit(main())
