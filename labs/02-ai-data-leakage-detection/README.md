# Lab 02: AI Data Leakage Detection Lab

## Objective

Build a Python tool that detects possible sensitive data exposure in AI prompts, AI outputs, and user-submitted text.

## Why This Lab Matters

AI systems can create security risks when users accidentally or intentionally include sensitive information in prompts. This can include credentials, API keys, passwords, tokens, personal information, internal notes, or confidential business data.

This lab demonstrates how Python can help identify possible data leakage before information is sent to or returned by an AI system.

## Security Concepts Demonstrated

- AI data leakage detection
- Sensitive data identification
- Secure AI usage
- AI governance
- Data loss prevention
- Risk scoring
- Security automation
- Responsible AI workflows

## What This Tool Checks For

The detector reviews text for indicators such as:

- Passwords
- API keys
- Access tokens
- Secret keys
- Email addresses
- Social Security number patterns
- Credit card number patterns
- Confidential language
- Internal-use-only language

## Lab Files

| File | Purpose |
|---|---|
| `data_leakage_detector.py` | Python script that detects possible sensitive data exposure |
| `sample_inputs.txt` | Sample text inputs to test |
| `data_leakage_report.md` | Example risk report |
| `screenshots/` | Evidence screenshots |

## How to Run

```bash
python data_leakage_detector.py
