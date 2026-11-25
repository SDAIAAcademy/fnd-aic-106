---
course: "Technical Writing for Data and AI Work"
code: "FND-AIC-106"
version: "2027.1.0"
scope: "course"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-aic-106/"
---

# Technical Writing for Data and AI Work

Write the README, decision memo, experiment report and model card a data or AI project runs on, for a named reader, with every claim checked

Participants write the documents that data and AI work runs on: a README, a design document, a decision memo, an experiment report and a model or system card. Each starts from a repository, a model comparison or an evaluation log and ends with a peer test; one draft is unassisted, another is revised with an assistant, and every claim is checked.

- **Audience:** Beginners. Graduates, career changers and computing professionals preparing for Developer or Specialist courses, who can run a Python notebook but have not yet studied AI methods.
- **Prerequisites:** Has a small data or code project, own or provided, to document
- **Case study:** Tarthuth Veterinary Clinics: A fictional private chain of veterinary clinics whose two-person data team built a small Python project, the request urgency tagger, that sorts owners' appointment messages in Arabic, English and mixed text into urgent, soon and routine. Every file is synthetic and generated with a fixed seed: the messages, a 400-message test set, the outputs of a keyword-rules baseline that really runs, the simulated and recorded outputs of two hosted models labelled Model S and Model L with their cost and latency, and the evaluation log. No model was called.

## Outcomes

- LO1 (Awareness): Identify the reader, purpose and required sections of five common technical document types, given five scenarios with named readers
- LO2 (Applied): Draft a README that lets a stranger install, run and check a small project, given an undocumented repository
- LO3 (Applied): Draft a one-page decision memo with options, trade-offs, a recommendation and the conditions that would change it, given a measured comparison of two models on quality, cost and latency
- LO4 (Applied): Prepare an experiment report and a model card that state uncertainty, results by data slice and known limits, given an evaluation run log
- LO5 (Awareness): Compare an unassisted draft with an assisted revision for accuracy, clarity and invented content, given the participant's two drafts

## Day 1: Writing for a reader

One reader, the bottom line first, and the documents a project needs before anyone else can use it

#### [day1#title] Writing for a reader

*SDAIA Academy · Technical Writing for Data and AI Work*

Day 1: One reader, the bottom line first, and the documents a project needs before anyone else can use it

Data & AI Foundations Track · 2 teaching days + capstone day · 3 sessions · 3 labs · FND-AIC-106

#### [day1#agenda] Writing for a reader

*Today*

- **Session 1 · Write for one reader**: Name the reader and the decision before choosing the document, then put the bottom line first
- **Session 2 · READMEs, designs and decisions**: Write what a stranger needs to install, run and check a project, and keep designs and decisions as text beside the code
- **Session 3 · The decision memo**: Turn a measured comparison into one page: options, trade-offs, a recommendation and what would change it

#### [day1#setup-check] Clone the course, open the labs folder and run the setup check

*Before the first lab*

- Clone the course repository, open a terminal in its `labs` folder.
- Run `uv run kit/setup_check.py`: uv fetches Python 3.11 or later if it is missing.
- You write every file of the day in `labs/work/`, which git ignores.
- No account, no key, no model download: the tools read and check text on your laptop.

- **What proves it works.** The last line reads `setup: ok`. Any line that starts with `missing:` names a file to fetch again.

### Session 1: Write for one reader

#### [day1#s1] Write for one reader

*Session 1*

- Name the reader, purpose and decision behind a request for a document
- Choose the document type and its required sections for a scenario
- Rewrite an update so the bottom line, the request and the uncertainty come first

#### [day1#reader-first] Name the reader and their decision before you pick a document

*Before you write*

- **Who reads?** One person, by role: the operations director, a new developer, the head of reception. "Everyone" is nobody.
- **What will they do?** Install, approve, choose, repeat, rely. The verb decides the document and its first line.
- **What do they know?** You know the project too well to see its gaps: write for what the reader already knows, not for you.

> **What goes wrong.** A document written for "the stakeholders" answers nobody's question and buries the one decision someone has to make.

#### [day1#five-documents] Five documents, five readers, five jobs

*Documents for data and AI work*

| Document | Its reader | The reader then | It cannot do without |
| --- | --- | --- | --- |
| README | A stranger to the project | installs, runs and checks it | exact commands and what success prints |
| Design document | An approver, before code | approves, changes or refuses | alternatives and risks |
| Decision memo | A decision maker | signs one option | trade-offs and what would change it |
| Experiment report | The team, now and later | repeats and compares | the setup and the uncertainty |
| Model or system card | A user of the system | decides how far to rely on it | intended use, slices, limits |

#### [day1#bluf-before-after] Put what the reader must do in the first two sentences

*Bottom line first*

