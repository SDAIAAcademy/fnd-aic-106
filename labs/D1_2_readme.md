---
course: "Technical Writing for Data and AI Work"
code: "FND-AIC-106"
version: "2027.1.0"
lab: "1.2"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-aic-106/labs/D1_2_readme.html"
---

# Lab 1.2 · Peer-tested README

Write the README of the undocumented urgency tagger, test it with a clean run, then have a partner follow it and log the run

Day 1 · Session 2: READMEs, designs and decisions

### You leave with

- A README for the urgency tagger that a stranger can follow to install, run and check it on a clean machine.
- Two run logs: the clean-run test's and your partner's, written while following your README by hand.

## What you need

[**urgency-tagger/**The undocumented repository: code, synthetic data, simulated and recorded model outputs (no model runs), tests and an old notes file.](https://sdaiaacademy.github.io/fnd-aic-106/labs/files/urgency-tagger/pyproject.toml)

`uv` and a terminal. Copy the folder `files/urgency-tagger` to `work/urgency-tagger` before you change anything in it, and write your README as `work/README.md`.

> **AI in this lab: tutor.** An assistant may comment on the order of your sections. It cannot tell you what a stranger will trip on: only a clean run can.

## Steps

### 1 · Explore the repository and list what a stranger would have to guess 10 min

Open every top-level file. Try to run the tagger the way `NOTES.txt` says. Write down each thing you had to work out: the Python version, the command, a file to create, what "working" looks like.

### 2 · Write the install, run and check sections 20 min

Put every command in a ```` ```sh ```` block, exactly as typed, from the project folder. After a command whose output proves something, add a ```` ```text ```` block with the line it must print. Say what the check commands print when all is well.

### 3 · Add the purpose, inputs and outputs, limits and a text diagram 10 min

Two sentences on what the tagger does and does not do; where the data and outputs live; one or two limits; a Mermaid flowchart of the message's path. Then check the diagram renders in a Markdown preview.

### 4 · Run the clean-run test on your README and fix what fails 10 min

```
uv run kit/readme_run.py work/README.md
```

It copies the project fresh, without `config.toml` or an environment, runs your commands in order, compares the promised output and writes `work/runlog.md`. It runs only `uv` commands and file copies.

### 5 · Swap: a partner follows your README on a clean copy and writes the run log 10 min

Your partner copies `files/urgency-tagger` to a new folder and follows your README by hand, writing each command, what happened and where they hesitated. Read their log; fix the README where they hesitated.

### ✱ Stretch

Start the README of your own project, the first part of the capstone, and run the same test on it with `--project`.

## Check yourself

1. Which step of your README did the clean run or your partner find missing?
2. How does a reader know the tagger works, not only that it ran?
3. What would you move to a design document rather than keep in the README?
