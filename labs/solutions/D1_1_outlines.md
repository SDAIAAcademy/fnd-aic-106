# Reference outlines for lab 1.1

The reference structure each participant's outline is compared with. Section names may differ;
what each section does may not.

## Scenario 1

- Reader: a new developer, alone, on the first morning
- Purpose: install, run and check the tagger without help
- Document: README
- Sections:
  1. What the tagger does, in two sentences, and what it does not do
  2. Requirements: Python version, uv, no key needed
  3. Install: the exact commands, the config copy step
  4. Run: tag the sample messages, and what the output looks like
  5. Check: the tests and the data check, with their expected last lines
  6. Where things are: folders, data, recorded outputs; who owns the project

## Scenario 2

- Reader: the lead veterinarian, approving before any code is written
- Purpose: approve, change or refuse a proposed change
- Document: design document
- Sections:
  1. Summary: the change and the decision asked for
  2. Problem and goals, with what is out of scope
  3. Proposed design, with a text diagram of the message flow
  4. Alternatives considered and why not
  5. Risks, failure cases and how a livestock message reaches a veterinarian if the species is missed
  6. Open questions, reviewers and approver

## Scenario 3

- Reader: the operations director, ten minutes, signs one option
- Purpose: choose a tagger for the reception desk
- Document: decision memo
- Sections:
  1. Bottom line: the recommendation and the decision asked for
  2. Options: rules, Model S, Model L
  3. Trade-offs: quality, cost, latency, with the measured numbers and their intervals
  4. Recommendation and why
  5. What would change the recommendation
  6. Author, reviewer, the decision and its date

## Scenario 4

- Reader: the data team lead, now and at the next run
- Purpose: record a run so it can be repeated and compared
- Document: experiment report
- Sections:
  1. Question and the result in one paragraph
  2. Setup: data, prompt version, settings, scorer, run identifier
  3. Results overall and by slice, with counts and intervals
  4. Uncertainty and threats: small slices, overlap with development data
  5. Limits and what the result does not show
  6. Next steps and how to repeat the run

## Scenario 5

- Reader: the head of reception, not a programmer
- Purpose: decide which messages her staff may leave to the tag
- Document: model card (or a system card for the tagger with its queue)
- Sections:
  1. What the tagger is for and who uses it
  2. What it is not for (out of scope)
  3. Evaluation data, in words a non-programmer can read
  4. Results by kind of message, with counts and intervals
  5. Known limits and what staff must do about each
  6. Ethical considerations, owner, reviewer and approver, and the date
