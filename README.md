<!-- academy:title -->
# Technical Writing for Data and AI Work

الكتابة التقنية لأعمال البيانات والذكاء الاصطناعي

Data & AI Foundations Track · SDAIA Academy · FND-AIC-106 · Level 100

Write the README, decision memo, experiment report and model card a data or AI project runs on, for a named reader, with every claim checked

Participants write the documents that data and AI work runs on: a README, a design document, a decision memo, an experiment report and a model or system card. Each starts from a repository, a model comparison or an evaluation log and ends with a peer test; one draft is unassisted, another is revised with an assistant, and every claim is checked.

**Format:** Workshop: one and a half days of writing labs and a tracked follow-up review

**Course page:** https://sdaiaacademy.github.io/fnd-aic-106/
<!-- /academy:title -->

## Outcomes

| | Outcomes | Level | Evidence |
|---|---|---|---|
| LO1 | Identify the reader, purpose and required sections of five common technical document types, given five scenarios with named readers | Awareness | an outline per scenario matching the reference structure |
| LO2 | Draft a README that lets a stranger install, run and check a small project, given an undocumented repository | Applied | the README and a peer's run log on a clean environment |
| LO3 | Draft a one-page decision memo with options, trade-offs, a recommendation and the conditions that would change it, given a measured comparison of two models on quality, cost and latency | Applied | a memo scored on a five-criterion rubric |
| LO4 | Prepare an experiment report and a model card that state uncertainty, results by data slice and known limits, given an evaluation run log | Applied | a report and card that pass a peer checklist |
| LO5 | Compare an unassisted draft with an assisted revision for accuracy, clarity and invented content, given the participant's two drafts | Awareness | a revision log of how each claim was checked |

<!-- academy:units -->
## Units

| Unit | Title | Sessions | Slides |
|---|---|---|---|
| Day 1 | Writing for a reader | Write for one reader; READMEs, designs and decisions; The decision memo | [`slides/day1.html`](slides/day1.html) |
| Day 2 | Evidence documents and writing with assistance | Experiment reports and model cards; Writing with an assistant | [`slides/day2.html`](slides/day2.html) |
| Capstone | Documentation set review |  | [`slides/capstone.html`](slides/capstone.html) |
<!-- /academy:units -->

## Case study

**Tarthuth Veterinary Clinics** is a fictional private chain of veterinary clinics. Its two-person data team built a small Python project, the request urgency tagger, which sorts owners' appointment messages in Arabic, English and mixed text into urgent, soon and routine, and never wrote its documents. Every lab writes one of them from the project's own files.

Every file is synthetic and generated with a fixed seed (`labs/_tools/make_case.py`): the messages, a 400-message test set, the recorded outputs of a keyword-rules baseline and of two hosted models labelled Model S and Model L, their cost and latency, and the evaluation logs. No model was called to make them: the keyword rules are real code that runs, and the two models' outputs are simulated and recorded. The organisation, its roles and its data do not describe any real clinic. People appear by role only; owners, animals and messages by code.

<!-- academy:labs -->
## Labs

Every lab is a page in `labs/`, opened from the course page and from the lab slide of its session.

| | Session | Lab | File |
|---|---|---|---|
| 1.1 | Day 1 · Session 1 | Bottom-line-first rewrite | [`D1_1_bluf.html`](labs/D1_1_bluf.html) |
| 1.2 | Day 1 · Session 2 | Peer-tested README | [`D1_2_readme.html`](labs/D1_2_readme.html) |
| 1.3 | Day 1 · Session 3 | Decision memo | [`D1_3_memo.html`](labs/D1_3_memo.html) |
| 2.1 | Day 2 · Session 1 | Experiment report and model card | [`D2_1_report_card.html`](labs/D2_1_report_card.html) |
| 2.2 | Day 2 · Session 2 | Unassisted draft against assisted revision | [`D2_2_revision.html`](labs/D2_2_revision.html) |
<!-- /academy:labs -->

Each lab page runs small checkers from `labs/kit/` with `uv` on a laptop; `labs/README.md` says
what a participant needs and where each lab starts. No lab calls a model, needs a key or downloads
one.

## How the course is organised

One full day, a half day, and a follow-up review. Twelve hours in all (720 minutes):

| Part | Minutes | What happens |
|---|---|---|
| Instruction | 210 | Concepts, demonstrations and a checkpoint in each of the five sessions: 50 for session 1.1, then 40 each for 1.2, 1.3, 2.1 and 2.2 |
| Labs | 300 | Five writing labs of 60 minutes: 1.1, 1.2 and 1.3 on Day 1; 2.1 and 2.2 on Day 2 |
| Assessment | 60 | The supervised AI-off memo, opening Day 2: rules and handing out 5, writing 50, collection 5 |
| Guided self-study | 90 | Before Day 1: set up uv, open the case project, choose your own project (30). After Day 2: finish the documentation set (45) and review a partner's set with the lab checklists (15) |
| Capstone | 60 | The follow-up review in groups of six: opening 3; six participants each with 4 minutes to show the set, 4 minutes of questions and the history check, and 1 minute of changeover (54); close 3 |

