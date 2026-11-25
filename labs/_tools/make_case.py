# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Write the synthetic case files of Tarthuth Veterinary Clinics (fictional), seed 106.

From labs/:  uv run _tools/make_case.py

Writes the tagger's data (sample requests, the 400-message test set, the recorded outputs of
Model S and Model L), the comparison table of lab 1.3, the evaluation log of lab 2.1, the second
evaluation log of the capstone, and labs/solutions/case_numbers.json with every figure the slides,
the answer key and the reference documents quote. Same bytes on every run. Model S and Model L
are labels for two hosted models; their outputs are simulated here, not produced by any model.
The keyword-rules baseline is the real code of the tagger, run on the same messages.
"""
from __future__ import annotations

import csv
import io
import json
import math
import random
import sys
from pathlib import Path

LABS = Path(__file__).resolve().parents[1]
REPO = LABS / "files" / "urgency-tagger"
sys.path.insert(0, str(REPO))
from urgency_tagger import metrics, rules  # noqa: E402

SEED = 106

SPECIES = {
    "companion": {"en": ["My cat", "My dog", "Our kitten", "Our puppy"], "ar": ["قطتي", "كلبي", "قطنا الصغير", "جرونا"]},
    "livestock": {"en": ["Our camel", "The sheep", "Our goat", "Our horse"], "ar": ["الناقة", "الخروف", "الماعز", "الحصان"]},
    "other": {"en": ["My parrot", "My rabbit", "Our tortoise"], "ar": ["الببغاء", "الأرنب", "السلحفاة"]},
}
SYMPTOMS = {
    ("urgent", "explicit"): {
        "en": ["is bleeding from the mouth", "ate chocolate this morning", "is not breathing well", "had a seizure",
               "was hit by a car", "swallowed a needle", "collapsed and is shaking"],
        "ar": ["ينزف من فمه", "أكل سم فئران", "لا يتنفس جيدا", "جاءته تشنجات", "صدمته سيارة", "بلع إبرة", "سقط ولا يتحرك"],
    },
    ("urgent", "implicit"): {
        "en": ["keeps straining and nothing comes out", "has a hard belly that is getting bigger", "cannot stand up",
               "has pale cold gums", "has been in labour for many hours with no baby", "has not passed urine all day"],
        "ar": ["يحاول التبول ولا يخرج شيء", "بطنه قاس ويكبر", "لا يستطيع الوقوف", "لثته بيضاء وباردة",
               "في الولادة منذ ساعات ولم يخرج المولود", "لم يتبول طوال اليوم"],
    },
    ("soon", "explicit"): {
        "en": ["has been vomiting since yesterday", "is limping on the back leg", "is not eating for two days",
               "has a lump on the neck", "has a cough", "has diarrhoea"],
        "ar": ["يستفرغ من أمس", "يعرج على رجله الخلفية", "لا يأكل منذ يومين", "عنده ورم في الرقبة", "عنده كحة", "عنده إسهال"],
    },
    ("soon", "implicit"): {
        "en": ["seems tired and quiet", "drinks far more water than usual", "is losing weight", "keeps shaking the head"],
        "ar": ["خامل وهادئ على غير عادته", "يشرب ماء أكثر من المعتاد", "ينقص وزنه", "يهز رأسه كثيرا"],
    },
    ("routine", "plain"): {
        "en": ["needs the yearly vaccination", "is due for a nail trim", "needs a health certificate for travel",
               "needs a check-up", "needs deworming", "needs a microchip"],
        "ar": ["يحتاج تطعيم سنوي", "يحتاج قص أظافر", "يحتاج شهادة صحية للسفر", "يحتاج فحص دوري", "يحتاج دواء الديدان", "يحتاج شريحة تعريف"],
    },
    ("routine", "decoy"): {
        "en": ["has a small cut that stopped bleeding last week", "had a blood test last month and needs the follow-up"],
        "ar": ["عنده جرح صغير توقف الدم منه الأسبوع الماضي", "سوى تحليل دم الشهر الماضي ويحتاج المراجعة"],
    },
}
OPENERS = {"en": ["", "Hello, ", "Please help, ", "Good day, "], "ar": ["", "السلام عليكم، ", "لو سمحتم، ", "مرحبا، "]}
CLOSERS = {"en": ["", " Can we come in?", " When can you see us?"], "ar": ["", " متى نقدر نجي؟", " هل يوجد موعد؟"]}


def message(rng: random.Random, lang: str, group: str, gold: str, kind: str) -> str:
    if lang == "mixed":
        subj = rng.choice(SPECIES[group]["ar"])
        sym = rng.choice(SYMPTOMS[(gold, kind)]["en"])
        return f"{subj} {sym}"
    subj = rng.choice(SPECIES[group][lang])
    sym = rng.choice(SYMPTOMS[(gold, kind)][lang])
    return f"{rng.choice(OPENERS[lang])}{subj} {sym}.{rng.choice(CLOSERS[lang])}".strip()


def exact(rng: random.Random, counts: dict[str, int]) -> list[str]:
    out = [k for k, v in counts.items() for _ in range(v)]
    rng.shuffle(out)
    return out


WRONG = {"urgent": ["soon", "soon", "soon", "routine"], "soon": ["routine", "routine", "urgent"], "routine": ["soon", "soon", "urgent"]}
MODELS = {
    "model_s": {"p": {("urgent", "explicit"): 0.95, ("urgent", "implicit"): 0.78, ("soon", "explicit"): 0.88,
                      ("soon", "implicit"): 0.74, ("routine", "plain"): 0.94, ("routine", "decoy"): 0.80},
                "livestock_urgent": -0.22, "mixed": -0.15, "lat_median": 0.70, "lat_sigma": 0.38, "out_tokens": 6},
    "model_l": {"p": {("urgent", "explicit"): 0.98, ("urgent", "implicit"): 0.90, ("soon", "explicit"): 0.92,
                      ("soon", "implicit"): 0.84, ("routine", "plain"): 0.95, ("routine", "decoy"): 0.90},
                "livestock_urgent": -0.18, "mixed": -0.22, "lat_median": 2.60, "lat_sigma": 0.50, "out_tokens": 40},
}


def simulate(rng: random.Random, name: str, item: dict) -> dict:
    m = MODELS[name]
    p = m["p"][(item["gold"], item["kind"])]
    if item["gold"] == "urgent" and item["species_group"] == "livestock":
        p += m["livestock_urgent"]
    if item["lang"] == "mixed":
        p += m["mixed"]
    ok = rng.random() < p or (name == "model_l" and item["in_dev_set"])
    pred = item["gold"] if ok else rng.choice(WRONG[item["gold"]])
    lat = m["lat_median"] * math.exp(rng.gauss(0, m["lat_sigma"]))
    words = len(item["message"].split())
    return {"pred": pred, "latency_ms": int(round(lat * 1000)), "tokens_in": 180 + round(words * 1.6), "tokens_out": m["out_tokens"]}


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    path.write_bytes(buf.getvalue().encode("utf-8"))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))


def summary(gold, pred, lat=None, cost=None) -> dict:
    k, n = metrics.recall(gold, pred, "urgent")
    lo, hi = metrics.wilson(k, n)
    d = {"n": len(gold), "urgent_hits": k, "urgent_n": n, "urgent_recall": round(k / n, 2) if n else None,
         "urgent_ci": [round(lo, 2), round(hi, 2)],
         "accuracy": round(sum(g == p for g, p in zip(gold, pred)) / len(gold), 2),
         "macro_f1": round(metrics.macro_f1(gold, pred), 2)}
    if lat is not None:
        d["latency_median_s"] = round(metrics.percentile(lat, 50), 2)
        d["latency_p95_s"] = round(metrics.percentile(lat, 95), 2)
    if cost is not None:
        d["cost_sar_per_1000"] = round(sum(cost) / len(cost) * 1000, 2)
    return d


def main() -> None:
    rng = random.Random(SEED)
    prices = {"model_s": 0.04, "model_l": 0.16}

    # Sample requests for the README lab: no labels, a request code, a date and a channel.
    sample = []
    for i in range(30):
        lang = rng.choice(["ar", "ar", "en", "mixed"])
        group = rng.choice(["companion", "companion", "companion", "livestock", "other"])
        gold = rng.choice(["urgent", "soon", "soon", "routine", "routine", "routine"])
        kind = {"urgent": rng.choice(["explicit", "implicit"]), "soon": rng.choice(["explicit", "implicit"]), "routine": "plain"}[gold]
        sample.append({"id": f"SR-T{701 + i}", "received": f"2026-10-{1 + i % 28:02d}",
                       "channel": rng.choice(["web form", "front desk", "phone note"]),
                       "message": message(rng, lang, group, gold, kind)})
    write_csv(REPO / "data" / "sample_requests.csv", sample, ["id", "received", "channel", "message"])

    # The test set: 400 messages with exact slice sizes.
    langs = exact(rng, {"ar": 230, "en": 146, "mixed": 24})
    groups = exact(rng, {"companion": 300, "livestock": 70, "other": 30})
    golds = exact(rng, {"urgent": 80, "soon": 120, "routine": 200})
    dev = set(rng.sample(range(400), 12))
    items = []
    for i in range(400):
        g = golds[i]
        if g == "routine":
            kind = "decoy" if rng.random() < 0.12 else "plain"
        else:
            kind = "explicit" if rng.random() < 0.6 else "implicit"
        items.append({"id": f"TS-K{1001 + i}", "lang": langs[i], "species_group": groups[i], "kind": kind,
                      "gold": g, "in_dev_set": i in dev, "message": message(rng, langs[i], groups[i], g, kind)})
    write_csv(REPO / "data" / "test_set.csv",
              [{k: (str(v).lower() if isinstance(v, bool) else v) for k, v in it.items() if k != "kind"} for it in items],
              ["id", "lang", "species_group", "message", "gold", "in_dev_set"])

    recorded = {}
    for name in ("model_s", "model_l"):
        r = random.Random(f"{SEED}-{name}")
        recorded[name] = [dict(id=it["id"], **simulate(r, name, it)) for it in items]
        write_csv(REPO / "data" / "recorded" / f"{name}.csv", recorded[name], ["id", "pred", "latency_ms", "tokens_in", "tokens_out"])

    gold = [it["gold"] for it in items]
    rule_pred = [rules.tag(it["message"]) for it in items]
    numbers = {"seed": SEED, "systems": {}}
    numbers["systems"]["rules"] = summary(gold, rule_pred)
    numbers["systems"]["rules"].update({"latency_median_s": 0.0, "latency_p95_s": 0.0, "cost_sar_per_1000": 0.0})
    for name in recorded:
        pred = [r["pred"] for r in recorded[name]]
        lat = [r["latency_ms"] / 1000 for r in recorded[name]]
        cost = [(r["tokens_in"] + r["tokens_out"]) / 1000 * prices[name] for r in recorded[name]]
        numbers["systems"][name] = summary(gold, pred, lat, cost)

    # Lab 1.3: the measured comparison.
    rows = []
    for key, label in (("rules", "Keyword rules"), ("model_s", "Model S"), ("model_l", "Model L")):
        s = numbers["systems"][key]
        rows.append({"system": label, "test_messages": s["n"], "urgent_found": s["urgent_hits"], "urgent_total": s["urgent_n"],
                     "urgent_recall": f"{s['urgent_recall']:.2f}", "urgent_recall_low": f"{s['urgent_ci'][0]:.2f}",
                     "urgent_recall_high": f"{s['urgent_ci'][1]:.2f}", "accuracy": f"{s['accuracy']:.2f}",
                     "macro_f1": f"{s['macro_f1']:.2f}", "cost_sar_per_1000_messages": f"{s['cost_sar_per_1000']:.2f}",
                     "latency_median_s": f"{s['latency_median_s']:.2f}", "latency_p95_s": f"{s['latency_p95_s']:.2f}"})
    write_csv(LABS / "files" / "D1_3" / "comparison.csv", rows, list(rows[0].keys()))

    # Lab 2.1: the evaluation log of Model L, one JSON record per line, the run record first.
    def log_lines(system_label, preds, lats, run_extra):
        head = {"type": "run", "system": system_label, "task": "urgency tag (urgent, soon, routine)",
                "test_set": "test_set.csv, 400 messages", "prompt_version": "p3", "temperature": 0,
                "run_date": "2026-10-14", "scorer": "exact label match", **run_extra}
        out = [json.dumps(head, ensure_ascii=False)]
        for it, p, l in zip(items, preds, lats):
            words = len(it["message"].split())
            out.append(json.dumps({"type": "item", "id": it["id"], "lang": it["lang"], "species_group": it["species_group"],
                                   "length": "short" if words <= 6 else "long", "in_dev_set": it["in_dev_set"],
                                   "gold": it["gold"], "pred": p, "latency_ms": l}, ensure_ascii=False))
        return "\n".join(out) + "\n"

    s_pred = [r["pred"] for r in recorded["model_l"]]
    s_lat = [r["latency_ms"] for r in recorded["model_l"]]
    write_text(LABS / "files" / "D2_1" / "eval_log.jsonl", log_lines("Model L", s_pred, s_lat, {"run_id": "EV-L3"}))

    # Capstone: version 0.4, Model L with a keyword override for urgent words (computed, not simulated).
    v2 = ["urgent" if rp == "urgent" else sp for rp, sp in zip(rule_pred, s_pred)]
    write_text(LABS / "files" / "capstone" / "eval_log_v2.jsonl",
               log_lines("Model L with keyword override", v2, s_lat, {"run_id": "EV-L4", "run_date": "2026-11-02"}))
    numbers["systems"]["model_l_override"] = summary(gold, v2)

    # Slices of Model L, for the answer key and the reference report.
    slices = {}
    for field in ("lang", "species_group"):
        for val in sorted({it[field] for it in items}):
            idx = [i for i, it in enumerate(items) if it[field] == val]
            slices[f"{field}={val}"] = summary([gold[i] for i in idx], [s_pred[i] for i in idx])
    idx = [i for i, it in enumerate(items) if not it["in_dev_set"]]
    slices["without_dev_overlap"] = summary([gold[i] for i in idx], [s_pred[i] for i in idx])
    idx = [i for i, it in enumerate(items) if it["in_dev_set"]]
    slices["dev_overlap_only"] = summary([gold[i] for i in idx], [s_pred[i] for i in idx])
    numbers["model_l_slices"] = slices
    write_text(LABS / "solutions" / "case_numbers.json", json.dumps(numbers, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({k: {kk: v[kk] for kk in ("urgent_recall", "urgent_ci", "macro_f1", "accuracy")} for k, v in numbers["systems"].items()}, indent=0))
    for k, v in slices.items():
        print(k, v["n"], v["urgent_hits"], "/", v["urgent_n"], v["urgent_recall"], v["urgent_ci"], v["accuracy"])


if __name__ == "__main__":
    main()
