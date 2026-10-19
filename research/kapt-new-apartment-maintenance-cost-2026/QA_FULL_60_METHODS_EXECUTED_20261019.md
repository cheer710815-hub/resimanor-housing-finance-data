# N02 full 60-complex 17-operation QA, 2026-10-19

Executed the same offline 17-operation audit against original raw CSV data for both cohorts. Previous20 original CSV sources were reconstructed using `N02_20complex_full_raw_reaudit/source_manifest.csv`; **20/20 SHA-256 values matched**. New40 raw CSV inputs were retrieved from the uploaded `cohort_results.zip`. The combined run verified **60 complexes x 24 months x 17 methods = 24,480 distinct OK responses**, with **zero missing/duplicate compound keys, unexpected methods, malformed JSON, or non-OK response rows**. No live API calls were made.

Raw JSON null value cells across all 35 observed monetary candidate fields: **1,295** (previous20 **105**; new40 **1,190**). These are value cells, not failed API response rows; null must not be treated as zero. Other zero candidate-field cells were **20,260** across 60 complexes. The provider has not yet officially confirmed cost units/area denominators.

This report supersedes the 40-only structural QA's scope, not its results. The runnable inspector, complete per-complex QA CSV, source SHA-256 match list, issues CSV, and JSON summary are packaged as `N02_60단지_17API_통합품질검증_20261019.zip` in the research working files. Raw API data are not republished in this GitHub entry.

Preserve existing Zenodo N02 v2 DOI 10.5281/zenodo.23432629. N02 v3 is a prepublication draft only and requires central approval.
