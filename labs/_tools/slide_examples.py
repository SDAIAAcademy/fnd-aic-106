# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Figures of the slides' parallel example, which is not lab data.

From labs/:  uv run _tools/slide_examples.py

The parallel example is the clinics' pharmacy team (fictional): a weekly reorder forecast that
flags medicines at risk of running out. Two methods, A (a seasonal average) and B (a boosted-tree
model), were scored on 60 synthetic weeks in which a medicine ran out. The counts below are
written for the slides; every derived figure is computed here so the slides quote this output.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "files" / "urgency-tagger"))
from urgency_tagger.metrics import wilson  # noqa: E402

runouts = 60
caught = {"Method A": 41, "Method B": 52}
cost_per_run = {"Method A": 0.0, "Method B": 3.50}  # SAR per weekly run, synthetic
minutes = {"Method A": 1, "Method B": 14}
budget = 20.0  # SAR a month
for m, k in caught.items():
    lo, hi = wilson(k, runouts)
    month = cost_per_run[m] * 52 / 12
    print(f"{m}: caught {k}/{runouts} = {k / runouts:.2f} (95% interval {lo:.2f} to {hi:.2f}); "
          f"SAR {month:.2f} a month at one run a week; {minutes[m]} min a run")
runs_in_budget = budget / cost_per_run["Method B"]
print(f"Method B runs inside SAR {budget:.0f} a month: {runs_in_budget:.2f} runs, so daily runs (about 30) would break it")
print(f"A run at SAR 4.62 would break the budget at weekly runs: {4.62 * 52 / 12:.2f} a month")
lo, hi = wilson(7, 9)
print(f"A small slice: 7/9 = {7 / 9:.2f} (95% interval {lo:.2f} to {hi:.2f})")
