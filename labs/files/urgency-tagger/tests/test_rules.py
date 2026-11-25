import unittest

from urgency_tagger import metrics, rules


class RulesTest(unittest.TestCase):
    def test_urgent_english(self):
        self.assertEqual(rules.tag("My dog swallowed a sock and is bleeding"), "urgent")

    def test_urgent_arabic(self):
        self.assertEqual(rules.tag("القط لا يتنفس جيدا"), "urgent")

    def test_soon(self):
        self.assertEqual(rules.tag("The cat is vomiting since yesterday"), "soon")

    def test_routine(self):
        self.assertEqual(rules.tag("أريد موعد تطعيم سنوي"), "routine")


class MetricsTest(unittest.TestCase):
    def test_wilson_contains_rate(self):
        lo, hi = metrics.wilson(17, 20)
        self.assertTrue(lo < 0.85 < hi)

    def test_macro_f1_perfect(self):
        g = ["urgent", "soon", "routine"]
        self.assertAlmostEqual(metrics.macro_f1(g, g), 1.0)


if __name__ == "__main__":
    unittest.main()
