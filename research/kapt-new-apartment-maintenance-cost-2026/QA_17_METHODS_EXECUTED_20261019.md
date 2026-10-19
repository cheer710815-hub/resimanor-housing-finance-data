# N02: 17-method full coverage QA execution — 2026-10-19

The original uploaded `cohort_results.zip` containing **new 40 complexes** was inspected directly using a Python standard-library-only program. Exactly **40** unique complexes had **16,320** successful API response records. Per-complex coverage was **24 months x 17 methods = 408 rows**, with **zero** duplicate compound keys, missing expected keys, unexpected methods, malformed JSON, and non-OK statuses. Raw JSON numeric-field cells included **1,190 nulls**. API response completeness is not proof that monetary fields are present or correctly denominated.

An independent five-test synthetic unit suite was **executed**, not only authored: valid response set, missing method, duplicate key, malformed JSON, non-OK response. **5/5 passed**. Audit outputs include `per_complex.csv`, `issues.csv` (zero rows), code and tests in local package `N02_17API_자동품질검증_20261019.zip`.

**Scope:** the 40-complex ZIP only, not a new independent rerun of the prior 20. Does not establish government source field monetary units, area denominator, revision history or national representativeness. Keep Zenodo v2 DOI `10.5281/zenodo.23432629`; v3 not released. Ministry field-definition query is pending.
