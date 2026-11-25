# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Solution check of lab 2.1. From labs/: uv run solutions/check_D2_1.py"""
import json

from _run import LABS, expect, kit

code, out = kit("evalstats.py", "files/D2_1/eval_log.jsonl", "--out", "work/stats")
expect("the statistics tool runs on the evaluation log", code == 0, out)
s = json.loads((LABS / "work" / "stats.json").read_text(encoding="utf-8"))["slices"]
expect("overall: 75/80 urgent, 0.94 (0.86 to 0.97)", (s["all"]["urgent_found"], s["all"]["urgent_total"], s["all"]["urgent_low"], s["all"]["urgent_high"]) == (75, 80, 0.86, 0.97))
expect("livestock: 8/12, 0.67 (0.39 to 0.86), small", (s["species_group=livestock"]["urgent_found"], s["species_group=livestock"]["urgent_total"], s["species_group=livestock"]["urgent_low"], s["species_group=livestock"]["urgent_high"], s["species_group=livestock"]["small"]) == (8, 12, 0.39, 0.86, True))
expect("mixed: 24 messages, accuracy 0.79", (s["lang=mixed"]["n"], s["lang=mixed"]["accuracy"]) == (24, 0.79))
expect("12 messages overlap the development set, all tagged right", (s["in_dev_set=true"]["n"], s["in_dev_set=true"]["accuracy"]) == (12, 1.0))
expect("without the overlap: accuracy 0.93, urgent 73/78", (s["in_dev_set=false"]["accuracy"], s["in_dev_set=false"]["urgent_found"], s["in_dev_set=false"]["urgent_total"]) == (0.93, 73, 78))
for kind, doc in (("report", "solutions/D2_1_report.md"), ("card", "solutions/D2_1_card.md")):
    code, out = kit("cardcheck.py", kind, doc, "--stats", "work/stats.json")
    expect(f"the reference {kind} passes the checker", code == 0, out)
code, out = kit("cardcheck.py", "card", "files/D2_2/draft_unassisted.md", "--stats", "work/stats.json")
expect("a report draft is not a card: the card checker lists the missing sections", code == 1 and "no section on intended use" in out, out)
for f in ("stats.json", "stats.md"):
    (LABS / "work" / f).unlink()
print("PASS lab 2.1")
