"""Keyword rules: the baseline tagger. Urgent words first, then soon words; anything else is routine."""
from __future__ import annotations

import re

URGENT = [
    "bleeding", "blood", "poison", "ate chocolate", "not breathing", "can't breathe", "cannot breathe",
    "seizure", "fitting", "collapsed", "hit by", "broken leg", "swallowed",
    "نزيف", "ينزف", "تنزف", "دم", "تسمم", "سم", "لا يتنفس", "لا تتنفس", "صعوبة في التنفس",
    "تشنج", "تشنجات", "سقط", "سقطت", "صدمته", "صدمتها", "كسر", "بلع", "بلعت",
]
SOON = [
    "vomiting", "vomit", "diarrhoea", "diarrhea", "limping", "not eating", "won't eat", "lump", "itching",
    "eye", "ear", "cough", "coughing", "swollen",
    "يستفرغ", "تستفرغ", "استفراغ", "إسهال", "اسهال", "يعرج", "تعرج", "لا يأكل", "لا تأكل", "ورم", "حكة",
    "عين", "عينه", "عينها", "أذن", "اذن", "كحة", "يكح", "تكح", "منتفخ", "منتفخة",
]

_SPLIT = re.compile(r"[^\w']+", re.UNICODE)


def _contains(text: str, phrase: str) -> bool:
    if " " in phrase:
        return phrase in text
    return phrase in _SPLIT.split(text)


def tag(message: str) -> str:
    """Return 'urgent', 'soon' or 'routine' for one owner's message."""
    text = message.lower()
    if any(_contains(text, w) for w in URGENT):
        return "urgent"
    if any(_contains(text, w) for w in SOON):
        return "soon"
    return "routine"
