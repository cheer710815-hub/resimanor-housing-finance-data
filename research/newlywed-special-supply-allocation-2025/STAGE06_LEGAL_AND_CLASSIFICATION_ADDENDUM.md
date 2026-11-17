# Stage 6 addendum — legal text discrepancy and supply-title review sensitivity (2026-11-17)

**Research ID:** `ARHRN-INDEPENDENT-BRIDAL-SPECIAL-SUPPLY-REFORM-20261108`

## Official legal-source distinction

- The 2025-03-31 amendment to *주택공급에 관한 규칙* (국토교통부령 제1471호) **explicitly replaced 18% with 23%** in Article 41(1). Its Article 3 transitional provision preserves the previous rule for notices publicly announced **before** the effective date. [Official amendment text](https://law.go.kr/LSW/lsRvsDocListP.do?chrClsCd=010202&lsId=008243&lsRvsGubun=all), [transitional provision](https://www.law.go.kr/LSW/lsInfoP.do?ancYnChk=0&chrClsCd=010202&efYd=20250630&joNo=005300&lsiSeq=272665&urlMode=lsInfoP).
- The ministry's [2025-04-22 explainer](https://www.korea.kr/multi/visualNewsView.do?newsId=148942198) also states an 18% → 23% increase.
- **However**, the officially displayed 2025-03-31 *신혼부부 주택 특별공급 운용지침*, 국토교통부고시 제2025-160호, Article 3(1)(1), still says **18% for private housing**. [Official administrative-rule text](https://www.law.go.kr/admRulLsInfoP.do?admRulSeq=2100000256910). The legal/administrative explanation for the textual discrepancy has **not been independently established**. Do not silently treat the guidance as amended to 23%; do not adjudicate individual projects' lawfulness without their full applicable source documents.

## New supply-type review sensitivity

The earlier title-based manual-review regex overlooked five announcements mentioning cooperative member status loss, expulsions or reserved allotments (terms such as `조합원`, `자격상실`, `제명세대`, `보류지`). These are *review flags*, **not official supply-type classification or automatic exclusion rules**.

| Sample (notice-title review only) | Announcements | Descriptive 2025-vs-2024 four-cell contrast |
|---|---:|---:|
| All | 502 | +5.223659 percentage points |
| Original review flags excluded | 472 | +5.155668 pp |
| Expanded review flags excluded | 467 | +5.148225 pp |
| Notices with nonzero newlywed units only | 467 | +5.447121 pp |
| Expanded review flags excluded AND nonzero newlywed units | 448 | +5.439399 pp |

The sign remains positive under each listed selection, but these values **are not causal effect estimates**, legal compliance measures, or inferential confidence bounds. The five newly flagged notice names and cohort diagnostics are included below for transparent audit.

## Reuse conditions

The data are the 2025-11-28 official ApplyHome CSV snapshot, covering Jan 1–Nov 28 of 2024 and 2025, **not full calendar years**. Reproduction of this extra sensitivity uses the notice-level analysis panel and does not substitute for independent verification of 502 corrections, approval dates, or exceptions. No source CSV redistribution claim is made. No DOI and no peer review.

**Corrective note:** The earlier README's concise policy statement should be read with the explicit legal-text discrepancy above. The exact raw legal source must be consulted before using this study as legal evidence.
