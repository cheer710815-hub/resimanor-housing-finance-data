# N02: decomposition of the matched-sample `cleanCost` sign reversal — 2026-10-20

Input is the archived 60-complex 180-row field-level eligibility and per-complex change table. There are 50 `cleanCost`-eligible complexes; precisely 45 are eligible on all three `pay`, `cleanCost`, and `guardCost` fields.

| Valid for cleaning but not all three | Cleaning response-field change | Other-field exclusion |
|---|---:|---|
| A10022707 | +32.93% | guardCost, zero/nonpositive endpoint |
| A10022793 | +6.86% | guardCost, zero/nonpositive endpoint |
| A10022821 | +16.84% | guardCost, zero/nonpositive endpoint |
| A10023233 | +14.72% | guardCost, zero/nonpositive endpoint |
| A10023329 | +67.99% | pay, zero/nonpositive endpoint |

All five are positive. The full 50-case cleaning group has 27 positive versus 23 negative changes and median **+2.242365%**. The matched 45-case group has 22 positive versus 23 negative changes and median **-2.094951%**. The 5 removed cases are a nonrandom subset conditional on other-field eligibility; removing them shifts the central order statistic and changes the sign. This is a documented *compositional sensitivity*, not a numerical error or causal explanation for cleaning charges.

The 35 candidate field units and area denominator still lack official ministry confirmation. Do not conclude that monthly KRW or KRW/m² cleaning charges increased or declined nationally. Existing Zenodo v2 unchanged, v3 unpublished.
