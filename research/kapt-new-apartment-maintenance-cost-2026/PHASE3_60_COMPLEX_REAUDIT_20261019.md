# N02 60-complex raw-source unified re-audit — 2026-10-19

## Evidence and scope
- **Original 20**: verified original 20 raw `cost_raw_long.csv` files against **all 20 SHA-256 hashes** in `N02_20complex_full_raw_reaudit.zip/source_manifest.csv`.
- **New 40**: reopened uploaded `cohort_results.zip`, loaded 40 independent original raw `cost_raw_long.csv` source files.
- **All 60**: 60 distinct K-apt codes, **24,480 successful records** (60 × 24 × 17), 24 distinct monthly labels and 17 operations each; zero duplicated (code, month, operation) keys or errors recorded in each source CSV; 20/20 original file hashes match source manifest.
- This is an archived-source consistency check, **not a fresh government API refetch**.

## Calculations and strict definition
For each complex and each component `pay`, `cleanCost`, `guardCost`, select the **first 3 and last 3 sorted reporting months**; require that **all six component values are numeric and strictly greater than 0**. If eligible, compute `(mean(last three) / mean(first three) - 1) * 100`; report **median of within-complex percentage changes** in each group. Missing and zero are excluded from the strict subset rather than imputed.

| Component | Original 20 median (n) | New 40 median (n) | Combined 60 median (n) |
|---|---:|---:|---:|
| `pay` | −8.00% (16) | +2.68% (34) | +1.93% (50) |
| `cleanCost` | +0.30% (16) | +2.24% (34) | +2.24% (50) |
| `guardCost` | −0.76% (16) | +1.86% (31) | +1.86% (47) |

The combined median is calculated **from individual complex percentage changes**, not by averaging the two cohort medians or pooling monetary totals.

## Revision flag: earlier Phase-3 summary differs
The 2026-10-18 `PHASE3_40_COMPLEX_RAW_AUDIT_20261018.md` had reported strict counts 28/28/27 and medians +2.40/+2.60/+1.86 for the new 40. **Those figures do not reproduce** under the above field-specific six-point rule when re-reading all 40 raw CSV files: the current counts are 34/34/31. The previous report's computation code is not preserved in this repository; therefore the exact cause of the discrepancy **cannot be established**. Keep the earlier numbers as historical *superseded/unreconciled* estimates, not as confirmed field-specific strict figures.

**Important methodological distinction:** requiring the six points to be positive for **all three fields jointly** is a different rule from field-by-field positivity. In the new 40, joint eligibility gives **31 complexes**, while field-specific positivity gives **34/34/31**. The previous **28/28/27** cannot be explained solely by this joint criterion.

## Interpretation and publication holds
- Monetary units and denominators for source fields still lack official provider confirmation. Avoid stating KRW, KRW/m², per-household amounts or an overall management fee.
- The two cohorts may differ in size, region, calendar windows, and missingness. **Do not** treat the 60 complexes as a representative national sample, claim time trends, causal changes, or a statistically confirmed between-cohort difference.
- This re-audit **does not change** Zenodo N02 v2 (DOI 10.5281/zenodo.23432629); do not release v3 until methodology and public report revisions receive central approval.
- Aggregated computation files (`source_qa.csv`, `component_comparison.csv`, `summary.csv`) prepared as `N02_60개단지_통합원자료검증_20261019.zip`. Individual raw API JSON files remain unpublished.
