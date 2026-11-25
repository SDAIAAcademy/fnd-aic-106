# Answer key for the trainer

Every figure below comes from a run of the kit on the committed files (`labs/solutions/check_*.py`)
or from `labs/solutions/case_numbers.json`, written by `labs/_tools/make_case.py` (seed 106).
Model S and Model L outputs are simulated and recorded; no model ran.

## Lab 1.1 · Bottom-line-first rewrite

| Planted in `files/D1_1/status_update.md` | Found by |
|---|---|
| The request (six hours of reception time, two receptionists, before the end of next week) is in the last paragraph | `doccheck.py bluf`: "does not say what you ask"; step 3 |
| Glossary drift: critical, emergency, catch rate, sensitivity | `doccheck.py bluf`: four glossary findings |
| Hedges where numbers exist: quite, generally, very, significantly, seem | `doccheck.py bluf` |
| 339 words; average sentence 24.2 words | `doccheck.py bluf` |
| Uncertainty stated without numbers, although the update gives 80 urgent messages of 400 | the rubric's fourth line |

The original fails with 12 findings. Reference outlines: README, design document, decision memo,
experiment report, model (or system) card, in the scenarios' order.

## Lab 1.2 · Peer-tested README

Planted in `files/urgency-tagger/`: `config.toml` must be copied from `config.example.toml`
(`error: config.toml not found`); Python 3.11 or later; `NOTES.txt` names a `tagger.py` that does
not exist; the command is `uv run python -m urgency_tagger`. The reference README passes the clean
run with five commands; without the copy step it fails. Sample tags with the rules: urgent 2,
soon 3, routine 25. `check` prints `check: ok, 30 sample rows, 400 test rows, 2 recorded systems`.

## Lab 1.3 · Decision memo

| 400 messages, 80 urgent | Keyword rules | Model S | Model L |
|---|---|---|---|
| Urgent found | 53 | 66 | 75 |
| Urgent recall (95% interval) | 0.66 (0.55 to 0.76) | 0.82 (0.73 to 0.89) | 0.94 (0.86 to 0.97) |
| Accuracy, macro F1 | 0.78, 0.76 | 0.85, 0.84 | 0.94, 0.93 |
| SAR per 1,000 messages | 0.00 | 8.02 | 37.52 |
| A month at 9,000 messages | 0 | 72.18 | 337.68 |
| Latency median, 95th percentile (s) | 0.00, 0.00 | 0.71, 1.24 | 2.41, 5.59 |

Only Model L's point estimate meets reception's 0.90, and its interval reaches below it; Model S's
interval lies wholly below. At 37.52 per 1,000, 10,661 messages a month cost more than SAR 400.

## Lab 2.1 · Experiment report and model card (run EV-L3)

| Slice | Messages | Urgent found | Urgent recall (95% interval) | Accuracy |
|---|---|---|---|---|
| All | 400 | 75/80 | 0.94 (0.86 to 0.97) | 0.94 |
| Arabic | 230 | 42/46 | 0.91 (0.80 to 0.97) | 0.94 |
| English | 146 | 29/30 | 0.97 (0.83 to 0.99) | 0.95 |
| Mixed, planted weak | 24 | 4/4 | 1.00 (0.51 to 1.00) | 0.79 |
| Livestock, planted weak | 70 | 8/12 | 0.67 (0.39 to 0.86) | 0.90 |
| In the development set, planted | 12 | 2/2 | 1.00 (0.34 to 1.00) | 1.00 |
| Not in the development set | 388 | 73/78 | 0.94 (0.86 to 0.97) | 0.93 |

False urgent tags: 9. Latency: median 2.41 s, 95th percentile 5.59 s.

## Lab 2.2 · Unassisted draft against assisted revision

On `files/D2_2/draft_unassisted.md` the stand-in makes 9 changes, 6 flagged by the claim diff:
an added overclaim ("relied on to triage emergencies without a person reading the message"); the
first interval dropped; accuracy 0.94 changed to 0.97 (also the English recall, so a careless
check passes it); an invented citation, evaluation note EV-N7; the livestock limit removed; the
development-set overlap removed. Three changes are wording only. Verdicts in the reference log:
removed, restored, corrected, removed, restored, restored for the six, in that order; kept for the three.

## Capstone · version 0.4 (run EV-L4, Model L with keyword override)

Overall urgent recall 0.96 (77/80, interval 0.90 to 0.99), accuracy 0.91, false urgent tags 22
(against 9 in EV-L3); livestock 10/12 (0.83, 0.55 to 0.95); mixed accuracy 0.75 on 24 messages;
the same 12 messages overlap the development set. Latency is unchanged (the override adds the
keyword rules' time only). A good memo weighs two more urgent messages found against 13 more false
urgent tags for reception to read, and keeps the livestock and mixed-language limits.

## The supervised memo

Its result sheet is not written yet. The Academy's assessment pack must supply it before the first
cohort, outside this repository, as a comparison different from lab 1.3. Score the memo on the
five-criterion rubric of lab 1.3, two points each.

## Rounding

Every figure is rounded once, to two decimals, by Python's `round` and `:.2f`, and quoted the same
way everywhere. Three exact values sit on a half, and binary floating point rounds them
unevenly: Model S's urgent recall 66/80 = 0.825 shows as 0.82, Model L's median time 2.415 s as
2.41, but Model L's accuracy 374/400 = 0.935 as 0.94. A participant who works 66/80 out by
hand and writes 0.83 is not wrong: `memocheck.py` flags 0.83 as untraced until the memo shows it on
a `Working:` line (66 / 80 = 0.825), which is the habit the lab teaches.
