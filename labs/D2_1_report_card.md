---
course: "Technical Writing for Data and AI Work"
code: "FND-AIC-106"
version: "2027.1.0"
lab: "2.1"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-aic-106/labs/D2_1_report_card.html"
---

# Lab 2.1 · Experiment report and model card

From the evaluation log, write an experiment report for the data team lead and a model card for the head of reception, the report drafted with AI off

Day 2 · Session 1: Experiment reports and model cards

### You leave with

- An experiment report of run EV-L3 for the data team lead, drafted with AI off: question, setup, results by slice, uncertainty, limits, next steps.
- A model card for the head of reception: what the tagger is for and not for, results by kind of message, known limits and what staff do about each.

## What you need

[**D2_1/eval_log.jsonl**The evaluation log of Model L on the 400 test messages: a run record, then one line per message.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/D2_1/eval_log.jsonl) [**D1_1/glossary.csv**The agreed terms, as in lab 1.1.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/D1_1/glossary.csv)

Write `work/report.md` and `work/card.md`. Model L's outputs in the log are synthetic and recorded; no model runs in this lab.

> **AI in this lab: off for the report.** The report draft is the course's one unassisted first draft; lab 2.2 compares it with an assisted revision. For the card, an assistant may comment on structure only.

## Steps

### 1 · Run the statistics tool on the evaluation log and read the slice table 10 min

```
uv run kit/evalstats.py files/D2_1/eval_log.jsonl
```

It prints the run record and a table by language, species group, length and overlap with the development set, and writes `work/stats.md` and `work/stats.json`. Read each row marked "small" twice.

### 2 · Draft the experiment report with AI off: question, setup, results, uncertainty 20 min

Sections: result in brief, setup, results, uncertainty, limits, next steps. Every rate with its count and its interval. Say which results rest on few urgent messages, and what the run record tells you about how to repeat it.

### 3 · Draft the model card for the head of reception 15 min

Sections: what it is for, what it is not for, evaluation data, results by kind of message, known limits with what staff do about each, ethical considerations. Then three lines, three different roles: `Owner:`, `Reviewed by:`, `Approved by:`.

### 4 · Run the card checker and fix what it reports 5 min

```
uv run kit/cardcheck.py report work/report.md
uv run kit/cardcheck.py card work/card.md
```

### 5 · Swap with a partner and complete the peer checklist 10 min

| Peer checklist | Yes or no |
| --- | --- |
| The first paragraph of the report gives the result with its count and interval |  |
| Every rate has its count beside it |  |
| Each small slice is named as small, and the weakest slice is a stated limit |  |
| The overlap with development data is reported |  |
| The card tells staff what to do about each limit |  |
| The card says what the tagger is not for |  |
| Owner, reviewer and approver are three different roles |  |

### ✱ Stretch

Add a Mermaid diagram of the evaluation flow to the report: test set, model, recorded outputs, statistics, report.

## Check yourself

1. Which slice would you tell the head of reception about first, and what should her staff do?
2. Which result in your report would change most if the test set had twice as many urgent messages?
3. What does the report need that the card leaves out, and why?
