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

A verified payment-schedule correction is also included for **인천가정2 B2블록 공공분양 잔여세대 추가 입주자모집공고**. The official LH correction notice provides both the original and revised amounts for the 74A type's option item 18 (13-inch wall pad): contract payment 68→24 thousand KRW, each of the 1st-3rd interim payments 136→49 thousand KRW, and balance 203→73 thousand KRW.

The seed file now also includes two verified specification-change events from **인천계양 A6블록 공공분양주택**. The official LH correction notice explicitly provides both the original and changed bathroom-option labels for the affected housing types.

Two additional **남양주왕숙2 A-3BL 공공분양주택** correction rows are retained as `partial_evidence`. The official LH correction page explicitly shows the before/after income threshold (9,906,236 → 9,906,263) and the service-area label change, but the parsed public page does not expose a correction publication date. They remain outside the conservative public-ready subset until that date is independently verified.

A fourth candidate from **영천문외 센트럴타운 공공분양주택** is retained as `partial_evidence`: the official correction page explicitly states that stamp-duty cost-sharing content was added and required documents were revised, but the full before/after wording has not yet been reconstructed. It is therefore excluded from the conservative public-ready subset.

## Planned unit of observation

One row will represent one verified change event for one housing recruitment notice.

A project can therefore have multiple rows when multiple fields or multiple correction events are verified.

## Planned fields

See [DATA-DICTIONARY.md](./DATA-DICTIONARY.md).

## Verification principle

A correction is recorded only when a before/after state can be supported by official evidence or a preserved official record. A later promotional condition, residual-unit sales condition, or first-come sales condition is **not** treated as a correction to the original recruitment notice unless the official notice itself was corrected.

## Pilot snapshot (2026-10-05)

- Public-ready verified events: **6**
- Partial-evidence events retained for review: **3**
- Public-ready projects represented: **3**
- Public pilot CSV: [correction-events-public-pilot-2026-10-05.csv](./correction-events-public-pilot-2026-10-05.csv)
- Full working seed: [correction-events-seed-2026-10-05.csv](./correction-events-seed-2026-10-05.csv)
- Pilot summary: [PILOT-SUMMARY.md](./PILOT-SUMMARY.md)

This pilot is intentionally not assigned a DOI because the 2026 national denominator and coverage are not yet fixed.

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


## Pilot package metadata

- Version: **0.1-pilot**
- [Data Package metadata](./datapackage.json)
- [Citation metadata](./CITATION.cff)
- [Release notes](./RELEASE-NOTES.md)
- [License and source-rights note](./LICENSE-NOTE.md)
- [Screening register](./SCREENING-REGISTER.md)

The pilot package is frozen as a methodological snapshot. New verified events should be collected in a later snapshot rather than silently rewriting the 2026-10-05 pilot CSV.
