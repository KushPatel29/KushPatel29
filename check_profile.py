"""
This profile is one of three front doors, with the portfolio site and each
repository's README, and they have disagreed before. This holds the profile to
the site's manifest so the three keep telling the same story:

    python check_profile.py            # compares with the live manifest
    python check_profile.py --offline  # skips the comparison and says so

Checked:
- every project in the site's manifest has a row in the table, and nothing else
  does;
- the manifest's flagships are the three listed under "Start with these three",
  and lead the table in the same order;
- no headline test total and no per-row test counts. The site dropped them: a
  total mostly measures parametrization, and a reviewer who checks discounts it;
- DP-600 is described as an exam being prepared for, never as a credential.
"""
import json
import hashlib
import re
import sys
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

README = Path(__file__).resolve().parent / "README.md"
MANIFEST = ("https://raw.githubusercontent.com/KushPatel29/KushPatel29.github.io/"
            "main/portfolio-manifest.json")
ROW = re.compile(r"^\| \S+ \[\*\*[^*]+\*\*\]\(https://github\.com/KushPatel29/([\w.-]+)\)", re.M)

text = README.read_text(encoding="utf-8")
failures = []

# Share the exact current snapshot with the portfolio and upstream audit.
# A page/layout check used to pass while this paragraph called an inconclusive
# disparity "noise, not bias" and quoted groups from a different model run.
receipt = json.loads(README.with_name("fairness-evidence.json").read_text(encoding="utf-8"))
upstream, evidence = receipt["upstream"], receipt["evidence"]
if (upstream["repository"] != "KushPatel29/hr-attrition-analytics"
        or upstream["path"] != "output/fairness_evidence.json"
        or not re.fullmatch(r"[a-f0-9]{40}", upstream["revision"])):
    raise SystemExit("The fairness source must name an immutable HR evidence record")
start_marker, end_marker = "<!-- fairness-evidence:start -->", "<!-- fairness-evidence:end -->"
source = f"https://github.com/{upstream['repository']}/blob/{upstream['revision']}/{upstream['path']}"
block = start_marker + "\n" + evidence["display"]["summary"] + f"\n\n[Audit counts and limitations]({source})\n" + end_marker
if text.count(start_marker) != 1 or text.count(end_marker) != 1:
    raise SystemExit("Exactly one public fairness summary is required")
prefix, rest = text.split(start_marker, 1)
_, suffix = rest.split(end_marker, 1)
expected_text = prefix + block + suffix
if "--write" in sys.argv:
    README.write_text(expected_text, encoding="utf-8")
    text = expected_text
elif text != expected_text:
    failures.append("fairness facts drifted: run python check_profile.py --write")
if "small-sample noise, not bias" in text or "p ≈ 0.23" in text:
    failures.append("the obsolete fairness interpretation/example returned")
if "independently modelled plan" not in text:
    failures.append("identify the independent utility planning baseline")
if "HubSpot run as a production integration" in text:
    failures.append("describe the executed HubSpot developer-account integration without implying customer production tenure")

if re.search(r"[\d,]{3,}\s+automated tests", text, re.I):
    failures.append("a headline test total is back")
if re.search(r" [\d,]+ (?:dbt |pytest )?tests\.(?= |\|)", text):
    failures.append("a table row prints a test count")
if re.search(r"Associate \(DP-600\)", text):
    failures.append("DP-600 reads as a credential; say the exam is being prepared for")

rows = [r.lower() for r in ROW.findall(text)]
start = text.split("## Start with these three", 1)
featured = []
if len(start) == 2:
    section = start[1].split("\n## ", 1)[0]
    featured = [m.lower() for m in re.findall(
        r"^\d\. \*\*\[[^\]]+\]\(https://github\.com/KushPatel29/([\w.-]+)\)", section, re.M)]
if len(featured) != 3:
    failures.append(f'"Start with these three" lists {len(featured)} projects, not 3')
elif rows[:3] != featured:
    failures.append("the table does not lead with the three featured projects in order")

if "--offline" in sys.argv:
    print(f"offline: {len(rows)} table rows; manifest comparison skipped")
else:
    for ref in (upstream["revision"], upstream["branch"]):
        url = f"https://raw.githubusercontent.com/{upstream['repository']}/{ref}/{upstream['path']}"
        with urllib.request.urlopen(url, timeout=30) as response:
            payload = response.read().decode("utf-8").replace("\r\n", "\n")
        if (hashlib.sha256(payload.encode("utf-8")).hexdigest() != upstream["sha256"]
                or json.loads(payload) != evidence):
            failures.append(f"HR source changed at {ref}; review and refresh the versioned fairness snapshot")
    with urllib.request.urlopen(MANIFEST, timeout=30) as response:
        manifest = json.load(response)

    def repo_of(project):
        url = project["repository"].rstrip("/")
        if "/tree/" in url or url.lower().endswith("kushpatel29.github.io"):
            return "kushpatel29.github.io"
        return url.rsplit("/", 1)[-1].lower()

    expected = {repo_of(p) for p in manifest["projects"]}
    flagships = [repo_of(p) for p in manifest["projects"] if p["priority"] == "flagship"]
    if set(rows) != expected:
        if expected - set(rows):
            failures.append(f"missing from the table: {sorted(expected - set(rows))}")
        if set(rows) - expected:
            failures.append(f"in the table but not the manifest: {sorted(set(rows) - expected)}")
    if sorted(featured) != sorted(flagships):
        failures.append(f"featured {featured} but the manifest's flagships are {flagships}")
    print(f"manifest: {len(expected)} projects, flagships {flagships}")

print(f"table: {len(rows)} rows; featured: {featured}")
if failures:
    print("\n".join(f"✗ {f}" for f in failures))
    sys.exit(1)
print("✓ the profile matches the portfolio")
