# Methodology — Mortgage Rate Shock × DSR Mortgage Limit 2026 H2 v0.1

## Cohort

The source dataset contains 160 scenarios formed from:
- annual income: 40M / 50M / 60M / 80M KRW
- existing monthly debt service: 0 / 300k / 500k / 700k / 1M KRW
- actual mortgage rate: 3.5% / 4.0% / 4.5% / 5.0%
- region assumptions: capital/regulatory and non-capital/non-regulatory

## Comparison

For each fixed income × existing-debt × region combination, the DSR-based theoretical mortgage limit at 3.5% actual rate was compared with the limit at 5.0%.

This produces 40 matched comparisons.

## Derived fields

- limit loss = limit at 3.5% - limit at 5.0%
- loss rate = limit loss / limit at 3.5%

## Main summary

Average across 40 matched comparisons:
- absolute loss: approximately 38.14M KRW
- proportional loss: approximately 14.8%

## Limits

This is not a lender quote or approval result. It is a standardized stress-DSR scenario comparison.
