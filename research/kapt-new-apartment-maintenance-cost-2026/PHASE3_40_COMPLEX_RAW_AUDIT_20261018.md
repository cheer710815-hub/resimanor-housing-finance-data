# N02 Phase 3 — 40-complex full raw-data audit (2026-10-18)

**Source:** user-provided `cohort_results.zip` (40 per-complex `cost_raw_long.csv`, `qa.json`, `basic_info.json`; 1 aggregate run summary). The source archive and 40-complex audit workbooks are held in the research workspace, **not redistributed through this public repository**.

## Reproducibility summary
- Total: **40 complex folders × 24 months × 17 API methods = 16,320 response records**; 40 unique complex codes.
- CSV status: **16,320 `ok`; 0 error**. Per-folder QA confirms 408 successes and zero errors.
- All 40: exact 408 rows, 24 distinct reporting months, 17 distinct methods, **zero duplicate** (complex, month, method) keys, **zero missing** expected keys, **zero malformed JSON**.
- There are **35 candidate monetary keys** per complete 17-method month; across **33,600 value cells**, **18,895 nonzero numerical values, 13,515 numerical zeros, 1,190 nulls**. These are key-level cells, NOT API responses and NOT cost sums.
- Nulls appear in **12 of 40 complexes**, representing 34 complex-months in which 35 monetary keys each report null.
- Three-month endpoint comparisons use first 3 vs last 3 reporting months for each complex, with 24 months per complex but **not necessarily from actual occupation date**.
- The **complete-six-month, strictly positive subset** yields within-complex median percentage differences: `pay` +2.40% (**n=28**), `cleanCost` +2.60% (**n=28**), `guardCost` +1.86% (**n=27**).
- API monetary units and denominators **remain unverified** pending provider response. These are descriptive raw-field percentage changes, not actual management-fee amounts per household or per square meter, and the selected sample is not nationally representative.

## Publication hold
Do not merge these figures with the 20-complex v2 report or publish N02 v3 until the earlier 20 raw sources are re-audited under the same pipeline, period comparability is reviewed, and user approves. No Zenodo record or DOI was modified by this QA. Official field-unit enquiry has been sent; response pending.