Day 1 is 310 minutes of teaching (sessions of 110, 100 and 100); Day 2 is the 60-minute memo and
200 minutes of teaching (two sessions of 100).

## Assessment

- Supervised AI-off memo from a provided result (30%)
- Documentation set with revision log (60%)
- Peer review given (10%)

Passing: 60% overall and at least 50% on the supervised memo.

Authenticity: The supervised memo is written in session; revision logs and document history are inspected.

Certificate: completion with assessed work.

The memo is scored on the five-criterion rubric of lab 1.3. The documentation set is scored on
the capstone rubric below. Peer review given is scored on the reviews a participant gives in the
labs and on a partner's set before the follow-up.

## AI policy

AI-off for the supervised memo and one first draft. AI-tutor for feedback on structure in the
labs. AI-full for the logged assisted revision and for polishing the capstone.

The one first draft is the experiment report of lab 2.1, which lab 2.2 compares with an assisted
revision.

## Responsible use

Participants state limits honestly, disclose AI assistance, check every generated claim and citation, and keep personal or classified details out of examples

In the case, only Public, synthetic text goes to any assistant: the clinics' own rule, modelled on
SDAIA's Generative Artificial Intelligence Guidelines for Government, which limit government use
of these tools to data classified Public.

## Capstone

A documentation set for one project (README, decision memo, model or system card, revision log),
reviewed in a follow-up. The project is the participant's own, with public or synthetic data, or
the urgency tagger at version 0.4 with its second evaluation log (`labs/files/capstone/`). It is
individual and submitted as a public GitHub repository link before the review. At the review each
participant has four minutes to show the set and four for questions; the reviewer opens the
commit history and checks two rows of the revision log live.

| Criterion | Weight |
|---|---|
| The README lets a stranger install, run and check the project on a clean machine | 20 |
| The decision memo states options, trade-offs, a recommendation and the conditions that would change it | 20 |
| The card states intended use, results by slice with uncertainty, and known limits | 25 |
| The revision log shows how each assisted change was checked, with a disclosure line | 20 |
| Each document is written for its named reader: bottom line first, consistent terms, plain uncertainty | 15 |

## Prerequisites

- Has a small data or code project, own or provided, to document

<!-- academy:tools -->
## Tools

Each line is a capability; the examples are interchangeable.

- **Documents and diagrams as text:** Markdown in a Git repository, Mermaid, PlantUML
- **Prose and style checks:** Vale, a spelling and grammar checker
- **Writing assistant:** a locally served open-weight model, an approved general-purpose assistant
<!-- /academy:tools -->

<!-- academy:sources -->
## Sources

### National references

- [SDAIA, AI Ethics Principles (English)](https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf)
- [سدايا، مبادئ أخلاقيات الذكاء الاصطناعي (Arabic)](https://sdaia.gov.sa/ar/SDAIA/about/Documents/ai-principles.pdf)
- [SDAIA, Generative Artificial Intelligence Guidelines for Government (English)](https://sdaia.gov.sa/en/SDAIA/about/Files/GenAIGuidelinesForGovernmentENCompressed.pdf)
- [سدايا، المبادئ التوجيهية للذكاء الاصطناعي التوليدي للجهات الحكومية (Arabic)](https://sdaia.gov.sa/ar/SDAIA/about/Files/GenAIGuidelinesForGovernmentARCompressed.pdf)

### Documents for systems and evidence

- [Mitchell et al., Model Cards for Model Reporting (2019)](https://arxiv.org/abs/1810.03993)
- [Hugging Face Hub documentation: Model Cards](https://huggingface.co/docs/hub/model-cards)
- [Michael Nygard, Documenting Architecture Decisions (2011)](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [Architectural Decision Records](https://adr.github.io/)
- [Diátaxis, a systematic approach to technical documentation](https://diataxis.fr/)
- [AGENTS.md, a format for guiding coding agents](https://agents.md/)

### Writing for a reader

- [Google for Developers, Technical Writing One](https://developers.google.com/tech-writing/one)

### Tools

- [Mermaid: diagrams from text](https://mermaid.js.org/intro/)
- [GitHub Docs: Creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)
- [PlantUML](https://plantuml.com/)
- [Vale documentation](https://docs.vale.sh/)
<!-- /academy:sources -->

### National references

- SDAIA AI Ethics Principles: <https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf> (Arabic: <https://sdaia.gov.sa/ar/SDAIA/about/Documents/ai-principles.pdf>)
- SDAIA Generative Artificial Intelligence Guidelines for Government: <https://sdaia.gov.sa/en/SDAIA/about/Files/GenAIGuidelinesForGovernmentENCompressed.pdf> (Arabic: <https://sdaia.gov.sa/ar/SDAIA/about/Files/GenAIGuidelinesForGovernmentARCompressed.pdf>)
