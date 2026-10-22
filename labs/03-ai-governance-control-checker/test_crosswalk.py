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

    def test_secondary_required_field_missing(self):
        self.system.pop("business_purpose")
        result = checker.check(self.controls, self.mapping, self.system)
        self.assertEqual(result["missing"], 1)
        self.assertEqual(result["results"][1]["missing_fields"], ["business_purpose"])

    def test_blank_and_non_text_are_missing(self):
        self.system["system_owner"] = "  "
        self.system["use_case"] = True
        self.assertEqual(checker.check(self.controls, self.mapping, self.system)["missing"], 2)

    def test_documented_never_means_verified(self):
        result = checker.check(self.controls, self.mapping, self.system)
        self.assertTrue(all(r["implementation_status"] == "Not verified" for r in result["results"]))

    def test_missing_rationale_rejected(self):
        self.mapping["mappings"][0]["mapping_rationale"] = ""
        with self.assertRaises(ValueError):
            checker.check(self.controls, self.mapping, self.system)

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
