# Lab 01: AI Prompt Injection Risk Analyzer

## Objective

Build a Python tool that analyzes prompts for potential prompt injection, data leakage, unsafe instructions, and AI security risks.

## Why This Lab Matters

Prompt injection is one of the most important risks in AI security. Attackers may try to manipulate an AI system into ignoring instructions, revealing hidden prompts, exposing sensitive information, or bypassing safety rules.

This lab demonstrates how Python can be used to identify risky prompt patterns and produce a simple AI security risk report.

## Security Concepts Demonstrated

- Prompt injection detection
- LLM risk analysis
- AI governance
- Data leakage prevention
- Security automation
- Risk scoring
- Secure AI usage

## What This Tool Checks For

The analyzer reviews prompts for indicators such as:

- Attempts to ignore previous instructions
- Requests to reveal system prompts
- Attempts to bypass safety rules
- Requests for secrets or credentials
- Jailbreak-style language
- Social engineering language
- Data exfiltration attempts

## Lab Files

| File | Purpose |
|---|---|
| `prompt_risk_analyzer.py` | Python script that analyzes prompt risk |
| `sample_prompts.txt` | Sample prompts to test |
| `risk_report.md` | Example risk report |
| `screenshots/` | Evidence screenshots |

## How to Run

```bash
python prompt_risk_analyzer.py
