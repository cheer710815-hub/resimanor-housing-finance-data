#!/usr/bin/env python3
"""Validate and derive HUG regional presale guarantee figures from the official downloaded CSV.

Usage: python analyze_hug.py /path/to/official.csv --out output
No implicit downloads. No raw figures or empirical findings are fabricated.
"""
import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

FIELDS = ("연도", "지역", "보증실적(억원)", "세대수")
ALIASES = {"연도": ["연도"], "지역": ["지역"], "보증실적(억원)": ["보증실적(억원)", "보증실적"], "세대수": ["세대수"]}
def parse_number(value):
    cleaned = str(value).replace(",", "").strip()
    if cleaned in ("", "-", "–", "—", "N/A", "null"):
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None

def load_rows(path):
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "cp949", "euc-kr"):
        try:
            decoded = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("CSV encoding unrecognized")
    reader = csv.DictReader(decoded.splitlines())
    headers = reader.fieldnames or []
    mapping = {}
    for canonical, candidates in ALIASES.items():
        matches = [h for h in headers if h.strip() in candidates]
        if len(matches) != 1:
            raise ValueError(f"Expected one column for {canonical}: {headers}")
        mapping[canonical] = matches[0]
    return [dict(row) for row in reader], mapping, hashlib.sha256(raw).hexdigest()

def analyze(path, out):
    rows, cols, digest = load_rows(path)
    out.mkdir(parents=True, exist_ok=True)
    exclusions = Counter()
    periods = Counter()
    cleaned = []
    keys = set()
    samples = []
    for i, source in enumerate(rows, start=2):
        period = str(source[cols["연도"]]).strip()
        region = str(source[cols["지역"]]).strip()
        amount = parse_number(source[cols["보증실적(억원)"]])
        households = parse_number(source[cols["세대수"]])
        if not region or not period:
            exclusions["missing_period_or_region"] += 1
            continue
        if amount is None or households is None:
            exclusions["non_numeric_or_missing_values"] += 1
            continue
        if amount < 0 or households < 0 or households != int(households):
            exclusions["invalid_negative_or_fractional_households"] += 1
            continue
        if not re.match(r"^20\d{2}", period):
            exclusions["unrecognized_period"] += 1
            continue
        key = (period, region)
        if key in keys:
            exclusions["duplicate_period_region"] += 1
            continue
        keys.add(key)
        period_type = "quarter" if re.search(r"(분기|Q[1-4]|[1-4]Q)", period, re.I) else ("year" if re.fullmatch(r"20\d{2}년?",period) else "unknown")
        periods[period_type] += 1
        if any(token in region for token in ("합계", "총계", "전국", "계")):
            exclusions["possible_aggregate_region"] += 1
            continue
        clean = dict(period=period, region=region, guarantee_amount_100m_krw=amount, households=int(households),
                     guarantee_amount_per_household_100m_krw=(amount / households if households else None), period_type=period_type)
        cleaned.append(clean)
        if len(samples) < 10: samples.append({"source_row": i, "period": period, "region": region, "amount": amount, "households": int(households)})
    if not cleaned:
        raise ValueError("No validated observations, check field formats and period schema")
    fieldnames = list(cleaned[0])
    with (out / "hug_regional_clean.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames); w.writeheader(); w.writerows(cleaned)
    report = {"source": "https://www.data.go.kr/data/15002513/fileData.do", "sha256": digest,
        "raw_records": len(rows), "catalog_expected_records": 818, "catalog_count_matches": len(rows)==818,
        "clean_records": len(cleaned), "period_types": dict(periods), "excluded_or_flagged": dict(exclusions),
        "manual_spot_check_needed": samples,
        "publication_ready": False,
        "limitations": ["Period labels must be audited before aggregate/year-on-year analysis",
            "Possible aggregate rows must be manually reconciled",
            "HUG guarantee amount per household is NOT apartment price"]}
    (out / "VALIDATION_REPORT.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k:report[k] for k in ("raw_records","catalog_count_matches","clean_records","period_types","excluded_or_flagged")}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--out", type=Path, default=Path("output"))
    args = parser.parse_args()
    analyze(args.input_csv, args.out)
