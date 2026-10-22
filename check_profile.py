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
import re
import sys
import urllib.request
from pathlib import Path

README = Path(__file__).resolve().parent / "README.md"
MANIFEST = ("https://raw.githubusercontent.com/KushPatel29/KushPatel29.github.io/"
            "main/portfolio-manifest.json")
ROW = re.compile(r"^\| \S+ \[\*\*[^*]+\*\*\]\(https://github\.com/KushPatel29/([\w.-]+)\)", re.M)

text = README.read_text(encoding="utf-8")
failures = []

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
