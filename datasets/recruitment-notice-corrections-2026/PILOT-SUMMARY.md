# Pilot Summary — South Korea Housing Recruitment Notice Correction History 2026

> Pilot snapshot date: **2026-10-05**

This pilot validates a conservative event-level method for recording corrections to official South Korean housing recruitment notices.

## Pilot counts

- Verified public-ready correction events: **6**
- Partial-evidence events retained for review: **3**
- Public-ready projects represented: **3**
- Official source system for public-ready rows: **LH청약플러스**

## Public-ready projects

1. **양주회천 A-26BL 공공분양주택**
   - 3 verified correction events
   - schedule, specification, eligibility-label corrections

2. **인천계양 A6블록 공공분양주택**
   - 2 verified correction events
   - bathroom option/specification corrections

3. **인천가정2 B2블록 공공분양 잔여세대 추가 입주자모집공고**
   - 1 verified correction event
   - payment-schedule correction for a 74A optional item

## Partial-evidence records

- **영천문외 센트럴타운 공공분양주택**
  - official correction summary found, but complete before/after wording not reconstructed

- **남양주왕숙2 A-3BL 공공분양주택**
  - official before/after correction values found, but correction publication date not independently established from the parsed public page

## What this pilot proves

The pilot demonstrates that correction notices can be represented as structured change events rather than replacing the prior state. The model keeps:

- original source record
- correction source record
- before value
- after value
- change category
- evidence status
- public-release eligibility

This preserves the historical audit trail and prevents later corrected values from being mistaken for the original notice content.

## Files

- Public-ready pilot CSV: `correction-events-public-pilot-2026-10-05.csv`
- Full working seed file: `correction-events-seed-2026-10-05.csv`
- Methodology: `METHODOLOGY.md`
- Data dictionary: `DATA-DICTIONARY.md`

## Release decision

This snapshot is intentionally **not assigned a DOI**. It is a pilot with limited coverage, not a complete 2026 national correction-history dataset.

A DOI/versioned public release should wait until a defined 2026 denominator or a clearly bounded cohort is collected and the correction-date completeness rule can be applied consistently.
