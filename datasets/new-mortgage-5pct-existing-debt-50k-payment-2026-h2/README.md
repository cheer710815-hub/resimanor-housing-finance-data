# Resimanor New Mortgage 5% + Existing Debt Service 500k KRW — Monthly Payment Analysis 2026 H2

## Research question

If a borrower already pays 500,000 KRW per month in principal and interest on existing DSR-counted debt, how much additional monthly repayment burden arises when taking a new variable-rate mortgage at 5.0%?

## Assumptions

- New mortgage actual interest rate: 5.0%
- New mortgage term: 30 years
- Repayment method: equal principal + interest
- Existing monthly debt service: 500,000 KRW
- Bank DSR limit: 40%
- Regional stress-rate assumptions follow the Resimanor 2026 H2 scenario dataset
- New mortgage amount uses the existing DSR-based theoretical limit for each income × region scenario

## Main results

Total monthly debt service after adding the new mortgage:

- Income 40M KRW:
  - capital/regulatory: about 1.11M KRW
  - non-capital/non-regulatory: about 1.27M KRW
- Income 50M KRW:
  - capital/regulatory: about 1.35M KRW
  - non-capital/non-regulatory: about 1.57M KRW
- Income 60M KRW:
  - capital/regulatory: about 1.60M KRW
  - non-capital/non-regulatory: about 1.88M KRW
- Income 80M KRW:
  - capital/regulatory: about 2.09M KRW
  - non-capital/non-regulatory: about 2.49M KRW

The additional burden above the existing 500,000 KRW is simply the new mortgage's monthly repayment, ranging from about 610,000 KRW to 1.99M KRW across the eight scenarios.

## Interpretation

This dataset answers a monthly cash-flow question rather than only a borrowing-limit question.

The DSR-based mortgage amount is calculated from the scenario dataset; the monthly mortgage payment is then calculated at the actual 5.0% mortgage rate over 30 years with equal principal-and-interest repayment.

## Important limitation

These are standardized calculations, not lender approval quotes. Actual payment schedules and approved amounts can differ due to product structure, LTV, recognized income, debt treatment and lender underwriting.

## Source

Derived from:
`datasets/dsr-mortgage-limit-2026-h2/resimanor_dsr_mortgage_limit_scenarios_2026_h2_v1.csv`

## License

CC BY 4.0.
