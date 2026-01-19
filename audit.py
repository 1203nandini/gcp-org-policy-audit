 import json
import csv

BASELINE_FILE = "baseline.json"
POLICIES_FILE = "sample_policies.json"
REPORT_FILE = "compliance_report.csv"


def load_baseline(path):
    with open(path, "r") as f:
        return json.load(f)


def load_current(path):
    with open(path, "r") as f:
        return json.load(f)


def compare(baseline, current):
    rows = []
    idx = 1

    for policy, rule in baseline.items():
        expected = rule.get("expected")
        typ = rule.get("type")
        actual = current.get(policy)

        status = "FAIL"
        notes = ""

        if typ == "boolean":
            if actual == expected:
                status = "PASS"
            else:
                notes = "expected enforcement not met"

        elif typ == "list":
            # containment mode: expected ⊆ actual
            if isinstance(actual, list) and set(expected).issubset(set(actual)):
                status = "PASS"
            else:
                notes = "baseline values missing"

        else:
            notes = "unknown type"

        rows.append({
            "id": idx,
            "policy": policy,
            "expected": expected,
            "actual": actual,
            "status": status,
            "notes": notes
        })
        idx += 1

    return rows


def write_csv(rows, path):
    headers = ["id", "policy", "expected", "actual", "status", "notes"]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def main():
    baseline = load_baseline(BASELINE_FILE)
    current = load_current(POLICIES_FILE)
    rows = compare(baseline, current)
    write_csv(rows, REPORT_FILE)
    print("report written to", REPORT_FILE)


if __name__ == "__main__":
    main()
