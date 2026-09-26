# SchemaFinder Submission Pack

Verified submission form:
https://schemafinder.com/submit

Prepared: 2026-09-26

## Dataset 1 — Korea Stress DSR Mortgage Limits by Income 2026

Name:
Korea Stress DSR Mortgage Limits by Income 2026

Source URL:
https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/income_mortgage_limits.csv

Description:
Open South Korean housing-finance reference data comparing estimated mortgage limits by annual income under multiple stress-DSR screening-rate scenarios. Includes DSR limit, actual mortgage rate, term, repayment method, base date, and canonical methodology source.

Publisher:
Resimanor

Category:
Housing

Format:
CSV

Geographic scope:
South Korea

Update frequency:
Updated when stress-DSR policy assumptions or reference scenarios change.

Documentation URL:
https://resimanor.com/housing-finance-dsr-data/

Tags:
housing finance, mortgage, south korea, stress dsr, dsr, mortgage limit, home buying, lending

Access:
Open

Columns:
- annual_income_krw — integer
- scenario — string
- screening_rate_pct — number
- estimated_mortgage_limit_krw — integer
- dsr_limit_pct — number
- actual_mortgage_rate_pct — number
- mortgage_term_years — integer
- repayment_method — string
- base_date — date
- canonical_source — string

Attribution:
Resimanor
https://resimanor.com/

---

## Dataset 2 — Korea Mortgage Limits by Existing Credit Debt 2026

Name:
Korea Mortgage Limits by Existing Credit Debt 2026

Source URL:
https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/credit_debt_mortgage_limits.csv

Description:
Open South Korean housing-finance reference data showing how existing credit-loan balances and annual debt service affect remaining mortgage capacity under a stress-DSR scenario. Includes income, DSR limit, debt-service assumptions, mortgage screening rate, term, and estimated mortgage limit.

Publisher:
Resimanor

Category:
Housing

Format:
CSV

Geographic scope:
South Korea

Update frequency:
Updated when stress-DSR policy assumptions or reference scenarios change.

Documentation URL:
https://resimanor.com/housing-finance-dsr-data/

Tags:
housing finance, mortgage, south korea, stress dsr, credit loan, debt service, mortgage limit, lending

Access:
Open

Columns:
- annual_income_krw — integer
- dsr_limit_pct — number
- credit_loan_balance_krw — integer
- credit_loan_rate_pct — number
- credit_dsr_maturity_years — integer
- annual_existing_debt_service_krw — integer
- annual_mortgage_capacity_remaining_krw — integer
- mortgage_screening_rate_pct — number
- mortgage_term_years — integer
- repayment_method — string
- estimated_mortgage_limit_krw — integer
- base_date — date
- canonical_source — string

Attribution:
Resimanor
https://resimanor.com/
