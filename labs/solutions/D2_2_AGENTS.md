# AGENTS.md: request urgency tagger

## Project overview

A small Python project that tags owners' appointment messages as urgent, soon or routine for the
reception queue of Tarthuth Veterinary Clinics (a fictional course case). The keyword rules are in
`urgency_tagger/rules.py`; the outputs of Model S and Model L are recorded files in
`data/recorded/`. Read `README.md` first.

## Setup and run commands

```sh
cp config.example.toml config.toml
uv run python -m urgency_tagger tag data/sample_requests.csv
uv run python -m urgency_tagger evaluate --system rules
```

## Testing

Run both before you propose a change, and report their last lines:

```sh
uv run python -m unittest discover -s tests
uv run python -m urgency_tagger check
```

`check` must print `check: ok, 30 sample rows, 400 test rows, 2 recorded systems`.

## Code conventions

- Python 3.11 or later, standard library only. Add no dependency without asking.
- Keep the keyword lists in `rules.py` in two blocks, English then Arabic.
- Never edit `data/test_set.csv` or `data/recorded/`: they are the evidence the reports cite.

## Data and security rules

- All data here is synthetic. Do not add real messages, owners' names, phone numbers or animals'
  records, even as examples.
- Send only Public, synthetic text to any hosted model or assistant.
- Do not change the numbers in `config.example.toml`: the decision memo quotes them.