- **As sent.** "Since the spring the pharmacy team has looked at several ways of forecasting reorders. We first tried a seasonal average, which was generally fine, then a boosted-tree model, which seems better on most weeks. ... So we would like to buy a quarter of model runs."
- **Bottom line first.** "Please approve SAR 46 for one quarter of weekly forecast runs with Method B. In 60 past weeks when a medicine ran out, it flagged 52 in advance; the current method flagged 41."

> **Test.** If the reader stopped after the first paragraph, could they act?

#### [day1#bluf-shape] Decision, then reasons, then detail, then next step

*The shape*

1. **1 · Bottom line** the request or the finding, with its size and date
2. **2 · Why** the two or three facts it rests on
3. **3 · Detail** method, numbers, caveats, for whoever reads on
4. **4 · Next** what happens after the reader acts

> **Headings help.** A reader who scans the headings alone should get the argument.

#### [day1#glossary] One term, one meaning, in both languages

*Arabic and English glossaries*

- A reader who meets **run-out**, **stock-out** and **shortage** wonders if they are three things.
- Agree the term once, with its Arabic pair and the words to avoid.
- Keep the glossary in the repository, beside the documents that use it.
- A checker can then flag every word to avoid, in every document.

| term_en | term_ar | avoid |
| --- | --- | --- |
| run-out | نفاد المخزون | stock-out; shortage |
| reorder | إعادة الطلب | top-up; refill |

#### [day1#uncertainty-in-words] Say how sure you are, and on how many cases

*Uncertainty in plain words*

- **Says nothing.** "Method B is significantly better at catching run-outs."
- **Says how sure.** "Method B flagged 52 of 60 past run-outs (0.87). With 60 cases, the 95% interval runs from 0.76 to 0.93."

- The count tells the reader how much evidence there is; the interval tells them how far to trust the rate.
- On nine cases, 7 of 9 (0.78) has an interval from 0.45 to 0.94: say so, or do not report the rate.

#### [day1#hedges] Replace a hedge with a number, a condition or "not measured"

*Hedges*

| Hedge | Replace with |
| --- | --- |
| "quite good", "generally fine" | the rate and its count: 41 of 60 |
| "seems better" | the difference, and whether the intervals overlap |
| "should be enough" | the condition: enough if at least 20 new cases are urgent |
| "no issues" | what was checked: 60 weeks, no missing values |
| "probably fine for other branches" | "not measured on other branches" |

> **"Not measured" is a finding.** It tells the reader where the evidence stops.

#### [day1#peer-review] Review against the rubric, the text and the reader, not the writer

*Rubric-based peer review*

- **Score each line.** 0, 1 or 2 against criteria written before anyone wrote: no overall impression.
- **Quote the words.** "Paragraph 2: 'quite well'": the writer can find it and fix it.
- **One strength, one change.** At least one of each, so the writer knows what to keep.

> **Read as the reader.** Pretend you are the operations director with two minutes, not a fellow writer with a red pen.

#### [day1#check-reader] Which document does this reader need?

*Checkpoint*

**Question:** The pharmacy team wants to add a second supplier feed to its forecast. Before anyone writes code, the finance manager must approve, change or refuse the plan, and wants to know what else was considered and what could go wrong.

- A. A README for the forecast repository and its feed
- B. A design document with alternatives and risks
- C. An experiment report on the new feed
- D. A system card for the forecast

#### [day1#lab-1-1] Bottom-line-first rewrite

Lab 1.1 · 60 min

Outline five documents for five readers, then rewrite the data team's status update bottom line first and check it

