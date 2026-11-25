---
course: "Technical Writing for Data and AI Work"
code: "FND-AIC-106"
version: "2027.1.0"
lab: "1.1"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-aic-106/labs/D1_1_bluf.html"
---

# Lab 1.1 · Bottom-line-first rewrite

Outline five documents for five readers, then rewrite the data team's status update bottom line first and check it

Day 1 · Session 1: Write for one reader

### You leave with

- Five outlines, one per scenario: the reader, the purpose, the document type and its sections.
- The data team's status update rewritten bottom line first, in the glossary's terms, with its uncertainty stated as a number.

## What you need

[**D1_1/scenarios.md**Five requests for a document, each from one reader named by role.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/D1_1/scenarios.md) [**D1_1/status_update.md**The data team's update to the operations director, as it was sent.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/D1_1/status_update.md) [**D1_1/glossary.csv**The agreed English and Arabic terms, and the words to avoid.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/D1_1/glossary.csv)

A text editor that saves Markdown, and `uv` to run the checker from the `labs` folder. Write your files in `labs/work/`, which git ignores.

> **AI in this lab: tutor.** You may ask an approved assistant for feedback on the structure of your outline. Write the rewrite yourself. The files are synthetic and Public, so nothing here is restricted.

## Steps

### 1 · Read the five scenarios and name each reader's decision 8 min

For each scenario write one line: who reads, and what they will do after reading (approve, install, choose, repeat, rely). The decision decides the document, not the other way round.

### 2 · Outline the five documents: reader, purpose, sections 17 min

In `work/outlines.md` write one `## Scenario n` block per scenario with the lines `Reader:`, `Purpose:`, `Document:` and `Sections:`, then at least four sections in reading order. Then check the form:

```
uv run kit/doccheck.py outlines work/outlines.md
```

### 3 · Mark where the status update hides its bottom line 5 min

Find the sentence that asks the director for something. Note where it sits, which words drift from the glossary, and which claims are vague where a number exists.

### 4 · Rewrite it bottom line first, with glossary terms and uncertainty in words 20 min

In `work/rewrite.md`: the request, its size and its deadline in the first paragraph; then why, in the glossary's terms; then what happens next. State how sure the team is with the counts the update gives, not with "quite" or "significantly".

### 5 · Run the checker, then score a partner's rewrite with the rubric 10 min

```
uv run kit/doccheck.py bluf work/rewrite.md
```

Fix what it reports, then swap with a partner and score each other's rewrite, one point per line:

| Criterion | Score (0 or 1) |
| --- | --- |
| The reader can act on the first paragraph alone |  |
| The request names who, how much and by when |  |
| Every term is the glossary's term |  |
| The uncertainty is a number with what it rests on |  |

### ✱ Stretch

Write the first paragraph again in Arabic, with the glossary's Arabic terms.

## Check yourself

1. Which two scenarios ask for the same kind of reader action, and why do they still need different documents?
2. Could the director approve the request after reading only your first paragraph?
3. Where did the checker disagree with you, and who was right?
