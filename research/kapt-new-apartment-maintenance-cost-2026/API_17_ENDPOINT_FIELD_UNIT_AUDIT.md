# N02: 17 official common-maintenance API endpoints — field/unit validation ledger

**Checked:** 2026-10-17. **Status: endpoint inventory completed; per-response monetary field units NOT universally verified.**

## Primary official references

- Ministry of Land, Infrastructure and Transport, public data portal **공동주택관리비(공용관리비)정보제공서비스**: https://www.data.go.kr/data/15057937/openapi.do (official JSON API, marked "이용허락범위 제한 없음" as seen on portal; do not infer copyright status of non-portal compilations). API family: `AptCmnuseManageCostServiceV3`.
- K-apt official regional statistics: https://www.k-apt.go.kr/apiinfo/index/apiIndexSearch.do explicitly reports **발생 공용관리비 (원/㎡, 주거전용면적기준)** for those aggregated displays, and says utilities and long-term repair funds excluded.
- K-apt official side-by-side comparison: https://www.k-apt.go.kr/apiinfo/goApiSearchCompare_detail.do displays **(단위: 원/㎡)** with area-basis selector; published area-basis criteria can differ from unit costs actually billed.
- Existing N02 published expanded report: https://doi.org/10.5281/zenodo.23432629 (exploratory 20-complex, 24-month report). Previous report: https://doi.org/10.5281/zenodo.23393936.

## Endpoint inventory and validation status

The following list identifies endpoints used by the N02 collector and their category interpretation. It is **not** a validated JSON response schema; without official response field descriptions or concrete response payloads, no monetary field should be assigned a unit by analogy with K-apt website display.

| # | Collector API method | Cost category | Parent/overlap warning | JSON value fields | Unit/denominator |
|---:|---|---|---|---|---|
| 1 | `getHsmpLaborCostInfoV3` | 인건비 | 일반관리비의 하위 항목 | **Not independently mapped** | **Unverified for this endpoint** |
| 2 | `getHsmpTaxdueInfoV3` | 제세공과금 | 일반관리비 내 분류 관계 확인 필요 | **Not independently mapped** | **Unverified for this endpoint** |
| 3 | `getHsmpVhcleMntncCostInfoV3` | 차량유지비 | 일반관리비 내 분류 관계 확인 필요 | **Not independently mapped** | **Unverified for this endpoint** |
| 4 | `getHsmpEtcCostInfoV3` | 기타비용 | 상위 항목 확인 필요 | **Not independently mapped** | **Unverified for this endpoint** |
| 5 | `getHsmpOfcrkCostInfoV3` | 사무용품비 | 일반관리비 내 분류 관계 확인 필요 | **Not independently mapped** | **Unverified for this endpoint** |
| 6 | `getHsmpClothingCostInfoV3` | 피복비 | 일반관리비 내 분류 관계 확인 필요 | **Not independently mapped** | **Unverified for this endpoint** |
| 7 | `getHsmpEduTraingCostInfoV3` | 교육훈련비 | 일반관리비 내 분류 관계 확인 필요 | **Not independently mapped** | **Unverified for this endpoint** |
| 8 | `getHsmpCleaningCostInfoV3` | 청소비 | 공용관리비 별도 항목 | **Not independently mapped** | **Unverified for this endpoint** |
| 9 | `getHsmpGuardCostInfoV3` | 경비비 | 공용관리비 별도 항목 | **Not independently mapped** | **Unverified for this endpoint** |
| 10 | `getHsmpDisinfectionCostInfoV3` | 소독비 | 공용관리비 별도 항목 | **Not independently mapped** | **Unverified for this endpoint** |
| 11 | `getHsmpElevatorMntncCostInfoV3` | 승강기유지비 | 공용관리비 별도 항목 | **Not independently mapped** | **Unverified for this endpoint** |
| 12 | `getHsmpHomeNetworkMntncCostInfoV3` | 지능형 홈네트워크 설비유지비 | 공용관리비 별도 항목 | **Not independently mapped** | **Unverified for this endpoint** |
| 13 | `getHsmpRepairsCostInfoV3` | 수선비 | 수선유지비 하위 항목 | **Not independently mapped** | **Unverified for this endpoint** |
| 14 | `getHsmpFacilityMntncCostInfoV3` | 시설유지비 | 수선유지비 하위 항목 | **Not independently mapped** | **Unverified for this endpoint** |
| 15 | `getHsmpSafetyCheckUpCostInfoV3` | 안전점검비 | 수선유지비 하위 항목 | **Not independently mapped** | **Unverified for this endpoint** |
| 16 | `getHsmpDisasterPreventionCostInfoV3` | 재해예방비 | 수선유지비 하위 항목 | **Not independently mapped** | **Unverified for this endpoint** |
| 17 | `getHsmpConsignManageFeeInfoV3` | 위탁관리수수료 | 공용관리비 별도 항목 | **Not independently mapped** | **Unverified for this endpoint** |


## Archived JSON field-name inspection (2026-10-17)

A locally archived `cost_raw_long(5).csv` for **A10023388** contains **408 response rows** from **17 operations × 24 months**. Parsing `result_json` confirms **35 distinct candidate numeric value keys** across these methods (excluding `kaptCode`, `kaptName`):

- Labor: `pay`, `sundryCost`, `bonus`, `pension`, `accidentPremium`, `employPremium`, `nationalPension`, `healthPremium`, `welfareBenefit`.
- Tax/communications: `electCost`, `telCost`, `postageCost`, `taxrestCost`.
- Vehicle: `fuelCost`, `refairCost`, `carInsurance`, `carEtc`.
- Other expense: `careItemCost`, `accountingCost`, `hiddenCost`.
- Office: `officeSupply`, `bookSupply`, `transportCost`.
- One field per remaining twelve methods: `cleanCost`, `clothesCost`, `manageCost`, `lrefCost4`, `disinfCost`, `eduCost`, `elevCost`, `lrefCost2`, `guardCost`, `hnetwCost`, `lrefCost1`, `lrefCost3`.

