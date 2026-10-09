# 2025 H1 vs 2026 H1 matched-region-quarter comparison

Source: HUG official 분양보증 발급현황 (2026-06-30), processed 818-row CSV.
Derived file: [hug_2025_2026_h1_matched_region_quarter.csv](./hug_2025_2026_h1_matched_region_quarter.csv).

## Why matched pairs?
The raw source contains only 30 validly mapped region-quarter observations in 2025 Q1-Q2 and 33 in 2026 Q1-Q2. Comparing raw aggregate totals is confounded by the unmatched records. This analysis therefore restricts to 29 region-quarter keys appearing in *both* years (same province and same quarter Q1 or Q2).

## Results (units: 억원 and 세대)
| Scope | 2025 H1 guarantee amount | 2026 H1 guarantee amount | 2025 H1 households | 2026 H1 households |
|---|---:|---:|---:|---:|
| All reported standard-region rows | 202,579 | 431,426 | 45,023 | 90,160 |
| 29 matched region-quarter observations | 202,601 | 426,340 | 45,023 | 88,896 |
| Matched-pair arithmetic change | | +223,739 | | +43,873 |

The difference between 2025's all-record and matched amount is due to an **unmatched negative amount (-22억원) for 세종, Q1 2025**; its household value is zero. Four 2026 region-quarter observations (대전 Q1, 세종 Q2, 전남 Q1, 제주 Q1) have no 2025 counterpart and are excluded from pairwise comparison.

## How to reproduce
1. Read `hug_presale_guarantee_clean_2009_2026q2.csv` preserving original signed values.
2. Keep years 2025 and 2026, quarters 1 and 2, and rows with a standard province value.
3. Join the 2025 and 2026 records on (region_standard, quarter), inner join only.
4. Calculate differences as 2026 minus 2025, without treating missing observations as zero.
5. Sum 29 individual joined records, and compare separately with all reported rows in each year.

## Interpretation
- These are HUG *guarantee issuance* figures, not sale price or sales transactions.
- Differences may reflect issuance timing, guarantee coverage, housing supply, accounting adjustments, and reported geographic coverage; causal explanations are not established.
- A common-key panel reduces but does not eliminate differences in source data quality.
- Comparisons should always be disclosed as '29 matched region-quarter records', not 'complete 17-region census'.
- All values are in `억원` unless stated otherwise.

Official source: https://www.data.go.kr/data/15002513/fileData.do
