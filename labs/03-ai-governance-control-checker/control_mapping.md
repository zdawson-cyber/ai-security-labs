# AI Governance Control Mapping

## Method and scope

This manually curated educational crosswalk uses NIST AI RMF 1.0 functions and selected SP 800-53 Rev. 5 base controls. Each mapping is an interpretation requiring system-specific tailoring; control titles and full statements should be checked against the official catalog. It does not select a federal baseline or assert compliance.

The sample is a fictional analyst assistant. Its policy statements are inputs to evidence collection, not proof that safeguards operate. The validator checks all required documentation fields; the companion report lists unverified implementation evidence.

## Risk-to-control rationale

### AI-GOV-001: Unowned AI deployment delays risk decisions

**AI RMF function:** GOVERN. **SP 800-53 reference:** PM-2 — Information Security Program Leadership Role.

A designated program leadership role supports accountability; a system owner record alone does not satisfy PM-2.

**Evidence to request:** Approved responsibility matrix with named decision authority.

**Validation:** Confirm assigned owner and risk acceptance authority with an approver.

### AI-GOV-002: Undocumented use expands exposure beyond intended scope

**AI RMF function:** MAP. **SP 800-53 reference:** RA-3 — Risk Assessment.

Risk assessment needs system context and impacts; a use-case statement is only an input.

**Evidence to request:** Approved boundary and data-flow diagram plus risk assessment.

**Validation:** Trace data sources, recipients, prohibited uses and impact assumptions.

### AI-GOV-003: Unreviewed AI recommendations enter official remediation plans

**AI RMF function:** GOVERN. **SP 800-53 reference:** SA-8 — Security and Privacy Engineering Principles.

Human review is an illustrative engineering safeguard, not an explicit equivalence to SA-8.

**Evidence to request:** Review-gate design and sampled reviewer approvals.

**Validation:** Attempt to publish an unapproved recommendation and verify the gate blocks it.

### AI-GOV-004: Sensitive prompt data crosses unauthorized boundaries

**AI RMF function:** MAP. **SP 800-53 reference:** AC-4 — Information Flow Enforcement.

Data restrictions require enforced flow policy rather than a written prohibition alone.

**Evidence to request:** Approved flow rules, enforcement configuration and synthetic blocked-flow tests.

**Validation:** Attempt prohibited synthetic data flows and inspect redacted decision logs.

### AI-GOV-005: Malicious retrieved text redirects assistant behavior

**AI RMF function:** MEASURE. **SP 800-53 reference:** SI-10 — Information Input Validation.

Input checks support validation, but cannot by themselves prevent semantic prompt injection.

**Evidence to request:** Versioned direct and indirect injection cases with expected and actual outcomes.

**Validation:** Test untrusted retrieved text and confirm tool permissions remain bounded.

### AI-GOV-006: Fabricated findings produce incorrect security recommendations

**AI RMF function:** MEASURE. **SP 800-53 reference:** CA-2 — Control Assessments.

CA-2 supports assessing output-review safeguards; it is not an AI accuracy requirement.

**Evidence to request:** Evaluation set, acceptance thresholds and reviewer decisions.

**Validation:** Compare outputs to trusted references and record unsupported claims and failures.

### AI-GOV-007: Unsafe AI usage goes undetected

**AI RMF function:** MANAGE. **SP 800-53 reference:** AU-6 — Audit Record Review, Analysis, and Reporting.

Reviewing events supports detection; log generation and retention require additional controls.

**Evidence to request:** Redacted event samples, alert rule and dated review record.

**Validation:** Trigger a synthetic event and trace ingestion, alert delivery and analyst review.

### AI-GOV-008: AI data exposure lacks containment and escalation

**AI RMF function:** MANAGE. **SP 800-53 reference:** IR-4 — Incident Handling.

Incident handling supports containment and recovery; broader risk treatment needs separate governance.

**Evidence to request:** AI incident playbook and tabletop results.

**Validation:** Exercise data exposure containment, notification and service-disable steps.

### AI-GOV-009: Unapproved users administer the assistant

**AI RMF function:** GOVERN. **SP 800-53 reference:** AC-2 — Account Management.

Account lifecycle review supports access governance; least privilege also needs AC-6 tailoring.

**Evidence to request:** Role export, provisioning approval and removal test.

**Validation:** Verify unauthorized access is denied and removed users lose access.

### AI-GOV-010: Users mistake generated text for authoritative advice

**AI RMF function:** GOVERN. **SP 800-53 reference:** PT-5 — Privacy Notice.

PT-5 applies to privacy notice where PII processing is relevant; generic AI disclosure is only a conceptual connection.

**Evidence to request:** Rendered AI usage notice and conditional privacy notice.

**Validation:** Inspect user-facing notice and determine whether PII-specific notice requirements apply.

## Evidence handling and gap closure

For real assessments, track artifact ID, system boundary, control reference, artifact location, collection date, review period, reviewer, method (examine/interview/test), outcome and limitations. Keep sensitive artifacts outside the public repository. A policy assertion starts as documented/unverified. Only a qualified review of current, scoped artifacts can support an implementation finding. Failed tests remain gaps; dates and acceptance decisions belong to the accountable owner.

## Official references

- [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1): GOVERN, MAP, MEASURE and MANAGE organizing functions.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final): control statements and catalog updates. This lab uses selected Rev. 5 base controls, not a full release-level implementation.
- [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1): further risk-scoping guidance, not a claim of implemented profile actions.

SOC 2 and ISO equivalences are outside this lab’s validated mapping scope.
