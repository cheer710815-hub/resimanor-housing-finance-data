# Resimanor Mortgage Rate Shock × DSR Mortgage Limit 2026 H2 — v0.1

## Research question

How much does the theoretical DSR-based mortgage limit fall when the actual mortgage rate rises from 3.5% to 5.0%, under the same income and debt conditions?

## Base assumptions

- Bank DSR limit: 40%
- Term: 30 years
- Repayment: equal principal + interest
- Variable-rate mortgage
- 2026 H2 stress-rate assumptions from the existing Resimanor scenario dataset
- This is a DSR-based theoretical limit, not an approval guarantee.

## Main result

Across all 40 matched income × existing-debt × region scenarios, the average theoretical limit loss between 3.5% and 5.0% actual mortgage rates was approximately **38.14 million KRW**, or **14.8%**.

For borrowers with no existing monthly debt service:

- Income 40M KRW:
  - capital/regulatory: 210.95M → 181.71M KRW, **-29.24M**
  - non-capital/non-regulatory: 271.04M → 228.48M KRW, **-42.56M**
- Income 50M KRW:
  - capital/regulatory: 263.68M → 227.14M KRW, **-36.55M**
  - non-capital/non-regulatory: 338.79M → 285.60M KRW, **-53.20M**
- Income 60M KRW:
  - capital/regulatory: 316.42M → 272.57M KRW, **-43.85M**
  - non-capital/non-regulatory: 406.55M → 342.72M KRW, **-63.84M**
- Income 80M KRW:
  - capital/regulatory: 421.90M → 363.42M KRW, **-58.47M**
  - non-capital/non-regulatory: 542.07M → 456.96M KRW, **-85.12M**

## Interpretation

The percentage reduction is fairly stable within each region assumption because the same DSR structure is applied proportionally, but the absolute KRW loss grows as the baseline borrowing capacity rises.

This means higher-income borrowers can lose more borrowing capacity in absolute terms when mortgage rates rise, even when their proportional reduction is similar.

## Important limitation

Actual mortgage approval can differ due to LTV, policy caps, lender underwriting, recognized income, debt-type treatment and product-specific rules.

## Source

Derived from:
`datasets/dsr-mortgage-limit-2026-h2/resimanor_dsr_mortgage_limit_scenarios_2026_h2_v1.csv`

## License

CC BY 4.0.

## Release decision

No standalone DOI at v0.1. This is a scoped derivative dataset.
