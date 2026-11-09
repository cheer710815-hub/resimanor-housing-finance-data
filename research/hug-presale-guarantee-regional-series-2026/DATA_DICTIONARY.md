# Data dictionary — HUG regional presale guarantee issuances, 2009–2026 Q2

**Status:** description of the existing published GitHub CSV (818 data rows, 11 columns). This is a documentation correction, **not** a new release, not a reprocessing of the official source, and not a new DOI.

- Existing CSV: [`hug_presale_guarantee_clean_2009_2026q2.csv`](https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/research/hug-presale-guarantee-regional-series-2026/hug_presale_guarantee_clean_2009_2026q2.csv)
- Official HUG source: https://www.data.go.kr/data/15002513/fileData.do
- Existing archived research DOI: https://doi.org/10.5281/zenodo.23262918
- Verified methodology: [`METHODOLOGY_VERIFIED.md`](https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/research/hug-presale-guarantee-regional-series-2026/METHODOLOGY_VERIFIED.md)

## Columns in the currently accessible GitHub CSV

| CSV field | Observed storage | Definition / unit |
| --- | --- | --- |
| `source_row` | integer-like text | Row identifier carried from source ingestion; source traceability reference, not the housing-project ID. |
| `period` | text | Original reporting period, e.g. `2009`, `2017 1분기`; preserve exactly. |
| `year` | integer-like text | Extracted calendar year used for grouping. |
| `quarter` | integer-like text or empty | Quarter number (1–4) for quarterly records; empty for annual records. |
| `period_type` | `year` / `quarter` | Distinguishes annual and quarterly observations; do not aggregate both types as independent periods. |
| `region_original` | text | Unmodified original region label, including ambiguous `전라` when present. |
| `region_standard` | text | Region label used by the derived table; check exceptional/unmapped values before geographic totals. |
| `guarantee_amount_100m_krw` | numeric text | HUG guarantee issuance amount in units of KRW 100 million (`억원`); may be negative. Not sale price or realized sales. |
| `households` | integer-like text | Household count in the guarantee record; can be negative or zero. Not completed sales contracts. |
| `amount_per_household_100m_krw` | numeric text or empty | Derived amount / household when **both** amount and households are positive; otherwise blank. Not average apartment selling price. |
| `quality_flags` | text or empty | Pipe-delimited data-quality annotations, including `negative_amount`, `negative_households`, `zero_households`, `unmapped_region`; flags may co-occur. |

## Observed quality checks (GitHub CSV, read-only verification)

- 818 rows: 119 annual rows and 699 quarterly rows.
- 13 negative guarantee-amount rows; 3 negative-household rows; 21 zero-household rows.
- 1 row with original region `전라`; do not arbitrarily split into Jeonbuk/Jeonnam.
- For all nonempty derived `amount_per_household_100m_krw` cells, reported value agrees with amount / households to within 0.000000011 (allowing stored decimal rounding).
- Missing region-quarter observations are **missing**, not guaranteed zeros.

## Reuse and provenance boundaries

Compare annual with annual, and quarterly with like quarters. Year 2026 ends at Q2 in this research package; it is not a complete 2026 annual total. HUG guarantee issuances and MOLIT apartment presale supply statistics have different scopes and are not a numerator and denominator for a contract rate.

The original HUG official data remain subject to their own source terms. Resimanor's original curation and explanatory prose are offered under CC BY 4.0, without claiming exclusive rights over official source data. Later cross-source tables on GitHub were not included in the original Zenodo v1.0 deposit.

**Caution:** A previous documentation draft referred to provisional fields `region` and `guarantee_amount_per_household_100m_krw`. Neither is a column name in the current published 11-column CSV. Use the field names in the table above.
