# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Solution check of lab 1.1. From labs/: uv run solutions/check_D1_1.py"""
from _run import expect, kit

code, out = kit("doccheck.py", "bluf", "files/D1_1/status_update.md")
expect("the supplied status update fails the bottom-line check", code == 1 and "12 to fix" in out, out)
for planted in ("'critical'", "'emergency'", "'catch rate'", "'sensitivity'", "does not say what you ask"):
    expect(f"the check reports the planted problem {planted}", planted in out, out)
code, out = kit("doccheck.py", "bluf", "solutions/D1_1_rewrite.md")
expect("the reference rewrite passes", code == 0, out)
code, out = kit("doccheck.py", "outlines", "solutions/D1_1_outlines.md")
expect("the reference outlines pass", code == 0 and out.count("6 sections") == 5, out)
print("PASS lab 1.1")
