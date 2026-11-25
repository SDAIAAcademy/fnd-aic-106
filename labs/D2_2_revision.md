---
course: "Technical Writing for Data and AI Work"
code: "FND-AIC-106"
version: "2027.1.0"
lab: "2.2"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-aic-106/labs/D2_2_revision.html"
---

# Lab 2.2 · Unassisted draft against assisted revision

Compare your AI-off report with an assisted revision claim by claim, keep a revision log, disclose the assistance and write the repository's agent context file

Day 2 · Session 2: Writing with an assistant

### You leave with

- A revision log of every sentence an assisted revision changed in your AI-off report: the verdict, what you checked it against and how.
- A final version with a disclosure line, and an `AGENTS.md` context file for the tagger repository.

## What you need

[**D2_2/draft_unassisted.md**An AI-off report draft, for anyone without their own from lab 2.1.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/D2_2/draft_unassisted.md) [**D2_1/eval_log.jsonl**The evidence every claim is checked against.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/D2_1/eval_log.jsonl)

Your own draft is `work/report.md` from lab 2.1; if you have none, use the supplied draft. The assisted revision comes from `kit/stand_in_revise.py`, a scripted stand-in: no model runs in this course's files, and the stand-in makes the kinds of change assisted revisions of reports often make.

> **AI in this lab: full, and logged.** The clinics' rule, modelled on SDAIA's Generative AI Guidelines for Government, is that only Public data goes into a generative AI tool. The case files are synthetic and Public. If you revise with an approved assistant in the stretch, paste nothing else, and log that revision the same way.

## Steps

### 1 · Produce the assisted revision of your draft 5 min

```
uv run kit/stand_in_revise.py work/report.md
```

With the supplied draft, copy `files/D2_2/draft_unassisted.md` to `work/report.md` first, so every command on this page works as written. It writes `work/revision_assisted.md`. Read it once as its reader would: is it better?

### 2 · Run the claim diff 10 min

```
uv run kit/claimdiff.py work/report.md work/revision_assisted.md
```

It lists every sentence removed, added or changed, flags numbers, sources, stronger claims and dropped limits, and writes `work/revision_log.csv` with a row per change.

### 3 · Check each changed claim and log it 20 min

For each row fill `verdict` (kept, corrected, removed or restored), `checked_against` (the file or source) and `how_checked`. Check numbers against `kit/evalstats.py`; look for every cited document in the course files. An unflagged change is still a claim: read it.

### 4 · Write the final version and its disclosure line 10 min

Keep what the revision improved, undo what it broke, and end with one line that starts `Disclosure:`, saying what the assistance did and how you checked it.

### 5 · Write the agent context file for the tagger 10 min

In `work/AGENTS.md`: what the project is, the setup and run commands as typed, how to test, the code conventions, and the data rules an agent must follow. Then check it:

```
uv run kit/doccheck.py agents work/AGENTS.md
```

### 6 · Run the log checker and fix it 5 min

```
uv run kit/logcheck.py work/revision_log.csv work/final.md
```

### ✱ Stretch

Revise your draft with an approved assistant, Public text only, save it as `work/revision_real.md`, and run the claim diff and the log on it too. Which kinds of change did it make?

## Check yourself

1. Which change would a reader in a hurry never notice, and what would it have cost?
2. How did you prove a cited document does not exist?
3. Which improvements of the revision did you keep, and how did you know they changed no claim?
