#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check internal consistency of published POOL-28 summary tables.

This DOES NOT revalidate official source responses or determine the cause of
record differences. For archived-source validation, use reproduce_pool28.py.
Run: python validate_public_tables.py
"""
from collections import Counter, defaultdict
import csv
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent
MONTHS = ("202601", "202602", "202603", "202604")
DISTRICTS = ("JUNGGU", "BUSANJINGU")
NUMERIC = (
    "busan_rows", "molit_rows",
    "coarse_molit_only_excess", "coarse_busan_only_excess",
    "strict_molit_only_excess", "strict_busan_only_excess",
    "molit_cancel_marked_rows",
)

def fail(message):
    raise ValueError(message)

def load(path):
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))

def validate(base=BASE):
    rows = load(base / "MONTHLY_RESULTS.csv")
    exceptions = load(base / "EXCEPTION_SIGNATURES.csv")
    if len(rows) != 8:
        fail("Expected exactly 8 district-month result rows")
    pairs = [(r["district"], r["month"]) for r in rows]
    if len(set(pairs)) != 8 or set(pairs) != {(d, m) for d in DISTRICTS for m in MONTHS}:
        fail("District-month coverage or uniqueness differs from published scope")

    sums = defaultdict(int)
    for r in rows:
        for name in NUMERIC:
            try:
                v = int(r[name])
            except (ValueError, KeyError, TypeError):
                fail("Missing or non-integer value in " + name)
            if v < 0:
                fail("Negative count in " + name)
            sums[name] += v
            r[name] = v
        if (r["molit_rows"] - r["busan_rows"] !=
                r["strict_molit_only_excess"] - r["strict_busan_only_excess"]):
            fail("Multiset count difference doesn't reconcile for " + str((r["district"], r["month"])))
        if r["molit_cancel_marked_rows"] > r["molit_rows"]:
            fail("Cancellation marks exceed total MOLIT rows")
        if (r["coarse_molit_only_excess"] - r["coarse_busan_only_excess"] !=
                r["molit_rows"] - r["busan_rows"]):
            fail("Coarse comparison does not reconcile")
    expected = {"busan_rows": 1703, "molit_rows": 1706,
                "strict_molit_only_excess": 3, "strict_busan_only_excess": 0,
                "molit_cancel_marked_rows": 89}
    for name, value in expected.items():
        if sums[name] != value:
            fail("Published aggregate changed in {}: {} != {}".format(name, sums[name], value))

    per_month = defaultdict(int)
    unique_exc = set()
    for r in exceptions:
        if r["district"] != "BUSANJINGU" or r["month"] not in ("202603", "202604"):
            fail("Exception outside reported scope")
        key = (r["district"], r["month"], r["contract_day"],
               r["amount_10000krw"], r["area_sqm_exact"],
               r["floor"], r["building_normalized"])
        if key in unique_exc:
            fail("Duplicate exception signature entry")
        unique_exc.add(key)
        try:
            n = int(r["molit_excess_rows"])
        except (ValueError, KeyError):
            fail("Invalid exception multiplicity")
        if n < 1:
            fail("Non-positive exception multiplicity")
        if "cause unverified" not in r["finding"]:
            fail("Unverified cause qualifier missing")
        per_month[r["month"]] += n
    if len(exceptions) != 3 or dict(per_month) != {"202603": 2, "202604": 1}:
        fail("Exception list and monthly 2+1 split disagree")

    by_month = {r["month"]: r["strict_molit_only_excess"]
                for r in rows if r["district"] == "BUSANJINGU"}
    if any(by_month.get(month, 0) != count for month, count in per_month.items()):
        fail("Exception list not reconciled with monthly result table")

    report = (base / "TECHNICAL_REPORT_KO.md").read_text(encoding="utf-8")
    for required in ("1,706", "1,703", "89", "원인", "DOI"):
        if required not in report:
            fail("Report is missing: " + required)
    print("PASS: 8 scope rows, 1,706 MOLIT / 1,703 Busan, "
          "3 multiset excess (2 March + 1 April), 89 MOLIT cancellation marks.")
    print("LIMIT: Public-table consistency only; source authenticity and "
          "real-world data accuracy NOT verified by this script.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(validate())
    except (ValueError, FileNotFoundError, UnicodeError) as error:
        print("FAIL:", error, file=sys.stderr)
        sys.exit(1)
