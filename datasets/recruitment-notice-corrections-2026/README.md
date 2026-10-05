# South Korea Housing Recruitment Notice Correction History 2026

> Status: **work in progress**. This directory defines the collection and verification structure for a future public dataset. It is not yet a frozen or citable release.

Resimanor is building a change-history dataset for South Korean apartment housing recruitment notices and later correction notices in 2026.

The goal is to preserve **what changed, when it changed, and which official notice supports the change** instead of treating a corrected recruitment notice as if it had always contained the final values.

## Official source

Primary source:

- Korea Real Estate Board / ApplyHome housing recruitment information
- Public Data Portal service: **한국부동산원_청약홈 분양정보 조회 서비스**
- API family: `ApplyhomeInfoDetailSvc`

The public service includes APT recruitment information and related supply categories. This project will use official notice pages or official public-data responses as the primary evidence layer.

## Planned unit of observation

One row will represent one verified change event for one housing recruitment notice.

A project can therefore have multiple rows when multiple fields or multiple correction events are verified.

## Planned fields

See [DATA-DICTIONARY.md](./DATA-DICTIONARY.md).

## Verification principle

A correction is recorded only when a before/after state can be supported by official evidence or a preserved official record. A later promotional condition, residual-unit sales condition, or first-come sales condition is **not** treated as a correction to the original recruitment notice unless the official notice itself was corrected.

## Planned outputs

- correction-event CSV
- project-level correction summary
- change-type counts
- time from original notice to correction
- media/research brief if the data reveals a meaningful pattern

## License

The intended release license for Resimanor-created metadata and derived change-history fields is **CC BY 4.0**, subject to final source review before publication.

## Source note

The Korea Real Estate Board ApplyHome public-data service is available through the Korean Public Data Portal and provides official housing recruitment information for APT and related supply categories.
