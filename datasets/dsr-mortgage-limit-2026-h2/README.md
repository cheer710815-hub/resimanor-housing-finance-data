# 2026 H2 Korea Mortgage DSR Limit Scenario Dataset

Version 1.0 · Resimanor · 2026-10-07

This directory contains 160 controlled scenarios estimating the DSR-based theoretical limit for an additional Korean home mortgage.

## Variables
- Annual income: KRW 40m, 50m, 60m, 80m
- Existing DSR debt-service burden, monthly equivalent: KRW 0, 300k, 500k, 700k, 1m
- Actual mortgage rate: 3.5%, 4.0%, 4.5%, 5.0%
- Bank borrower-level DSR ceiling assumption: 40%
- Term: 30 years
- Repayment: equal principal and interest
- Variable-rate mortgage baseline
- Regional scenarios: metropolitan/regulatory area 3.0% stress rate; non-metropolitan/non-regulated 0.75% controlled reference scenario

## Key interpretation
The output is a **DSR-based theoretical calculated limit**, not an actual bank approval amount.

The 0.75% value is a controlled reference scenario corresponding to 1.5% × 50%. It must not be interpreted as a universal fixed official stress rate for every non-metropolitan/non-regulated mortgage in 2026 H2.

## Key finding
At a 4.0% mortgage rate under the metropolitan/regulatory 3.0% stress-rate scenario:
- KRW 50m income + zero existing monthly-equivalent DSR burden ≈ KRW 250.51m
- KRW 80m income + KRW 1m existing monthly-equivalent DSR burden ≈ KRW 250.51m

The higher-income borrower can therefore have the same remaining DSR capacity when existing debt service absorbs the income advantage.

## Files
- resimanor_dsr_mortgage_limit_scenarios_2026_h2_v1.csv
- METHODOLOGY.md
- DATA_DICTIONARY.md
- RELEASE_NOTES.md
- MEDIA_RESEARCH_SUMMARY.md
- LICENSE.md

## License
CC BY 4.0 for Resimanor's original dataset and documentation. Third-party regulations and source materials retain their own terms.
