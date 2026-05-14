# AI Data Leakage Detection Lab
# This script reviews text for possible sensitive data exposure.

import re


LEAKAGE_PATTERNS = {
    "password": {
        "pattern": r"(?i)(password|passwd|pwd)\s*[:=]\s*\S+",
        "score": 30,
        "description": "Possible password exposure",
    },
    "api_key": {
        "pattern": r"(?i)(api[_-]?key)\s*[:=]\s*\S+",
        "score": 30,
        "description": "Possible API key exposure",
    },
    "secret_key": {
        "pattern": r"(?i)(secret[_-]?key|client[_-]?secret)\s*[:=]\s*\S+",
        "score": 35,
        "description": "Possible secret key exposure",
    },
    "token": {
        "pattern": r"(?i)(access[_-]?token|bearer token|auth[_-]?token)\s*[:=]\s*\S+",
        "score": 35,
        "description": "Possible authentication token exposure",
    },
    "email": {
        "pattern": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "score": 10,
        "description": "Possible email address exposure",
    },
    "ssn": {
        "pattern": r"\b\d{3}-\d{2}-\d{4}\b",
        "score": 40,
        "description": "Possible SSN pattern detected",
    },
    "credit_card": {
        "pattern": r"\b(?:\d[ -]*?){13,16}\b",
        "score": 40,
        "description": "Possible credit card number pattern detected",
    },
    "confidential": {
        "pattern": r"(?i)(confidential|internal use only|do not share|restricted)",
        "score": 20,
        "description": "Confidentiality warning language detected",
    },
}


def analyze_text(text):
    findings = []
    risk_score = 0

    for name, details in LEAKAGE_PATTERNS.items():
        matches = re.findall(details["pattern"], text)

        if matches:
            findings.append(
                {
                    "type": name,
                    "description": details["description"],
                    "matches_detected": len(matches),
                }
            )
            risk_score += details["score"]

    risk_score = min(risk_score, 100)
    risk_level = get_risk_level(risk_score)

    return {
        "text_reviewed": text,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "findings": findings,
        "recommendation": get_recommendation(risk_level),
    }


def get_risk_level(score):
    if score >= 80:
        return "Critical"
    if score >= 50:
        return "High"
    if score >= 25:
        return "Medium"
    if score > 0:
        return "Low"
    return "Minimal"


def get_recommendation(risk_level):
    recommendations = {
        "Critical": "Block submission and escalate for security review.",
        "High": "Remove sensitive data before using with an AI system.",
        "Medium": "Review and redact sensitive information before processing.",
        "Low": "Monitor and use caution before sharing externally.",
        "Minimal": "No major sensitive data indicators detected.",
    }

    return recommendations.get(risk_level, "Review manually.")


def main():
    sample_inputs = [
        "Summarize this public cloud security article.",
        "My password=Summer2026! Can you check if this config is secure?",
        "Here is my api_key=12345ABCDE. Help me connect to the service.",
        "This is confidential and internal use only. Please summarize it.",
        "Contact user@example.com for access.",
        "The test SSN is 123-45-6789.",
        "Authorization access_token=abcd1234xyz should be added to the script.",
    ]

    print("AI Data Leakage Detector")
    print("=" * 40)

    for text in sample_inputs:
        result = analyze_text(text)

        print(f"\nText Reviewed: {result['text_reviewed']}")
        print(f"Risk Score: {result['risk_score']}")
        print(f"Risk Level: {result['risk_level']}")
        print(f"Findings: {result['findings']}")
        print(f"Recommendation: {result['recommendation']}")


if __name__ == "__main__":
    main()
