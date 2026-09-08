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
"""
import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent / "README.md"

# dbt asserts with its own test framework, not pytest, so its contribution is
# written as "154 dbt data tests" and does not match the pattern below.
# 148 generic and singular tests plus 6 unit tests.
DBT_TESTS = 154


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
    # ASCII on purpose: this runs on a Windows console as often as on a CI
    # runner, and cp1252 cannot encode a tick.
    print("\nOK: the featured counts add up to the number this page claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
