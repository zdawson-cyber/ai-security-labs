"""Synthetic AI governance mapping. No external dependencies or network access."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FUNCTIONS = {"GOVERN", "MAP", "MEASURE", "MANAGE"}

def priority(score):
    return "High" if score >= 15 else "Medium" if score >= 8 else "Low"

def analyze(records):
    if not isinstance(records, list) or not records:
        raise ValueError("Expected a nonempty list")
    ids = set()
    output = []
    for r in records:
        required = ("id", "risk", "likelihood", "impact", "controls", "ai_rmf_function", "evidence_request", "unverified_gap")
        if any(k not in r for k in required):
            raise ValueError("Missing field")
        if r["id"] in ids:
            raise ValueError("Duplicate risk ID")
        ids.add(r["id"])
        if any(type(r[k]) is not int or not 1 <= r[k] <= 5 for k in ("likelihood", "impact")):
            raise ValueError("Scores must be integers 1-5")
        if r["ai_rmf_function"] not in FUNCTIONS or not isinstance(r["controls"], list) or not r["controls"]:
            raise ValueError("Invalid mapping")
        if not all(isinstance(r[k], str) and r[k].strip() for k in ("id", "risk", "evidence_request", "unverified_gap")):
            raise ValueError("Invalid text")
        score = r["likelihood"] * r["impact"]
        output.append({**r, "score": score, "priority": priority(score)})
    return sorted(output, key=lambda r: (-r["score"], r["id"]))

def markdown(rows):
    lines = ["# Synthetic AI Governance Mapping Report", "", "Candidate control mappings and evidence requests only; no compliance determination.", "", "| ID | Risk | Score | Priority | AI RMF | Candidate controls |", "|---|---|---:|---|---|---|"]
    for r in rows:
        lines.append(f'| {r["id"]} | {r["risk"]} | {r["score"]} | {r["priority"]} | {r["ai_rmf_function"]} | {", ".join(r["controls"])} |')
    lines += ["", "## Evidence requests and unverified gaps", ""]
    for r in rows:
        lines += [f'### {r["id"]}: {r["risk"]}', f'- Evidence to request: {r["evidence_request"]}', f'- Unverified gap: {r["unverified_gap"]}', ""]
    return "\n".join(lines)

def main():
    rows = analyze(json.loads((ROOT / "risks.json").read_text(encoding="utf-8")))
    out = ROOT / "outputs"
    out.mkdir(exist_ok=True)
    (out / "mapping_report.md").write_text(markdown(rows), encoding="utf-8")
    with (out / "mapping_report.csv").open("w", newline="", encoding="utf-8") as file:
        fields = ["id", "risk", "likelihood", "impact", "score", "priority", "ai_rmf_function", "controls", "evidence_request", "unverified_gap"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({**row, "controls": "; ".join(row["controls"])})
    print(f"Generated {len(rows)} risk mappings in {out}")

if __name__ == "__main__":
    main()
