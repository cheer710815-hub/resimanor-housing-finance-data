# K-apt New-Apartment Maintenance Cost Stabilization — Research Protocol (2026)

**Status: exploratory 15-complex research report published; expanded empirical dataset work remains ongoing.**  
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
- **No duplicate DOI:** This report DOI is the existing N02 canonical publication. Future extensions should cite this work and use clearly versioned updates rather than independent duplicate records.

This publication update supersedes the earlier statement below that there were no validated observations, while preserving the initial protocol for transparency.

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
