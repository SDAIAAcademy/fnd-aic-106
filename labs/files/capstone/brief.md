# Capstone brief: a documentation set for one project

An individual task. Submit a public GitHub repository link before the follow-up review.

## The task

Write the documentation set of one small data or code project:

1. **README** that lets a stranger install, run and check the project on a clean machine.
2. **Decision memo**, one page, on one decision the project faces: options, trade-offs with
   traced numbers, a recommendation and the conditions that would change it.
3. **Model or system card** for the people who rely on the project's output: intended use, what
   it is not for, results by slice with counts and intervals, known limits with actions, owner,
   reviewer and approver.
4. **Revision log** of at least one assisted revision of one of the three documents, made with
   AI-full use, every changed claim checked, ending with a disclosure line.

## Which project

- **Your own** small project, if it uses only public or synthetic data. Nothing personal or
  classified goes into the repository, the examples or any assistant.
- **Or the urgency tagger** of the course case, at its version 0.4: Model L with a keyword
  override (any message the keyword rules tag urgent stays urgent). Its evaluation log is
  `eval_log_v2.jsonl` beside this brief. The decision for the memo: should reception move from
  version 0.3 (run EV-L3, lab 2.1) to version 0.4 (run EV-L4)? Your labs' README, memo and card
  are your first drafts; the set must be revised for version 0.4, not copied from the labs.

## Checks to run before you submit

From the course's `labs` folder (point the tools at your own files):

```sh
uv run kit/readme_run.py <your README> --project <your project folder>
uv run kit/memocheck.py <your memo> --evidence <your comparison as CSV> --context <your context note>
uv run kit/evalstats.py <your evaluation log>
uv run kit/cardcheck.py card <your card> --stats work/stats.json
uv run kit/logcheck.py <your revision log> <your final document> --log <your evaluation log>
```

For your own project the checkers may not fit its files: then say in the README which checks you
ran instead. The checkers are a first pass; the follow-up review is the judgement.

## The follow-up review

Groups of six. Each participant has four minutes to show the set and four minutes of questions.
The reviewer opens your commit history and picks two rows of your revision log to check live.
Before the review, review one partner's set with the lab checklists and send them your scores:
that review is the "peer review given" part of the assessment.

## How it is scored

| Criterion | Weight |
|---|---|
| The README lets a stranger install, run and check the project on a clean machine | 20 |
| The decision memo states options, trade-offs, a recommendation and the conditions that would change it | 20 |
| The card states intended use, results by slice with uncertainty, and known limits | 25 |
| The revision log shows how each assisted change was checked, with a disclosure line | 20 |
| Each document is written for its named reader: bottom line first, consistent terms, plain uncertainty | 15 |
