# Lab 03: AI Governance Control Mapping and Checker

**Status: Complete as a synthetic portfolio exercise.** Operational control effectiveness remains unverified.

## Objective

Map AI risks to selected NIST-style controls, separate policy assertions from implementation evidence, and generate a repeatable evidence-gap review for a fictional AI Security Assistant that drafts security findings and remediation notes. No deployed AI service, customer data, CUI, or classified evidence is used.

## Security concepts

AI risk ownership; scope and data flows; human oversight; prompt injection; data leakage; output reliability; access management; audit review; incident response; transparency. The ten local AI-GOV identifiers are lab controls, not NIST control identifiers.

## Architecture and workflow

`controls.json` + `control_crosswalk.json` + `sample_ai_system.json` → `validate_crosswalk.py` → `generate_mapping_report.py` → `evidence_gap_report.md`.

1. Define the AI use case, boundary, users and data paths.
2. Describe a concrete failure scenario for each local control.
3. Select a relevant SP 800-53 Rev. 5 base control and explain the connection and limits. AI RMF functions provide organizing context; they are not one-to-one equivalences.
4. Check every required profile field, mapping coverage and metadata.
5. Record evidence to request and a validation step. Documentation presence stays separate from effectiveness.
6. Have actual system owners tailor requirements, collect evidence, assign dates, and approve risk treatment before operational use.

## Run from repository root

Python 3.12; standard library only; no cloud account, API keys, package installation or model calls.

```bash
python -m unittest discover -s labs/03-ai-governance-control-checker -p 'test_*.py' -v
python labs/03-ai-governance-control-checker/validate_crosswalk.py
python labs/03-ai-governance-control-checker/generate_mapping_report.py
python labs/03-ai-governance-control-checker/ai_governance_checker.py
```

The validator exits 0 for complete synthetic documentation, 2 for missing documentation, and raises an error for invalid mappings. Exit 0 does not mean compliance. The report generators overwrite their respective checked-in reports. Expected mapping result: 10 documented controls, 0 independently verified implementations.

## Artifacts

| File | Purpose |
|---|---|
| `controls.json` | Ten local control definitions and required fields |
| `control_crosswalk.json` | Risk, framework reference, rationale, owner, evidence request and validation procedure |
| `validate_crosswalk.py`, `test_crosswalk.py` | Mapping coverage, metadata and missing-field validation |
| `generate_mapping_report.py`, `evidence_gap_report.md` | Deterministic evidence-gap output |
| `ai_governance_checker.py`, `governance_report.md` | Legacy keyword-based documentation heuristic; not an effectiveness assessment |
| `control_mapping.md` | Mapping method, rationale and official source references |
| `lessons-learned.md`, `portfolio_notes.md` | Technical takeaways and bounded portfolio language |
| `screenshots/` | Existing historical checker output; not proof of current operational controls |

## Risk analysis and limits

All ten synthetic profile areas contain policy statements. None supplies approved operational artifacts or observed test results. Prioritize data-flow enforcement, injection resilience, human review, output evaluation and unauthorized-access tests before deployment. The companion gap report proposes evidence and validation for each risk; it does not claim those tests were performed.

The legacy keyword heuristic searches the entire profile and can reward unrelated words or even negative statements. Its score is retained for continuity and explicitly labeled a documentation heuristic. It must not be used to approve deployment, calculate residual risk, or represent compliance.

This exercise is a small manually curated mapping, not an official NIST crosswalk, complete control baseline, ATO package, or production governance platform. Bias/fairness evaluation, supplier assurance, model changes, availability and broader privacy obligations need separate scoping.
