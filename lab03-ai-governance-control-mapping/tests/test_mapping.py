import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from map_controls import analyze, markdown, priority

class MappingTests(unittest.TestCase):
    def setUp(self):
        self.risks = json.loads((ROOT / "risks.json").read_text(encoding="utf-8"))

    def test_six_risks(self):
        self.assertEqual(len(analyze(self.risks)), 6)

    def test_sorted(self):
        scores = [r["score"] for r in analyze(self.risks)]
        self.assertEqual(scores, sorted(scores, reverse=True))

    def test_thresholds(self):
        self.assertEqual([priority(i) for i in (7, 8, 14, 15)], ["Low", "Medium", "Medium", "High"])

    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):
            analyze(self.risks + [self.risks[0]])

    def test_out_of_range_rejected(self):
        with self.assertRaises(ValueError):
            analyze([{**self.risks[0], "impact": 6}])

    def test_report_has_evidence(self):
        self.assertIn("Unverified gap", markdown(analyze(self.risks)))

if __name__ == "__main__":
    unittest.main()
