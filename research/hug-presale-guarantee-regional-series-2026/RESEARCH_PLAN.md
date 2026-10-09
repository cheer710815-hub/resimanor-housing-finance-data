# HUG presale-guarantee issuance: regional time-series research plan (2026)

**Status: source identified; RAW DATA NOT YET INGESTED. Not a published dataset or empirical finding.**
**Maintainer:** Resimanor
**Source checked:** 2026-10-09

## Official source
- Provider: Korea Housing & Urban Guarantee Corporation (HUG, 주택도시보증공사)
- Catalog: https://www.data.go.kr/data/15002513/fileData.do
- Source title: 주택도시보증공사_분양보증 발급현황_20260630
- Source data reference date: 2026-06-30
- Catalog modification date: 2026-09-30
- Catalog-reported rows: 818
- Frequency: quarterly, with historical 2009 onward; quarterly splits from 2016 onward.
- Documented fields: 연도, 지역, 보증실적(억원), 세대수.
- Provider catalog says redistribution/reuse permission is unrestricted; retain attribution and record file license.
- **No CSV has yet been downloaded into this repository.** Do not cite 818 as validated ingested rows.

## Research questions
1. How has HUG presale-guarantee issuance shifted across regions and quarters?
2. What is the issuance-amount-per-guaranteed-household (억원 / 세대) by region and year/quarter?
3. How concentrated are issuance amount and insured household counts across regions?
4. Are regional issuance trends consistent across partial-year comparable quarters?

## Method once source file is obtained
1. Archive source file and its original filename, download timestamp, SHA-256, catalog reference, declared license.
2. Validate actual file row count, field types, date formatting, monetary and household units, zero/negative values, missing values and total rows.
3. Detect national/subtotal lines before summing by region. Keep original region labels and separately provide normalized regions with mapping log.
4. Segregate annual observations before 2016 from quarterly observations after 2016. Do not treat them as equal-duration records.
5. Compute guaranteed_amount_per_household_100m_krw = guarantee_amount_100m_krw / households only where households > 0. Label this as **guarantee issuance amount per household**, NOT average sale price or purchase price.
6. Compare same-calendar-quarter or complete-year aggregates only. Exclude incomplete 2026 from full-year year-over-year comparisons.
7. Publish transformed CSV, validation summary, methodology, data dictionary, citation recommendation, and code under CC BY 4.0 for Resimanor-authored transformations subject to original-source conditions.

## Minimum validation gates before publication
- Reconcile file actual rows to catalog's 818 or explain the gap.
- Identify duplicated geographic totals and prevent double counting.
- Reconcile quarterly sums to annual totals where such totals exist.
- Quantify missing and invalid observations.
- Peer-review spot checks: at least 10 source-vs-derived rows.
- Every material finding must have traceable records and tested code.

## Intended output
- `hug_presale_guarantee_regional_clean_2009_2026q2.csv`
- `hug_presale_guarantee_regional_metrics_2009_2026q2.csv`
- `DATA_DICTIONARY.md`, `METHODOLOGY.md`, `VALIDATION_REPORT.md`, reproducible scripts
- Resimanor article AFTER factual results have been validated.

**Interpretation warning:** issuance amounts are not actual apartment sale prices, newly sold home prices, mortgage values or realized transactions. Insured households are not necessarily households completing purchases. Do not infer causality from issuance trends.
