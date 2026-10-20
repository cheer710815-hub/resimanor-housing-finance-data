# N02 v3 — Early-stage apartment common-cost component trajectories in South Korea: an exploratory 60-complex reanalysis

**PREPUBLICATION DRAFT — no new Zenodo publication or DOI has been issued.**
Date: 2026-10-19. Existing study series: [N02 v2](https://doi.org/10.5281/zenodo.23432629).

## Abstract

This exploratory study re-examines monthly public K-apt API cost-component responses for 60 purposively selected complexes, of which 40 extend a previously published 20-complex cohort. Each complex has 24 months and 17 API service calls per month, totaling 24,480 archived successful responses. Three numeric API fields — `pay`, `cleanCost`, and `guardCost` — were analysed separately; their official units/area denominators have not yet been confirmed. Under a strict condition requiring positive numeric values for each of the first three and last three observed months, the medians of complex-level changes were +1.93% (n=50), +2.24% (n=50), and +1.86% (n=47). Descriptive 20,000-resample bootstrap intervals of these sample medians were [-2.94%, +3.93%], [-4.31%, +4.70%], and [-3.17%, +3.93%]. Each interval contains zero; moreover, the nonprobability selection means these are not population confidence intervals or evidence of nationwide trends.

## Research materials and integrity

The prior 20-complex source files match a frozen SHA-256 archive manifest (20/20 matched). The newer 40-complex source files were separately audited. Across the 60 complexes, 24 months x 17 API methods = 24,480 successful responses with no missing/duplicate complex-month-operation keys in the archived CSVs. A successful API response is not proof of a nonmissing amount or official field semantics. Across 35 candidate monetary JSON keys, 1,295 null value cells were observed; null values are kept distinct from numeric zero.

## Reproducible field-level analysis

For each of the three API fields and each complex, the first and last three *chronologically ordered reporting months* were extracted. If any of those six amounts is null, nonnumeric, missing, zero, or negative, that complex is excluded **only for that field**. Otherwise calculate 100 x [(last-three arithmetic mean / first-three arithmetic mean) - 1], then take the unweighted median of valid complex changes. This comparison does not establish that the first reporting month equals the actual commencement of occupancy.

| Field | Older 20 median (valid n) | Added 40 median (valid n) | Combined 60 median (valid n) | Apartments-only 58 median (valid n) |
|---|---:|---:|---:|---:|
| `pay` | -8.00% (16) | +2.68% (34) | +1.93% (50) | +1.95% (49) |
| `cleanCost` | +0.30% (16) | +2.24% (34) | +2.24% (50) | +1.92% (49) |
| `guardCost` | -0.76% (16) | +1.86% (31) | +1.86% (47) | +1.51% (46) |

The previous new-40 interim report listed strict counts 28/28/27; the unified archived-source rerun instead reproduces 34/34/31. The earlier intermediate calculation code is unavailable, so the precise discrepancy cause remains unknown. The superseded counts should not be quoted as final.

## Exploratory bootstrap uncertainty

For each valid field's observed complex-level percentage differences, resample complexes with replacement **20,000 times** using a fixed random seed **20261019**, calculate the sample median for each resample, and extract the 2.5th and 97.5th percentiles.

| Field | Valid n | Sample median | Exploratory bootstrap percentile interval |
|---|---:|---:|---|
| `pay` | 50 | +1.93% | -2.94% to +3.93% |
| `cleanCost` | 50 | +2.24% | -4.31% to +4.70% |
| `guardCost` | 47 | +1.86% | -3.17% to +3.93% |

All three resampling intervals include zero. **These intervals quantify within-observed-sample variability under bootstrap resampling, not national 95% confidence intervals.** No significance or causal effect can be inferred from interval inclusion/exclusion alone, especially for the purposefully selected sample. The older20 and added40 have different composition and possibly calendar windows; do not interpret subgroup differences as confirmed cohort effects.

## Sampling, sensitivity and missingness

The added 40 were purposively distributed eight each across five size strata, improving sample size balance but not geographic or temporal representativeness. Among all 60, the corresponding stratum counts are 10/20/10/10/10. Two mixed-use complexes were removed in the apartment-only sensitivity analysis; the three median signs remained positive, without resolving compositional confounding.

For the added40, eligible counts for `pay`, `cleanCost`, and `guardCost` are 34/34/31, with six exclusions involving null for each field and three additional zero-related exclusions for security. The older20 contribute 16 valid complexes per field.

### Field-specific exclusions and potential selection bias (audit 2026-10-20)

The strict six-positive-endpoint rule excludes different complexes for different response fields. The 60-complex data yield the following eligibility breakdown:

| Source response field | Eligible complexes | Null/nonnumeric endpoint exclusion | Zero/nonpositive endpoint exclusion | Excluded complexes (rate) |
|---|---:|---:|---:|---:|
| `pay` | 50 | 8 | 2 | 10 / 60 (16.7%) |
| `cleanCost` | 50 | 8 | 2 | 10 / 60 (16.7%) |
| `guardCost` | 47 | 8 | 5 | 13 / 60 (21.7%) |

Across all three outcomes, the **33 excluded complex-field observations** belong to **15 unique complexes**, of which **9 are ineligible for all three fields** and **6 are ineligible for only one field**; none are excluded for exactly two fields. Thus the three reported field-level medians do **not** necessarily summarize identical sets of complexes.

For the original20, each field excludes 4 / 20 complexes (20.0%). In the additional40, `pay` and `cleanCost` each exclude 6 / 40 (15.0%), whereas `guardCost` excludes 9 / 40 (22.5%). The differing eligibility rates and overlapping exclusions raise a **possible selection-bias limitation**, but neither its direction nor magnitude can be inferred without valid endpoint values for excluded complexes. Missing or zero values must not be imputed as actual absence of incurred costs; no missing-at-random assumption is supported by this dataset. Small region-by-component cells should not be presented as population ranking: for the apartment-only regional breakdown, 37 of 48 region-field combinations have fewer than five valid complexes.

Region labels and approval dates must be time-aligned; preserve historical location designations and distinguish them from current display labels. K-apt updates can also change recent-month displayed statistics after the archived collection time; this study does not establish whether any specific archived row was subsequently revised.


### Identical-complex sensitivity: 45 common eligible complexes (2026-10-20)

Because the three primary medians were calculated from different field-specific eligibility sets, we additionally restricted all three to the **same 45 complexes** with positive first/last three-month values for every field.

| Source field | Initial field-specific median (n) | Common 45-complex median | Difference |
|---|---:|---:|---:|
| `pay` | +1.93% (50) | +1.90% | -0.02 percentage points |
| `cleanCost` | +2.24% (50) | **-2.09%** | **-4.34 percentage points** |
| `guardCost` | +1.86% (47) | +1.17% | -0.69 percentage points |

**Important:** the `cleanCost` median **changes sign** when restricting to the same 45 eligible complexes. It would be misleading to describe its upward trend as robust to sample composition. This is a field-eligibility sensitivity result, not a statistical population estimate; it does not establish a national cost trend or correct unverified government source units. See [matched sample source audit](./V3_COMMON_45_COMPLEX_SENSITIVITY_20261020.md).


#### Why does `cleanCost` reverse sign in the common sample? (2026-10-20)

The original field-eligible `cleanCost` group contains 50 complexes. Exactly five complexes are valid for `cleanCost` but fail at least one **other** field's eligibility rule and therefore leave the three-field matched sample: A10022707 (+32.93%), A10022793 (+6.86%), A10022821 (+16.84%), A10023233 (+14.72%), and A10023329 (+67.99%). All five have positive `cleanCost` change. Four fail the `guardCost` positive-endpoint rule; A10023329 fails the `pay` positive-endpoint rule. These are field-eligibility exclusions, **not missing `cleanCost` amounts**.

The full 50 `cleanCost`-valid complexes split into 27 positive and 23 negative changes (median +2.242365%). The 45 matched complexes split into 22 positive and 23 negative changes (median -2.094951%). Accordingly, the median sign reversal can be explained directly by five excluded positive-change cases and the shifted median order statistic. This is a **composition effect** and does not establish which sample is representative or the cause of the underlying changes. Audit reference: [five-complex composition check](./V3_CLEANCOST_FIVE_COMPLEX_EXCLUSION_20261020.md).

## Limits and release hold

1. The 35 observed API amount fields' **official monetary units, denominators and aggregation hierarchy remain insufficiently documented**. The public-data service desk confirmed forwarding the technical request to the Ministry on 2026-10-19 but provided no technical field definitions. Do not label the source numeric values as monthly KRW totals, KRW/m² or household costs; never add overlapping 17 API methods as if they were independent total expenses.
2. Missingness, 0-value interpretation, seasonality, inflation, changes to occupancy, contracts, calendar cohorts, and area-standardization remain unresolved.
3. Results are exploratory and may not be generalized to nationwide apartment maintenance-cost change.
4. Government-source revision-date alignment, official field definitions and rights, full editorial cross-check and the research coordinator's explicit approval are prerequisites to issuing a new Zenodo version. The existing N02 v2 DOI is retained without modification.


## Final editorial integrity checks (2026-10-19)

**Quality assurance versus financial meaning.** The 24,480-record count establishes completeness of the *archived API response grid*, not independently confirmed accuracy of the billed amounts. The 1,295 nulls are **JSON monetary-field cells across 35 candidate fields**, not 1,295 failed API requests, missing months, or complexes. Comparisons are complete-case/positive-only at each individual cost field; reporting their positive median alone would obscure the 10 / 10 / 13 exclusions in `pay`, `cleanCost`, and `guardCost` respectively.

**Uncertainty interpretation.** The 20,000-resample percentile intervals condition on the already selected, eligible complexes. They omit uncertainty arising from purposive cohort selection, missing or zero-valued records, regional/time heterogeneity, source reporting corrections and unknown units. Zero falling inside an interval is descriptive evidence of instability under this reweighting, **not** a formal acceptance of a null hypothesis or proof that real costs were unchanged.

**Terminology constraint.** Until the official API schema is supplied, identify outputs as changes in the `pay`, `cleanCost`, and `guardCost` *response-field values*; do not call them a complete management fee, a national increase, or an inflation-adjusted per-area cost. No official technical response has yet confirmed those terms.

**Current release gate:** HOLD — await verified provider schema/units/denominators, then update field definitions and conduct line-by-line source review before the owner's approval. Do not publish Zenodo v3 from this draft merely because the structural QA and bootstrap runs passed.

## Source audit references

- [60-source reproduction](./V3_60_SOURCE_REPRODUCTION_20261019.md)
- [17-method full audit](./QA_FULL_60_METHODS_EXECUTED_20261019.md)
- [Building-type sensitivity](./TYPE_SENSITIVITY_20261019.md)
- [Exploratory bootstrap audit](./V3_BOOTSTRAP_SENSITIVITY_20261019.md)
- [Response field unit audit](./API_17_ENDPOINT_FIELD_UNIT_AUDIT.md)
- [Field eligibility correction](./V3_REGION_AND_ELIGIBILITY_CORRECTION_20261019.md)
- [60-complex exclusion and overlap audit](./V3_60_FIELD_EXCLUSION_OVERLAP_20261020.md)
