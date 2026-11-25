# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Solution check of lab 1.2. From labs/: uv run solutions/check_D1_2.py

Runs the clean-run test on the reference README (a real run: uv builds a fresh environment for a
fresh copy of the project), then on a copy of it without the config step, which must fail.
"""
from pathlib import Path

from _run import LABS, expect, kit

code, out = kit("readme_run.py", "solutions/D1_2_README.md", "--log", "work/runlog_reference.md")
expect("the reference README passes the clean run", code == 0 and "5 commands run" in out, out)
log = (LABS / "work" / "runlog_reference.md").read_text(encoding="utf-8")
expect("the run log shows the data check line", "check: ok, 30 sample rows, 400 test rows, 2 recorded systems" in log, log)
expect("the run log shows Model L's urgent recall", "urgent recall: 75/80 = 0.94" in log, log)

ref = (LABS / "solutions" / "D1_2_README.md").read_text(encoding="utf-8")
bad = ref.replace("```sh\ncp config.example.toml config.toml\n```\n", "")
work = LABS / "work"
(work / "README_no_config.md").write_text(bad, encoding="utf-8")
code, out = kit("readme_run.py", "work/README_no_config.md", "--log", "work/runlog_no_config.md")
expect("without the config step the clean run fails", code == 1 and "config.toml not found" in out, out)
for f in ("README_no_config.md", "runlog_no_config.md", "runlog_reference.md"):
    (work / f).unlink()
print("PASS lab 1.2")
