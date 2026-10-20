# N02 updated numeric parser: 60-source rerun — 2026-10-20

The archived raw CSVs were read again after modifying the parser to reject NaN and positive/negative infinity. Twenty prior source entries were extracted according to the original `source_manifest.csv` and independently SHA-256 compared: **20/20 matched**. The added 40 `cost_raw_long.csv` files came from the saved `cohort_results.zip`. A total of **24,480 distinct complex/month/API keys**, with **zero duplicate keys and zero structural issues**, was found. No NaN or infinite raw values were detected in the three analyzed endpoint fields.

| Cohort | pay (eligible n; median) | cleanCost (eligible n; median) | guardCost (eligible n; median) |
|---|---|---|---|
| Previous 20 | 16; -7.99783% | 16; +0.29851% | 16; -0.76408% |
| Additional 40 | 34; +2.67726% | 34; +2.24237% | 31; +1.85916% |
| All 60 | 50; **+1.92566%** | 50; **+2.24237%** | 47; **+1.85916%** |

All values reproduce previously documented accepted results. All-60 `null_or_nonnumeric` exclusions: 8 per field; `zero_or_nonpositive` exclusions: 2/2/5 for pay/cleanCost/guardCost. The local downloadable archive `N02_60단지_수정코드_최종재현_20261020.zip` includes the actual independent rerun program, eligible-status CSV, issues.csv, hash evidence and summary.csv, but does not redistribute the raw source payloads.

This is a source-integrity and descriptive numeric-statistics check, not an official field-unit validation or population inference. **No v3 DOI was issued.** Preserve v2 DOI `10.5281/zenodo.23432629` pending Ministry specification and owner approval.
