# AI Prompt Injection Risk Report

## Report Summary

This report documents sample prompt injection risks identified during Lab 01.

## Findings

| Prompt Type | Risk Level | Reason | Recommended Action |
|---|---|---|---|
| Normal security question | Minimal | No risky patterns detected | Allow |
| Ignore previous instructions | High | Attempts to override system behavior | Block or review |
| Reveal system prompt | High | Attempts to expose hidden instructions | Block |
| Jailbreak request | High | Attempts to bypass AI safety rules | Block |
| Credential search request | Medium | May involve sensitive data exposure | Review |

## Security Impact

Prompt injection can create risk by attempting to manipulate AI systems into ignoring instructions, exposing sensitive information, or producing unsafe responses.

## Recommended Controls

- Validate user prompts before processing
- Block known jailbreak patterns
- Log risky prompts for review
- Avoid placing secrets in prompts
- Use least privilege for AI-connected tools
- Apply human review for high-risk AI actions

## Portfolio Reflection

This lab demonstrates how Python can support AI security by identifying risky prompts and producing a simple risk-based analysis. It connects AI security, cybersecurity automation, and governance documentation.
