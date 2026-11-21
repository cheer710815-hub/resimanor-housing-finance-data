# Is an LH commercial-shop entry-date field a notice-level fact?

**Resimanor / ARHRN research technical note — published November 21, 2026**  
Research ID: ARHRN-LH-SHOP-PAYMENT-TERMS-GRAIN-QA-20261115  
**Zenodo deposit and DOI are on hold. No DOI has been assigned.**

## Abstract

We compared two separately catalogued official Korea Land & Housing Corporation (LH) CSV datasets about commercial-shop notices: a file labelled December 31, 2020 (2,545 rows, 29 columns) and another labelled August 27, 2025 (5,763 rows, 34 columns). We distinguished *notice–shop matching keys* from *shop composites* and compared the published entry-date values at year–month resolution. A strict notice–shop key appeared in both releases for 1,825 combinations; 1,822 were comparable, of which 1,820 agreed and two differed. The two differences trace to one shop composite, Entrarium unit 101. At shop-composite level, 1,210 were shared; 1,207 were comparable, with 1,206 agreements and one difference.

Within each separate dataset, all composites with multiple notice posting dates (381 for the 2020-labelled dataset and 476 for the 2025-labelled dataset) retain one entry-date literal, even though listed prices vary across notices for 107 and 131 composites respectively. This matters for data users who might count repeated notices as separate physical shops or treat the date field in a later catalogue as a historical event directly observed at each notice.

## Sources and provenance

1. LH, [상가 입찰 공고 내역_20201231](https://www.data.go.kr/data/15072453/fileData.do): 2,545 rows, 29 columns, CP949; SHA-256 cb3d3c0fbd33ee3ac5c581729996a4964766dd874bbc3e2e52a888069d6bf702.
2. LH, [상가 공급 및 대금납부정보_20250827](https://www.data.go.kr/data/15119259/fileData.do): 5,763 rows, 34 columns, CP949; SHA-256 4fc36e8ff8900e2619adba940537eb935eebc6b04bd0c18e900a44052e99d92c.

**Critical provenance qualification:** The dates in the filenames are dataset reference dates, not authenticated consecutive versions of one file. The portal lists the first as last modified on November 19, 2025 and the second as last modified on August 27, 2025. Portal metadata does not establish when the underlying CSV bytes changed. Our comparison cannot prove chronological revision, retroactive overwriting, or the mechanism of any differing field.

## Methods

The strict notice–shop key comprises the notice title, posting date, shop name, unit number, and exclusive area. A separate research-defined shop composite comprises the business district, block, shop name, unit, and exclusive area. Neither is an LH-certified unique physical-asset identifier. Numeric area representations and insignificant spacing are normalized; fuzzy linking is not used.

The 2020-labelled dataset expresses nonblank entry-date values with day = 01, so we compare *year and month only*. A string of the form '2025-MM-YY 00:00:00' in the 2025-labelled file is interpreted solely as a **candidate** year-month '20YY-MM' in a distinct derived column; we never alter original data.

## Findings

| Unit | Matched | Comparable | Same year-month | Different year-month |
|---|---:|---:|---:|---:|
| Notice–shop key | 1,825 | 1,822 | **1,820** | 2 |
| Shop composite | 1,210 | 1,207 | **1,206** | 1 |

Both notice-level nonmatches concern **Entrarium unit 101**. The 2020-labelled source records 2019-10-01 for notices posted in 2019 and 2020. The 2025-labelled source records 2025-02-22 00:00:00 for those notices and one from 2021; its candidate reconstructed year-month is 2022-02. This establishes a difference between published records, not a change to physical entry/occupancy.

For shop composites appearing under multiple posting dates, 381/381 in the 2020-labelled dataset and 476/476 in the 2025-labelled dataset show no within-dataset entry-date variation. Listed prices vary for 107 and 131 composites, respectively. Thus the field behaves as a *shop-associated published attribute within each file*, rather than as an independently observed, changing fact at each notice.

## Limitations and practical reuse

The original datasets may share an internal source. Agreement between them is not independent confirmation of actual occupancy dates. No source-system logs, relevant original shop PDFs for all historical notices, or agency explanations establishing a particular conversion mechanism were reviewed. The data do not establish causality, a confirmed spreadsheet parsing defect, retrospective overwriting or an endorsed method to correct the entire 2025 file.

When researching administrative notices, retain the original value, source dataset reference, posting date, research-defined matching key and optional candidate year-month **as separate columns**. Avoid interpreting notice-row counts as unique physical shops or sales. Some entries concern rental-space notices, not outright sales.

## Reproduction and citation

The standard-library Python script reproduces the analysis from the **two original LH CSV files downloaded directly from their official source pages**, verifying their SHA-256 hashes. The CSV originals are not redistributed.

Code and documentation: https://github.com/cheer710815-hub/resimanor-housing-finance-data/tree/main/research/lh-shop-entry-date-provenance-2026

Suggested citation: Resimanor / ARHRN (2026), *Is an LH commercial-shop entry-date field a notice-level fact?*, ARHRN-LH-SHOP-PAYMENT-TERMS-GRAIN-QA-20261115, public GitHub research note. **DOI: not assigned; Zenodo on hold.**
