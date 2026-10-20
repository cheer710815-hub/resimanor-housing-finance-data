# N02: 60-complex 24-consecutive-calendar-month check (2026-10-20)

The original archived source CSVs were read again: 20 previous sources SHA-256 matched the manifest (20/20) and 40 additional `cohort_results.zip` files were read. Every complex/selected-field series had 24 **strictly consecutive valid calendar months** in `YYYYMM` format. There were zero invalid-month or skipped-month series, zero detected duplicate compound keys and zero other structural issues in this recheck.

| Source field | Valid n | Median first-three vs last-three % change | Missing/invalid calendar month series |
|---|---:|---:|---:|
| `pay` | 50 | +1.925659% | 0 |
| `cleanCost` | 50 | +2.242365% | 0 |
| `guardCost` | 47 | +1.859155% | 0 |

All values match the previously published internal v3 draft analysis; no statistical revision is warranted. Eight *locally reconstructed* synthetic checks of valid months, short/gapped periods, invalid month, null, zero, nonfinite amounts and repeated month passed. These were reconstructed from the source behavior in the execution environment and **were not a direct invocation of the checked-in GitHub unittest file**, so do not represent them as an Actions CI run. Archived CSV `result_json` used flat response objects; the raw QA reader handled that format. The audit outputs are distributed in the project working bundle `N02_60단지_연속24개월_재검증_20261020.zip` without raw API payload redistribution.

These structural and numerical checks do not validate official API monetary units or denominators. Existing Zenodo v2 DOI `10.5281/zenodo.23432629` remains unchanged. v3 is not published, pending official provider definitions and research coordinator's approval.
