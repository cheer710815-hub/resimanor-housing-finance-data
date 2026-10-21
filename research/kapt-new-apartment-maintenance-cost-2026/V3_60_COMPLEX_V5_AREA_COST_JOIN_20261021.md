# N02 60-complex raw-cost x current V5 area join — 2026-10-21

## Completed
- 60/60 distinct K-apt complex codes present in `n02_60_privarea_results.csv`, V5 basic-information area fields (`privArea`, `kaptMarea`, `kaptTarea`), all successful HTTP 200 in input.
- Retrieved and parsed archived raw cost records for **all 60/60 complexes** from the existing 40-complex `cohort_results.zip`, 10-complex and five-complex pilot ZIPs, plus smaller independent archived complex ZIPs.
- Matched raw numeric monthly `pay`, `cleanCost`, `guardCost` to V5 `privArea` and `kaptMarea` by complex code. **4,155 unique (complex, month, field) finite numeric cells** available. No conflicting duplicate numeric values. Do not conflate this number with all requested endpoint/month responses or the earlier strict eligibility population.
- Example A10020809 202501 cleanCost: raw 3,667,763; V5 privArea 23,943.96 sqm; calculated 153.18 KRW/sqm exclusive-area basis. Also calculate billing-area basis separately. These are **exploratory normalized fields** using a current area snapshot.

## Unresolved interpretation
- Current V5 areas are not proven equal to the historical corresponding month's denominator. No date-specific official cleaning display has been verified directly.
- Existing study's within-complex raw-field relative trajectories and strict eligibility population unchanged.
- Missing/null numeric values are not zeros. The prior 4 flagged unusual area relationships need manual historical source review; do not silently drop or 'correct' them.
- No Zenodo v3 publication was made.

## Attached reproducible local artifact
`N02_V5_60단지_관리비_면적연결_20261021.zip` contains README, 4,155-row monthly area-normalized exploratory CSV, per-complex/field coverage CSV and conflicting-duplicate issues CSV.
