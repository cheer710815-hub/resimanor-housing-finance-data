# Validation Report — 2026 H2 DSR Mortgage Limit Scenarios v1.0

Validation date: 2026-10-08

Dataset: [2026 H2 Korea Mortgage DSR Limit Scenario Dataset](https://doi.org/10.5281/zenodo.23231673)

## Scope and results

Checks performed against the CSV published in this GitHub repository:

| Check | Result |
| --- | --- |
| Data rows, excluding header | 160 |
| Columns | 16 |
| Distinct combinations of annual income, existing monthly-equivalent DSR debt service, actual mortgage rate, and region group | 160 |
| Duplicate combinations of those four scenario dimensions | 0 |
| Missing required dimension column names | 0 |
| Negative values in `dsr_based_new_mortgage_limit_krw` | 0 |

## Limitations

This is a structural validation, **not** an independent audit of every calculation or a certification of regulatory accuracy. It does not establish whether any lender will approve the calculated amount. The values are theoretical DSR-based scenarios; actual lending is subject to applicable policy, LTV and other caps, lender underwriting, and borrower circumstances.

The 0.75% non-metropolitan/non-regulated stress-rate value is a controlled analytical reference scenario, not a universal fixed official rate.

## Reproducibility

Source file: [resimanor_dsr_mortgage_limit_scenarios_2026_h2_v1.csv](./resimanor_dsr_mortgage_limit_scenarios_2026_h2_v1.csv)

Methodology: [METHODOLOGY.md](./METHODOLOGY.md)

Data dictionary: [DATA_DICTIONARY.md](./DATA_DICTIONARY.md)

Citation: [CITATION.cff](./CITATION.cff)

License: CC BY 4.0.

Version DOI: https://doi.org/10.5281/zenodo.23231673

Concept DOI: https://doi.org/10.5281/zenodo.23231672

## 2026-11-24 arithmetic reproduction

A separate arithmetic recheck was performed on all 160 published scenarios using the stated annuity present-value formula. Source CSV Git blob SHA: `4499098669fec31302000488b6e01276b7caf8c0`.

| Check | Result |
| --- | --- |
| Rows / columns | 160 / 16 |
| Duplicate scenario keys | 0 |
| Row-width mismatches | 0 |
| Annual DSR capacity mismatches | 0 |
| Remaining annual capacity mismatches | 0 |
| Assessment-rate mismatches (tolerance 1e-9 percentage points) | 0 |
| Mortgage principal mismatches after KRW rounding | 0 |
| Maximum rounded principal difference | KRW 0 |
| Limit-reduction mismatches exceeding KRW 1 rounding tolerance | 0 |

For each row, annual capacity = income × assumed DSR ceiling; remaining capacity = max(0, annual capacity − 12 × monthly-equivalent existing DSR burden); monthly assessment rate = (actual rate + scenario stress rate) / 1200; theoretical principal = (remaining capacity / 12) × (1 − (1 + monthly rate)^(-12 × term in years)) / monthly rate. Compare the rounded principal against the CSV; the reduction is compared against a zero-existing-burden scenario with otherwise identical inputs.

This arithmetic reproduction does not verify individual lender practices, applicable regulatory parameters, source-policy currency, or eligibility. In particular, 0.75% is a controlled reference assumption, not a universal current official rate. The original CSV, DOI and historical structural-validation record are unchanged. No new deposit or DOI was made.
