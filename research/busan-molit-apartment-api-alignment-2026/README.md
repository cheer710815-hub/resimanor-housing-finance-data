# ARHRN POOL-28 — Busan–MOLIT Apartment Transaction API Alignment

**Public technical research record · 2026-11-17 · v1.0.0**  
Research ID: `ARHRN-POOL28-BUSAN-MOLIT-API-ALIGNMENT-20261111`

## Findings

For apartment sales in Busan **Jung-gu** and **Busanjin-gu**, January–April 2026 contracts, archived government API responses collected in November 2026 yielded:

- MOLIT: **1,706** response rows; Busan City: **1,703** rows.
- Record-signature multiset comparison: **3 excess MOLIT signature occurrences**, all in Busanjin-gu (2 in March, 1 in April).
- MOLIT cancellation-marked rows: **89** (not 89 missing records in Busan City).
- The underlying cause of the three differences is **unconfirmed**. They are **not demonstrated missing contracts or official errors**.

The record signature includes contract year/month/day, price, area at original precision, floor, normalized apartment name, dong, and lot number. Identical signatures are counted with multiplicity, not deduplicated.

## Files
- [Technical report (Korean)](TECHNICAL_REPORT_KO.md)
- [Monthly comparison (CSV)](MONTHLY_RESULTS.csv)
- [Three exception signatures (CSV)](EXCEPTION_SIGNATURES.csv)

### Official source datasets
- [Busan City House Trade Price API](https://www.data.go.kr/data/15167888/openapi.do)
- [MOLIT apartment sales API](https://www.data.go.kr/data/15126469/openapi.do)

**Important limitations:** two districts only; November 2026 snapshots covering January–April 2026 contract months; no unique contract identifiers; no proof of agency error. Historical raw responses are **not redistributed here**. Fresh API requests may return updated rows and cannot guarantee reproduction of the old snapshot. Original offline validation used 23 preserved API response objects.

## Attribution and reuse
**ARHRN** identifies the research project, **not a verified legal author name**. The responsible individual/organization has not been publicly designated. No separate license grant for this research directory has been confirmed; do not assume the dataset-specific license statements elsewhere in this repository automatically cover this new study. Provider rights and source attribution remain applicable. **No DOI has been registered.**

For citation, use the study title, research ID, this repository URL, publication date (2026-11-17), and the specific commit hash. Do not identify the data providers as the report authors. This initial publication is the technical report and summary tables; source-collection and reproduction scripts are still being incorporated, so this directory does not yet provide a turnkey independent re-run.