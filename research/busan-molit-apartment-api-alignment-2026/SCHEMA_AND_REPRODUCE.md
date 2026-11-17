# POOL-28 — Fields, identity and reproduction

**Scope:** January–April 2026 apartment-sale contract months; Busan Jung-gu (`26110`) and Busanjin-gu (`26230`). Archived source responses were collected in November 2026.

| Concept | MOLIT XML element | Busan City JSON field |
|---|---|---|
| Contract month | `dealYear` + `dealMonth` | `ctrtYm` |
| Contract day | `dealDay` | `ctrtDay` |
| Price (10,000 KRW) | `dealAmount` | `dlngAmt` |
| Exclusive area, m² | `excluUseAr` | `xuar` (**not** `siar`) |
| Floor | `floor` | `flr` |
| Apartment name | `aptNm` | `bldgNm` |
| Dong | `umdNm` | last place-name token of `sggNm` |
| Lot number | `jibun` | `lnbr` |
| Cancellation mark | `cdealType` | No confirmed corresponding field in archived responses |
| Cancellation date | `cdealDay` | No confirmed corresponding field in archived responses |

The archived records were compared as **multisets of normalized record signatures**. Two rows with identical signatures are not automatically duplicates. An equal signature does not prove a shared legal contract ID.

## Independent audit using historical archived source ZIPs

1. Obtain the three original ZIPs separately: `POOL28_JUNGGU_202601_SOURCE_REVIEW.zip`, `POOL28_202602_202604_SOURCE_REVIEW.zip`, and `POOL28_BUSANJINGU_MOLIT_4MONTH_RAW.zip`. They are **not included in this public repository**.
2. Put these ZIPs beside `reproduce_pool28.py`; run `python reproduce_pool28.py` with Python 3.10+.
3. Check `ARHRN_POOL28_STAGE6_SENSITIVITY_AUDIT.json` and `ARHRN_POOL28_STAGE6_MONTHLY_RESULTS.csv`.
4. Compare the outputs against `MONTHLY_RESULTS.csv` and `EXCEPTION_SIGNATURES.csv`.

**Historic snapshots are not reproducible from this repository alone.** Public APIs may have since been corrected or updated. When collecting again, preserve query parameters, UTC collection time, page counts and SHA-256 checksums, then report the **new** snapshot separately. Do not label changed results as agency errors without independent evidence.

## Sources

- Busan: https://www.data.go.kr/data/15167888/openapi.do
- MOLIT: https://www.data.go.kr/data/15126469/openapi.do

No DOI. The ARHRN research ID identifies the project, not a verified legal author identity or granted license.