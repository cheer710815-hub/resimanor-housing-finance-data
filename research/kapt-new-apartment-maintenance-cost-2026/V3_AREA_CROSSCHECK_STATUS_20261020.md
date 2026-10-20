# N02 area-denominator cross-check: independently verified public surfaces

Status: **BLOCKED ON EXACT APARTMENT RESIDENTIAL EXCLUSIVE AREA DENOMINATOR AND SAME-MONTH DISPLAY VALUE**. No conversion calculated.

## Direct source values and evidence

- Target: complex A10020809, reporting month 202501, raw API getHsmpCleaningCostInfoV3 field cleanCost = 3,667,763 (archived response). This is an unconverted raw numeric field.
- Official K-apt 1:N comparison: https://www.k-apt.go.kr/apiinfo/apiComparativeSearch.do — result display shows (단위:원/㎡). It also says shown costs are for the whole complex before miscellaneous communal-income offsets and may differ from charges to individual units.
- Official K-apt 1:1 comparison: https://www.k-apt.go.kr/apiinfo/goApiSearchCompare_detail.do — result display shows (단위: 원/㎡); alternative area-basis entries are provided by each management body and may differ.
- Official Ministry apartment basic-information API: https://www.data.go.kr/data/15058453/openapi.do — public description includes building gross floor area and household counts; it **does not establish** the precise complex-wide residential-exclusive-floor-area sum used for the above official billing-period display.

## Missing join keys and verification

Need two *independently sourced* same-complex-month-item observations: (1) official residential-exclusive-floor-area **total in m²**, and (2) corresponding official cleaning cost **per m²** with the same cost definition and reporting version.

Conditional formula: `archived raw cleanCost / verified residential exclusive area total`. Do not substitute `kaptMarea` or building gross area unless government definitions directly equate them to the K-apt cost-basis denominator. Do not assert the raw response is 'KRW/month' solely from its magnitude.

Comparison must account for period versioning, page rounding, cost category granularity, and differences between pre- versus post-offset billed amounts. As of this check those values are unavailable, hence **no numeric per-m² result**.

Retain the 60-complex relative numeric change comparisons as exploratory and current v2 DOI 10.5281/zenodo.23432629. v3 remains unpublished pending explicit approval.