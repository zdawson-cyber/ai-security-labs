# AI Governance Mapping and Evidence Gaps

Synthetic AI Security Assistant scenario. All evidence below is requested evidence, not collected operational evidence.

Documentation present: 10/10. Implementation independently verified: 0/10.

No risk acceptance, compliance result, or completed remediation is asserted. Priorities and role owners are illustrative; dates and commitments require the actual system owner.

## AI-GOV-001 — PM-2

- Risk: Unowned AI deployment delays risk decisions
- Documentation: Documentation present; not independently verified
- Missing profile fields: None
- Implementation: Not verified
- Evidence gap: Approved responsibility matrix with named decision authority
- Proposed validation: Confirm assigned owner and risk acceptance authority with an approver
- Proposed owner: GRC lead; priority: High

## AI-GOV-002 — RA-3

- Risk: Undocumented use expands exposure beyond intended scope
- Documentation: Documentation present; not independently verified
- Missing profile fields: None
- Implementation: Not verified
- Evidence gap: Approved boundary and data-flow diagram plus risk assessment
- Proposed validation: Trace data sources, recipients, prohibited uses and impact assumptions
- Proposed owner: Business owner; priority: High

## AI-GOV-003 — SA-8

- Risk: Unreviewed AI recommendations enter official remediation plans
- Documentation: Documentation present; not independently verified
- Missing profile fields: None
- Implementation: Not verified
- Evidence gap: Review-gate design and sampled reviewer approvals
- Proposed validation: Attempt to publish an unapproved recommendation and verify the gate blocks it
- Proposed owner: AI product owner; priority: High

## AI-GOV-004 — AC-4

- Risk: Sensitive prompt data crosses unauthorized boundaries
- Documentation: Documentation present; not independently verified
- Missing profile fields: None
- Implementation: Not verified
- Evidence gap: Approved flow rules, enforcement configuration and synthetic blocked-flow tests
- Proposed validation: Attempt prohibited synthetic data flows and inspect redacted decision logs
- Proposed owner: Privacy lead; priority: High

## AI-GOV-005 — SI-10

- Risk: Malicious retrieved text redirects assistant behavior
- Documentation: Documentation present; not independently verified
- Missing profile fields: None
- Implementation: Not verified
- Evidence gap: Versioned direct and indirect injection cases with expected and actual outcomes
- Proposed validation: Test untrusted retrieved text and confirm tool permissions remain bounded
- Proposed owner: AppSec team; priority: High

## AI-GOV-006 — CA-2

- Risk: Fabricated findings produce incorrect security recommendations
- Documentation: Documentation present; not independently verified
- Missing profile fields: None
- Implementation: Not verified
- Evidence gap: Evaluation set, acceptance thresholds and reviewer decisions
- Proposed validation: Compare outputs to trusted references and record unsupported claims and failures
- Proposed owner: Model owner; priority: High

## AI-GOV-007 — AU-6

- Risk: Unsafe AI usage goes undetected
- Documentation: Documentation present; not independently verified
- Missing profile fields: None
- Implementation: Not verified
- Evidence gap: Redacted event samples, alert rule and dated review record
- Proposed validation: Trigger a synthetic event and trace ingestion, alert delivery and analyst review
- Proposed owner: Security operations; priority: Medium

## AI-GOV-008 — IR-4

- Risk: AI data exposure lacks containment and escalation
- Documentation: Documentation present; not independently verified
- Missing profile fields: None
- Implementation: Not verified
- Evidence gap: AI incident playbook and tabletop results
- Proposed validation: Exercise data exposure containment, notification and service-disable steps
- Proposed owner: Risk owner; priority: High

## AI-GOV-009 — AC-2

- Risk: Unapproved users administer the assistant
- Documentation: Documentation present; not independently verified
- Missing profile fields: None
- Implementation: Not verified
- Evidence gap: Role export, provisioning approval and removal test
- Proposed validation: Verify unauthorized access is denied and removed users lose access
- Proposed owner: IAM owner; priority: High

## AI-GOV-010 — PT-5

- Risk: Users mistake generated text for authoritative advice
- Documentation: Documentation present; not independently verified
- Missing profile fields: None
- Implementation: Not verified
- Evidence gap: Rendered AI usage notice and conditional privacy notice
- Proposed validation: Inspect user-facing notice and determine whether PII-specific notice requirements apply
- Proposed owner: Policy owner; priority: Medium
