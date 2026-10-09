# Data dictionary — HUG presale guarantee regional issuance

**Status:** provisional derived schema; no official CSV processed yet. Official source: https://www.data.go.kr/data/15002513/fileData.do

| Field | Type | Unit / interpretation |
|---|---|---|
| period | string | Original source field 연도, preserved verbatim |
| region | string | Original source field 지역, preserved verbatim |
| guarantee_amount_100m_krw | float | Original 보증실적(억원); unit: 100 million KRW |
| households | integer | Original 세대수 |
| guarantee_amount_per_household_100m_krw | float/null | guarantee_amount_100m_krw / households, null if households=0 |
| period_type | string | year / quarter / unknown, provisional parser output |

**Never call amount-per-household an apartment sale price.** Guarantee issuance covers insured exposure, not transaction price. Compare annual with annual and quarter with matching quarter only.

Source-file actual header values, seasonal flags and subtotal rows must be verified after original CSV ingestion. Full-year 2026 totals must not be inferred from 2026 H1.
