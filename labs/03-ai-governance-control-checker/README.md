# Lab 03: AI Governance Control Checker

## Objective

Build a Python-based AI governance checker that reviews an AI system profile against basic governance, security, privacy, and risk management controls.

## Why This Lab Matters

AI systems create new governance and security risks, including prompt injection, sensitive data leakage, lack of human oversight, unclear ownership, poor documentation, and weak monitoring.

This lab demonstrates how Python can support AI governance by checking whether an AI system has documented controls, risk owners, monitoring, human review, data protection, and security safeguards.

## Security and Governance Concepts Demonstrated

- AI governance
- AI risk management
- Secure AI usage
- Prompt injection awareness
- Sensitive data protection
- Human oversight
- Risk ownership
- Control validation
- GRC-style reporting
- Python automation

## Framework Inspiration

This lab is inspired by:

- NIST AI Risk Management Framework functions: Govern, Map, Measure, and Manage
- NIST Generative AI Profile concepts
- OWASP Top 10 for LLM Applications risks
- GRC control assessment workflows

This is not an official compliance assessment. It is a portfolio lab that demonstrates how governance controls can be reviewed using Python automation.

## Lab Files

| File | Purpose |
|---|---|
| `ai_governance_checker.py` | Main Python script |
| `controls.json` | Control library used by the checker |
| `sample_ai_system.json` | Sample AI system profile being assessed |
| `governance_report.md` | Generated AI governance report |
| `lessons-learned.md` | Lab reflection |
| `screenshots/` | Evidence screenshots |

## How the Checker Works

The checker:

1. Loads a sample AI system profile.
2. Loads a JSON control library.
3. Reviews whether the system profile contains evidence for each control.
4. Assigns pass, partial, or fail status.
5. Calculates a governance readiness score.
6. Generates a Markdown report.

## How to Run

```powershell
py ai_governance_checker.py
