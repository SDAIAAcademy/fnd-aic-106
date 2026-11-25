# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Solution check of lab 2.2. From labs/: uv run solutions/check_D2_2.py

Runs the scripted stand-in on the fallback draft, the claim diff on the pair, and the log checker
on the reference log and final version; confirms that the six planted changes are all found and
that the stand-in's revision, taken as final, fails.
"""
from _run import LABS, expect, kit

code, out = kit("stand_in_revise.py", "files/D2_2/draft_unassisted.md", "--out", "work/revision_assisted.md")
expect("the stand-in writes a revision and says no model ran", code == 0 and "no model ran" in out, out)
code, out = kit("claimdiff.py", "files/D2_2/draft_unassisted.md", "work/revision_assisted.md", "--log", "work/revision_log.csv")
expect("the claim diff lists 9 changes, 6 flagged", "9 changes, 6 flagged" in out, out)
planted = {
    "added overclaim": "added [certainty]",
    "dropped interval": "urgent recall of 0.94.",
    "invented source": "added [source]",
    "changed accuracy": "Accuracy was 0.97.",
    "dropped livestock limit": "removed [number limit]",
    "dropped development-set limit": "removed [limit]",
}
for name, mark in planted.items():
    expect(f"planted change found: {name}", mark in out, out)
code, out = kit("logcheck.py", "solutions/D2_2_revision_log.csv", "solutions/D2_2_final.md")
expect("the reference log and final version pass", code == 0, out)
code, out = kit("logcheck.py", "work/revision_log.csv", "work/revision_assisted.md")
expect("the stand-in revision taken as final fails on the invented source and the overclaim",
       code == 1 and "EV-N7 is cited but exists nowhere" in out and "'relied on'" in out, out)
code, out = kit("doccheck.py", "agents", "solutions/D2_2_AGENTS.md")
expect("the reference agent context file passes", code == 0, out)
for f in ("revision_assisted.md", "revision_log.csv"):
    (LABS / "work" / f).unlink()
print("PASS lab 2.2")
