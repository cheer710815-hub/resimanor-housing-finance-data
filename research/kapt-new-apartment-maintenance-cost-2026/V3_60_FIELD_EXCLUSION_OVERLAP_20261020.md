# N02 field-level exclusion and overlap audit — 2026-10-20

Input is the 180 complex-field eligibility decisions from the archived-source 24-consecutive-month rerun. Previous 20 IDs came from the frozen original-source manifest; the other 40 are the expansion cohort. This step reaggregates **existing** outcomes without imputing excluded endpoint amounts.

| Group | Source field | Valid | Null/nonnumeric exclusion | Zero/nonpositive exclusion | Total excluded (%) | Median % of valid complexes |
|---|---|---:|---:|---:|---:|---:|
| All 60 | pay | 50 | 8 | 2 | 10 (16.67%) | +1.925659 |
| All 60 | cleanCost | 50 | 8 | 2 | 10 (16.67%) | +2.242365 |
| All 60 | guardCost | 47 | 8 | 5 | 13 (21.67%) | +1.859155 |
| Previous 20 | pay | 16 | 2 | 2 | 4 (20.0%) | -7.997830 |
| Previous 20 | cleanCost | 16 | 2 | 2 | 4 (20.0%) | +0.298514 |
| Previous 20 | guardCost | 16 | 2 | 2 | 4 (20.0%) | -0.764076 |
| Added 40 | pay | 34 | 6 | 0 | 6 (15.0%) | +2.677257 |
| Added 40 | cleanCost | 34 | 6 | 0 | 6 (15.0%) | +2.242365 |
| Added 40 | guardCost | 31 | 6 | 3 | 9 (22.5%) | +1.859155 |

There are **33 excluded complex-field outcomes**, involving **15 distinct complexes**: 9 excluded for all three fields; 6 excluded for one field only. No complex was excluded from precisely two fields in the archived eligibility decision table.

Selection is field-specific. The unknown values for excluded complexes prevent identification of the direction or magnitude of selection bias. Do **not** interpret any excluded raw value as zero; do not infer missing-at-random, national cost trends, statistical significance, or causality. The official monetary units/area denominators remain unverified.

Local reproducible result archive: `N02_60단지_결측표본_제외영향_20261020.zip` (summary and per-complex exclusions; no redistributed source JSON). Existing Zenodo v2 DOI 10.5281/zenodo.23432629 remains unchanged. N02 v3 not published.
