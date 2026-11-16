# Data Dictionary — Mortgage Rate Shock × DSR Limit 2026 H2 v0.1

| Field | Meaning |
|---|---|
| annual_income_krw | Annual recognized income |
| existing_monthly_debt_service_krw | Existing monthly debt-service assumption |
| region_group | Stress-rate regional scenario |
| mortgage_limit_at_3_5pct_krw | Theoretical DSR mortgage limit at 3.5% actual mortgage rate |
| mortgage_limit_at_5_0pct_krw | Theoretical DSR mortgage limit at 5.0% actual mortgage rate |
| limit_loss_krw | Difference between the two limits |
| limit_loss_pct | Percentage loss relative to the 3.5% limit |

## Table scope

The existing v0.1 comparison CSV contains 8 zero-existing-debt illustrative rows. `resimanor-mortgage-rate-shock-limit-2026-h2-40pairs-SUPPLEMENTAL.csv` contains all 40 matched income × existing-debt-service × region comparisons used for the headline mean. Both share the 7 fields documented above. The percentage column is rounded to 2 decimal places.
