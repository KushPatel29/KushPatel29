"""
The per-repo test counts on this page have to add up to the total it claims.

This profile is one of three front doors — the GitHub profile, the portfolio
site, and each repository's own badge — and they have disagreed before. When
they did, it was not a rounding difference: this page was quoting 81 tests for
a repository whose badge said 404, because the numbers were typed once and
never compared to anything again.

For a portfolio whose single stated rule is that no claim ships without a test,
two front doors disagreeing is the worst defect on it. So the arithmetic is
checked here rather than trusted:

    python check_totals.py

Exits non-zero if the featured figures stop summing to the headline. The dbt
project contributes data tests rather than pytest cases, so it is counted
explicitly and named, not silently folded in.

Adding up is not enough, though. On 2026-09-17 this page summed perfectly to
11,119 while four of its rows were behind their repositories -- Marketing said
91 against a badge of 128. So each row is also compared with the portfolio
site's manifest, whose counts the site's own CI holds to every repository's
badge. That needs the network; `--offline` skips it and says so.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

README = Path(__file__).resolve().parent / "README.md"
MANIFEST = ("https://raw.githubusercontent.com/KushPatel29/KushPatel29.github.io/"
            "main/portfolio-manifest.json")
ROW = re.compile(r"^\|[^|]*?\(https://github\.com/KushPatel29/([\w.-]+)\)"
                 r".*?([\d,]+) tests\. \|", re.M)


def rows_that_disagree_with_the_site(text: str) -> list[str] | None:
    try:
        with urllib.request.urlopen(MANIFEST, timeout=30) as response:
            manifest = json.load(response)
    except OSError as error:
        print(f"site manifest unreachable ({error}); rows not compared")
        return None
    site = {p["repository"].rstrip("/").rsplit("/", 1)[-1].lower(): p["testCount"]
            for p in manifest["projects"]}
    wrong = []
    for repo, count in ROW.findall(text):
        stated = int(count.replace(",", ""))
        expected = site.get(repo.lower())
        if expected is None:
            wrong.append(f"{repo}: on this page, not on the site")
        elif stated != expected:
            wrong.append(f"{repo}: this page says {stated:,}, the site says {expected:,}")
    print(f"{len(ROW.findall(text))} rows compared with the site manifest")
    return wrong


# dbt asserts with its own test framework, not pytest, so its contribution is
# written as "157 dbt data tests" and does not match the pattern below.
# 151 generic and singular tests plus 6 unit tests.
DBT_TESTS = 157


def main() -> int:
    text = README.read_text(encoding="utf-8")

    featured = [int(n.replace(",", "")) for n in re.findall(r"([\d,]+) tests\.", text)]
    if not featured:
        print("no per-repo test counts found on the page", file=sys.stderr)
        return 1

    claimed = re.search(r"\*\*([\d,]+) automated tests across", text)
    if not claimed:
        print("no headline total found on the page", file=sys.stderr)
        return 1
    headline = int(claimed.group(1).replace(",", ""))

    dbt_stated = re.search(r"(\d+) dbt data tests", text)
    dbt = int(dbt_stated.group(1)) if dbt_stated else 0
    if dbt != DBT_TESTS:
        print(f"the dbt line says {dbt} data tests, this check expects "
              f"{DBT_TESTS}", file=sys.stderr)
        return 1

    total = sum(featured) + dbt
    print(f"{len(featured)} featured repos + dbt: "
          f"{' + '.join(f'{n:,}' for n in featured)} + {dbt} = {total:,}")
    print(f"headline claims {headline:,}")

    if total != headline:
        print(f"\nFAIL: they disagree by {abs(total - headline):,}. Update the "
              "cards and the headline together.", file=sys.stderr)
        return 1

    if "--offline" not in sys.argv:
        wrong = rows_that_disagree_with_the_site(text)
        if wrong:
            print("\nFAIL: rows that disagree with the site:\n  " + "\n  ".join(wrong),
                  file=sys.stderr)
            return 1
    # ASCII on purpose: this runs on a Windows console as often as on a CI
    # runner, and cp1252 cannot encode a tick.
    print("\nOK: the featured counts add up to the number this page claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
