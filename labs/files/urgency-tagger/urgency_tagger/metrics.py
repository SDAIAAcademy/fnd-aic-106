"""Metrics for three labels, with a Wilson interval for proportions."""
from __future__ import annotations

import math

LABELS = ("urgent", "soon", "routine")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """95% Wilson score interval for k successes out of n."""
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (c - h, c + h)


def recall(gold: list[str], pred: list[str], label: str) -> tuple[int, int]:
    hits = sum(1 for g, p in zip(gold, pred) if g == label and p == label)
    return hits, sum(1 for g in gold if g == label)


def macro_f1(gold: list[str], pred: list[str]) -> float:
    scores = []
    for lab in LABELS:
        tp = sum(1 for g, p in zip(gold, pred) if g == lab and p == lab)
        fp = sum(1 for g, p in zip(gold, pred) if g != lab and p == lab)
        fn = sum(1 for g, p in zip(gold, pred) if g == lab and p != lab)
        prec = tp / (tp + fp) if tp + fp else 0.0
        rec = tp / (tp + fn) if tp + fn else 0.0
        scores.append(2 * prec * rec / (prec + rec) if prec + rec else 0.0)
    return sum(scores) / len(scores)


def percentile(values: list[float], q: float) -> float:
    """Nearest-rank percentile, q between 0 and 100."""
    s = sorted(values)
    if not s:
        return 0.0
    k = max(1, math.ceil(q / 100 * len(s)))
    return s[k - 1]
