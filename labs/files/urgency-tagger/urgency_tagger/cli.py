"""Command line: tag, evaluate, check."""
from __future__ import annotations

import argparse
import csv
import sys
import time
import tomllib
from pathlib import Path

from . import metrics, rules

ROOT = Path(__file__).resolve().parent.parent


def load_config() -> dict:
    path = ROOT / "config.toml"
    if not path.exists():
        sys.exit("error: config.toml not found")
    with path.open("rb") as f:
        return tomllib.load(f)


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def cmd_tag(args, cfg) -> int:
    rows = read_csv(Path(args.file))
    out_dir = ROOT / cfg["output_dir"]
    out_dir.mkdir(exist_ok=True)
    out = out_dir / "tags.csv"
    counts = {lab: 0 for lab in metrics.LABELS}
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "label"])
        for r in rows:
            lab = rules.tag(r["message"])
            counts[lab] += 1
            w.writerow([r["id"], lab])
    print(f"tagged {len(rows)} messages: " + ", ".join(f"{k} {v}" for k, v in counts.items()))
    print(f"wrote {out.relative_to(ROOT).as_posix()}")
    return 0


def predictions(system: str, test: list[dict], cfg) -> tuple[list[str], list[float], list[float]]:
    if system == "rules":
        preds, lat = [], []
        for r in test:
            t0 = time.perf_counter()
            preds.append(rules.tag(r["message"]))
            lat.append(time.perf_counter() - t0)
        return preds, lat, [0.0] * len(test)
    rec = {r["id"]: r for r in read_csv(ROOT / cfg["recorded_dir"] / f"{system.replace('-', '_')}.csv")}
    price = cfg["price_sar_per_1000_tokens"][system.replace("-", "_")]
    preds = [rec[r["id"]]["pred"] for r in test]
    lat = [int(rec[r["id"]]["latency_ms"]) / 1000 for r in test]
    cost = [(int(rec[r["id"]]["tokens_in"]) + int(rec[r["id"]]["tokens_out"])) / 1000 * price for r in test]
    return preds, lat, cost


def cmd_evaluate(args, cfg) -> int:
    test = read_csv(ROOT / cfg["test_set"])
    gold = [r["gold"] for r in test]
    preds, lat, cost = predictions(args.system, test, cfg)
    k, n = metrics.recall(gold, preds, "urgent")
    lo, hi = metrics.wilson(k, n)
    acc = sum(g == p for g, p in zip(gold, preds)) / len(gold)
    print(f"system: {args.system}  test messages: {len(gold)}")
    print(f"urgent recall: {k}/{n} = {k / n:.2f} (95% interval {lo:.2f} to {hi:.2f})")
    print(f"accuracy: {acc:.2f}  macro F1: {metrics.macro_f1(gold, preds):.2f}")
    print(f"cost per 1,000 messages (SAR): {sum(cost) / len(cost) * 1000:.2f}")
    print(f"latency median: {metrics.percentile(lat, 50):.2f} s  p95: {metrics.percentile(lat, 95):.2f} s")
    return 0


def cmd_check(args, cfg) -> int:
    problems = []
    sample = read_csv(ROOT / "data" / "sample_requests.csv")
    test = read_csv(ROOT / cfg["test_set"])
    for r in test:
        if r["gold"] not in metrics.LABELS:
            problems.append(f"{r['id']}: unknown label {r['gold']}")
    systems = 0
    for name in cfg["price_sar_per_1000_tokens"]:
        rec = read_csv(ROOT / cfg["recorded_dir"] / f"{name}.csv")
        systems += 1
        if {r["id"] for r in rec} != {r["id"] for r in test}:
            problems.append(f"{name}: recorded ids differ from the test set")
    for p in problems:
        print("problem:", p)
    status = "ok" if not problems else f"{len(problems)} problems"
    print(f"check: {status}, {len(sample)} sample rows, {len(test)} test rows, {systems} recorded systems")
    return 1 if problems else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="urgency_tagger")
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("tag")
    t.add_argument("file")
    e = sub.add_parser("evaluate")
    e.add_argument("--system", choices=["rules", "model-s", "model-l"], default="rules")
    sub.add_parser("check")
    args = ap.parse_args(argv)
    cfg = load_config()
    return {"tag": cmd_tag, "evaluate": cmd_evaluate, "check": cmd_check}[args.cmd](args, cfg)
