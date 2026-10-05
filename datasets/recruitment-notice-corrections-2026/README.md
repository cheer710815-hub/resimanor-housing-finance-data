# South Korea Housing Recruitment Notice Correction History 2026

> Status: **work in progress**. This directory defines the collection and verification structure for a future public dataset. It is not yet a frozen or citable release.

Resimanor is building a change-history dataset for South Korean apartment housing recruitment notices and later correction notices in 2026.

The goal is to preserve **what changed, when it changed, and which official notice supports the change** instead of treating a corrected recruitment notice as if it had always contained the final values.

## Official source

Primary source families:

- Korea Real Estate Board / ApplyHome housing recruitment information
- Public Data Portal service: **한국부동산원_청약홈 분양정보 조회 서비스**
- API family: `ApplyhomeInfoDetailSvc`
- Korea Land & Housing Corporation / **LH청약플러스** official recruitment and correction notices

ApplyHome remains the main national reference layer. LH청약플러스 is also used when the original and corrected public-housing notices are both available from LH and the before/after change can be verified directly.

## First verified seed records

The first verified event rows were collected from the official LH correction notice for **양주회천 A-26BL 공공분양주택**. The correction notice explicitly shows before/after text for the model-house viewing period, a lighting-specification line, and a household-income table label.

See `correction-events-seed-2026-10-05.csv`.

The seed file now also includes two verified specification-change events from **인천계양 A6블록 공공분양주택**. The official LH correction notice explicitly provides both the original and changed bathroom-option labels for the affected housing types.

A fourth candidate from **영천문외 센트럴타운 공공분양주택** is retained as `partial_evidence`: the official correction page explicitly states that stamp-duty cost-sharing content was added and required documents were revised, but the full before/after wording has not yet been reconstructed. It is therefore excluded from the conservative public-ready subset.

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
