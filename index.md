---
course: "Technical Writing for Data and AI Work"
code: "FND-AIC-106"
version: "2027.1.0"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-aic-106/index.html"
---

# Technical Writing for Data and AI Work

الكتابة التقنية لأعمال البيانات والذكاء الاصطناعي

Data & AI Foundations Track · 2 teaching days + capstone day · 12 hours · Level 100

Write the README, decision memo, experiment report and model card a data or AI project runs on, for a named reader, with every claim checked

Participants write the documents that data and AI work runs on: a README, a design document, a decision memo, an experiment report and a model or system card. Each starts from a repository, a model comparison or an evaluation log and ends with a peer test; one draft is unassisted, another is revised with an assistant, and every claim is checked.

**Who it is for:** Beginners. Graduates, career changers and computing professionals preparing for Developer or Specialist courses, who can run a Python notebook but have not yet studied AI methods.

**Format:** Workshop: one and a half days of writing labs and a tracked follow-up review

## The case study

**Tarthuth Veterinary Clinics.** A fictional private chain of veterinary clinics whose two-person data team built a small Python project, the request urgency tagger, that sorts owners' appointment messages in Arabic, English and mixed text into urgent, soon and routine. Every file is synthetic and generated with a fixed seed: the messages, a 400-message test set, the outputs of a keyword-rules baseline that really runs, the simulated and recorded outputs of two hosted models labelled Model S and Model L with their cost and latency, and the evaluation log. No model was called.

## The course

### Day 1: Writing for a reader

Slides: https://sdaiaacademy.github.io/fnd-aic-106/slides/day1.md

- **Session 1: Write for one reader**
  - Name the reader, purpose and decision behind a request for a document
  - Choose the document type and its required sections for a scenario
  - Rewrite an update so the bottom line, the request and the uncertainty come first
  - [Lab 1.1: Bottom-line-first rewrite (60 min)](https://sdaiaacademy.github.io/fnd-aic-106/labs/D1_1_bluf.html)
- **Session 2: READMEs, designs and decisions**
  - Write install, run and check steps a stranger can follow on a clean machine
  - Separate a README from a design document and a decision record
  - Draw a pipeline as text that the repository renders
  - [Lab 1.2: Peer-tested README (60 min)](https://sdaiaacademy.github.io/fnd-aic-106/labs/D1_2_readme.html)
- **Session 3: The decision memo**
  - State the decision and the recommendation in the first two sentences
  - Compare options on quality, cost and latency with numbers traced to the source
  - Write the conditions under which the recommendation would change
  - [Lab 1.3: Decision memo (60 min)](https://sdaiaacademy.github.io/fnd-aic-106/labs/D1_3_memo.html)

### Day 2: Evidence documents and writing with assistance

Slides: https://sdaiaacademy.github.io/fnd-aic-106/slides/day2.md

- **Session 1: Experiment reports and model cards**
  - Report results by data slice with the number of cases and an interval
  - Write known limits and out-of-scope uses a reader can act on
  - Check a report and a card with a peer checklist
  - [Lab 2.1: Experiment report and model card (60 min)](https://sdaiaacademy.github.io/fnd-aic-106/labs/D2_1_report_card.html)
- **Session 2: Writing with an assistant**
  - Spot the typical errors of an assisted revision: changed numbers, dropped limits, invented sources
  - Keep a revision log that says how each claim was checked
  - Write a disclosure line and a context file for a coding agent
  - [Lab 2.2: Unassisted draft against assisted revision (60 min)](https://sdaiaacademy.github.io/fnd-aic-106/labs/D2_2_revision.html)

### Capstone: Documentation set review

Slides: https://sdaiaacademy.github.io/fnd-aic-106/slides/capstone.md

## Capstone

A documentation set for one project (README, decision memo, model or system card, revision log), reviewed in a follow-up

**What you submit:** An individual task, submitted as a public GitHub repository link before the follow-up review. The repository holds the project or a link to it, the README, the decision memo, the model or system card, the revision log with its disclosure line, and the commit history that shows the drafts. Only public or synthetic material is used, and only Public text goes to any assistant.

**Rubric:**

- The README lets a stranger install, run and check the project on a clean machine: 20%
- The decision memo states options, trade-offs, a recommendation and the conditions that would change it: 20%
- The card states intended use, results by slice with uncertainty, and known limits: 25%
- The revision log shows how each assisted change was checked, with a disclosure line: 20%
- Each document is written for its named reader: bottom line first, consistent terms, plain uncertainty: 15%

## Outcomes

- **LO1** Identify the reader, purpose and required sections of five common technical document types, given five scenarios with named readers (Awareness) Evidence: an outline per scenario matching the reference structure
- **LO2** Draft a README that lets a stranger install, run and check a small project, given an undocumented repository (Applied) Evidence: the README and a peer's run log on a clean environment
- **LO3** Draft a one-page decision memo with options, trade-offs, a recommendation and the conditions that would change it, given a measured comparison of two models on quality, cost and latency (Applied) Evidence: a memo scored on a five-criterion rubric
- **LO4** Prepare an experiment report and a model card that state uncertainty, results by data slice and known limits, given an evaluation run log (Applied) Evidence: a report and card that pass a peer checklist
- **LO5** Compare an unassisted draft with an assisted revision for accuracy, clarity and invented content, given the participant's two drafts (Awareness) Evidence: a revision log of how each claim was checked

## Tools

- **Documents and diagrams as text:** Markdown in a Git repository, Mermaid, PlantUML
- **Prose and style checks:** Vale, a spelling and grammar checker
- **Writing assistant:** a locally served open-weight model, an approved general-purpose assistant

## Prerequisites

- Has a small data or code project, own or provided, to document

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

---

SDAIA Academy · Data & AI Foundations Track · Technical Writing for Data and AI Work

Course version 2027.1.0 · engine 1.0.0 · built 2026-11-25 · commit 9351b4a
