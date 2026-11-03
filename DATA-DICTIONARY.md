# Data Dictionary — 2026 Stress DSR Mortgage Reference Data

**Publisher:** Resimanor Data Project  
**Repository:** https://github.com/cheer710815-hub/resimanor-housing-finance-data  
**Canonical data center:** https://resimanor.com/housing-finance-dsr-data/  
**Documentation checked:** 2026-11-03  
**Reference snapshot:** 2026-09-18  
**License:** CC BY 4.0 (see repository licensing terms)

This dictionary describes the existing **mortgage example CSVs and JSON**, not lender credit decisions or live regulatory thresholds. Values are illustrative outputs under the recorded assumptions.

## 1. `income_mortgage_limits.csv`

- **Row grain:** one annual-income × mortgage-rate scenario.
- **Key:** (`annual_income_krw`, `scenario`).

| Column | Type | Definition | Unit / interpretation |
| --- | --- | --- | --- |
| `annual_income_krw` | integer | Assumed borrower annual income. | KRW |
| `scenario` | string | Scenario label identifying screening assumptions. | `no_stress`, `regional_example`, `capital_regulated_example` |
| `screening_rate_pct` | number | Interest rate used to calculate the DSR mortgage capacity in the example. | Percent per annum |
| `estimated_mortgage_limit_krw` | integer | Modelled mortgage principal for the specified assumptions. | KRW, illustrative |
| `dsr_limit_pct` | number | Assumed maximum debt-service share of annual income. | Percent |
| `actual_mortgage_rate_pct` | number | Assumed contractual mortgage interest rate, separately from the screening rate. | Percent per annum |
| `mortgage_term_years` | integer | Assumed mortgage term. | Years |
| `repayment_method` | string | Amortisation formula. | `equal_principal_interest` = equal monthly total principal-and-interest payments |
| `base_date` | date string | Reference date of published assumptions. | `YYYY-MM-DD` |
| `canonical_source` | URL string | Original explanatory data page. | HTTPS URL |

## 2. `credit_debt_mortgage_limits.csv`

- **Row grain:** one existing-credit-loan balance under a specified annual-income and mortgage scenario.
- **Key in current example set:** (`annual_income_krw`, `credit_loan_balance_krw`).

| Column | Type | Definition | Unit / interpretation |
| --- | --- | --- | --- |
| `annual_income_krw` | integer | Assumed annual borrower income. | KRW |
| `dsr_limit_pct` | number | Maximum annual debt service as a share of income. | Percent |
| `credit_loan_balance_krw` | integer | Outstanding existing credit-loan principal in the scenario. | KRW |
| `credit_loan_rate_pct` | number | Interest rate assumption for the existing credit loan. | Percent per annum |
| `credit_dsr_maturity_years` | integer | Assumed maturity used for credit-loan DSR treatment. | Years; an assumption, not proof of each lender's policy |
| `annual_existing_debt_service_krw` | integer | Modelled annual existing-debt service deducted from available DSR capacity. | KRW/year |
| `annual_mortgage_capacity_remaining_krw` | integer | Annual debt-service amount remaining for the new mortgage. | KRW/year |
| `mortgage_screening_rate_pct` | number | Mortgage screening interest-rate assumption. | Percent per annum |
| `mortgage_term_years` | integer | Assumed new mortgage maturity. | Years |
| `repayment_method` | string | Mortgage amortisation formula. | `equal_principal_interest` |
| `estimated_mortgage_limit_krw` | integer | Modelled new mortgage principal compatible with the assumptions. | KRW |
| `base_date` | date string | Reference date of published assumptions. | `YYYY-MM-DD` |
| `canonical_source` | URL string | Original explanatory data page. | HTTPS URL |

## 3. `stress_dsr_mortgage_examples_2026.json`

| Property / path | JSON type | Definition |
| --- | --- | --- |
| `name` | string | Dataset title. |
| `base_date` | string | `YYYY-MM-DD` reference snapshot date. |
| `canonical_source` | string | URL for the model assumptions and data. |
| `assumptions.dsr_limit_pct` | number | Assumed DSR limit, percent. |
| `assumptions.actual_mortgage_rate_pct` | number | Assumed contract interest rate, percent per annum. |
| `assumptions.mortgage_term_years` | number | Mortgage maturity, years. |
| `assumptions.repayment_method` | string | `equal_principal_interest` as defined above. |
| `income_scenarios[]` | array of objects | Income-specific summaries with `annual_income_krw` and `no_stress`, `regional_example`, `capital_regulated_example` estimated mortgage limits, all in KRW. |
| `credit_debt_scenarios_for_income_80000000[]` | array of objects | Scenarios for KRW 80 million income: `credit_loan_balance_krw` and `estimated_mortgage_limit_krw`, both KRW. |

## Important interpretation and citation rules

1. These are reproducible **illustrative scenarios**, not a loan eligibility decision, lender commitment, actual available mortgage, or automatically applicable current regulatory limit.
2. `screening_rate_pct` and `actual_mortgage_rate_pct` deliberately describe different rate concepts.
3. Apply the mortgage product's current effective rules and lender-specific risk assessment before using scenarios for an actual transaction.
4. The JSON's `income_scenarios` numbers are **KRW amounts**, not percentages or thousands of won.
5. Prefer the canonical [data page](https://resimanor.com/housing-finance-dsr-data/) and [METHODOLOGY.md](METHODOLOGY.md); cite the specific archived release only if its contents/version have been checked.
6. This file does not imply that the original 2026-09-18 reference dataset has been amended or that prior DOI deposits have been replaced.