These field names are **observed in archived data**, not descriptions or units certified by official Swagger. In particular the spelling `refairCost` is retained exactly as in source response; do not normalize or invent an alternative. No claim of a common unit or ability to sum the fields follows from this observation.

## Confirmed versus unresolved

**Confirmed by official K-apt page:** Area-standardized public *regional* common-maintenance statistics display in **KRW/m²** using residential exclusive floor area; they exclude personal utilities and long-term repair fund charges. **Not confirmed:** Whether each endpoint's raw `response.body.item` field is monthly KRW, KRW/m², another area basis, or a mixture. Do not divide numeric values by `kaptMarea` until validated against field definition. The basic-info field `kaptMarea` is **not automatically identical** to the residential exclusive area denominator displayed in regional statistics.

**Known analysis keys from existing N02 downstream tables:** `pay`, `cleanCost`, `guardCost`. These are names used in the research transformation, not independently verified public API schema declarations. Do not silently equate `pay` with all labor cost.

**No double counting:** In the official management-cost hierarchy labor-related items fall inside general management; repair/facility/safety/disaster items fall under repair and maintenance. The collection of 17 endpoints does not constitute 17 disjoint contributions to total building management costs. Do not sum until parent-child hierarchy, field unit and scope are verified.

**Data-quality treatment:** Keep source numeric 0 distinct from `null` / absent keys; valid success status is not proof of a valid monetary value. Public v2 20-complex sensitivity results describe 16 complexes with all first-three and final-three month amounts present and nonzero, and should not be generalized nationally.

## Actionable closure checklist (before area-normalized/total-cost claims)

1. Obtain/download the **official Swagger/OpenAPI model definitions** for each of 17 `getHsmp*V3` operations (output property name, type, description, unit, null meaning); use *official portal* rather than inferred fields from API method names.
2. From **one complete archived source CSV** inspect representative `result_json` for each endpoint; record the true response keys, shape, numeric range, and source sample date. Never record API service keys in this repository.
3. Match at least three distinctive component amounts on official K-apt monthly site to archived API values for the **same complex, month, component and area basis**; determine whether they represent monthly total KRW versus price per square meter and verify any applicable denominator.
4. Only then label endpoint as `VERIFIED_UNIT` and authorize derived per-household or KRW/m² metrics. Record exact source URLs and timestamp; refrain from publicly claiming field/unit verification based only on regional display.

**Publication policy:** Existing v1 and v2 Zenodo reports remain as published. This document does not claim the 17 response units have been fully validated; do not create a new duplicate DOI from this audit ledger.

## Official portal follow-up — 2026-10-17

Verified against the [government API service entry](https://www.data.go.kr/data/15057937/openapi.do): the provider is the Ministry of Land, Infrastructure and Transport; the transport format is **JSON**, and the listing identifies the permitted use as **이용허락범위 제한 없음** (no use-scope restriction). The public service page provides an **Open API specification guide**, but its rendered listing **does not include** a field-by-field definition, unit, or denominator for the 35 candidate value keys. Therefore this page **cannot support a claim that the 17 API endpoints' amounts are all KRW/m²**. No numeric normalization is authorized by this inspection alone.

**Evidence status:** provider/format/use-scope verified; raw field names observed in archived response; each amount's official unit/area denominator **unverified**. The public page's permission notice does not independently establish the rights of ancillary K-apt website content or third-party datasets.


## Direct public page inspection and agency clarification questions — 2026-10-17

Directly inspected public service page [data.go.kr/data/15057937/openapi.do](https://www.data.go.kr/data/15057937/openapi.do). It identifies the Ministry's `주택건설운영과` as managing department, the API as REST/JSON, and a generic **Open API specification guide**. The publicly extracted page gives **no machine-readable response-element table for the N02 35 cost keys**. A guide on how to view Swagger is not evidence of individual response field units. The project therefore does **not** claim all 17 endpoints were unit-validated.

### Questions to submit to the responsible provider

1. For each of the 17 `AptCmnuseManageCostServiceV3` methods, provide output `response.body.item` field names, Korean display names, and **exact unit** for each monetary element, including `pay`, `cleanCost`, `guardCost`, and `lrefCost1`–`lrefCost4`.
2. Are each field's values **monthly KRW total**, **KRW/m²**, **KRW/household**, or some other measure? If area-standardized: **which K-apt area definition** is the denominator (residential exclusive area vs management area vs another area), and is rounding applied?
3. Are salary, retirement and insurance amounts all *subcomponents* of labor cost; and are `lrefCost1`–`lrefCost4` all nested below repairs/maintenance? State which API values overlap and are **non-additive**.
4. For a numeric value of `0`, what can be inferred about reporting vs no incurred cost? What does `null` mean, and are unreported months or correction statuses distinguished?
5. Can historical 2023–2025 monthly amounts be revised after originally published? If so how can users retrieve amendment date or snapshots?
6. Is reuse of the raw API JSON as a redistributed scholarly derived dataset permitted under this API listing's **이용허락범위 제한 없음**, and are any separate attribution/source terms required?

**Until written field-level answers or downloadable specification are secured, all 35 field units stay `UNVERIFIED`.** Report them by API labels; do not calculate new household-/area-adjusted management costs. Future findings will document the date, exact answered fields, and provider evidence URL.

