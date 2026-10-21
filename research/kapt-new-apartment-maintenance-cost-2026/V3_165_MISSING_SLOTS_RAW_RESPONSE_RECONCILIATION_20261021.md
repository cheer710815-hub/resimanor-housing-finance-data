# N02: 165 missing joined numeric slots reconciled to archived raw API responses (2026-10-21)

Recomputed from original archived monthly response files for all 60 complexes (8 original named ZIPs) and joined 4,155-row current-V5-area exploratory table, for each complex's 24-month period and three source operations: labor/pay, cleaning/cleanCost, security/guardCost.

| Exact cause | Count |
|---|---:|
| Original API request row exists, status=ok, JSON numeric field value is `null` | **111** |
| No monthly operation row in selected original `cost_raw_long.csv` | **54** |
| Actual numeric response not carried into area join | **0** |
| Unparseable JSON, missing JSON field, non-numeric other | **0** |
| **Total** | **165** |

The 54 absent operation rows are all **A10023388, 강릉역 동도센트리움**, **202309–202502 (18 months × 3 fields)**. Both `A10023388_202303.zip` and `N02_A10023388_309건_이어받기_재수집.zip` include a `cost_raw_long.csv` with only **98 lines of data / 6 distinct months 202303–202308** (CSV 98 data rows). A companion `cost_raw_long.tmp.csv` has **99 data rows**, but still contains only those 6 months, so does not recover the missing period. This is **absence in the currently accessible archive**, not proof that the public provider lacks 18 months.

The 111 actual `null` field cells are distributed across **15 affected complexes** (the same 15 include A10023388's additional three nulls); *only one* affected complex has 54 absent rows. The 45 other complexes have 72/72 joined numeric slots.

Interpretation: raw `null` must not be coerced into zero, and absent archived rows must not be treated as confirmed zero or same as raw `null`. Neither should be silently imputed for area-normalized descriptive analysis. Original N02 60-complex longitudinal source validity and earlier strict eligibility findings must be assessed from their respective archived collection audit; a missing cell in this three-field join alone is not an HTTP/API failure.

Generated `N02_165_미연결원인_검증결과_20261021.zip` includes `missing_slot_reconciliation.csv`, `by_complex.csv`, `summary.json`, and `README.md`. The 60-complex **current** V5 area-based KRW/sqm values remain exploratory, because historical denominators were not authenticated. V3 not published.