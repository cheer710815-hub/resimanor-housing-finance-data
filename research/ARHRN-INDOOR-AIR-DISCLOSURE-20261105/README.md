# ARHRN Indoor Air Quality Disclosure Research — Stage 0

**Study ID:** ARHRN-INDOOR-AIR-DISCLOSURE-20261105  
**Lead site:** https://resimanor.com  
**Status:** Stage 0 / exploratory source registry only / **not a validated results dataset**  
**Updated:** 2026-11-05 (Asia/Seoul)

## Purpose

Audit the accessibility, traceability and comparability of published indoor-air-quality measurement reports for newly constructed multi-unit housing in Korea. The primary questions are whether reported buildings can be matched across government postings, whether repeated listing indicates the same measurement or separate tests, and whether the underlying measurements (including dates, analytes and units) can be independently verified.

## Confirmed scope and strict limits

Five Seoul Metropolitan Government monthly listings (August–December 2025) appear to identify 9, 5, 7, 5 and 6 **listing appearances** respectively (32 in total). **These are neither 32 distinct apartment developments nor 32 independent laboratory measurements.** The figures are initial government-page discovery counts, not independently audited attachment records.

Several names recur between months, but duplicate projects, duplicate tests and repeat testing **have not been established**. An Uijeongbu City disclosure-list page is an additional comparison source; it is **not a comparable numerical cohort** yet.

**No raw attachment/PDF result tables have been extracted and verified. No pollutant concentrations, legal exceedance rates, regional comparison estimates, or health claims are published by this repository.** Webpage descriptions have not been independently reconciled with the attachment bytes.

## Source register (official sources, attachment-level verification pending)

| ID | Authority | Period | Official page | Preliminary count |
| --- | --- | --- | --- | ---: |
| SEOUL_2025_08 | Seoul | 2025-08 | https://news.seoul.go.kr/env/archives/565409 | 9 |
| SEOUL_2025_09 | Seoul | 2025-09 | https://news.seoul.go.kr/env/archives/565412 | 5 |
| SEOUL_2025_10 | Seoul | 2025-10 | https://news.seoul.go.kr/env/archives/566501 | 7 |
| SEOUL_2025_11 | Seoul | 2025-11 | https://news.seoul.go.kr/env/archives/566574 | 5 |
| SEOUL_2025_12 | Seoul | 2025-12 | https://news.seoul.go.kr/env/archives/566869 | 6 |
| UIJEONGBU_LIST | Uijeongbu | List page | https://www.ui4u.go.kr/depart/indoorAirQuality/list.do?mId=0601100000 | Not audited |

Relevant legal background: [Indoor Air Quality Control Act](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1033619167) Article 9. The builder's measurement/disclosure obligations must not be confused with the scope of discretionary local government online publication.

## Pre-registered quality controls

1. Retrieve and preserve the original government attachments; record source URLs, retrieval dates and SHA-256 file hashes.
2. Capture building name, address, notice date, measurement date, measuring entity and test/report identifier.
3. Parse concentrations and units **only where source attachments are verified**. Preserve source-specific standards and whether a row is first test or retest.
4. Match exact names first; then addresses and report-level identifiers. Classify as `SAME_MEASUREMENT`, `REPEAT_TEST`, `NEW_DOCUMENT` or `UNRESOLVED`.
5. Report coverage and missingness; do not infer a nationwide rate from two municipalities or infer a legal breach from absence of online records.
6. Halt or limit to a website-only methods note if reproducible data or independent public value is not demonstrated.

## Data availability / publication status

This public file is a **preliminary research design and source registry**, **not** a released study, peer-reviewed finding, or completed open dataset. Raw source records, curated measurement tables, reproducibility code and a validated research report **are not yet available**.

**DOI:** none. **Figshare:** not published. **Zenodo:** withheld while account access is unresolved. Future datasets will be screened for redistribution rights and duplicate-DOI risk before deposition.

**Project context:** https://resimanor.com

## Citation

Until the official attachments are independently audited, please cite the **primary government documents**, not this preliminary registry, for factual pollutant measurements or compliance conclusions.
