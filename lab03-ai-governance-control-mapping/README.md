# Lab 03: AI Governance Control Mapping

**Status: Complete — synthetic educational lab, not a production assessment**

## Objective
Build a reproducible Python workflow mapping six representative generative-AI risks to **candidate** NIST SP 800-53 Rev. 5 controls, NIST AI RMF top-level functions, requested evidence, and unverified gaps.

## Scenario
A fictional healthcare organization is considering an internal generative-AI knowledge assistant. No patient records, PHI, CUI, live systems, or customer information are used. This is an independent portfolio exercise, not a healthcare audit or certification.

## Security concepts
Risk identification; likelihood/impact scoring; NIST AI RMF GOVERN, MAP, MEASURE, MANAGE; SP 800-53 control selection; evidence traceability; gap analysis; automated reporting; human review.

## Files
- `risks.json`: six synthetic risks, candidate controls, evidence requests, and gaps.
- `map_controls.py`: offline, standard-library-only scoring, validation, and report generation.
- `tests/test_mapping.py`: automated validation tests.
- `outputs/`: generated CSV and Markdown report after running.

## Execute
From the repository root:
```bash
python lab03-ai-governance-control-mapping/map_controls.py
python -m unittest discover -s lab03-ai-governance-control-mapping/tests -v
```
Requires Python 3.10+; no external packages or API keys.

## Method
1. Define a fictional use case and six AI-specific threats.
2. Score likelihood and impact 1–5; multiply for a **demonstration-only** priority score (High 15–25, Medium 8–14, Low 1–7).
3. Select possible SP 800-53 controls and one illustrative AI RMF function per risk.
4. Record **potential evidence to request** and an **unverified gap**. These are not confirmed findings.
5. Generate sorted CSV and Markdown outputs and inspect the mapping manually.

## Risk analysis
The highest sample risk is sensitive-data exposure (20), followed by prompt injection and monitoring gaps (16 each). Scores are hypothetical and are not organizational risk acceptance decisions.

## Lessons learned
- Conventional security controls can support AI governance, but AI-specific evaluation and implementation evidence are still necessary.
- Candidate mappings are not official NIST crosswalks or proof of control effectiveness.
- AI RMF functions overlap; assigning one function per risk is a teaching simplification.
- Auditable deterministic reporting reduces unsupported assertions.
- Healthcare applicability, HIPAA obligations, and deployment safeguards require separate real-world review.

## Resume-safe description
"Developed a synthetic Python-based AI governance control mapping lab covering six AI risks, candidate NIST SP 800-53 controls, AI RMF functions, and evidence/gap reporting. Built reproducible CSV/Markdown outputs and automated tests."

## References
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI 600-1 GenAI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

**Disclosure:** This lab's code, mappings, and documentation were prepared with AI assistance for the repository owner's review. It does not demonstrate production deployment, personal authorship of every line, or completed control validation.
