# N02: A10020809, January 2025 — cleaning-cost numeric and denominator cross-check

**Status:** Archived monthly amount cross-checked against an independent K-apt-derived third-party display; both area-based arithmetic variants computed. **Not** a direct screenshot or official K-apt site cross-check of the exclusive-area per-m² cleaning field. Do not call it official display confirmation.

## Inputs

- Complex A10020809, 대라수어썸브릿지 1,2단지아파트.
- Archived K-apt monthly common-cost JSON, `cleanCost` for reporting month `202501`: **3,667,763** (raw numeric value).
- Live apartment basic-information **V5** response supplied by the researcher: `getAphusBassInfoV5`, `privArea="23943.96"`, `kaptMarea=33255.69`, `kaptTarea=59665.82`.
- Independent third-party page deriving data from K-apt, 2025-01: https://www.aptdamoa.com/apt/A10020809/202501.html . It shows **청소비 3,667,763원, 110원/㎡** and says the displayed unit uses **관리비 부과면적**. Exact monthly raw numeric amount matches the archive.
- Official K-apt 1:1 comparison page https://www.k-apt.go.kr/apiinfo/goApiSearchCompare_detail.do states `원/㎡` and warns different area denominators are separately used by managing entities; **the official same-complex same-month exact cleaning figure was not accessible**.

## Arithmetic (rounded)

| Basis | Area, sqm | Calculation | Derived KRW/sqm |
|---|---:|---|---:|
| Residential exclusive-area sum (`privArea`) | 23,943.96 | 3,667,763 / 23,943.96 | **153.18** |
| Management billing area (`kaptMarea`) | 33,255.69 | 3,667,763 / 33,255.69 | **110.29**, displayed **110** by the third-party site |

## Interpretation

- The byte-for-byte numerical match of the monthly `cleanCost` to a separately published KRW total strongly supports interpretation of the archived field as **monthly whole-complex KRW amount**, not a raw per-m² cost.
- Both normalized results are mathematically correct for **different** area denominators, assuming present-day area sums also applied in 2025-01. The comparison-site 110 KRW/sqm **is not evidence that the exclusive-area value should be 110**; it is explicitly a billing-area value.
- Before claiming an *officially validated* K-apt exclusive-area cleaning figure, collect the actual official 2025-01 complex-item display and check denominator effective date and rounding. The third-party page's time and revisions might differ.
- `privArea` is now directly verified in a V5 user-provided response. This supersedes the older "missing area denominator" status for this example complex, but does not establish 60-complex availability or date stability.

**Release**: Existing v2 DOI 10.5281/zenodo.23432629 unchanged; v3 not published. No recalculation of 60 complexes without obtaining and evaluating respective denominators.
