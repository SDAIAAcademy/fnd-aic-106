# Model card: the request urgency tagger with Model L

For the head of reception. Version 0.3, evaluated in run EV-L3 on 2026-10-14.

Owner: data team lead
Reviewed by: lead veterinarian
Approved by: operations director

## What it is for

It puts a tag on each owner's message (urgent, soon or routine) so that reception reads urgent
messages first. Reception staff still read every message. A veterinarian decides about the
animal; the tag decides only the order of the queue.

## What it is not for

- Deciding whether an animal is seen, or when. That is a person's decision.
- Messages typed by staff during a phone call with a frightened owner: handle the call first.
- Advice to owners. The tag is never shown to them.

## Evaluation data

400 synthetic owners' messages written for testing, 80 of them urgent: 230 in Arabic, 146 in
English and 24 mixing the two; 300 about cats and dogs, 70 about livestock, 30 about other
animals. Each has a tag agreed by reception and a veterinarian.

## Results by kind of message

| Kind of message | Messages | Urgent found | Urgent recall (95% interval) |
|---|---|---|---|
| All | 400 | 75/80 | 0.94 (0.86 to 0.97) |
| Cats and dogs | 300 | 61/62 | 0.98 (0.91 to 1.00) |
| Livestock | 70 | 8/12 | 0.67 (0.39 to 0.86) |
| Mixed Arabic and English | 24 | 4/4 | 1.00 (0.51 to 1.00) |

Out of 80 urgent messages it missed 5. It also tagged 9 messages urgent that were not.

## Known limits, and what staff do about each

- **Livestock:** it found 8 of 12 urgent livestock messages. Read every livestock message at once,
  whatever its tag.
- **Mixed Arabic and English:** only 24 such messages were tested, and 0.79 of them were tagged
  right, the lowest of any language. Read them at once too.
- **Small test:** with 80 urgent messages, its urgent recall of 0.94 could be as low as 0.86 (the
  95% interval). Reception asked for 0.90: likely, not shown.
- **Test overlap:** 12 test messages are also in the development set, used to tune the tagger; the results above
  include them, and without them urgent recall is unchanged at 0.94.

## Ethical considerations

Owners are not told their message was tagged by software unless the clinics' notice says so;
the clinics' rule is to state it in the web form. A missed urgent message can harm an animal,
so the tag orders the queue and never closes a message. Only synthetic or Public text was sent to
the model in testing.

## Contact

Report a wrong tag to the data team lead with the message's code, never its text.
