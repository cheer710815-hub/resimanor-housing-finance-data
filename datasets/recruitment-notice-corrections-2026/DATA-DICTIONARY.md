# Data Dictionary — Housing Recruitment Notice Correction History 2026

> Draft schema. Field names may change before Version 1.0.

| Field | Meaning |
|---|---|
| house_manage_no | ApplyHome housing management number |
| pblanc_no | Recruitment notice number where available |
| project_name | Project / housing name |
| region | Province or metropolitan region |
| original_announcement_date | Initial recruitment notice publication date |
| correction_date | Official correction publication/effective date |
| correction_sequence | 1, 2, 3... within the project |
| change_category | High-level category of the correction |
| field_name | Specific field or item changed |
| old_value | Verified value before correction |
| new_value | Verified value after correction |
| change_summary | Short human-readable description |
| evidence_status | verified / partial_evidence / unresolved |
| source_original_url | Official source supporting original state |
| source_correction_url | Official source supporting corrected state |
| evidence_note | Verification note |
| verified_date | Date the change event was checked |
| publication_ready | Whether the row qualifies for conservative public release |

## Planned change categories

- schedule
- eligibility
- supply_quantity
- housing_type
- price_payment
- application_contract_date
- project_information
- contact_information
- other

## Public-release rule

Only `evidence_status = verified` rows with traceable official evidence should be included in the conservative public subset.
