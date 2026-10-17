# N02 Phase 3 — stratified expansion cohort and batch audit protocol

**Status:** prospective methods plan; **no additional observations collected or analysed by this file**.  
**Date:** 2026-10-17. **Research series:** [Zenodo N02 v2](https://doi.org/10.5281/zenodo.23432629), 20 complexes × 24 months. Retain the same study lineage; any future Zenodo release must be a clearly labeled new version, not a duplicate independent publication.

## Why expand?
The 20-complex pilot is nonrandom and unevenly distributed across building sizes and locations. Prior archived candidate screening suggested approximately **833** qualifying complexes for the 2023-01 through 2024-08 move-in cohort. That **833 figure is a historical screening count, not currently revalidated against the master source file**, and cannot itself be treated as the denominator for an inference until the manifest is retrieved and checked.

## Sampling frame gate
Required fields for every candidate: `kaptCode`, `kaptName`, `usedate` (occupancy date source field), `kaptdaCnt` (units; confirm actual API key), region (province + city/district), `kaptMarea` (management area). Source is official K-apt basic information API and dated local master export. Persist both the observed date and source field, and do **not** equate `usedate` with the official building completion date.

A candidate is eligible only if its apartment property type is confirmed, its code is nonempty/unique, and a full requested 24-month reporting window is available. Keep exclusion counts by cause. Exclude the existing 20 `kaptCode` IDs from new sample draws to prevent accidental double weighting.

## Proposed stratified batch — 40 NEW complexes (target, not yet selected)
| Size stratum (housing units) | Target complexes |
|---|---:|
| under 300 | 8 |
| 300–599 | 8 |
| 600–999 | 8 |
| 1,000–1,499 | 8 |
| 1,500 or more | 8 |
| **Total** | **40** |

Within each size stratum, spread candidates across provinces and metropolitan regions as far as the eligible frame permits. Require at least **three distinct high-level regions per size stratum** when possible; record any deviation and do not invent replacements. Use deterministic sampling from a frozen eligible frame, sorted by `kaptCode`, with disclosed seed **20261017**; preserve selected, reserve and excluded IDs in one locked manifest. Sample-size allocations are **research design targets**, not estimated existing frequencies.

## Acquisition and restart rules
- Each complex: 24 reporting months × 17 cost API operations = **408 responses**. 40 newly selected complexes imply **16,320 API response attempts** before retries; verify API quota and break into daily batches accordingly.
- Always carry forward existing `cost_raw_long.csv` rows and deduplicate by (complex ID, month, API method). Checkpoints and retry logs must not leak the `serviceKey`.
- Retain **raw JSON** locally as official-source evidence, but do not redistribute raw payloads pending authoritative reuse interpretation; publish derived aggregates/reproducible code only after review.
- Save one audit for **all new complexes at once**, not separate manual 408-line investigations: row counts, HTTP/response status, empty values, null vs zero, exact months, hashes, and original-to-derived reconciliation.
- Compare paired first-three and last-three reporting months **by component**. Strict sensitivity requires all six endpoint observations to be available and nonzero; report the actual denominator for each field.
- Never sum 17 API services into total common costs or apply a KRW/m² conversion until provider clarifies units/denominators. Agency question is pending response as of 2026-10-17.

## Reporting and publication gates
1. Freeze and audit the candidate master + previously used 20-ID exclusion manifest.
2. Select 40 new codes as above. **Do not claim that selection happened until the complete source frame is read.**
3. Batch collect and audit 40 × 408 = 16,320 responses, with explicit missingness and start months.
4. Recompute *all* prior and new complexes from raw archived JSON before discussing pooled change estimates; stratified descriptive results only, no national representativeness claims.
5. Submit QA code, schema, notes on cost-unit uncertainty, valid-case denominators, and report for user approval. Keep Zenodo N02 v2 unchanged during analysis. Avoid secondary DOI mirrors to Figshare/Mendeley.

## Immediate next input / blocker
The historical **833-candidate master CSV** and frozen **existing 20 `kaptCode` ID manifest** are not in this GitHub protocol. Retrieve them from the research archive before generating a concrete 40-ID collection list. If missing, rerun official basic-info extraction to reconstruct the frame. No new data was collected and no official cost-unit definition was invented during this protocol update.
