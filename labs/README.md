# Technical Writing for Data and AI Work: the labs

Five writing labs of 60 minutes for SDAIA Academy course **FND-AIC-106**. Each lab is a page in
this folder: the goal, the files, the steps with their minutes, a stretch item, questions to check
yourself and notes for the trainer. Participants write Markdown documents in `work/` (git ignores
it), then run a small checker from `kit/` that reads their document and prints what to fix, or
`PASS`.

All labs use one fictional case, **Tarthuth Veterinary Clinics**, and its small Python project,
the request urgency tagger (`files/urgency-tagger/`). Every file is synthetic, generated with a
fixed seed by `_tools/make_case.py`. People appear by role only; owners, animals and messages by
code. The tagger's keyword rules are real code that runs; the outputs of Model S and Model L are
simulated and recorded, and no lab calls a model.

## What a participant needs

- A laptop with a text editor that saves UTF-8 Markdown, and a terminal.
- `uv`. From this folder, `uv run kit/setup_check.py` must end with `setup: ok`; uv fetches Python
  3.11 or later if it is missing. The kit uses the Python standard library only.
- No account, no key, no model download, no `.env` file. The assisted revision of lab 2.2 is made
  by `kit/stand_in_revise.py`, a scripted stand-in; an approved assistant may be used in its
  stretch with Public text only.

## Labs, starting files and references

Every lab starts from supplied files and needs no other lab's result.

| Lab | Page | Starts from | Kit | Reference for the trainer |
|---|---|---|---|---|
| 1.1 | `D1_1_bluf.html` | `files/D1_1/` | `doccheck.py outlines`, `doccheck.py bluf` | `solutions/D1_1_outlines.md`, `solutions/D1_1_rewrite.md` |
| 1.2 | `D1_2_readme.html` | `files/urgency-tagger/` | `readme_run.py` | `solutions/D1_2_README.md` |
| 1.3 | `D1_3_memo.html` | `files/D1_3/` | `memocheck.py` | `solutions/D1_3_memo.md` |
| 2.1 | `D2_1_report_card.html` | `files/D2_1/eval_log.jsonl` | `evalstats.py`, `cardcheck.py` | `solutions/D2_1_report.md`, `solutions/D2_1_card.md` |
| 2.2 | `D2_2_revision.html` | your lab 2.1 draft, or `files/D2_2/draft_unassisted.md` | `stand_in_revise.py`, `claimdiff.py`, `logcheck.py`, `doccheck.py agents` | `solutions/D2_2_revision_log.csv`, `solutions/D2_2_final.md`, `solutions/D2_2_AGENTS.md` |

The capstone brief is `files/capstone/brief.md`, with the tagger's second evaluation log
`files/capstone/eval_log_v2.jsonl`.

## For the trainer

- `uv run solutions/check_D1_1.py` (and `check_D1_2.py` to `check_D2_2.py`) runs the kit on the
  reference documents and on the planted starting files, and prints `PASS lab n.n`. Run all five
  before a cohort. `check_D1_2.py` makes a real clean run: uv builds a fresh environment for a
  copy of the tagger.
- `solutions/answer_key.md` lists every planted problem, the lab that finds it and the figures the
  slides quote.
- `uv run _tools/make_case.py` writes every case file again, byte for byte;
  `uv run _tools/slide_examples.py` prints the figures of the slides' parallel example (the
  clinics' pharmacy team), which is not lab data.
