# AI Governance Control Checker
# This lab reviews a sample AI system profile against a basic AI governance control library.

import json
from pathlib import Path
from datetime import date


CONTROLS_FILE = "controls.json"
SYSTEM_PROFILE_FILE = "sample_ai_system.json"
REPORT_FILE = "governance_report.md"


def load_json(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def normalize_text(value):
    if isinstance(value, list):
        return " ".join(str(item) for item in value).lower()

    if value is None:
        return ""

    return str(value).lower()


def evaluate_control(control, system_profile):
    required_fields = control.get("required_fields", [])
    keywords = control.get("keywords", [])

    field_matches = []
    keyword_matches = []

    combined_profile_text = " ".join(
        normalize_text(value) for value in system_profile.values()
    )

    for field in required_fields:
        value = system_profile.get(field)

        if value and normalize_text(value).strip():
            field_matches.append(field)

    for keyword in keywords:
        if keyword.lower() in combined_profile_text:
            keyword_matches.append(keyword)

    field_score = len(field_matches) / len(required_fields) if required_fields else 0
    keyword_score = min(len(keyword_matches) / 2, 1)

    total_match_score = (field_score * 0.75) + (keyword_score * 0.25)

    if total_match_score >= 0.85:
        status = "Pass"
    elif total_match_score >= 0.40:
        status = "Partial"
    else:
        status = "Fail"

    weighted_score = round(control["weight"] * total_match_score, 2)

    return {
        "control_id": control["control_id"],
        "control_name": control["control_name"],
        "category": control["category"],
        "risk_area": control["risk_area"],
        "status": status,
        "weight": control["weight"],
        "weighted_score": weighted_score,
        "field_matches": field_matches,
        "keyword_matches": keyword_matches,
        "recommendation": control["recommendation"],
    }


def calculate_summary(results):
    total_possible = sum(result["weight"] for result in results)
    total_earned = sum(result["weighted_score"] for result in results)

    readiness_score = round((total_earned / total_possible) * 100, 2) if total_possible else 0

    status_counts = {
        "Pass": 0,
        "Partial": 0,
        "Fail": 0,
    }

    category_scores = {}

    for result in results:
        status_counts[result["status"]] += 1

        category = result["category"]
        if category not in category_scores:
            category_scores[category] = {
                "earned": 0,
                "possible": 0,
            }

        category_scores[category]["earned"] += result["weighted_score"]
        category_scores[category]["possible"] += result["weight"]

    for category, values in category_scores.items():
        values["score"] = round((values["earned"] / values["possible"]) * 100, 2)

    if readiness_score >= 85:
        readiness_level = "Strong"
    elif readiness_score >= 70:
        readiness_level = "Moderate"
    elif readiness_score >= 50:
        readiness_level = "Needs Improvement"
    else:
        readiness_level = "High Risk"

    return {
        "readiness_score": readiness_score,
        "readiness_level": readiness_level,
        "status_counts": status_counts,
        "category_scores": category_scores,
    }


def generate_markdown_report(system_profile, results, summary):
    lines = []

    lines.append("# AI Governance Control Report")
    lines.append("")
    lines.append(f"**Report Date:** {date.today()}")
    lines.append("")
    lines.append("## System Reviewed")
    lines.append("")
    lines.append(f"**System Name:** {system_profile.get('system_name', 'Not documented')}")
    lines.append(f"**System Owner:** {system_profile.get('system_owner', 'Not documented')}")
    lines.append(f"**Use Case:** {system_profile.get('use_case', 'Not documented')}")
    lines.append("")
    lines.append("## Governance Readiness Summary")
    lines.append("")
    lines.append(f"**Readiness Score:** {summary['readiness_score']}%")
    lines.append(f"**Readiness Level:** {summary['readiness_level']}")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---:|")

    for status, count in summary["status_counts"].items():
        lines.append(f"| {status} | {count} |")

    lines.append("")
    lines.append("## Category Scores")
    lines.append("")
    lines.append("| Category | Score |")
    lines.append("|---|---:|")

    for category, values in summary["category_scores"].items():
        lines.append(f"| {category} | {values['score']}% |")

    lines.append("")
    lines.append("## Control Results")
    lines.append("")
    lines.append("| Control ID | Category | Control Name | Status | Score | Recommendation |")
    lines.append("|---|---|---|---|---:|---|")

    for result in results:
        lines.append(
            f"| {result['control_id']} | {result['category']} | "
            f"{result['control_name']} | {result['status']} | "
            f"{result['weighted_score']}/{result['weight']} | {result['recommendation']} |"
        )

    lines.append("")
    lines.append("## Detailed Findings")
    lines.append("")

    for result in results:
        lines.append(f"### {result['control_id']}: {result['control_name']}")
        lines.append("")
        lines.append(f"**Status:** {result['status']}")
        lines.append("")
        lines.append(f"**Risk Area:** {result['risk_area']}")
        lines.append("")
        lines.append(f"**Matched Fields:** {', '.join(result['field_matches']) if result['field_matches'] else 'None'}")
        lines.append("")
        lines.append(f"**Matched Keywords:** {', '.join(result['keyword_matches']) if result['keyword_matches'] else 'None'}")
        lines.append("")
        lines.append(f"**Recommendation:** {result['recommendation']}")
        lines.append("")

    lines.append("## Portfolio Summary")
    lines.append("")
    lines.append(
        "This report demonstrates how Python can be used to automate AI governance "
        "control checks by reviewing an AI system profile against risk management, "
        "security, privacy, monitoring, access control, and human oversight expectations."
    )
    lines.append("")

    return "\n".join(lines)


def print_console_summary(system_profile, results, summary):
    print("AI Governance Control Checker")
    print("=" * 45)
    print(f"System Reviewed: {system_profile.get('system_name', 'Not documented')}")
    print(f"Readiness Score: {summary['readiness_score']}%")
    print(f"Readiness Level: {summary['readiness_level']}")
    print("\nControl Results:")

    for result in results:
        print(
            f"- {result['control_id']} | {result['status']} | "
            f"{result['control_name']} | Score: {result['weighted_score']}/{result['weight']}"
        )

    print(f"\nReport generated: {REPORT_FILE}")


def main():
    controls = load_json(CONTROLS_FILE)
    system_profile = load_json(SYSTEM_PROFILE_FILE)

    results = [evaluate_control(control, system_profile) for control in controls]
    summary = calculate_summary(results)

    report = generate_markdown_report(system_profile, results, summary)

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write(report)

    print_console_summary(system_profile, results, summary)


if __name__ == "__main__":
    main()
