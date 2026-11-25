# Experiment report: Model L on the 400-message test set, run EV-L3

To: data team lead · Author: data analyst · Reviewed by: a second analyst · Run date: 2026-10-14

## Result in brief

Model L found 75 of 80 urgent messages (urgent recall 0.94, 95% interval 0.86 to 0.97) and tagged
0.94 of all messages correctly. It is weaker on livestock: 8 of 12 urgent livestock messages
(0.67, interval 0.39 to 0.86). Twelve test messages are also in the development set.

## Setup

- System: Model L, prompt version p3, temperature 0; tags urgent, soon or routine.
- Data: `test_set.csv`, 400 synthetic messages, 80 of them urgent; 230 Arabic, 146 English, 24 mixed.
- Scorer: exact match with the agreed tag. Statistics from `kit/evalstats.py` on `eval_log.jsonl`.

## Results

| Slice | Messages | Urgent found | Urgent recall (95% interval) | Accuracy |
|---|---|---|---|---|
| All | 400 | 75/80 | 0.94 (0.86 to 0.97) | 0.94 |
| Arabic | 230 | 42/46 | 0.91 (0.80 to 0.97) | 0.94 |
| English | 146 | 29/30 | 0.97 (0.83 to 0.99) | 0.95 |
| Mixed Arabic and English | 24 | 4/4 | 1.00 (0.51 to 1.00) | 0.79 |
| Cats and dogs | 300 | 61/62 | 0.98 (0.91 to 1.00) | 0.94 |
| Livestock | 70 | 8/12 | 0.67 (0.39 to 0.86) | 0.90 |
| Other animals | 30 | 6/6 | 1.00 (0.61 to 1.00) | 0.93 |

Model L tagged 9 messages urgent that were not. Time to a tag: median 2.41 s, 95th percentile 5.59 s.

## Uncertainty

Only the overall rate rests on enough urgent messages to be useful: its interval spans 0.86 to
0.97, so reception's 0.90 is likely but not shown. The livestock interval reaches from 0.39 to
0.86 on 12 urgent messages: the weakness is likely real, its size is not known. Mixed messages
are 24, with 4 urgent: their accuracy of 0.79 is the lowest of any language and rests on few
messages.

## Limits

- Twelve test messages also appear in the development set, where prompt p3 was tuned. On those
  12 the tag was always right; without them accuracy is 0.93 and urgent recall stays 0.94 (73/78).
- The messages are synthetic; real owners write longer, with spelling the test set lacks.
- Model L's outputs were recorded once; a second run may differ.

## Next steps

1. Remove the 12 overlapping messages and add the 150 new labelled messages, with more urgent
   livestock and mixed messages.
2. Repeat the run with the same prompt and settings and compare by slice.
3. To repeat this run: `uv run kit/evalstats.py files/D2_1/eval_log.jsonl`.
