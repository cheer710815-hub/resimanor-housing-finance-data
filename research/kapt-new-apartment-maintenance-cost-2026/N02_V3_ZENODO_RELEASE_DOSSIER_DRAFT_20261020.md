# N02 v3 — Zenodo release dossier (DRAFT ONLY)

**Prepared: 2026-10-20. NOT APPROVED FOR PUBLICATION.**
**Existing N02 v2 DOI:** https://doi.org/10.5281/zenodo.23432629. A future v3 would be a new version of this record sequence, not a parallel independent deposit.

## Suggested title (English)

Early-Stage Apartment Common-Maintenance API Field Trajectories in South Korea: A 60-Complex Replication and Sample-Composition Sensitivity Study

## Suggested Korean title

전국 60개 공동주택 단지의 공용관리비 관련 API 응답값 변화와 표본 구성 민감도 분석: 24개월 재현성 검증

The term “nationwide” in the Korean title refers to coverage of selected complexes across multiple regions, **not a representative national sample**; remove or narrow this term if a final regional-coverage audit does not establish geographically distributed coverage.

## Short public-facing description (conditional draft)

This exploratory, nonprobability-sample study analyzes 24 months of archived K-apt common-maintenance API responses for 60 selected residential complexes (17 operations per month and 24,480 total successful response records). The study contrasts early and late three-month arithmetic means for three separately assessed raw numerical fields. The field-specific median percentage changes are +1.93% for `pay` (50 eligible), +2.24% for `cleanCost` (50 eligible), and +1.86% for `guardCost` (47 eligible). When the three fields are compared on exactly the same 45 complexes, the `cleanCost` median reverses to -2.09%. The difference is attributable to five positive `cleanCost` cases omitted from the common cohort by other fields' eligibility rules. Both exploratory cleaning-field bootstrap intervals cover zero; the results do not establish a nationwide increase or decline. Exact monetary units, denominators and parent-child relationships of these government API output fields are awaiting official confirmation; no conversion to KRW/m², KRW/household, or total management costs is undertaken.

## Suggested keywords

South Korea; K-apt; apartment maintenance; data provenance; nonprobability sample; missingness; sample composition; robustness analysis; reproducibility; bootstrap; administrative API

## Major revisions relative to v2

1. **Expanded cohort:** 20 → 60 archived complexes; source integrity checks on 20 historical files and all 40 new archived source files.
2. **Enhanced QA:** 24,480 complex-month-operation responses, 24 consecutive reporting months for each complex; method-key uniqueness, JSON structural stability, missing/zero distinction, nonfinite numeric exclusion checks.
3. **Field-specific strict eligibility:** `pay` n=50, `cleanCost` n=50, `guardCost` n=47; 15 unique complexes excluded for at least one field.
4. **Common-sample sensitivity:** matched 45 complexes, including `cleanCost` sign change from +2.24% to -2.09%, a major limitation on interpretation.
5. **Exploratory bootstrap:** 20,000 resamples within eligible cohorts; confidence limits must not be presented as national population confidence intervals.
6. **Reproducibility artifacts:** updated code, synthetic regression tests, per-complex eligibility outcomes, and documented sensitivity outputs. Final inventory and hashes of proposed deposit assets **not yet approved**.

## Reviewer-oriented integrity and rights checklist

- [x] Archived response grid and 60-source structural checks documented on GitHub.
- [x] Field-wise central statistics reproducible in archived-source reruns.
- [x] Same-complex sensitivity and five excluded cleaning cases explained in abstract and conclusion.
- [x] Nonprobability sampling and bootstrap interpretation qualified.
- [ ] Official response-field monetary units and area denominator confirmed by authoritative, field-specific evidence.
- [ ] Missing/null/zero provider reporting semantics clarified and incorporated.
- [ ] Archival raw-JSON reuse and attribution terms reviewed at the level of the exact data proposed for redistribution. The portal's general unrestricted-scope badge alone should not resolve all ancillary rights.
- [ ] Final deposited filenames, sizes, SHA-256 manifests, README, and code execution environment verified.
- [ ] Year-of-publication, authorship, affiliations, funding, license, contributors, grant metadata, and records cross-checked **against the existing v2 Zenodo record**. Do not invent or inherit them without checking.
- [ ] Coordinator gives explicit publication approval after inspecting the final files and metadata.
- [ ] Deposit created as a new version of the existing N02 Zenodo record, with no duplicate DOI chain.

## Proposed assets (not automatically staged or uploaded)

1. Final approved research report (with corrected field definitions and units if secured).
2. Analysis-method README and dated release notes.
3. Cohort inclusion/exclusion manifest and per-complex field eligibility tables.
4. Source integrity audit reports and reproducible standard-library calculations.
5. Matched-45 sensitivity and bootstrap comparison outputs.
6. Rights-cleared source records **only if licensing/attribution and privacy checks pass**; do not silently redistribute archived third-party API payloads.

## Status and next gate

**HOLD:** Official government response definitions and explicit final publication approval. Neither this dossier nor existing GitHub prepublication drafts authorize issuing a new DOI or editing published v2. Source analysis: [English v3 draft](./N02_V3_DRAFT_WITH_UNCERTAINTY_20261019.md), [Korean editorial review](./N02_V3_KOREAN_EDITORIAL_REVIEW_20261020.md), [field-unit verification matrix](./V3_35_FIELDS_PROVIDER_RESPONSE_MATRIX_20261019.md).

## Zenodo v2 metadata verification attempted (2026-10-20)

Direct reads of the current Zenodo v2 record `https://zenodo.org/records/23432629`, Zenodo REST API `https://zenodo.org/api/records/23432629`, DOI resolver `https://doi.org/10.5281/zenodo.23432629`, and DataCite DOI API were **not accessible in the current web runtime**. A connected Gmail search for Zenodo confirmation messages from October 2026 returned no matching emails. Consequently **no independent verification of creators, licenses, registered files, grants or version metadata was possible from these attempted sources**. This is an access limitation, not evidence that the Zenodo record has been deleted or its metadata changed. Keep the corresponding reviewer checklist items unchecked; do not extrapolate a creator name or license from the GitHub repo.

