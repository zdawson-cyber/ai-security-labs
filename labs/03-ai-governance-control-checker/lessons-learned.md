# Lab 03 Lessons Learned

## What I Learned

In this lab, I built a Python-based AI governance checker that reviews an AI system profile against a basic set of governance and security controls.

This helped me understand how AI governance can be translated into structured control checks.

## Key Takeaways

- AI systems should have documented ownership and accountability.
- AI use cases should be clearly defined before deployment.
- Human oversight is important for high-impact or security-related AI outputs.
- Sensitive data should not be placed into AI prompts without protection.
- Prompt injection and jailbreak attempts should be considered AI security risks.
- Logging and monitoring support auditability and incident response.
- Access control and least privilege apply to AI systems just like cloud systems.
- Governance documentation helps connect technical AI systems to GRC and compliance expectations.

## Troubleshooting Notes

This lab was intentionally designed with separate JSON files and Python logic so each part can be tested independently.

If the script fails, check:

- The JSON files are valid
- The file names match exactly
- The terminal is inside the correct lab folder
- Python is installed and working
- The report file is not open in another program

## Test Results

The AI Governance Control Checker successfully reviewed the sample AI system profile and generated a governance readiness score of 88.63%.

The system received a readiness level of Strong, but several controls returned Partial results. This showed that the checker was able to identify areas where documentation existed but could be improved.

Partial results included:

- AI-GOV-002: AI Use Case Documented
- AI-GOV-007: Logging and Monitoring Planned
- AI-GOV-010: User Disclosure or Usage Notice Provided

This helped validate that the tool was not simply passing every control. It provided a more realistic governance assessment by identifying documentation gaps and improvement areas.

## Portfolio Reflection

This lab helped me connect cybersecurity, GRC, Python automation, and AI governance. It demonstrates how a control-based review process can be applied to AI systems in a way that supports security documentation, audit readiness, and responsible AI usage.
