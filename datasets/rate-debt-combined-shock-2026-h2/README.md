# Resimanor Combined Mortgage-Rate + Existing-Debt Shock 2026 H2 — v0.1

## Research question

How much can the theoretical DSR-based mortgage limit shrink when two pressures occur at the same time:
1. the actual mortgage rate rises from 3.5% to 5.0%, and
2. existing monthly debt service increases from 0 to 500k or 1M KRW?

## Baseline

- actual mortgage rate: 3.5%
- existing monthly debt service: 0 KRW
- bank DSR limit: 40%
- term: 30 years
- repayment: equal principal + interest
- variable-rate mortgage
- 2026 H2 regional stress-rate assumptions from the Resimanor parent dataset

## Combined-shock results

### Shock A: rate 5.0% + monthly debt 500k KRW

Compared with the clean baseline of 3.5% + no existing monthly debt:

- Income 40M: limit falls by **46.2%–47.3%**
- Income 50M: **39.7%–41.0%**
- Income 60M: **35.4%–36.8%**
- Income 80M: **30.0%–31.5%**

Absolute losses range from approximately **97.38M KRW** to **170.80M KRW**.

### Shock B: rate 5.0% + monthly debt 1M KRW

- Income 40M: limit falls by **78.5%–78.9%**
- Income 50M: **65.5%–66.3%**
- Income 60M: **56.9%–57.9%**
- Income 80M: **46.2%–47.3%**

Absolute losses range from approximately **165.52M KRW** to **256.47M KRW**.

## Interpretation

The combined effect is materially larger than looking at a rate increase or existing debt in isolation.

Lower-income scenarios lose a larger share of their baseline borrowing capacity because a fixed monthly debt-service amount consumes a larger portion of their annual DSR capacity.

Higher-income scenarios can still show larger losses in absolute KRW terms because their baseline mortgage limits are higher.

## Important limitation

This is a standardized scenario comparison, not a bank approval estimate. Actual approval may differ due to LTV, product caps, recognized income, debt-type treatment and lender underwriting.

## Source

Derived from:
`datasets/dsr-mortgage-limit-2026-h2/resimanor_dsr_mortgage_limit_scenarios_2026_h2_v1.csv`

## License

CC BY 4.0.

## DOI policy

No standalone DOI at v0.1.
