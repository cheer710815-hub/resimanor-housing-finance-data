# N02 matched-sample sign-reversal: incremental composition audit (2026-10-20)

The validated **45 common-valid complexes** had a `cleanCost` response-field change median of **-2.0949505%**. Five further complexes are eligible for cleaning, but are excluded by the `pay` or `guardCost` eligibility rule; each has a positive cleaning-field percentage change. Enumerated all **32 subsets** of these five to test whether reversal arises from one outlier or systematic inclusion rules.

| Additional positive cases | Number of combinations | Included complexes | Median `cleanCost` change |
|---:|---:|---:|---:|
| 0 | 1 | 45 | -2.094951% |
| 1 | 5 | 46 | -0.788085% |
| 2 | 10 | 47 | +0.518781% |
| 3 | 10 | 48 | +1.219114% |
| 4 | 5 | 49 | +1.919447% |
| 5 | 1 | 50 | +2.242365% |

At a given subset size, the median was **identical across all possible subsets**, since each added change exceeds the central observations of the 45-case distribution. Thus the sign changes after **any two of five** excluded cases are added back. Conversely, removing any single complex from the 50-case analysis retains a positive cleaning-field median; across 50 leave-one-out runs, the median range is **+1.919447% to +2.565283%**. The sign flip is a **composition / order-statistic sensitivity**, not the effect of one particular outlier.

Based on actual per-complex change CSVs in the local working archive, with all 32 subset and 50 leave-one-out results packaged in `N02_청소비_5개단지_단계별_영향도_20261020.zip`. These results are not tests of causation or population inference. Original API fields have unverified official monetary units and area denominators. N02 Zenodo v2 DOI `10.5281/zenodo.23432629` unchanged; v3 remains unpublished.