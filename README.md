 GCP Org Policy Audit (Simulated)

Checks GCP org policy settings against a small security baseline. Useful for demonstrating baseline compliance logic when actual GCP access is not available.

Baseline
--------
Defined in baseline.json. Includes a mix of boolean and list style policy rules. The expected values represent the required posture.

Current Policies
----------------
sample_policies.json simulates what would normally be fetched from the GCP Org Policy API. Mixed values included so the report shows both PASS and FAIL.

Running
-------
python3 audit.py

Output
------
Generates compliance_report.csv with the fields:
id, policy, expected, actual, status, notes

Comparison Logic
----------------
Boolean: actual must equal expected.
List: expected values must be present in actual (containment).

Notes
-----
In a real deployment, load_current() would call GCP APIs with a service account that has Org Policy Viewer. This version skips that and focuses only on comparison and reporting logic.
