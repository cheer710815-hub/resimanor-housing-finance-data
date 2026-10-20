# N02 v3: archived API numeric-key schema stability (2026-10-20)

Independently opened the original 20-complex source files (all 20 original SHA-256 checks passed) and additional 40-complex source CSV files. Each archived record's flat JSON payload was inspected and the observed set of keys compared within each API operation across all 60 complexes and their 24 months.

**Results:** 60 complex source files, 17 methods, 24,480 archived response rows. Each of the 17 operations displayed **one consistent observed JSON field-name set** across the entire archive. The 17 sets contain **35 distinct numeric candidate key names** in total. There were **0** non-dictionary JSON bodies, **0** malformed JSON bodies, **0** observed field-set variants within a method, and **0** empty numeric-key response structures.

These results are *not* a government-certified response-field schema, an assertion that all monetary values are non-null, or verification of monetary units, denominators, changes to reporting over time, or statistical representativeness. The official API response-element definitions remain unanswered; retain all 35 as **UNVERIFIED UNIT** in the [provider response matrix](./V3_35_FIELDS_PROVIDER_RESPONSE_MATRIX_20261019.md).

An independently runnable local standard-library audit script, per-method schema variants, field-presence counts, and issue report were packaged in `N02_60단지_JSON필드구조_일치검증_20261020.zip`. Raw JSON was not republished. Keep existing N02 v2 DOI 10.5281/zenodo.23432629; v3 remains a draft pending provider definitions and owner approval.
