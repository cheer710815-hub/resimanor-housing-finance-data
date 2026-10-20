# N02 24-consecutive-month validation — 2026-10-20

Reconstructed the calendar continuity test in the execution environment and applied the YYYYMM/consecutive-month predicate to **60 actual archived source CSVs** (20 original and 40 new).

- Previous 20 SHA-256 comparisons: **20/20 match**.
- Each studied field had 24 consecutive valid reporting months; invalid calendar month and interrupted sequence findings: **0**.
- Raw row structural/duplicate issues observed: **0**.
- Eight synthetic edge-case tests passed in the execution environment. These checks were reconstructed from the current documented conditions; this is **not a claim that the exact GitHub unittest script itself ran in this step**.
- Recomputed strict first-three versus last-three median changes: `pay` **+1.925659% (n=50)**, `cleanCost` **+2.242365% (n=50)**, and `guardCost` **+1.859155% (n=47)**. Results equal the accepted pre-change values.

Working archive: `N02_60단지_연속24개월_재검증_20261020.zip` includes 180 complex-field eligibility outcomes, issues.csv, summary.json and README without raw source payloads.

No official confirmation of API monetary units or denominators. Existing Zenodo v2 DOI `10.5281/zenodo.23432629` remains unchanged; v3 remains unpublished pending source definitions and researcher approval.
