# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Solution check of lab 1.3. From labs/: uv run solutions/check_D1_3.py"""
import csv

from _run import LABS, expect, kit

rows = {r["system"]: r for r in csv.DictReader((LABS / "files" / "D1_3" / "comparison.csv").open(encoding="utf-8"))}
expect("Model L urgent recall 0.94, interval 0.86 to 0.97",
       (rows["Model L"]["urgent_recall"], rows["Model L"]["urgent_recall_low"], rows["Model L"]["urgent_recall_high"]) == ("0.94", "0.86", "0.97"))
expect("Model S interval lies below 0.90", float(rows["Model S"]["urgent_recall_high"]) < 0.90)
cost_l = 9000 / 1000 * float(rows["Model L"]["cost_sar_per_1000_messages"])
expect(f"Model L costs SAR {cost_l:.2f} a month, inside SAR 400", abs(cost_l - 337.68) < 0.01 and cost_l < 400)
expect("Model L's 95th-percentile time is inside 10 seconds", float(rows["Model L"]["latency_p95_s"]) < 10)
expect("10,661 messages a month cost more than SAR 400", 10661 / 1000 * float(rows["Model L"]["cost_sar_per_1000_messages"]) > 400 > 10660 / 1000 * float(rows["Model L"]["cost_sar_per_1000_messages"]))

code, out = kit("memocheck.py", "solutions/D1_3_memo.md")
expect("the reference memo passes the memo check", code == 0, out)
ref = (LABS / "solutions" / "D1_3_memo.md").read_text(encoding="utf-8")
work = LABS / "work"
work.mkdir(exist_ok=True)
(work / "memo_untraced.md").write_text(ref.replace("0.94 (0.86 to 0.97)", "0.95 (0.86 to 0.97)"), encoding="utf-8")
code, out = kit("memocheck.py", "work/memo_untraced.md")
expect("a number that is not in the evidence is reported", code == 1 and "0.95 is not in the evidence" in out, out)
(work / "memo_untraced.md").unlink()
print("PASS lab 1.3")
