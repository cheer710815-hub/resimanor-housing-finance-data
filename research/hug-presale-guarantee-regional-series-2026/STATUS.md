# HUG regional presale guarantee data — status (2026-10-09)

## Source received, 818 rows validated
- User supplied original `주택도시보증공사_분양보증 발급현황_20260630.csv`.
- CP949 source: **818 records / 4 columns**.
- Year/region duplication: none; missing cells: none.
- Original values preserved, with flags for negative amounts (13 rows), negative household counts (3 rows), zero-household cases (21 rows).
- 2023 Q4 `전라` 1 row not mapped to standard 17 provinces; excluded from standard regional aggregate but preserved as original.
- Some quarterly periods have fewer than 17 regional entries; omitted entries were not assigned zero values.
- CSV-derived output, anomaly report, methodology and reproducible build code generated within the current conversation and made available as a ZIP download to the user.

## GitHub publishing status
- Methodology/plans/source documentation and the factual verification summary are available in this repository.
- **The full 818-row processed CSV and ZIP have not yet been uploaded to GitHub.** Do not claim they are hosted here.
- Full results: `VERIFIED_RESULTS_2026-10-09.md`.
- The earlier `analyze_hug.py` is an initial draft; use the tested `build.py` bundled with the finished dataset for production, after review.

## Pending external actions
1. Upload the validated derived CSV / reproducible build script to a public repository (or durable archive) and verify their checksums.
2. Attach repository versioned release and license.
3. Register DOI through a suitable repository if approved.
4. Draft WordPress post with source and cross-links; **do not publish without explicit approval.**

## Interpretation
The guarantee issuance amount is not a transaction price or a contract completion count. No causal conclusions; do not annualize 2026 H1. The '전라' row remains unresolved.
