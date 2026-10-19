# N02 v3 actual 60-source rerun (2026-10-19)

Performed an independent local rerun with archived source files, not simply a summary-table re-read. The previous 20 complex files were identified from source_manifest.csv and independently checked against each SHA-256 hash (20/20 matched). Added 40 source CSV files were read from the uploaded cohort_results.zip. All 60 complexes have 408 response rows with no missing or duplicate complex-month-method key: 24,480 rows total.

Rule: 24 ordered months, all first three and last three field observations strictly positive; compute within-complex three-month percentage change and its unweighted median.

| Field | Previous20 median (n) | Added40 median (n) | Combined60 median (n) |
|---|---:|---:|---:|
| pay | -7.99783% (16) | +2.67726% (34) | +1.92566% (50) |
| cleanCost | +0.29851% (16) | +2.24237% (34) | +2.24237% (50) |
| guardCost | -0.76408% (16) | +1.85916% (31) | +1.85916% (47) |

Original 20 eligibility: each 16; 2 excluded due to null and 2 due to zero for each selected field. Added40 eligibility: 34/34/31; six null-excluded per field and three further zero-excluded for guardCost. Prior preliminary new40 counts 28/28/27 do not reproduce and the reason is unresolved because the old intermediate calculation is unavailable. Do not use those preliminary figures.

The rerun uses raw numeric API fields. Neither monetary units, per-area denominator nor nationally representative change is asserted. Research bundle: N02_60단지_통계재현_검증완료_20261019.zip (local QA and runnable code); raw payloads not redistributed on GitHub. Existing Zenodo DOI 10.5281/zenodo.23432629 unchanged; v3 not released.
