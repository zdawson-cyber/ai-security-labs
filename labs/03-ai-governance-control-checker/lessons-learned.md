# Technical Lessons and Review Notes

These are takeaways supported by the code and synthetic scenario, not a statement that the repository owner performed a production assessment.

- Nonempty policy text is documentation, not operational evidence. All ten sample controls remain unverified.
- Exact required-field checks prevent a use-case statement from hiding a missing business purpose.
- Mapping rationale matters: CA-2 assesses controls, rather than defining AI output accuracy; PT-5 concerns privacy notice rather than every generic AI disclosure.
- Prompt validation alone cannot establish resistance to semantic or indirect injection. Test cases and permission boundaries require independent review.
- A keyword score can improve without any change to the underlying system. Retain it only as an explicitly limited documentation heuristic.
- Reproducible reports and negative tests improve traceability, but cannot make an interpretive crosswalk authoritative.

## Validation scope

See `test_crosswalk.py` for positive coverage, missing mappings, duplicates, invalid fields, secondary required fields, blank/non-text values, missing rationale and the invariant that documentation never becomes verified implementation. See `evidence_gap_report.md` for generated findings. Existing screenshots are historical artifacts.

## Future hands-on work

Run the proposed access, data-flow, review-gate, injection and incident exercises in a controlled deployment. Record actual expected/observed outcomes and remaining failures before claiming operational control validation.