[D1_1_bluf.html](https://sdaiaacademy.github.io/fnd-aic-106/labs/D1_1_bluf.html)

- [ ] Read the five scenarios and name each reader's decision (8 min)
- [ ] Outline the five documents: reader, purpose, sections (17 min)
- [ ] Mark where the status update hides its bottom line (5 min)
- [ ] Rewrite it bottom line first, with glossary terms and uncertainty in words (20 min)
- [ ] Run the checker, then score a partner's rewrite with the rubric (10 min)
- [ ] ✱ Stretch: Write the first paragraph again in Arabic with the glossary's Arabic terms

#### [day1#debrief-1-1] The update as sent had its request in the last paragraph and 12 findings

*Lab 1.1 debrief*

- **Request last:** six hours of reception time appeared only in the closing paragraph.
- **Four drifts:** critical, emergency, catch rate and sensitivity, where the glossary says urgent and urgent recall.
- **Hedges:** "quite well", "significantly better", with numbers available.
- **Length:** 339 words, sentences of 24 words on average.

- **The uncertainty, stated.** 80 urgent messages left after the clean-up: on 80 cases a recall of 0.80 has a 95% interval from 0.70 to 0.87.

### Session 2: READMEs, designs and decisions

#### [day1#s2] READMEs, designs and decisions

*Session 2*

- Write install, run and check steps a stranger can follow on a clean machine
- Separate a README from a design document and a decision record
- Draw a pipeline as text that the repository renders

#### [day1#readme-job] A stranger installs, runs and checks the project without asking anyone

*A README's job*

- **Install.** Every command as typed, from which folder, with the versions it needs and any file to create.
- **Run.** The one command that does the project's job on supplied data, and where the output goes.
- **Check.** The tests, and the exact line they print when all is well: "it ran" is not "it works".

> **Then the rest.** What it is for and not for, where things are, its limits and its owner.

#### [day1#what-strangers-guess] A stranger stops at the steps the writer does without thinking

*What the writer forgets*

- **The language version** the code needs, and how to get it.
- **A file to create:** a settings file copied from an example, an empty folder.
- **The folder** a command runs from.
- **The real command,** when an old note names a script that no longer exists.
- **What success looks like:** the line a working run prints.

> **What goes wrong.** The writer tests the README on their own laptop, where every one of these is already true.

#### [day1#commands-exactly] Show the command and the line it must print

*Commands as typed*

````markdown
<!-- file: README.md -->
## Run

Forecast next week's reorders from the 60 sample weeks:

```sh
uv run python -m reorder forecast data/sample_weeks.csv
```

```text
forecast: 60 weeks read, 14 medicines flagged
```
````

> **The text block is a promise.** A reader, or a test, compares it with what the screen shows.

#### [day1#four-forms] A README points to the other kinds of documentation

*Not everything in one file*

- **Tutorial.** Learning by doing, step by step.
- **How-to guide.** One task, for someone who knows the basics.
- **Reference.** Every option and field, to look up.
- **Explanation.** Why it works the way it does.

> **The README is a front door:** install, run, check, then links to the rest.

#### [day1#design-document] A design document is written before the code, for the person who approves it

*Design document*

- **Summary:** the change and the decision asked for.
- **Problem and goals,** and what is out of scope.
- **The design,** with a diagram of what flows where.
- **Alternatives** and why not.
- **Risks** and failure cases, with what catches each.
- **Open questions,** reviewers and the approver.

- **Its test.** Could the approver say no for a good reason after reading it? If every alternative is a straw man, they cannot.

#### [day1#decision-record] A decision record keeps one decision and its reasons beside the code

*Decision record*

1. **Title** a short noun phrase
2. **Status** proposed, accepted, superseded
3. **Context** the forces, stated neutrally
4. **Decision** in a full, active sentence
5. **Consequences** good, bad and neutral

Numbered files in `docs/decisions/` become the project's decision log.

#### [day1#diagrams-as-text] A diagram written as text is reviewed and versioned like code

*Diagrams as text*

````markdown
<!-- file: README.md -->
```mermaid
flowchart LR
  W[Weekly sales] --> F[Forecast]
  S[Stock levels] --> F
  F --> R[Reorder list]
  R --> P[Pharmacist checks]
```
````

- Mermaid and PlantUML turn short text into flowcharts and sequence diagrams.
- GitHub renders Mermaid blocks in Markdown.
- A change to the diagram shows in the diff, line by line.

#### [day1#clean-run] Follow your README on a fresh copy, exactly as written

*Test the README*

1. **1 · Fresh copy** no settings file, no environment
2. **2 · Literal** type only what is written
3. **3 · Log** each command, its result, each hesitation
4. **4 · Fix** the README, not the laptop

> **Two testers.** The kit's clean-run tool types exactly what you wrote; a partner shows you where a person hesitates.

#### [day1#check-readme] What did this README leave out?

*Checkpoint*

**Question:** A stranger follows the forecast's README on a fresh copy. The install step works, then the run command stops with "error: settings.toml not found". The writer's laptop runs it fine.

- A. A step that copies the example settings file
- B. A note that the stranger's laptop is misconfigured
- C. The command that runs the tests
- D. An offer to send the writer's own settings file

#### [day1#lab-1-2] Peer-tested README

Lab 1.2 · 60 min

Write the README of the undocumented urgency tagger, test it with a clean run, then have a partner follow it and log the run

[D1_2_readme.html](https://sdaiaacademy.github.io/fnd-aic-106/labs/D1_2_readme.html)

- [ ] Explore the repository and list what a stranger would have to guess (10 min)
- [ ] Write the install, run and check sections (20 min)
- [ ] Add the purpose, inputs and outputs, limits and a text diagram (10 min)
- [ ] Run the clean-run test on your README and fix what fails (10 min)
- [ ] Swap: a partner follows your README on a clean copy and writes the run log (10 min)
- [ ] ✱ Stretch: Start the README of your own project, the first part of the capstone

#### [day1#debrief-1-2] Four things a stranger had to guess in the tagger's repository

*Lab 1.2 debrief*

| Gap | What the stranger saw | The README line that closes it |
| --- | --- | --- |
| Settings file | `error: config.toml not found` | copy `config.example.toml` to `config.toml` |
| Python version | a TOML import error on an old Python | Python 3.11 or later; uv installs it |
| Stale note | `NOTES.txt` names `tagger.py`, which does not exist | say the note is out of date |
| Success | output with nothing to compare | `check: ok, 30 sample rows, 400 test rows, 2 recorded systems` |

### Session 3: The decision memo

#### [day1#s3] The decision memo

*Session 3*

- State the decision and the recommendation in the first two sentences
- Compare options on quality, cost and latency with numbers traced to the source
- Write the conditions under which the recommendation would change

#### [day1#memo-one-page] One decision, one page, one signature

*The decision memo*

- **1** decision, asked as a question
- **450** words at most: one page
- **3** roles named: author, reviewer, decider

> **The reader has ten minutes.** Everything that does not help them choose goes in an appendix or the experiment report.

#### [day1#memo-shape] Bottom line, options, trade-offs, recommendation, what would change it

*Five parts*

1. **Bottom line** the recommendation and the request
2. **Options** each one, named once
3. **Trade-offs** measured, with intervals
4. **Recommendation** argued from the reader's needs
5. **What would change it** conditions with numbers

#### [day1#options-honest] Keep the current way as an option, and name every option the same way throughout

*Options*

- **The status quo** is a real option with real costs: say what staying costs.
- **Same names, same order** in the options, the table and the recommendation.
- **No straw men:** an option nobody would pick wastes the reader's ten minutes.
- **Unmeasured options** go in "what would change this", not in the table.

> **What goes wrong.** "Method B", then "the new model", then "the ML option": the reader wonders if they are three things.

#### [day1#tradeoff-table] Put the options side by side on the measures the reader cares about

*Trade-offs*

| Pharmacy reorder forecast | Method A (current) | Method B |
| --- | --- | --- |
| Run-outs flagged in advance, of 60 | 41 · 0.68 (0.56 to 0.79) | 52 · 0.87 (0.76 to 0.93) |
| Cost a month, one run a week | SAR 0 | SAR 15.17 |
| Time a run | 1 minute | 14 minutes |

A parallel example, synthetic, from `labs/_tools/slide_examples.py`.

#### [day1#requirement-first] Argue from the reader's requirement, not from "the best score"

*Recommendation*

- **From the score.** "Method B is better on every quality measure, so we recommend it."
- **From the requirement.** "The pharmacy needs 0.80 of run-outs flagged within SAR 20 a month. Only Method B is likely to meet it, and it costs SAR 15.17."

> **Requirements first.** State each one with its number, then show which options meet it and how surely.

#### [day1#conditions] Name the lines that, once crossed, bring the decision back

*What would change this*

- **A measured threshold:** if a larger test puts Method B below 0.80, bring a new option.
- **A volume:** at SAR 3.50 a run, five runs a month fit the SAR 20 budget and a sixth breaks it; daily runs do not fit.
- **A price:** at SAR 4.62 a run, weekly runs cost SAR 20.02 a month and break it.

> **Show the working.** Each computed number gets one line: 20 / 3.50 = 5.71 runs.

#### [day1#trace-numbers] Every number in the memo traces to the evidence or to its working

*Every claim checked*

- Copy numbers from the evidence; never retype them from memory.
- Round once, the same way everywhere.
- A number you computed has its working beside it.
- The reviewer checks numbers before style.

- **The checker in the lab.** `kit/memocheck.py` lists every number that is in neither the comparison, the context nor a Working line.

#### [day1#check-memo] Which sentence belongs in the pharmacy memo?

*Checkpoint*

**Question:** The pharmacy needs at least 0.80 of run-outs flagged. Method B flagged 52 of 60, 0.87, with a 95% interval from 0.76 to 0.93.

- A. "Method B meets the 0.80 requirement."
- B. "Method B cannot be shown to meet 0.80, so we cannot recommend it."
- C. "Method B is significantly better than the current method."
- D. "Likely meets 0.80; its interval reaches down to 0.76."

#### [day1#lab-1-3] Decision memo

Lab 1.3 · 60 min

Write a one-page memo to the operations director on which tagger the reception desk should use, from the measured comparison

[D1_3_memo.html](https://sdaiaacademy.github.io/fnd-aic-106/labs/D1_3_memo.html)

- [ ] Read the context and the comparison; write the decision in one line (8 min)
- [ ] Write the bottom line and the three options (12 min)
- [ ] Write the trade-offs with numbers from the comparison and their intervals (15 min)
- [ ] Write the recommendation and the conditions that would change it (10 min)
- [ ] Run the checker; a partner scores your memo on the five-criterion rubric (15 min)
- [ ] ✱ Stretch: Write the same choice as a decision record under five headings

#### [day1#debrief-1-3] Only Model L likely meets reception's 0.90, and it fits the budget

*Lab 1.3 debrief*

| 400 test messages, 80 urgent | Keyword rules | Model S | Model L |
| --- | --- | --- | --- |
| Urgent recall (95% interval) | 0.66 (0.55 to 0.76) | 0.82 (0.73 to 0.89) | 0.94 (0.86 to 0.97) |
| A month at 9,000 messages | SAR 0 | SAR 72.18 | SAR 337.68 |
| 95% of tags within | under 0.01 s | 1.24 s | 5.59 s |

Synthetic case: Model S and Model L outputs are simulated and recorded; no model ran.

> **And what would change it:** a larger test below 0.90; 10,661 messages a month or more; tags slower than 10 s.

#### [day1#wrap-up] Three things to keep

*Day 1 · wrap-up*

- **The reader decides.** One reader, one action: the document type and its first sentence follow from them.
- **Test the README.** A fresh copy, followed literally, by a tool and by a person.
- **Numbers with their doubt.** A count, an interval and the line that would change your mind.

#### [day1#next] Tomorrow: a supervised memo, then reports, cards and assistants

*Next*

- **First hour:** a one-page memo with AI off, from a result handed out on paper, scored on the lab 1.3 rubric.
- **Bring your project:** a small data or code project of your own, or keep the tagger.
- **Keep your files:** today's README and memo are the start of your capstone set.

## Day 2: Evidence documents and writing with assistance

Reports and cards that state uncertainty, slices and limits, and an assistant whose every change is checked

#### [day2#title] Evidence documents and writing with assistance

*SDAIA Academy · Technical Writing for Data and AI Work*

Day 2: Reports and cards that state uncertainty, slices and limits, and an assistant whose every change is checked

Data & AI Foundations Track · 2 teaching days + capstone day · 2 sessions · 2 labs · FND-AIC-106

#### [day2#agenda] Evidence documents and writing with assistance

*Today*

- **Session 1 · Experiment reports and model cards**: Report what an evaluation measured, by slice and with its uncertainty, and write the card a user of the model reads
- **Session 2 · Writing with an assistant**: Draft without the assistant first, then check every claim an assisted revision changes, log it and disclose it

#### [day2#review-day1] Which part of this memo is missing?

*Review of Day 1*

**Question:** A memo recommends Method B for the pharmacy, compares its quality, cost and time with Method A in a table with intervals, and argues from the 0.80 requirement. It ends there.

- A. A second table of results
- B. What would change the recommendation
- C. A section on how the methods were developed
- D. A third option that was not measured

#### [day2#supervised-memo] Supervised memo · 50 minutes of writing

*Assessment · AI off*

One page, from the result on your sheet, scored on the five-criterion rubric of lab 1.3. Devices closed; paper or a locked editor.

### Session 1: Experiment reports and model cards

#### [day2#s1] Experiment reports and model cards

*Session 1*

- Report results by data slice with the number of cases and an interval
- Write known limits and out-of-scope uses a reader can act on
- Check a report and a card with a peer checklist

#### [day2#report-job] A report lets someone repeat the run and compare the next one

*The experiment report*

- **What was asked.** The question, and the result in one paragraph with its count and interval.
- **What was run.** Data and its version, settings, scorer, run identifier and date.
- **What it shows.** Results overall and by slice, the uncertainty, the limits, the next run.

> **What goes wrong.** A report that gives only the best number cannot be compared with the next run, because nobody knows what produced it.

#### [day2#run-record] Copy the setup from the run record, not from memory

*Setup*

```json
// file: forecast_run.jsonl
{"type": "run", "system": "Method B", "run_id": "FC-B2",
 "data": "runouts_v3.csv, 60 weeks", "settings": "depth 4, 200 trees",
 "scorer": "flagged one week ahead", "run_date": "2026-09-02"}
```

- Every field the next run needs to match goes into the setup section.
- The run identifier ties the report to its log: cite it.

#### [day2#slices] An overall rate can hide the slice where the system fails

*Results by slice*

| Item | Value |
| --- | --- |
| All run-outs · 52/60 | 0.87 |
| Antibiotics · 30/32 | 0.94 |
| Vaccines · 15/19 | 0.79 |
| Parasite treatments · 7/9 | 0.78 |

Method B, run-outs flagged in advance, by medicine group. Parallel example from `labs/_tools/slide_examples.py`.

#### [day2#small-slices] Give every slice its count and interval, and say which are too small to read

*Small slices*

| Slice | Flagged | Rate | 95% interval |
| --- | --- | --- | --- |
| Antibiotics | 30/32 | 0.94 | 0.80 to 0.98 |
| Vaccines | 15/19 | 0.79 | 0.57 to 0.91 |
| Parasite treatments | 7/9 | 0.78 | 0.45 to 0.94 |

> **Neither drop it nor over-read it.** "On 9 cases the rate could be anywhere from 0.45 to 0.94: we need more before we rely on it."

#### [day2#overlap] Test cases that were also used in tuning make a result look better

*Threats to the result*

- A case seen while the system was tuned is not a test of new cases.
- Report how many test cases overlap, and the result without them.
- In the pharmacy run, 4 of the 60 weeks were also used to tune Method B.

**0.89** Method B on the 56 weeks not used in tuning: 50/56, interval 0.79 to 0.95

#### [day2#model-card] A model card tells a user how far to rely on the model

*Model cards*

- **What it is for,** and who uses it.
- **What it is not for:** out-of-scope uses, said plainly.
- **Evaluation data,** in words the user reads.
- **Results by slice,** with counts and intervals.
- **Known limits,** and what the user does about each.
- **Ethical considerations;** owner, reviewer, approver.

- **Where cards come from.** Mitchell and colleagues proposed model cards in 2019: results across groups, the intended context, how it was evaluated. Hub model cards are Markdown files with metadata.

#### [day2#system-card] A system card describes the whole system the reader meets

*Model or system card*

- **Model card.** One model: what it was evaluated on, how it did, where it fails.
- **System card.** The model with its rules, its queue, its people and its fallbacks: what happens to a message from arrival to a person.

> **Pick by the reader's question.** "Can I trust the model?" calls for a model card. "What happens to an owner's message?" calls for a system card.

#### [day2#limits-actionable] Write each limit with what the reader should do about it

*Known limits*

| Says nothing to act on | Tells the reader what to do |
| --- | --- |
| "May underperform on some medicine groups." | "Flagged 7 of 9 parasite-treatment run-outs: check their stock by hand every week." |
| "Not suitable for all uses." | "Not for ordering controlled medicines: those stay with the pharmacist." |
| "Results may vary." | "Tested on 60 past weeks of one store; not tested on the new branch." |

#### [day2#ethics-principles] SDAIA's AI Ethics Principles ask for what a card records

*National reference*

- **Fairness.** النزاهة والإنصاف: results by slice show who the system serves less well.
- **Transparency and Explainability.** الشفافية والقابلية للتفسير: what it is for, how it was tested, where it fails.
- **Accountability and Responsibility.** المساءلة والمسؤولية: an owner, a reviewer and an approver, by role.

#### [day2#check-card] Which line should the pharmacy's card carry?

*Checkpoint*

**Question:** The card for the head pharmacist says: "Method B flags run-outs with a recall of 0.87." The run flagged 7 of 9 parasite-treatment run-outs, and 4 test weeks were also used in tuning.

- A. "Method B is reliable for all medicines."
- B. "Parasite treatments: 0.78."
- C. "Parasite treatments: 7 of 9 flagged; check their stock by hand."
- D. "Results for small groups are left out."

#### [day2#lab-2-1] Experiment report and model card

Lab 2.1 · 60 min

From the evaluation log, write an experiment report for the data team lead and a model card for the head of reception, the report drafted with AI off

[D2_1_report_card.html](https://sdaiaacademy.github.io/fnd-aic-106/labs/D2_1_report_card.html)

- [ ] Run the statistics tool on the evaluation log and read the slice table (10 min)
- [ ] Draft the experiment report with AI off: question, setup, results, uncertainty (20 min)
- [ ] Draft the model card for the head of reception (15 min)
- [ ] Run the card checker and fix what it reports (5 min)
- [ ] Swap with a partner and complete the peer checklist (10 min)
- [ ] ✱ Stretch: Add a text diagram of the evaluation flow to the report

#### [day2#debrief-2-1] Model L found 75 of 80 urgent messages, but 8 of 12 on livestock

*Lab 2.1 debrief*

| Slice of run EV-L3 | Urgent found | Urgent recall (95% interval) | Accuracy |
| --- | --- | --- | --- |
| All, 400 messages | 75/80 | 0.94 (0.86 to 0.97) | 0.94 |
| Livestock, 70 | 8/12 | 0.67 (0.39 to 0.86) | 0.90 |
| Mixed Arabic and English, 24 | 4/4 | 1.00 (0.51 to 1.00) | 0.79 |
| Also in the development set, 12 | 2/2 | 1.00 (0.34 to 1.00) | 1.00 |

Synthetic case: Model L's outputs are simulated and recorded; no model ran.

### Session 2: Writing with an assistant

#### [day2#s2] Writing with an assistant

*Session 2*

- Spot the typical errors of an assisted revision: changed numbers, dropped limits, invented sources
- Keep a revision log that says how each claim was checked
- Write a disclosure line and a context file for a coding agent

#### [day2#ai-off-first] Write the first draft yourself, so you know what the assistant changed

*AI-off first drafts*

1. **1 · AI-off draft** your claims, your evidence
2. **2 · Assisted revision** clearer, shorter, maybe wrong
3. **3 · Claim diff** every changed sentence
4. **4 · Log and disclose** checked, then said

> **The course's AI levels.** Off for the supervised memo and the lab 2.1 report draft; tutor for structure in the labs; full, and logged, for this revision and the capstone's polish.

#### [day2#typical-errors] A fluent revision can change what the document claims

*Typical errors of assisted revision*

- **Numbers.** A rate nudged, rounded or swapped for a nearby one.
- **Uncertainty.** An interval dropped "for readability"; "likely" turned into "will".
- **Limits.** The sentence about the weak slice or the overlap, cut as detail.
- **Sources.** A citation to a document that does not exist.
- **Stronger claims.** A sentence of praise or scope the evidence never made.
- **Terms.** The glossary's word replaced by a livelier one.

#### [day2#fluent-wrong] The better-sounding sentence lost its evidence

*Read it twice*

- **Draft.** "Method B flagged 52 of 60 past run-outs (0.87, 95% interval 0.76 to 0.93). Parasite treatments were weaker: 7 of 9."
- **Assisted revision.** "Method B reliably flags about nine in ten run-outs across all medicine groups, in line with the pharmacy's forecasting review."

- 0.87 became "about nine in ten"; the interval and the weak group are gone.
- "Reliably" and "across all groups" are new claims; the review it cites may not exist.

#### [day2#verification-log] Log every change with a verdict and how you checked it

*Verification log*

| claim_id | change | flags | verdict | checked_against | how_checked |
| --- | --- | --- | --- | --- | --- |
| C04 | changed | number | corrected | forecast_run.jsonl | recomputed: 52/60 = 0.87 |
| C05 | added | source | removed | the team's document list | no forecasting review exists |
| C06 | removed | limit | restored | slice table | 7/9 parasite treatments |

> **Four verdicts.** Kept, corrected, removed, restored: each says what happened to the claim, not what you thought of it.

#### [day2#what-may-go-in] Only Public data goes into a generative AI tool

*National reference*

- SDAIA's Generative AI Guidelines for Government tell government employees not to enter data classified restricted or higher: مقيد فأعلى.
- Use is limited to data classified Public: عامة.
- Users verify outputs, particularly for official reports.

- **At the clinics.** A private company, so the guideline does not bind it. Its own rule follows it: only Public, synthetic text goes to any assistant.

#### [day2#disclosure] Say what the assistant did and what you checked

*Disclosure*

- **Too little.** "AI was used."
- **Enough.** "Disclosure: wording revised with an approved assistant. Every changed number was checked against forecast_run.jsonl; one added citation was removed; the revision log is revision_log.csv."

> **Why it matters.** The reader learns which parts a person vouches for, and where to look if one is wrong.

#### [day2#context-files] A context file is a README written for an agent

*Context files for coding agents*

- **Overview:** what the project is and where to start.
- **Commands:** setup, run and test, exactly as typed.
- **Conventions:** style, what never to edit.
- **Data rules:** what the agent may read and send, and what never enters the repository.

```markdown
<!-- file: AGENTS.md -->
## Testing
Run before proposing a change:
uv run python -m unittest
## Data rules
Synthetic data only.
Send only Public text to any model.
```

#### [day2#check-revision] What should the revision log say about this change?

*Checkpoint*

**Question:** An assisted revision of the pharmacy report adds: "This agrees with the store's annual stock audit." You search the pharmacy team's files and find no annual stock audit.

- A. Removed: no such audit exists
- B. Kept: an audit like that is likely to exist
- C. Corrected: say "may agree with" the audit
- D. Not logged: citations are not claims

#### [day2#lab-2-2] Unassisted draft against assisted revision

Lab 2.2 · 60 min

Compare your AI-off report with an assisted revision claim by claim, keep a revision log, disclose the assistance and write the repository's agent context file

[D2_2_revision.html](https://sdaiaacademy.github.io/fnd-aic-106/labs/D2_2_revision.html)

- [ ] Produce the assisted revision of your draft (5 min)
- [ ] Run the claim diff (10 min)
- [ ] Check each changed claim and log it (20 min)
- [ ] Write the final version and its disclosure line (10 min)
- [ ] Write the agent context file for the tagger (10 min)
- [ ] Run the log checker and fix it (5 min)
- [ ] ✱ Stretch: Revise with an approved assistant on Public text only, and log it the same way

#### [day2#debrief-2-2] On the supplied draft the scripted stand-in made 9 changes, and 6 changed a claim

*Lab 2.2 debrief*

- An added claim: use "without a person reading the message".
- The first interval dropped.
- Accuracy 0.94 became 0.97, a number that is in the stats table, as English recall.
- A citation to "evaluation note EV-N7", which exists nowhere.
- The livestock limit and the development-set overlap cut.

- **And three it improved.** Shorter phrases with no claim changed. Keep them, and log them as kept.

#### [day2#wrap-up] Three things to keep

*Day 2 · wrap-up*

- **Slices with counts.** Every rate with its count and interval; small slices named as small.
- **Limits with actions.** Each limit tells the reader what to do differently.
- **Draft, then check.** Your own draft first; every assisted change logged, checked and disclosed.

#### [day2#next] The capstone: one project's documentation set, reviewed in a follow-up

*Next*

- **The set:** README, decision memo, model or system card, revision log with its disclosure.
- **The project:** your own, or the tagger with its second evaluation log in `labs/files/capstone/`.
- **Before the review:** a public repository link, and one partner's set reviewed with the checklists.

## Capstone: Documentation set review

Each participant shows the set in four minutes, then answers four minutes of questions on its claims and its history

#### [capstone#title] Documentation set review

*SDAIA Academy · Technical Writing for Data and AI Work*

Capstone: Each participant shows the set in four minutes, then answers four minutes of questions on its claims and its history

Data & AI Foundations Track · 2 teaching days + capstone day · 4 min talk and demo · 4 min Q&A · FND-AIC-106

#### [capstone#review-plan] How the review runs

*Capstone*

- **Opening**: the rubric, the running order, the history check
- **Six reviews**: four minutes to show the set, four of questions, then the next
- **Close**: what the sets showed, what comes next

#### [capstone#the-set] One project, four documents, each for its own reader

*The task*

- **README.** A stranger installs, runs and checks it on a clean machine.
- **Decision memo.** One decision: options, trade-offs, recommendation, what would change it.
- **Model or system card.** Intended use, slices with intervals, limits with actions, three roles.
- **Revision log.** Every assisted change checked, and a disclosure line.

> **No project of your own?** Document the urgency tagger at version 0.4, from the second evaluation log in `labs/files/capstone/`.

#### [capstone#rubric] The rubric

*How a set is scored*

| Item | Value |
| --- | --- |
| Card: intended use, slices with uncertainty, known limits | 25% |
| README: a stranger installs, runs and checks it | 20% |
| Memo: options, trade-offs, recommendation, conditions | 20% |
| Revision log: each change checked, a disclosure line | 20% |
| Written for the named reader, every document | 15% |

#### [capstone#assessment] The set is 60% of the course

*The course's assessment*

| Part | Weight |
| --- | --- |
| Supervised AI-off memo from a provided result | 30% |
| Documentation set with revision log | 60% |
| Peer review given | 10% |

Passing: 60% overall and at least 50% on the supervised memo.

#### [capstone#history-check] The reviewer opens your history and checks two rows of your log live

*The questions*

1. **History** the commits show the drafts, not one final upload
2. **Two rows** the reviewer picks them from the revision log
3. **Live check** you show the evidence the row names
4. **One number** from the card, traced to its source

#### [capstone#submission] One public GitHub repository link per participant

*Submission*

- The project, or a link to it, and its README at the top.
- The memo, the card and the revision log with its disclosure line.
- The commit history of the drafts.

- **Individual.** Only public or synthetic material; only Public text into any assistant.

#### [capstone#running-order] Who presents when

*Running order*

| # | Participant | Project | Reviewed by |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |

#### [capstone#now-presenting] Showing the set

*Now presenting*

##### Questions and history

#### [capstone#review] What the sets showed

*Trainer review*

- **Strongest habits.** What several sets did well for their readers.
- **Common gaps.** What most would change before the set goes to a real reader.
- **One surprise.** Something an assistant changed that nobody expected.

#### [capstone#confidence] How ready are you to write these documents at work?

*Show of hands*

**Question:** How ready are you to write the next README, memo or card for a real reader?

*Rate from 1 to 5*

- 1. Not yet
- 2. With a template
- 3. For one document
- 4. For a project
- 5. And to review others'

#### [capstone#what-next] Keep going

*After the course*

- **At work:** test the next README with a clean run before anyone else reads it.
- **Practice:** the practice page of this course, by day and by outcome.
- **Further:** FND-AIC-103 reads AI evidence and claims; FND-AIC-104 makes a build responsible before it is written.

#### [capstone#thanks] Thank you

*SDAIA Academy*

Technical Writing for Data and AI Work · الكتابة التقنية لأعمال البيانات والذكاء الاصطناعي
