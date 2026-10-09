# HUG regional presale guarantee — release status (2026-10-09)

## Public, verified files
- [818-row cleaned source-preserving CSV](./hug_presale_guarantee_clean_2009_2026q2.csv): 819 lines including header, verified by read-back.
- [Quality flags CSV](./hug_presale_guarantee_quality_flags.csv): 32 lines including header, verified by read-back.
- [Quarter summary CSV](./hug_presale_guarantee_quarter_summary.csv): 43 lines including header, verified by read-back.
- [Year / H1 summary CSV](./hug_presale_guarantee_period_summary.csv): 18 time periods, published previously.
- [Verified methodology](./METHODOLOGY_VERIFIED.md), [verified data dictionary](./DATA_DICTIONARY_VERIFIED.md), [dataset README](./README_DATASET.md).
- [Analysis results and limitations](./VERIFIED_RESULTS_2026-10-09.md).

## Validation gates
The original provided source has 818 records and 4 columns (2009–2026 Q2), 49 distinct period labels, 18 region labels. Original values are retained, including negative issuance amount (13 rows), negative household counts (3), zero households (21), and the ambiguous '전라' geographic label (1). Subtotals for 17 clearly mapped jurisdictions exclude the unresolved '전라' record, not redistribute it. Missing regional observations are not set to zero.

**Do not treat guarantee issuance as actual apartment sale prices or actual contracts.** Annual / half-year figures must not be directly compared as equal duration.

## Publication state
- CSV data and methodology: **published on GitHub**.
- Original full official CSV: not uploaded; original source remains available from HUG's public catalog.
- Independent DOI: **not issued**.
- Resimanor WordPress article: **not published**.
- Metadata may be used as a preliminary citation with the repository permanent version reference. Add DOI only after the deposit is successful and verified.

Official source: https://www.data.go.kr/data/15002513/fileData.do
