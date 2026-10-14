"""Validate completeness of illustrative AI governance mapping, not actual compliance."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def check(controls, crosswalk, system):
    mappings = crosswalk["mappings"]
    original_ids = [c["control_id"] for c in controls]
    mapped_ids = [m["control_id"] for m in mappings]
    if len(set(original_ids)) != len(original_ids) or len(set(mapped_ids)) != len(mapped_ids):
        raise ValueError("Duplicate control IDs")
    if set(original_ids) != set(mapped_ids):
        raise ValueError("Crosswalk must cover each control exactly once")
    catalog = {c["control_id"]: c for c in controls}
    results = []
    for m in mappings:
        cid = m["control_id"]
        field = m["evidence_field"]
        if field not in catalog[cid]["required_fields"]:
            raise ValueError("Mapped evidence field is not in control catalog: " + cid)
        if m["ai_rmf_function"] not in {"GOVERN", "MAP", "MEASURE", "MANAGE"}:
            raise ValueError("Invalid AI RMF function")
        for name in ("nist_800_53_reference", "implementation_expectation", "owner", "remediation"):
            if not isinstance(m.get(name), str) or not m[name].strip():
                raise ValueError("Missing mapping metadata: " + cid + "." + name)
        value = system.get(field)
        present = isinstance(value, str) and bool(value.strip())
        results.append({"control_id": cid, "documentation_present": present,
                        "evidence_field": field, "owner": m["owner"],
                        "finding": "Documentation present; not independently verified" if present else "Missing documentation"})
    return {"total": len(results),
            "documented": sum(r["documentation_present"] for r in results),
            "missing": sum(not r["documentation_present"] for r in results),
            "results": results,
            "disclaimer": "Synthetic documentation-presence validation is NOT control effectiveness or regulatory compliance."}

def main():
    controls = json.loads((ROOT / "controls.json").read_text(encoding="utf-8"))
    crosswalk = json.loads((ROOT / "control_crosswalk.json").read_text(encoding="utf-8"))
    system = json.loads((ROOT / "sample_ai_system.json").read_text(encoding="utf-8"))
    report = check(controls, crosswalk, system)
    print(json.dumps(report, indent=2))
    return 0 if report["missing"] == 0 else 2

if __name__ == "__main__":
    raise SystemExit(main())
