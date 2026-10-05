# 2026 Verified Project Registry — Pilot

**AptToSell Verified Project Registry 2026** is a working project-identity layer for connecting multiple South Korean apartment subscription datasets with one stable internal project ID.

The registry is designed so that competition-rate, follow-up supply, price, payment-condition, and pre-move-in funding datasets can refer to the same housing project without creating a new identifier each time.

## Pilot status

- Working version: **0.4-pilot**
- Project IDs assigned: **196**
- Existing two pilot IDs preserved
- Pre-move-in public subset crosswalk: **41 / 41 matched**
- DOI: **not assigned**
- License for AptToSell-created metadata: **CC BY 4.0**

## Identifier format

`ATS-YYYY-REGION-NNNNNN`

Examples:

- `ATS-2026-GG-000001`
- `ATS-2026-SEOUL-000001`

The AptToSell ID is an internal join key. Official identifiers such as `house_manage_no` are retained and should not be replaced.

## Verification model

Project identity and competition-result verification are separated.

- `PRIMARY_VERIFIED`: supported by an official recruitment notice, ApplyHome/LH/public-agency record, or project-owner primary document
- `SECONDARY_VERIFIED`: supported by a reliable secondary reproduction or analysis but not yet captured from the primary result source
- `REGISTRY_SEEDED`: a stable AptToSell ID has been assigned from the existing validation registry; this does not mean all fields passed the final primary-source gate

## Cross-dataset demonstration

The fixed 41-project public subset from the **Korea Apartment Pre-Move-In Funding Dataset 2026** was joined against the 196-project ID map using `house_manage_no`.

Result:

- Matched: **41**
- Unmatched: **0**

The Version 1.0 DOI dataset itself was not modified. A separate crosswalk file was created to preserve reproducibility.

## Files

- 196-project ID map: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/verified-project-registry-2026/apttosell-project-id-map-196-pilot-v0.4.csv
- 41-project crosswalk: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/verified-project-registry-2026/pre-movein-public-41-with-project-id-pilot-v0.4.csv
- Methodology: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/verified-project-registry-2026/METHODOLOGY.md
- Data dictionary: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/verified-project-registry-2026/DATA-DICTIONARY.md
- Quality checks: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/verified-project-registry-2026/QUALITY-CHECKS.md
- Integration guide: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/verified-project-registry-2026/INTEGRATION-GUIDE.md
- Data Package metadata: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/verified-project-registry-2026/datapackage.json
- Schema.org Dataset JSON-LD: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/verified-project-registry-2026/schemaorg-dataset.jsonld

## Release decision

This pilot is intentionally not assigned a DOI.

Version 1.0 should wait until primary-source identity verification, duplicate/rename rules, regional coding, and publication-ready status are consistently complete across the intended release cohort.
