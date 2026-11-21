# LH commercial-shop entry-date fields: two official data catalogs

**Resimanor / ARHRN research note — published 2026-11-21**  
Research ID: `ARHRN-LH-SHOP-PAYMENT-TERMS-GRAIN-QA-20261115`  
Status: public technical note and reproducibility code. **Zenodo and DOI: on hold; no DOI assigned.**

- [국문 기술노트](TECHNICAL_NOTE_KO.md)
- [English technical note](TECHNICAL_NOTE_EN.md)
- [Reproduction script](stage8_reproduce.py)
- [Independent verification script](INDEPENDENT_CHECK.py)
- [Research data dictionary and scope](METHODS_AND_SCOPE.md)
- Resimanor research page: awaiting WordPress final publish confirmation; GitHub technical note is already public.

## Official source files (download separately)

1. Korea Land & Housing Corporation, **상가 입찰 공고 내역_20201231**: https://www.data.go.kr/data/15072453/fileData.do  
   2,545 rows, 29 columns, CP949, SHA-256 `cb3d3c0fbd33ee3ac5c581729996a4964766dd874bbc3e2e52a888069d6bf702`.
2. Korea Land & Housing Corporation, **상가 공급 및 대금납부정보_20250827**: https://www.data.go.kr/data/15119259/fileData.do  
   5,763 rows, 34 columns, CP949, SHA-256 `4fc36e8ff8900e2619adba940537eb935eebc6b04bd0c18e900a44052e99d92c`.

**The original LH CSVs are not redistributed in this repository.** Download the files above and retain the original bytes; the script rejects an input with an unexpected hash.

## Main results

| Comparison unit | Shared | Comparable entry year-month | Agree | Disagree | Missing |
|---|---:|---:|---:|---:|---:|
| Strict notice–shop key (notice, date, shop, unit, area) | 1,825 | 1,822 | 1,820 | 2 | 3 |
| Shop composite (business district, block, shop, unit, area) | 1,210 | 1,207 | 1,206 | 1 | 3 |

The two notice-level discrepancies concern **one shop composite: Entrarium unit 101**. Within each *individual dataset*, 381 (2020-labelled) and 476 (2025-labelled) multi-notice shop composites show a constant entry-date string despite listed-price differences for 107 and 131 composites respectively.

## Reproduce

Python 3.9+ standard library only:

```bash
python stage8_reproduce.py \
  --old2020 "한국토지주택공사_상가 입찰 공고 내역_20201231.csv" \
  --new2025 "한국토지주택공사_상가 공급 및 대금납부정보_20250827.csv" \
  --out results
```

Run from this directory or provide the absolute paths to the two downloaded files.

## Critical provenance limitation

The dates *2020-12-31* and *2025-08-27* are **reference dates in separately catalogued datasets**, not proof of a linear revision history. The portal lists the earlier-labelled dataset as **last modified 2025-11-19** and the later-labelled dataset as **last modified 2025-08-27**. Those metadata dates do not establish when the actual CSV bytes changed. This study does **not** claim retrospective overwriting by LH, an established date-conversion/Excel defect, actual shop occupancy dates, or correction accuracy for unmatched rows.

The string `2025-MM-YY 00:00:00` is mapped only to a *candidate* year-month `20YY-MM`. Never overwrite source values or use reconstructed years as verified dates. Composite matching keys are **research-defined**, not LH-issued physical asset identifiers.

**Cite without a DOI:** Resimanor / ARHRN (2026), *LH commercial-shop entry-date fields: a reproducible audit of two separately catalogued LH datasets*, research ID `ARHRN-LH-SHOP-PAYMENT-TERMS-GRAIN-QA-20261115`, GitHub repository URL.

No additional author/affiliation or license is asserted in this research-specific directory; the original LH dataset use conditions are governed by their official source pages.
