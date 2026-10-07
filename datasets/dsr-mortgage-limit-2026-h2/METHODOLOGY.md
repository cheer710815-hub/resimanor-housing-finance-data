# Methodology

## Purpose
To isolate how annual income, existing DSR debt-service burden, mortgage rate, and regional stress-DSR assumptions change remaining capacity for a new mortgage.

## Calculation
1. Annual DSR capacity = annual income × 40%.
2. Remaining annual capacity = max(0, annual DSR capacity − monthly-equivalent existing DSR burden × 12).
3. DSR assessment rate = actual mortgage rate + scenario stress rate.
4. Monthly remaining capacity = remaining annual capacity ÷ 12.
5. Mortgage limit = present value of 360 equal monthly payments at the DSR assessment rate.

## Scenario grid
4 incomes × 5 existing-debt-service values × 4 mortgage rates × 2 regional scenarios = 160 rows.

## Stress-rate treatment
The metropolitan/regulatory scenario uses 3.0%. The 0.75% non-metropolitan/non-regulated value is deliberately a controlled analytical reference (1.5% × 50%), not a claim that 0.75% is the universally fixed official rate for every applicable mortgage.

## Limitations
Actual lending can be lower because of LTV, housing-price mortgage caps, debt-type-specific DSR recognition, recognized income, loan product structure, maturity rules, and lender underwriting. Existing debt service in this dataset is an analytical monthly-equivalent DSR burden rather than a claim that a consumer's raw monthly payment maps one-to-one to regulatory DSR.
