# N02 V5 area-normalized exploratory join: completeness and anomaly re-audit (2026-10-21)

Source: `n02_60_privarea_results.csv`, `monthly_area_normalized_exploratory.csv`. Re-read input CSV files and recalculated tests.

- V5 area info 60/60 complex codes; all three area fields positive and present.
- Numeric three-field joined rows **4,155**, covering **1,385 distinct complex-months**. All three fields present per joined complex-month; no duplicate (complex, month, field), no nonfinite numeric values.
- Nominal full 60 × 24 × 3 = **4,320** slots. **165 missing numeric field-slots**, equal to **55 complex-month slots**. **15/60 complexes** have fewer than 24 distinct months represented in this joined numeric table.
- **67 raw zero cells** and **1 negative raw cell** are present among the 4,155; these are *not positive monthly costs*. The negative is **A10022732, 202503, `guardCost=-813210`**, archived in `cohort_results.zip`. It requires provider/source clarification and must not be silently converted into a nonnegative cost.
- Exact missing-value reasons cannot be determined from this *numeric-only join* alone; missing archive observations vs raw NULL/non-numeric vs ETL filter must be resolved by raw response-log reconciliation before claiming original endpoints lack months.
- Four V5 area consistency review flags (not proven errors): **A10023350 흑석자이, A10023362 부천일루미스테이트** have `privArea>kaptMarea`; **A10023277 공주금흥LH행복1단지, A10023388 강릉역 동도센트리움** have gross-to-exclusive area ratio > 5, potentially anomalous magnitude.
- V5 area values were captured **now**; historical monthly area effective dates not verified. Both current-area-based `원/㎡` normalizations remain **exploratory only**, not authoritative K-apt historical display reproductions.
- Prior **60-complex raw-field change analyses with strict positive first/last 3-month eligibility remain unchanged**. No Zenodo v3 publication.

Generated local reproducible QA bundle: `N02_V5_면적연결_추가검증_20261021.zip` with `metrics.json`, `monthly_coverage_60.csv`, `area_flags_60.csv`, `nonpositive_values.csv`, `flagged_monthly_rows.csv`, `README.md`.
