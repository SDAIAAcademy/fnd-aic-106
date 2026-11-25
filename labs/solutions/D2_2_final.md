# Experiment report: Model L, run EV-L3

To: data team lead · Author: data analyst · Run date: 2026-10-14

## Result in brief

To measure the tagger, we ran Model L on the 400 test messages. It found 75 of 80 urgent
messages, an urgent recall of 0.94 (95% interval 0.86 to 0.97). Reception asked for 0.90, which
is likely but not shown.

## Setup

Model L with prompt p3 and temperature 0 tagged each message as urgent, soon or routine. Most of
the messages are in Arabic (230), some in English (146) and 24 mix the two. The scorer counts an
exact match with the agreed tag.

## Results

Overall accuracy was 0.94. On Arabic messages urgent recall was 0.91 (42/46), on English 0.97
(29/30). Livestock messages were weaker: it found 8/12 urgent livestock messages, 0.67, with an
interval from 0.39 to 0.86. Mixed messages had the lowest accuracy, 0.79, on only 24 messages.

## Limits

Twelve test messages are also in the development set, so the results may be slightly too good.
The messages are synthetic. The tag was wrong in the urgent direction 9 times.

## Next steps

Add more urgent livestock and mixed messages to the test set and run it again.

Disclosure: the wording of this report was revised with an assisted revision (a scripted stand-in
in this course). Every changed sentence was checked against `eval_log.jsonl` with
`kit/evalstats.py`; changed numbers, the added claim and the added citation were rejected, and the
dropped limits restored. The revision log is `revision_log.csv`.
