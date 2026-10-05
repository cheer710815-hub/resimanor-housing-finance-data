# Methodology — Housing Recruitment Notice Correction History 2026

## 1. Research question

How often are 2026 apartment recruitment notices corrected after first publication, which fields change, and how long after the original notice do verified corrections occur?

## 2. Scope

Initial target scope:

- South Korea
- APT housing recruitment notices
- 2026 recruitment notices
- correction events that can be supported by official evidence

The first public release will be limited to records for which both the original state and corrected state can be verified.

## 3. Source hierarchy

1. Official ApplyHome recruitment/correction notice
2. Korea Real Estate Board public-data response
3. Official project-owner or public-agency notice reproducing the correction
4. Secondary source only as a pointer to locate the official evidence

A secondary article alone is not sufficient to create a verified correction event.

## 4. Correction-event definition

A **correction event** is a verified change to an official recruitment notice after its initial publication.

Examples may include:

- supply schedule
- qualification or eligibility wording
- supply quantity
- housing-type information
- price/payment schedule
- application or contract dates
- contact or project information
- other officially corrected notice content

Later residual-unit, first-come, unsold-unit, cashback, reduced-deposit, or other sales promotions are not classified as recruitment-notice corrections unless they are formally issued as corrections to the original notice.

## 5. Record structure

The dataset is event-based. One project may have multiple correction-event rows.

Each event should preserve:

- project identifiers
- original notice date
- correction date
- changed field/category
- old value
- new value
- source URL
- evidence note
- verification date

## 6. Before/after evidence rule

A row is `verified` only when both sides of the change can be reconstructed from official records.

If the corrected value is visible but the prior value cannot be verified, the event may be retained internally as `partial_evidence` but must not enter the conservative public subset.

## 7. Derived measures

Possible derived measures include:

- correction count per project
- days from original notice to first correction
- correction categories by frequency
- share of projects with at least one verified correction
- repeated corrections per project

These measures will not be published until the denominator and coverage are fixed for a release.

## 8. Versioning

The first public release will receive its own version and persistent identifier only after:

- collection coverage is documented
- field definitions are frozen
- source evidence is reviewed
- public subset criteria are fixed

Draft files must not be cited as a final dataset.

## 9. License

Planned license for Resimanor-created metadata and derived fields: CC BY 4.0, subject to final source and rights review.
