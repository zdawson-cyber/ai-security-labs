# AI Data Leakage Risk Report

## Report Summary

This report documents potential data leakage risks identified during Lab 02.

## Findings

| Input Type | Risk Level | Reason | Recommended Action |
|---|---|---|---|
| Public article summary | Minimal | No sensitive indicators detected | Allow |
| Password included in prompt | High | Possible credential exposure | Block or redact |
| API key included in prompt | High | Possible secret exposure | Block or redact |
| Confidential business text | Medium | Confidentiality warning language detected | Review before processing |
| Email address included | Low | Possible personal or business identifier | Review if unnecessary |
| SSN pattern detected | Critical | Possible regulated personal data | Block and escalate |
| Access token included | High | Possible authentication token exposure | Block or redact |

## Security Impact

AI data leakage can expose sensitive information through prompts, generated responses, logs, or connected tools. This can create confidentiality, compliance, privacy, and operational security risks.

## Recommended Controls

- Do not place passwords or secrets in AI prompts
- Redact sensitive information before AI processing
- Block prompts that contain credentials or tokens
- Monitor prompts for sensitive data patterns
- Use data loss prevention controls where possible
- Apply human review for high-risk content
- Train users on secure AI usage

## GRC Connection

This lab supports AI governance and security compliance by demonstrating how sensitive data can be detected and flagged before being processed by an AI system.

## Portfolio Reflection

This lab demonstrates how Python can support AI security by identifying possible sensitive data exposure and producing a simple risk-based report. It connects AI governance, data protection, cybersecurity automation, and secure AI workflows.
