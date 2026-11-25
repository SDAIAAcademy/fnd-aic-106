# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Setup check: from labs/, `uv run kit/setup_check.py`. Prints what is missing, then `setup: ok`."""
from __future__ import annotations

import platform
import shutil
import sys

import common as C

NEEDED = [
    "D1_1/scenarios.md", "D1_1/status_update.md", "D1_1/glossary.csv",
    "urgency-tagger/pyproject.toml", "urgency-tagger/data/test_set.csv",
    "D1_3/comparison.csv", "D1_3/context.md", "D2_1/eval_log.jsonl", "D2_2/draft_unassisted.md",
]

missing = [n for n in NEEDED if not (C.FILES / n).exists()]
print(f"python {platform.python_version()}")
print(f"uv found: {'yes' if shutil.which('uv') else 'no'}")
for n in missing:
    print(f"missing: files/{n}")
(C.LABS / "work").mkdir(exist_ok=True)
print("work folder: labs/work (git ignores it)")
print("setup: ok" if not missing and shutil.which("uv") else "setup: fix the lines above")
sys.exit(0 if not missing else 1)
