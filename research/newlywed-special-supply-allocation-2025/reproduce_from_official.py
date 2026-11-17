#!/usr/bin/env python3
"""Reproduce descriptive four-cohort audit from 2025-11-28 official ApplyHome CP949 CSV files."""
import csv, re, sys, hashlib
from collections import defaultdict
from pathlib import Path

def read(path):
    with open(path, encoding="cp949", newline="") as fp:
        return list(csv.DictReader(fp))

def checksum(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

if len(sys.argv) != 3:
    raise SystemExit("Usage: python reproduce_from_official.py NOTICE.csv TYPE.csv")
notice_path, type_path = sys.argv[1:]
expected = {
    "notice": "da0722409157619242fb614c145541051e1584aadfd1176f946910c5085d4ae2",
    "type": "f6a71618eee61414d9cc401f047192ea218f711927396fc5c1786060406d8642",
}
assert checksum(notice_path) == expected["notice"], "Notice file SHA-256 differs from audit snapshot"
assert checksum(type_path) == expected["type"], "Type file SHA-256 differs from audit snapshot"
by_id = {r["주택관리번호"]: r for r in read(notice_path)}
rows = defaultdict(lambda: [0, 0])
for r in read(type_path):
    n = by_id.get(r["주택관리번호"])
    if not n:
        continue
    if (n["주택구분코드명"], n["주택상세구분코드명"], n["분양구분코드명"]) != ("APT", "민영", "분양주택"):
        continue
    d = n["모집공고일"]
    if d[:4] not in ("2024", "2025") or d[5:] > "11-28":
        continue
    m = re.match(r"^\s*(\d+(?:\.\d+)?)", r["주택형"])
    if not m or float(m.group(1)) > 85:
        continue
    general, special = int(r["일반공급세대수"] or 0), int(r["특별공급세대수"] or 0)
    newlywed = int(r["특별공급_신혼부부세대수"] or 0)
    if general + special <= 0:
        continue
    rows[r["주택관리번호"]][0] += general + special
    rows[r["주택관리번호"]][1] += newlywed
summary = defaultdict(lambda: [0, 0, 0])
for management_id, (units, newlywed) in rows.items():
    d = by_id[management_id]["모집공고일"]
    era = "pre" if d[5:] < "03-31" else "post"
    v = summary[(d[:4], era)]
    v[0] += 1
    v[1] += units
    v[2] += newlywed
expected_counts = {
    ("2024", "pre"): (64, 25924, 4559),
    ("2024", "post"): (212, 93456, 16311),
    ("2025", "pre"): (32, 10965, 1889),
    ("2025", "post"): (194, 81404, 18168),
}
assert all(tuple(summary[k]) == v for k, v in expected_counts.items()), "Cohort totals changed"
assert sum(v[0] for v in summary.values()) == 502
share = {k: 100 * v[2] / v[1] for k, v in summary.items()}
for year, era in [("2024", "pre"), ("2024", "post"), ("2025", "pre"), ("2025", "post")]:
    count, units, newlywed = summary[(year, era)]
    print(f"{year},{era},{count},{units},{newlywed},{share[(year,era)]:.5f}")
contrast = (share[("2025","post")] - share[("2025","pre")]) - (share[("2024","post")] - share[("2024","pre")])
assert abs(contrast - 5.22366) < 0.0001
print(f"descriptive_difference_pp={contrast:.5f} (NOT causal)")
