# Quality Checks — Recruitment Notice Correction History 2026

## Pilot status

Snapshot date: **2026-10-05**

The pilot is considered internally complete when all rules below are satisfied.

## Row-level checks

A public-ready row must have:

- an official source system
- an original source record
- an official correction source record
- a project name
- a change category
- a specific field name
- a before value
- an after value
- an evidence note
- a verification date
- `evidence_status = verified`
- `publication_ready = yes`

If a key element is missing, the row remains `partial_evidence` and must not appear in the conservative public pilot CSV.

## Event-separation checks

- Multiple corrections within one project are separate rows.
- Multiple corrected fields in one correction notice are separate rows.
- Residual-unit, first-come, cashback, or other later promotional terms are not treated as corrections unless the official recruitment notice itself was formally corrected.
- A later correction never overwrites the recorded original value.

## Source checks

Accepted primary evidence for this pilot:

1. LH청약플러스 official original and correction notice pages.
2. ApplyHome official recruitment/correction records where before/after states can be reconstructed.
3. Korea Real Estate Board public-data responses supporting the official notice record.

Secondary sources may only be used to locate the official source.

## Pilot counts

- Verified public-ready rows: **6**
- Partial-evidence rows: **3**
- Public-ready projects: **3**

## DOI gate

Do not mint a DOI for this pilot.

A versioned DOI release requires:

- a defined national or otherwise bounded cohort
- documented denominator and coverage
- stable collection end date
- frozen schema
- consistent correction-date verification
- reproducible public subset rules
- final source-rights and license review
