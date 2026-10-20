# N02 direct raw-field vs official area-denominator audit (2026-10-20)

Raw archive `cohort_results.zip` -> `cohort_results/A10020809_202407/cost_raw_long.csv`, operation `getHsmpCleaningCostInfoV3`, reporting month `202501`, observed flat JSON `cleanCost=3667763`. This is the exact **unconverted** archived numeric response-field value; its formal unit is not proven merely by its magnitude.

Official K-apt regional maintenance statistics https://www.k-apt.go.kr/apiinfo/index/apiIndexSearch.do explicitly display **원/㎡, 주거전용면적기준**. K-apt comparison https://www.k-apt.go.kr/apiinfo/goApiSearchCompare_detail.do also displays 원/㎡ and notes that other selectable management-area denominators can differ.

Inspected the available official `20261009_단지_기본정보.xlsx` header: includes code, addresses, housing classification, household counts, administration/staffing, etc., but **does not provide the exact complex-wide residential exclusive floor-area sum needed for normalization**. Thus neither the actual official area denominator nor the exact same-complex, same-month, same-component K-apt display figure has been obtained. The ratio `3667763 / verified exclusive floor-area sum` is only a conditional formula, **not a calculated/validated KRW per square meter cost**.

The right next evidence is the date-matched K-apt official exclusive floor area **sum** for the complex and a precisely corresponding displayed cleaning component, with rounding/version checked. Do not multiply unit-size by household count or divide by unverified `kaptMarea` as a substitute. Existing 60-complex numeric-percentage medians remain unchanged. Zenodo v2 retained; v3 not published.
