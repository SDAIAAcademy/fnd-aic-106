---
course: "Technical Writing for Data and AI Work"
code: "FND-AIC-106"
version: "2027.1.0"
deck: "day2"
day: 2
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-aic-106/slides/day2.html"
---

# Technical Writing for Data and AI Work

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
