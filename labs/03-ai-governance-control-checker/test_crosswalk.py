import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("checker", ROOT / "validate_crosswalk.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

class MappingTests(unittest.TestCase):
    def setUp(self):
        self.controls = json.loads((ROOT / "controls.json").read_text())
        self.mapping = json.loads((ROOT / "control_crosswalk.json").read_text())
        self.system = json.loads((ROOT / "sample_ai_system.json").read_text())

    def test_complete_coverage_and_documentation(self):
        result = checker.check(self.controls, self.mapping, self.system)
        self.assertEqual(result["total"], 10)
        self.assertEqual(result["documented"], 10)

    def test_missing_documentation(self):
        self.system.pop("system_owner")
        self.assertEqual(checker.check(self.controls, self.mapping, self.system)["missing"], 1)

    def test_missing_mapping_rejected(self):
        self.mapping["mappings"].pop()
        with self.assertRaises(ValueError):
            checker.check(self.controls, self.mapping, self.system)

    def test_duplicate_mapping_rejected(self):
        self.mapping["mappings"].append(copy.deepcopy(self.mapping["mappings"][0]))
        with self.assertRaises(ValueError):
            checker.check(self.controls, self.mapping, self.system)

    def test_invalid_evidence_field_rejected(self):
        self.mapping["mappings"][0]["evidence_field"] = "unknown_field"
        with self.assertRaises(ValueError):
            checker.check(self.controls, self.mapping, self.system)

if __name__ == "__main__":
    unittest.main()
