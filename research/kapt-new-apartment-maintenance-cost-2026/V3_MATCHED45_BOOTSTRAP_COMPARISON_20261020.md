# N02 exploratory bootstrap comparison: field-specific sample vs common 45 complexes (2026-10-20)

Independent Python standard-library analysis on archived eligible complex-level percentages (60-complex eligibility CSV and matched 45-complex changes CSV). For each of six field/sample combinations, drew 20,000 with-replacement bootstrap samples with `random.Random(20261020)`. Reported empirical 2.5% and 97.5% order statistics. The random seed and algorithm here are **different from the original 2026-10-19 bootstrap**, so minor percentile differences are expected; underlying descriptive medians are unchanged.

| Field | Cohort | Valid n | Median % | Exploratory 95% bootstrap interval % |
|---|---|---:|---:|---|
| pay | Field-specific | 50 | +1.9257 | [-2.9928, +3.9297] |
| pay | All-three-valid common | 45 | +1.9024 | [-2.9424, +2.9350] |
| cleanCost | Field-specific | 50 | +2.2424 | [-4.3149, +4.7026] |
| cleanCost | All-three-valid common | 45 | **-2.0950** | **[-5.3550, +3.7087]** |
| guardCost | Field-specific | 47 | +1.8592 | [-3.1661, +3.9333] |
| guardCost | All-three-valid common | 45 | +1.1665 | [-3.1661, +3.3930] |

**Interpretation:** Restricting to exactly the same complexes flips the cleaning-field sample median sign. But both the 50-case and 45-case exploratory intervals contain zero; this does not establish robust field-value increase or decrease. Intervals reflect with-replacement resampling conditional on purposive selected complexes and eligible field observations; they are **not national population confidence intervals** and do not account for selection, missingness, timing, reporting changes, unknown monetary units or denominators.

Local result ZIP: `N02_동일45단지_부트스트랩_불확실성_20261020.zip` (comparison CSV and runnable Python script). Original source records are not redistributed. Zenodo v2 `10.5281/zenodo.23432629` preserved; v3 unpublished.
