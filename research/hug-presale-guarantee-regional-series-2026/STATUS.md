# HUG regional presale guarantee project — verification gate

Last verified: 2026-10-09 (Asia/Seoul)
Status: **BLOCKED ON OFFICIAL CSV ACQUISITION — DO NOT CLAIM DATASET COMPLETE**

## Completed
- Confirmed official public-data listing: https://www.data.go.kr/data/15002513/fileData.do
- Catalog title: 주택도시보증공사_분양보증 발급현황_20260630
- Catalog reports 818 records; actual file rows have NOT been validated.
- Research protocol, provisional data dictionary, acquisition log and validation script published in this folder.
- Fixed regex year detection and false region exclusion issues in script.

## Not completed — do not represent as done
- Source CSV file bytes and SHA-256
- Executing parser on actual HUG source file
- Verifying record totals / region subtotals and temporal periods
- Quantitative findings, plots and interpretation
- Validated, distributable versioned CSV dataset
- DOI deposition and journal/media outreach
- Resimanor publication

## Immediate unblock
From the official portal, download its CSV into a local file and supply it to the analysis environment.
Run: `python analyze_hug.py ORIGINAL.csv --out output`
Review `VALIDATION_REPORT.json`; its `publication_ready: false` is intentional until manual source spot checks are complete.
Do not aggregate periods or publish empirical claims before period / regional-total reconciliation.

## Integrity notes
- The source catalog's 818 refers to reported rows, not ingested records.
- HUG guarantee issuance amount per household is **not** new-apartment sale price.
- Partial-year 2026 must be compared with equivalent partial years only.
- No placeholder data, invented samples, or fabricated DOI should appear in releases.
