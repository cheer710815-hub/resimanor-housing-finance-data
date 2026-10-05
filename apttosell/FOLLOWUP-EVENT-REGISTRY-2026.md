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
- Numeric first follow-up notice IDs recovered: **103 / 103**
- `PRIMARY_VERIFIED`: **11**
- `ID_CORROBORATED_SECONDARY`: **92**
- `SECONDARY_CORROBORATED`: **0**
- Remaining discovery TODO: **0**

This milestone means the discovery/reconciliation pass is complete. It does not mean all events have direct official-source verification.

The next layer is **primary-source promotion**: locating the original ApplyHome/LH or official project notice artifact and promoting only directly supported rows.

- Crosswalk: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/FOLLOWUP-NOTICE-ID-CROSSWALK-v0.1.csv
- Progress: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/PRIMARY-VERIFICATION-PROGRESS.md


## Primary-promotion access audit

All remaining **102 non-primary** first-event rows have now been audited for promotion readiness.

- Numeric first-event notice ID: **102 / 102**
- Constructed official ApplyHome detail URL candidate: **102 / 102**
- Direct ApplyHome detail access in the current web environment: **0 / 102**
- Already direct-primary verified: **1**

The official ApplyHome endpoint is not accessible through the current web tool, so these rows remain `ID_CORROBORATED_SECONDARY` rather than being overstated as primary-verified.

The discovery problem is now closed: **103 / 103 first-event notice IDs are known**. The remaining work is purely official-artifact access and source-grade promotion.


## Direct-official-artifact promotions

The first primary-promotion pass has produced **3** directly supported events.

- **포레나더샵 인천시청역** — official project-hosted no-priority notice PDF
- **아크로 리버스카이** — official ACRO project-hosted no-priority notice PDF, notice ID `2026910194`
- **청주 푸르지오 씨엘리체** — official PRUGIO project-hosted no-priority notice PDF, notice ID `2026910133`

A separate conservative CSV contains only these direct-primary rows:

https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/followup-event-registry-2026/PRIMARY-VERIFIED-SUBSET-v0.1.csv

The remaining 92 events retain corroborated status until an official artifact can be directly inspected.


### First-event ID correction from an official artifact

**드파인 아르티아** was promoted after direct inspection of the official SK DEFINE no-priority recruitment notice PDF.

- Correct first-event notice ID: `2026910214`
- Notice date: 2026-08-07
- Residual supply: 15 units

The previously recovered `2026910233` was confirmed to be a later second no-priority notice and is retained only as later-event history.


- **쌍용 더 플래티넘 온수역** — official project-hosted no-priority notice PDF, notice ID `2026910070`, notice date 2026-03-25, 3 residual units.


### Official POSCO E&C Songdo Granterre cluster

Four blocks were promoted from directly inspected official POSCO E&C project-hosted no-priority notice PDFs, all dated 2026-07-30:

- G5-11: notice ID `2026910207`, 45 residual units
- G5-3: notice ID `2026910204`, 22 residual units
- G5-4: notice ID `2026910205`, 36 residual units
- G5-5: notice ID `2026910206`, 12 residual units

These four rows are included in the conservative primary-verified subset.

- **의왕역 SK VIEW** — official SK VIEW project-hosted no-priority notice PDF, notice ID `2026910225`, notice date 2026-08-28, 17 residual units.
