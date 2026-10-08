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
