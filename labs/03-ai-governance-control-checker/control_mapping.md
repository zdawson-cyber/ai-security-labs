# AI Governance Control Mapping

## Project Purpose

This mapping project demonstrates how AI governance controls can be translated into security, privacy, risk, and compliance expectations across multiple frameworks.

The goal is not to claim an official SOC 2 or ISO/IEC 27001 audit mapping. Instead, this project shows how a security engineer with NIST/RMF experience can interpret AI governance requirements and align them to familiar control concepts such as ownership, risk assessment, access control, monitoring, incident response, vendor risk, and evidence collection.

## Mapping Approach

The AI governance controls in this lab are mapped to the following control families and framework concepts:

* **NIST AI RMF:** Govern, Map, Measure, Manage
* **NIST SP 800-53:** Security and privacy control families such as Access Control, Audit and Accountability, Risk Assessment, Incident Response, Configuration Management, System and Information Integrity, and Supply Chain Risk Management
* **SOC 2 Concepts:** Security, confidentiality, privacy, monitoring, control activities, logical access, system operations, change management, and risk mitigation
* **ISO/IEC 27001 Concepts:** Information security management, risk treatment, access control, asset/information handling, supplier security, logging, monitoring, incident management, policy governance, and continual improvement

## AI Governance Control Crosswalk

| AI Control ID | AI Governance Control                    | NIST AI RMF Function | NIST SP 800-53 Alignment                                                                                | SOC 2 Alignment                                                 | ISO/IEC 27001 Alignment                                                            | Example Evidence                                                                |
| ------------- | ---------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| AI-GOV-001    | AI System Owner Assigned                 | Govern               | Program Management, Planning, Risk Assessment                                                           | Control Environment, Communication, Risk Management             | Roles and responsibilities, governance, accountability                             | System owner record, RACI, intake form, approval workflow                       |
| AI-GOV-002    | AI Use Case Documented                   | Map                  | Planning, Risk Assessment, System and Services Acquisition                                              | Risk Assessment, Communication, Control Activities              | ISMS scope, asset inventory, risk assessment, acceptable use                       | AI use case intake form, business purpose, intended users, data flow notes      |
| AI-GOV-003    | Human Oversight Defined                  | Govern / Measure     | Risk Assessment, Assessment/Authorization/Monitoring, System and Information Integrity                  | Control Activities, Monitoring Activities, Risk Mitigation      | Operational control, review/approval process, governance responsibility            | Human review process, approval criteria, escalation steps                       |
| AI-GOV-004    | Sensitive Data Handling Documented       | Map                  | Access Control, PII Processing and Transparency, System and Communications Protection, Media Protection | Confidentiality, Privacy, Logical Access, Data Protection       | Information classification, acceptable use, data handling, data leakage prevention | Data handling rules, redaction guidance, restricted data list, DLP expectations |
| AI-GOV-005    | Prompt Injection Risk Addressed          | Measure              | Risk Assessment, System and Information Integrity, Configuration Management                             | System Operations, Risk Mitigation, Control Activities          | Secure development, vulnerability management, monitoring, technical controls       | Prompt injection test cases, blocked prompt examples, input validation notes    |
| AI-GOV-006    | Output Review or Validation Defined      | Measure              | Assessment/Authorization/Monitoring, Risk Assessment, System and Information Integrity                  | Monitoring Activities, Control Activities, Processing Integrity | Review procedures, quality control, operational monitoring                         | Output review checklist, hallucination review notes, validation procedure       |
| AI-GOV-007    | Logging and Monitoring Planned           | Manage               | Audit and Accountability, System and Information Integrity, Continuous Monitoring                       | System Operations, Monitoring, Incident Detection               | Logging, monitoring, event review, security operations                             | Log sources, monitoring plan, risky prompt log, alerting workflow               |
| AI-GOV-008    | Risk Response Plan Documented            | Manage               | Risk Assessment, Incident Response, Plan of Action & Milestones, Continuous Monitoring                  | Risk Mitigation, Incident Response, Control Activities          | Risk treatment, incident management, lessons learned, corrective action            | Risk register, remediation plan, escalation path, POA&M-style tracker           |
| AI-GOV-009    | Access Control Defined                   | Govern               | Access Control, Identification and Authentication, Least Privilege                                      | Logical Access, Security, Confidentiality                       | Access control, identity management, access rights review                          | RBAC matrix, approved user list, admin access review, least privilege notes     |
| AI-GOV-010    | User Disclosure or Usage Notice Provided | Govern               | Privacy Transparency, Awareness and Training, Planning                                                  | Communication, Privacy, Confidentiality                         | Acceptable use, privacy notice, policy communication, awareness                    | AI usage notice, user guidance, acceptable use policy, training material        |

## Evidence Collection Examples

A practical AI governance review should collect evidence that proves the organization has considered the following:

| Evidence Area     | Example Artifact                                                                      |
| ----------------- | ------------------------------------------------------------------------------------- |
| Ownership         | AI system owner, business owner, security reviewer, approval authority                |
| Use Case          | AI tool name, business purpose, intended users, approved functions                    |
| Data Exposure     | Sensitive data restrictions, PII handling rules, redaction requirements               |
| Access Control    | Approved users, admin roles, RBAC, least privilege review                             |
| Human Oversight   | Review requirements before operational or customer-impacting use                      |
| Monitoring        | Logs, risky prompt reviews, alerting process, usage monitoring                        |
| Incident Response | Escalation path, root cause documentation, containment process                        |
| Vendor Risk       | Vendor privacy policy, model training terms, data retention terms                     |
| Compliance        | Control mapping, evidence tracker, audit support notes                                |
| Training          | AI acceptable use guidance, security awareness, phishing or prompt injection examples |

## AI Tool Review Questions

These questions can be used to evaluate AI tools, SaaS integrations, coding assistants, or LLM-enabled platforms.

1. What business problem does the AI tool solve?
2. Who owns the AI tool from a business and technical perspective?
3. What type of data will users submit into the AI tool?
4. Is confidential, regulated, customer, employee, or authentication data prohibited?
5. Does the vendor use customer inputs to train models?
6. Where is data stored, processed, and retained?
7. Can access be limited by role, group, or approved user list?
8. Are logs available for security review or audit purposes?
9. What safeguards exist for prompt injection, data leakage, or unauthorized disclosure?
10. Is human review required before AI-generated content is used in official decisions, reports, or customer-facing outputs?
11. What is the incident response process if sensitive data is submitted or exposed?
12. What evidence would support audit readiness for this AI tool?

## Portfolio Summary

This mapping demonstrates practical AI governance capability by connecting AI-specific risks to familiar GRC and security engineering concepts. It shows how NIST/RMF experience can transfer into AI governance, SOC 2 readiness, ISO/IEC 27001-style information security management, vendor risk assessment, control monitoring, and secure AI adoption.
