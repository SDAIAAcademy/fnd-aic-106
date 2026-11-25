# Decision memo: which tagger should sort the reception queue next quarter?

To: operations director · From: data team lead · Reviewed by: lead veterinarian
Decision needed by: the start of next quarter

## Bottom line

I recommend Model L for next quarter. Please sign it, on the condition that we re-measure it
on the larger test set before the quarter ends.

## Options

1. Keyword rules: the current tagger, no model cost.
2. Model S: a smaller hosted model.
3. Model L: a larger hosted model.

## Trade-offs

All three were measured on the same 400 synthetic test messages, 80 of them urgent.

| | Keyword rules | Model S | Model L |
|---|---|---|---|
| Urgent recall (95% interval) | 0.66 (0.55 to 0.76) | 0.82 (0.73 to 0.89) | 0.94 (0.86 to 0.97) |
| Cost a month at 9,000 messages | SAR 0 | SAR 72.18 | SAR 337.68 |
| Time to a tag, 95% of messages | under 0.01 s | 1.24 s | 5.59 s |

Only Model L reaches the 0.90 urgent recall reception asked for, and even its interval reaches
down to 0.86, so the target is likely but not certain. Model S finds more urgent messages
than the rules, but its whole interval lies below 0.90. Model L costs almost five times
as much as Model S and is slower, yet it stays within the SAR 400 budget and well inside the
10-second limit.

## Recommendation

Model L, because urgent recall is the requirement that protects animals, and it is the only
option likely to meet it within the budget and the time limit. Reception keeps reading every
message; the tag only orders the queue.

## What would change this

- If the larger test set puts Model L's urgent recall below 0.90, I would bring a new option
  rather than keep it.
- If messages reach 10,661 a month, Model L costs more than the SAR 400 budget at the current price.
- If its 95th-percentile time passes 10 seconds, it breaks reception's limit.

Working: 9,000 / 1,000 x 37.52 = 337.68; 9,000 / 1,000 x 8.02 = 72.18; 400 / 37.52 x 1,000 = 10,660.98, so 10,661 messages cost more than SAR 400; 37.52 / 8.02 = 4.7, almost five times; 0.01 s is a bound on the rules' 0.00.
