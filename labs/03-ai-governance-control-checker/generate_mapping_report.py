"""Generate an illustrative evidence-gap report; no operational evidence is verified."""
import json
from pathlib import Path
from validate_crosswalk import check
ROOT = Path(__file__).resolve().parent

def render(report):
    lines = ["# AI Governance Mapping and Evidence Gaps", "",
             "Synthetic AI Security Assistant scenario. All evidence below is requested evidence, not collected operational evidence.", "",
             f"Documentation present: {report['documented']}/{report['total']}. Implementation independently verified: 0/{report['total']}.", "",
             "No risk acceptance, compliance result, or completed remediation is asserted. Priorities and role owners are illustrative; dates and commitments require the actual system owner.", ""]
    for item in report['results']:
        lines += [f"## {item['control_id']} — {item['nist_reference']}", "",
                  f"- Risk: {item['risk_scenario']}",
                  f"- Documentation: {item['finding']}",
                  f"- Missing profile fields: {', '.join(item['missing_fields']) or 'None'}",
                  f"- Implementation: {item['implementation_status']}",
                  f"- Evidence gap: {item['evidence_gap']}",
                  f"- Proposed validation: {item['validation_step']}",
                  f"- Proposed owner: {item['owner']}; priority: {item['priority']}", ""]
    return "\n".join(lines)

def main():
    def load(name):
        return json.loads((ROOT / name).read_text(encoding='utf-8'))
    report = check(load('controls.json'), load('control_crosswalk.json'), load('sample_ai_system.json'))
    (ROOT / 'evidence_gap_report.md').write_text(render(report), encoding='utf-8')
    print(f"Mapped {report['total']} controls; {report['documented']} documented; 0 independently verified.")

if __name__ == '__main__':
    main()
