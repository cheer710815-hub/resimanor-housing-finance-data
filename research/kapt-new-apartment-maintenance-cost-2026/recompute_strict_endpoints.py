#!/usr/bin/env python3
"""N02: reproducible strict endpoint comparison from local cost_raw_long.csv files.

Example: python recompute_strict_endpoints.py cohort_results --out n02_recheck
Python standard library only. Read-only with respect to raw inputs.
Does NOT determine official units, area denominator, or national estimates.
"""
import argparse, csv, json, pathlib, collections, statistics
FIELDS = {"pay": "getHsmpLaborCostInfoV3",
          "cleanCost": "getHsmpCleaningCostInfoV3",
          "guardCost": "getHsmpGuardCostInfoV3"}
METHOD_KEYS = ("api_method", "method", "operation", "api", "service", "operation_name")
MONTH_KEYS = ("searchDate", "search_date", "yyyymm", "month", "report_month")
CODE_KEYS = ("kaptCode", "kapt_code", "code")
JSON_KEYS = ("result_json", "response_json", "raw_json", "json")

def get(row, options):
    for key in options:
        if key in row and str(row[key]).strip():
            return row[key]
    return None

def find_item(obj):
    if isinstance(obj, dict):
        for key in ("item", "items"):
            if key in obj:
                v = obj[key]
                if isinstance(v, list):
                    return v[0] if len(v) == 1 and isinstance(v[0], dict) else {}
                if isinstance(v, dict):
                    return v
        for key in ("response", "body", "data", "result"):
            if isinstance(obj.get(key), (dict, list)):
                found = find_item(obj[key])
                if found:
                    return found
        if any(k in obj for k in FIELDS):
            return obj
    if isinstance(obj, list) and len(obj) == 1:
        return find_item(obj[0])
    return {}

def amount(x):
    if x is None or isinstance(x, bool):
        return None
    try:
        return float(str(x).replace(",", "").strip())
    except (ValueError, TypeError):
        return None

def audit(files):
    groups, issues = collections.defaultdict(dict), []
    for f in files:
        with f.open("r", encoding="utf-8-sig", newline="") as fh:
            rows = csv.DictReader(fh)
            if not rows.fieldnames:
                issues.append([str(f), "empty CSV"]); continue
            for line, row in enumerate(rows, 2):
                method = get(row, METHOD_KEYS)
                month = get(row, MONTH_KEYS)
                code = get(row, CODE_KEYS) or f.parent.name.split("_")[0]
                raw = get(row, JSON_KEYS)
                if not method or not month or not raw:
                    issues.append([str(f), f"line {line}: unknown method, month or JSON column"]); continue
                try:
                    item = find_item(json.loads(raw))
                except (ValueError, TypeError):
                    issues.append([str(f), f"line {line}: malformed result_json"]); continue
                for field, target in FIELDS.items():
                    if str(method).split("/")[-1] != target:
                        continue
                    key = (code, field, str(month))
                    if str(month) in groups[code, field]:
                        issues.append([str(f), f"line {line}: duplicate {key}"])
                    groups[code, field][str(month)] = amount(item.get(field))
    results = []
    for (code, field), months in sorted(groups.items()):
        dates = sorted(months)
        first = [months[m] for m in dates[:3]]
        last = [months[m] for m in dates[-3:]]
        reason, change = "eligible", None
        if len(dates) != 24:
            reason = "month_count_not_24"
        elif any(x is None for x in first + last):
            reason = "null_or_nonnumeric"
        elif any(x <= 0 for x in first + last):
            reason = "zero_or_nonpositive"
        else:
            change = ((statistics.mean(last) / statistics.mean(first)) - 1) * 100
        results.append([code,field,len(dates),reason,"" if change is None else f"{change:.12g}"])
    return results, issues

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=pathlib.Path, help="directory recursively containing cost_raw_long.csv")
    ap.add_argument("--out", type=pathlib.Path, default=pathlib.Path("n02_recheck"))
    args = ap.parse_args()
    files = sorted(args.source.rglob("cost_raw_long.csv"))
    if not files:
        ap.error("No cost_raw_long.csv found. Extract the source ZIP first.")
    rows, issues = audit(files)
    args.out.mkdir(parents=True, exist_ok=True)
    with (args.out/"eligibility_by_complex_field.csv").open("w", encoding="utf-8-sig",newline="") as f:
        w = csv.writer(f); w.writerow(["kaptCode","field","months","status","change_pct"]);w.writerows(rows)
    with (args.out/"source_issues.csv").open("w", encoding="utf-8-sig",newline="") as f:
        w = csv.writer(f);w.writerow(["file","problem"]);w.writerows(issues)
    print("CSV files:",len(files), "issues:",len(issues))
    for field in FIELDS:
        vals=[float(row[4]) for row in rows if row[1]==field and row[3]=="eligible"]
        print(field, "eligible_n", len(vals), "median_pct", round(statistics.median(vals),4) if vals else "NA")
    if issues:
        raise SystemExit("Raw-source issues found; see source_issues.csv")
if __name__=="__main__":
    main()
