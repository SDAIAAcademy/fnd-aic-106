---
course: "Technical Writing for Data and AI Work"
code: "FND-AIC-106"
version: "2027.1.0"
lab: "1.3"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-aic-106/labs/D1_3_memo.html"
---

# Lab 1.3 · Decision memo

Write a one-page memo to the operations director on which tagger the reception desk should use, from the measured comparison

Day 1 · Session 3: The decision memo

### You leave with

- A one-page memo to the operations director: the bottom line, three options, the trade-offs with traced numbers, a recommendation and the conditions that would change it.
- A partner's score of your memo on the five-criterion rubric.

## What you need

[**D1_3/context.md**The reader, the choice, what reception needs and what the clinics can spend.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/D1_3/context.md) [**D1_3/comparison.csv**The keyword rules, Model S and Model L scored on the same 400 synthetic test messages. The two models' outputs are simulated and recorded: no model ran.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/D1_3/comparison.csv) [**D1_3/memo_template.md**The five sections and the Working line.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/D1_3/memo_template.md)

Copy the template to `work/memo.md`.

> **AI in this lab: tutor.** You may ask an assistant whether your sections are in a sensible order. The numbers and the recommendation are yours: tomorrow's supervised memo is written with AI off.

## Steps

### 1 · Read the context and the comparison; write the decision in one line 8 min

Write the question the director signs, as a question. Mark the three requirements of the context against each column of the comparison.

### 2 · Write the bottom line and the three options 12 min

Two sentences at most: what you recommend and what you ask him to sign. Then the options, one line each, in the order you will keep everywhere.

### 3 · Write the trade-offs with numbers from the comparison and their intervals 15 min

Quality, cost and latency for each option, with the interval beside every recall. Turn per-1,000 costs into a month at the clinics' volume, and show each computed number on the `Working:` line.

### 4 · Write the recommendation and the conditions that would change it 10 min

Say why, against what reception needs. Then two or three conditions with numbers: a threshold, a volume, a price or a time at which you would recommend something else.

### 5 · Run the checker; a partner scores your memo on the five-criterion rubric 15 min

```
uv run kit/memocheck.py work/memo.md
```

The checker traces every number to the comparison, the context or a Working line. Your partner then scores each criterion from 0 to 2:

| Criterion | Score (0 to 2) |
| --- | --- |
| Bottom line: the recommendation and the request in the first two sentences |  |
| Options: all three, named the same way throughout |  |
| Trade-offs: quality, cost and latency with traced numbers and intervals |  |
| Recommendation: argued from the reader's requirements |  |
| Conditions: what would change it, with numbers |  |

### ✱ Stretch

Write the same choice as a decision record under five headings: title, status, context, decision, consequences.

## Check yourself

1. Does any interval in the comparison weaken the option you recommend, and does your memo say so?
2. Which number in your memo is not in the comparison, and where did you show how you got it?
3. Who reviewed your memo, and are they a different person from its author?
