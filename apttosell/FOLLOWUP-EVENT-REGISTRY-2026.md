# 2026 Follow-Up Event Registry — Pilot

The **AptToSell Follow-Up Event Registry 2026** is an event-level extension of the published 2026 competition and follow-up supply analysis.

It links follow-up supply events to stable AptToSell project IDs and preserves the distinction between derived dates, corroborated event IDs, and primary-source verified official notices.

## Pilot status

- Original project cohort: **196**
- Projects with follow-up supply observed: **103**
- First follow-up event rows: **103**
- Stable AptToSell project-ID matches: **103 / 103**
- DOI: **not assigned**
- Existing published analysis DOI: https://doi.org/10.6084/m9.figshare.34064439

## First-event derivation

For the current pilot:

`derived_first_followup_date = initial_announcement_date + days_to_first_followup`

The date is reproducible from the published project-level analysis, but a derived date is not automatically treated as an independently verified official notice date.

## Event verification states

- `DERIVED_FIRST_EVENT_DATE` — deterministic reconstruction from project-level fields
- `SECONDARY_CORROBORATED` — date / event / numeric notice ID reproduced consistently across multiple public sources, but official source is not directly accessible
- `PRIMARY_VERIFIED` — reserved for an official notice or official artifact directly verified

## Harrington Place Nowon Central reconciliation

The earlier chronology mismatch has been resolved.

Current sequence:

1. **2026-04-28** — 58-unit no-priority/residual supply, notice ID **2026910100**, `SECONDARY_CORROBORATED`
2. **2026-06-08** — later 58-unit no-priority supply, notice ID **2026910147**
3. **2026-07-23** — 17-unit discretionary/optional supply, notice ID **2026940157**

The first event ID is now recovered, but direct access to the original ApplyHome record remains the primary-source verification gate.

## Primary-source verification queue

A **103-row primary-source verification queue** now tracks the remaining notice-level work.

Priority order:

1. projects with more recorded follow-up events
2. shorter time to first follow-up

Each row should eventually capture official notice ID, subtype, source URL/artifact, supply count, result data when available, and verification date.

## Repository files

- Event registry: https://github.com/cheer710815-hub/apttosell-subscription-data/tree/main/datasets/followup-event-registry-2026
- First-event CSV: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/apttosell-first-followup-events-pilot-v0.1.csv
- Verification queue: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/PRIMARY-VERIFICATION-QUEUE.csv
- Official notice verification register: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/OFFICIAL-NOTICE-VERIFICATION.md

## Release decision

No separate DOI is assigned to this event-level pilot.

The current Figshare DOI remains the citation target for the published competition/follow-up analysis. A new event-level DOI should wait until a clearly bounded notice-level cohort is primary-source verified.


## Evidence-review completion

The first-pass event discovery queue is now fully screened.

- First-event rows: **103**
- Evidence-reviewed: **103 / 103**
- Numeric follow-up notice IDs recovered: **95**
- `PRIMARY_VERIFIED`: **1**
- `ID_CORROBORATED_SECONDARY`: **94**
- `SECONDARY_CORROBORATED`: **8**
- Remaining discovery TODO: **0**

This milestone means the discovery/reconciliation pass is complete. It does not mean all events have direct official-source verification.

The next layer is **primary-source promotion**: locating the original ApplyHome/LH or official project notice artifact and promoting only directly supported rows.

- Crosswalk: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/FOLLOWUP-NOTICE-ID-CROSSWALK-v0.1.csv
- Progress: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/PRIMARY-VERIFICATION-PROGRESS.md
