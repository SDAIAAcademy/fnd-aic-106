# The decision the operations director must make

Fictional case, synthetic figures.

**Reader.** The operations director of Tarthuth Veterinary Clinics. He will read one page and sign
one option for the reception desk for next quarter.

**The choice.** Which tagger sorts the reception queue: the keyword rules, Model S or Model L.

**What reception needs** (from the head of reception):

- Urgent recall of at least 0.90: at least nine urgent messages in ten tagged urgent.
- The tag shown within 10 seconds of a message arriving, for 95% of messages. Nobody waits at a
  screen for it: messages arrive in a queue that reception reads.

**What the clinics can spend.** SAR 400 a month for the tagger's model use. The clinics receive
about 9,000 messages a month.

**The evidence.** `comparison.csv`: the three taggers on the same 400 synthetic test messages,
80 of them urgent. Urgent recall has its 95% interval (`urgent_recall_low`, `urgent_recall_high`).
Cost is in SAR per 1,000 messages at the synthetic prices of the project's configuration. Latency
is the time to a tag, median and 95th percentile, in seconds.

**What the comparison does not contain.** Results by kind of message (language, species) are in
the evaluation log of lab 2.1, not here.
