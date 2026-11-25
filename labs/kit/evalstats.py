# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Statistics of an evaluation log, overall and by slice, with counts and 95% intervals.

From labs/:
    uv run kit/evalstats.py files/D2_1/eval_log.jsonl
    uv run kit/evalstats.py files/capstone/eval_log_v2.jsonl --out work/stats_v2

Prints the run record, then one table: for each slice the number of messages, accuracy, the
urgent messages found out of all urgent ones, urgent recall and its 95% Wilson interval. Writes
the same table to work/stats.md (to paste into a report) and work/stats.json (which the card
checker reads to trace your numbers). A slice with fewer than 20 urgent messages is marked
"small": its interval is wide, and a report must say so.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import common as C

FIELDS = ("lang", "species_group", "length", "in_dev_set")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (c - h, c + h)


def stats(items: list[dict]) -> dict:
    n = len(items)
    acc = sum(i["gold"] == i["pred"] for i in items) / n if n else 0.0
    urgent = [i for i in items if i["gold"] == "urgent"]
    k = sum(i["pred"] == "urgent" for i in urgent)
    lo, hi = wilson(k, len(urgent))
    false_urgent = sum(1 for i in items if i["gold"] != "urgent" and i["pred"] == "urgent")
    return {"n": n, "accuracy": round(acc, 2), "urgent_found": k, "urgent_total": len(urgent),
            "urgent_recall": round(k / len(urgent), 2) if urgent else None,
            "urgent_low": round(lo, 2), "urgent_high": round(hi, 2), "false_urgent": false_urgent,
            "small": len(urgent) < 20}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("log")
    ap.add_argument("--out", default=str(C.LABS / "work" / "stats"))
    a = ap.parse_args()
    records = [json.loads(l) for l in C.read(a.log).splitlines() if l.strip()]
    run = next((r for r in records if r.get("type") == "run"), {})
    items = [r for r in records if r.get("type") == "item"]
    print("run:", ", ".join(f"{k}={v}" for k, v in run.items() if k != "type"))
    rows = [("all", stats(items))]
    for f in FIELDS:
        for v in sorted({str(i[f]).lower() for i in items}):
            rows.append((f"{f}={v}", stats([i for i in items if str(i[f]).lower() == v])))
    lat = sorted(i["latency_ms"] for i in items)
    p95 = lat[max(1, math.ceil(0.95 * len(lat))) - 1] / 1000 if lat else 0.0
    med = lat[max(1, math.ceil(0.5 * len(lat))) - 1] / 1000 if lat else 0.0
    head = "| Slice | Messages | Accuracy | Urgent found | Urgent recall | 95% interval | Note |"
    lines = [head, "|---|---|---|---|---|---|---|"]
    for name, s in rows:
        rec = f"{s['urgent_recall']:.2f}" if s["urgent_recall"] is not None else "n/a"
        lines.append(f"| {name} | {s['n']} | {s['accuracy']:.2f} | {s['urgent_found']}/{s['urgent_total']} | {rec} | "
                     f"{s['urgent_low']:.2f} to {s['urgent_high']:.2f} | {'small' if s['small'] else ''} |")
    lines.append("")
    lines.append(f"Time to a tag: median {med:.2f} s, 95th percentile {p95:.2f} s. False urgent tags: {rows[0][1]['false_urgent']}.")
    print("\n".join(lines))
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    payload = {"run": run, "slices": {n: s for n, s in rows}, "latency_median_s": round(med, 2), "latency_p95_s": round(p95, 2)}
    out.with_suffix(".json").write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    rel = out.relative_to(C.LABS).as_posix() if out.is_relative_to(C.LABS) else out.name
    print(f"wrote {rel}.md and {rel}.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
