# N02 v3 official source gate recheck — 2026-10-20

## Verified from authoritative public listing
- Provider: Ministry of Land, Infrastructure and Transport (국토교통부), responsible unit 주택건설운영과.
- API: 국토교통부_공동주택관리비(공용관리비)정보제공서비스, REST, JSON.
- Public listing: https://www.data.go.kr/data/15057937/openapi.do
- Listing reports 이용허락범위 제한 없음, last portal modification shown as 2026-08-06.
- The publicly available listing text contains a guide for seeing Swagger specifications, **not** a verified per-field unit/denominator mapping for N02's 35 observed raw JSON numeric keys.

## Mail evidence
Checked the researcher's connected mailbox for agency response on 2026-10-20. Only the 2026-10-19 10:44 KST reply from the public-data helpdesk was present; this acknowledges referral to the responsible ministry, **not** a substantive answer. No government written statement establishes the exact units of `pay`, `cleanCost` or `guardCost`.

## Hold the right inference
- Reproducible 60-complex medians: `pay` +1.93% (n=50), `cleanCost` +2.24% (n=50), `guardCost` +1.86% (n=47). These are changes of source numerical values, not officially defined monthly KRW, KRW/m², or overall maintenance fees.
- Use only field-specific first-/last-three-month comparisons; never sum 17 overlapping API endpoint monetary fields.
- K-apt website's regional normalized unit is **not evidence** that archived raw response keys share that same unit.
- Independent source QA, bootstrap reweighting and tests remain valid as documented, but **none substitutes for authoritative API metadata**.

## Action on a substantive ministry answer
For every explicitly documented raw key, capture: agency, answer date, official field name, exact unit, month-aggregation rule, denominator if any, overlap position, null/zero semantics and immutable citation URL or dated copy. Compare against at least one same-month official K-apt display where definitions allow. Update `V3_35_FIELDS_PROVIDER_RESPONSE_MATRIX_20261019.md`; only verified rows can be used for normalization. Re-run any affected analyses and require the research coordinator's approval before issuing **a version within the existing N02 Zenodo series**. Do not mint a parallel DOI or silently change v2 10.5281/zenodo.23432629.

**Status: scientific draft may remain public on GitHub; Zenodo v3 RELEASE HOLD.**
