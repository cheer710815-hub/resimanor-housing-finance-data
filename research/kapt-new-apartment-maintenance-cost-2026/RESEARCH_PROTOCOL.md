# K-apt New-Apartment Maintenance Cost Stabilization — Research Protocol (2026)

**Status: v1 (15 complexes), v2 (20 complexes) and v3 (60 complexes) published in the same Zenodo version chain. Monetary field units and historical-area assumptions remain under review.**  
**Publisher:** Resimanor  
**Source:** Korea Ministry of Land, Infrastructure and Transport / K-apt (https://www.k-apt.go.kr/)  
**Independent research question:** How do publicly reported monthly management costs change during the first 24 months after apartment completion, and how does the trajectory differ by complex size?

## Published pilot report — 15 complexes, 24 months (2026-10-15)
**Peer-reviewed status:** Not peer reviewed. **Publication type:** Exploratory research report (NOT a full public raw-data release).

- **Zenodo v1 record:** https://zenodo.org/records/23393936
- **Report DOI:** https://doi.org/10.5281/zenodo.23393936
- **Title:** Early-stage apartment maintenance-cost trajectories in South Korea: a 15-complex, 24-month observational pilot (2023–2026)
- **Author:** Eun Kim (Resimanor), ORCID 0009-0006-9445-4768.
- **Data processed:** 15 apartment complexes × 24 observed months × 17 K-apt common cost API categories = 6,120 category/month responses. The report PDF is hosted on Zenodo; raw government API response files are **not** deposited with the report.
- **Methods and limitations:** Separate cost subcomponents, do not add overlapping API fields to infer total maintenance costs. Some early months record zeros; sensitivity analyses exclude affected endpoint periods. Complex selection is not nationally representative. No causal stabilization claims.
- **Current research stage:** 15-complex observational pilot report **published**; expanded-cohort, field-license, unit-of-measure, and reproducible raw-data release research remain open.
- **No duplicate DOI:** The v1 and v2 report DOIs belong to the **same** Zenodo version chain. Cite the version used; do not mirror these as separate independent studies.

This publication update supersedes the earlier statement below that there were no validated observations, while preserving the initial protocol for transparency.

## Published expanded report — 20 complexes, 24 months (2026-10-17)
**Version:** 2.0 of the same Zenodo research record, NOT an independent duplicate deposit. **Peer review:** Not peer reviewed.

- **Zenodo v2 (historical version):** https://zenodo.org/records/23432629
- **v2 DOI:** https://doi.org/10.5281/zenodo.23432629
- **v1 predecessor:** https://zenodo.org/records/23393936 (DOI 10.5281/zenodo.23393936; retained unchanged)
- **Title:** Early-stage apartment maintenance-cost trajectories in South Korea: Expanded 20-complex, 24-month observational analysis (2023–2026)
- **Scope:** 20 complexes × 24 months × 17 cost API categories (8,160 category/month API responses). PDF report published; not a public raw K-apt API data deposit.
- **Reported first-three versus last-three month median percentage changes:** pay +0.27%, cleaning +3.18%, security +2.00% across 20 complexes.
- **Strict nonzero and complete-data sensitivity sample:** 16 complexes; pay −8.00%, cleaning +0.30%, security −0.76%. Missing amounts must not be interpreted as zero.
- **Verification scope:** New 5 complexes rechecked against their raw API exports; earlier 15 complexes reanalyzed from existing processed monthly data, **not** independently revalidated against each original API response in this iteration.
- **Limits:** Nonrandom, nonrepresentative sample; overlapping API expense categories and zero/missing reporting; no inference of a national total cost or causal stabilization.

For citations of the 20-complex result, use **v2 DOI 10.5281/zenodo.23432629**. Cite v1 only for the historical 15-complex pilot.

## Published dataset — 60 complexes, 24 months (2026-10-22)

**Version:** v3, within the same Zenodo version chain (not a new independent research record). **Peer review:** Not peer reviewed.

- **Zenodo v3:** https://zenodo.org/records/23553560
- **Version DOI:** https://doi.org/10.5281/zenodo.23553560
- **All-versions DOI:** https://doi.org/10.5281/zenodo.23393935
- **Prior v2:** https://doi.org/10.5281/zenodo.23432629
- **Title:** Changes in Apartment Maintenance Cost Components During the First 24 Months: A 60-Complex Study in South Korea
- **Registered archive:** `N02_Zenodo_v3_UPDATED_CANDIDATE_20261021.zip` (315.7 kB shown on record). Independently downloading and verifying its bytes against the local archive remains pending.
- **Scope:** 60 selected apartment complexes × 24 monthly observations × 17 API categories = 24,480 source-category requests.
- **Method:** For each eligible complex, compare the first-three-month average with the last-three-month average; report the **median of complex-level percentage changes**, not changes in total apartment fees.
- **Published strict-endpoint results:** pay/labor +1.93% (n=50), cleanCost/cleaning +2.24% (n=50), guardCost/security +1.86% (n=47).
- **Limits:** Nonrandom sample, not nationally representative and not causal. Individual API cost fields' absolute monetary units have not been independently confirmed. `privArea` and `kaptMarea` are distinct; present-day denominators are not established as fixed over historic observation months. API cost components may overlap and must not be added together to estimate total fees.
- **Source service:** https://www.data.go.kr/data/15057937/openapi.do

For current 60-complex results, cite **v3 DOI 10.5281/zenodo.23553560**. Use v2 and v1 DOIs only when referring specifically to their historical versions. Do not create another DOI merely to mirror this same dataset.

## Why this is distinct
This research tracks post-occupancy monthly costs using K-apt complex/month panels. It is not a continuation of existing mortgage DSR, housing-subscription, HUG presale-guarantee or subscription-competition studies. Avoid recycling their DOI records.

## Proposed observation unit
One apartment complex ID × one reporting month. Require a verified complex identifier and a documented completion / occupancy-start field. The cohort and sample period are **not confirmed** until access to source records is validated.

## Required source variables
- K-apt permanent complex identifier
- Region and city/district
- Completion / occupancy-start date with source field provenance
- Housing units and management floor area
- Monthly actual reported common-area management cost per relevant square meter
- Heating, electricity, water and other usage charges separately, where present
- Month observed and last updated
- Missing/zero/corrected records flag

## Planned reproducible analysis
1. Acquire K-apt monthly management-cost records from official public source / API.
2. Cross-reference complex master records, discard unmatched IDs and document attrition.
3. Compare the same cost component and denominator each month.
4. Generate event-time months 0–23 relative to occupancy / reporting start.
5. Stratify by complex size, region and heating type; account for seasonality.
6. Publish distributions (median/IQR) and missingness rates. Document all exclusions.
7. Do not assert post-occupancy stabilization without data.
8. Distinguish registration/reporting start from actual building completion where necessary.

## Verification / publication gates
- At least one independently reproducible official-data extract and its field dictionary.
- Source URLs, retrieval date and license/attribution statement.
- Data quality report: units, missingness, revised reports and inflation/season effects.
- Research README + schema + source snapshot/hash + code + CSV.
- Then create one canonical Zenodo release with one DOI; link from this GitHub folder.
- Submit related scholarly dataset to Mendeley / Figshare only after checking their duplicate-publication rules; use related identifiers and avoid representing mirrors as independent studies.
- Evaluate RePEc as a data-oriented research note only with adequate original methods/results and transparent sources.
- Track each release, review and approval result in the central work register.

## Publication integrity
This protocol contains the original registered research plan. A separate **exploratory report** based on collected K-apt API observations was published on Zenodo on 2026-10-15, DOI **10.5281/zenodo.23393936**. That DOI refers to the report PDF, **not** a publicly released, independently verified raw dataset or a nationally representative analysis.

## Independent reproduction confirmation — 2026-10-22

The publicly released Zenodo v3 archive (`10.5281/zenodo.23553560`) was compared against the prepublication archive on the publisher's local Windows environment. The 315,715-byte files matched both the preflight SHA-256 (`0bfc9edc2e6f051c1bbbb496fe7b07730a12fcb177fb067478bcf8715ad80d08`) and the Zenodo MD5 (`add3f57b550f6e299ffb5c84dc2b4de6`). The ZIP CRC check passed and the archive contained 21 files.

The included `REPRODUCE/n02_independent_recompute.py` was then executed locally with the packaged raw cohort ZIPs and reference endpoint table. Its reported results were 8,160 old-cohort records plus 16,320 new-cohort records (24,480 combined), 60 complexes, 180 endpoint comparisons, 180 matches, **zero mismatches**, and no reported issues. Reported median percentage changes (complex-level first-three vs last-three-month endpoint comparison) were:

| Cost component | Recomputed median change | Eligible complexes |
| --- | ---: | ---: |
| Labor | +1.9256590517834016% | 50 |
| Cleaning | +2.24236503693932% | 50 |
| Security | +1.8591552704096737% | 47 |

These reproduce the published rounded values (+1.93%, +2.24%, +1.86%). This is **package-based analytical reproducibility**, not a new independent download of the government API source records, validation of official monetary units, validation of historical area denominators, proof of licensing rights for every raw file, or evidence of nationally representative trends or causality. Do not interpret these percentages as increases in total maintenance fees. Preserve the existing v3 DOI and version lineage; no replacement DOI is needed.

## Official source licensing check — 2026-10-22

- Official API catalog: https://www.data.go.kr/data/15057937/openapi.do (MOLIT, “공동주택관리비(공용관리비)정보제공서비스”).
- On 2026-10-22 the catalog publicly displayed: **무료** (no fee), **이용허락범위 제한 없음** (no stated usage restrictions), REST/JSON, and a catalog modification date of 2026-08-06.
- Scope of this check: the licensing statement **for this catalog entry only**. It does not independently resolve whether all packaged files have third-party rights, whether any separate terms apply, or whether every derived field's unit and historical area denominator is correctly specified.
- The public HTML catalog page did not establish authoritative units for `pay`, `cleanCost`, and `guardCost`. Accordingly, retain the original-unit uncertainty disclosure; do **not** present absolute amounts as KRW/month or KRW/m²/month without authoritative field-level documentation.
- Keep the published v3 analysis and DOI unchanged. No new DOI, raw-data redistribution, or categorical license assertion follows from this check alone.

## K-apt display-unit cross-check — 2026-10-22

The official K-apt complex comparison interface (https://www.k-apt.go.kr/apiinfo/goApiSearchCompare_detail.do) visibly labels its displayed comparison values **원/㎡ (KRW per square meter)** and shows detailed common-cost categories. It also states that management-area standards entered by managers can differ from exclusive area and that display figures can differ from household bills.

**Crucial distinction:** The **web interface's display unit does not itself establish the raw API's units** for `pay`, `cleanCost`, or `guardCost` in the service catalog at https://www.data.go.kr/data/15057937/openapi.do. The specific API response-field dictionary or authoritative API provider answer is still needed, as is validation of monthly historical area denominators. No back-conversion to total KRW or KRW/m² was authorized by this visual cross-check. Continue reporting only component-level relative changes with the established limitations.

## Published v3 attached-archive audit — 2026-10-23

**Evidence scope:** User-supplied copy of `N02_Zenodo_v3_UPDATED_CANDIDATE_20261021 (2).zip`; Zenodo server's own file checksum **not** independently retrieved. The record's publication and v3 version chain were confirmed from the user's Zenodo screenshots.

- Size: **315,715 bytes**; SHA-256: `0bfc9edc2e6f051c1bbbb496fe7b07730a12fcb177fb067478bcf8715ad80d08`.
- Outer ZIP CRC: **PASS**. Exactly 21 files: `MANIFEST_SHA256.json` and 20 manifest-listed files; all **20/20 SHA-256** match, with no omitted or missing files.
- Nested 20-complex and 40-complex source ZIPs: **CRC PASS**. Included `REPRODUCE/n02_independent_recompute.py` independently reprocessed **24,480 API source records** (8,160 + 16,320), **60 unique complexes**, and **180 comparisons**; **180 matched, 0 mismatched, 0 issues**.
- Strict eligible median changes: pay **+1.9256590518% (n=50)**, cleaning **+2.2423650369% (n=50)**, security **+1.8591552704% (n=47)**.
- **Metadata wording issue, not a numerical-data failure:** the archived `PUBLICATION_STATUS.txt` still says `CANDIDATE — NOT PUBLISHED`, and `REPRODUCE/RUN_INSTRUCTIONS.md` retains candidate wording. The study is already published as v3; do not edit the immutable publication or invent a new DOI solely to fix this text. This paragraph documents the correction on the existing GitHub project.
- **Open limits:** source API raw-field monetary units, month-specific historic area denominators and Zenodo server-side byte hash remain unverified. Do not assert that the user-supplied copy has been proven byte-identical to the server-hosted archive.

**Canonical v3:** https://doi.org/10.5281/zenodo.23553560. **Concept DOI:** https://doi.org/10.5281/zenodo.23393935. Older v1/v2 remain part of this same version chain.
