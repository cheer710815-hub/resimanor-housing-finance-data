# 2026 Follow-Up Event Registry

The **AptToSell Follow-Up Event Registry 2026** is a published event-level dataset linking 103 South Korean apartment subscription projects in 2026 to their first observed follow-up supply notices.

It preserves stable AptToSell project IDs, official follow-up notice IDs, canonical official source URLs, first follow-up dates and explicit evidence grades.

## Published release

- Public version: **0.2**
- Publication date: **2026-10-06**
- Projects with follow-up supply observed: **103**
- First-event rows: **103**
- Stable AptToSell project-ID matches: **103 / 103**
- Official follow-up notice IDs: **103 / 103**
- Canonical official source links: **103 / 103**
- `PRIMARY_VERIFIED`: **13**
- `ID_CORROBORATED_SECONDARY`: **90**
- License: **CC BY 4.0**
- Zenodo DOI: **https://doi.org/10.5281/zenodo.23176906**

## Interpretation

A follow-up supply event means a later official supply notice was identified and linked to the initial project.

It must **not** be interpreted as a contract-failure rate, cancellation rate, or unsold-rate estimate.

## Evidence grades

- `PRIMARY_VERIFIED` — the event is supported by a directly inspected official project/public-agency artifact.
- `ID_CORROBORATED_SECONDARY` — the numeric official notice ID and canonical ApplyHome detail URL are retained, but the event artifact itself has not been promoted to direct-primary status.

Primary promotion is optional enrichment and does not change the published v0.2 cohort.

## Public files

- Publication-ready CSV: https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/datasets/followup-event-registry-2026/apttosell-followup-event-registry-public-v0.2.csv
- Dataset repository: https://github.com/cheer710815-hub/apttosell-subscription-data/tree/main/datasets/followup-event-registry-2026
- Publication notes: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/PUBLICATION-NOTES.md
- Methodology: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/METHODOLOGY.md
- Data dictionary: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/DATA-DICTIONARY.md
- Schema.org Dataset metadata: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/schemaorg-dataset.jsonld

## Citation

> Kim, Eun. *AptToSell Follow-Up Event Registry 2026*, version 0.2, 2026-10-06. AptToSell. CC BY 4.0. https://doi.org/10.5281/zenodo.23176906

## Related analysis

The earlier competition/follow-up analysis remains available separately:

https://doi.org/10.6084/m9.figshare.34064439

The Zenodo DOI above is the preferred citation for the version-specific public event registry.
