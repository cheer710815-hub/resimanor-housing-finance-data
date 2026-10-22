# N02 v3 — K-apt official field-definition verification request

**Prepared:** 2026-10-22. **Status:** Draft only; not sent, posted, or submitted.  
**Dataset record:** https://doi.org/10.5281/zenodo.23553560

## Why this is needed

N02 compares 60 selected complexes over the first 24 observed months using official K-apt public API data. The strictly eligible component-change medians have been published; however, the public source's precise monetary field units and the correct **historical month-specific** denominator for any official per-㎡ conversion have **not** yet been established. The study does not publish unverified official won/㎡ series.

### Target and channel distinction

- **Operator:** 한국부동산원, K-apt — https://www.reb.or.kr/reb/cm/cntnts/cntntsView.do?cntntsId=1204
- **Published K-apt management/area datasets:** https://www.reb.or.kr/reb/ad/bs/beffatinfosport/view/selectBeffatinfoList.do?mi=9624
- **K-apt primary service:** https://www.k-apt.go.kr/
- **REB public-data quality-error center:** https://www.reb.or.kr/reb/na/ntt/selectNttList.do?bbsId=1173&mi=9741 . This form is **for confirmed data quality errors** and should **not** be used as a promotional research submission or as a generic definition request unless the operator directs us there.
- **K-apt help center:** Contact mechanism on the official K-apt site. Confirm whether a structured public-data inquiry or data-go.kr provider question is the proper channel before sending.

## Korean question draft (for legitimate provider inquiry)

**제목: K-apt 공용관리비 OpenAPI 금액 필드 단위 및 월별 면적 분모 공식 정의 확인 요청**

K-apt 공개 API를 활용해 준공 초기 공동주택 관리비 세부 항목을 분석하면서, 원자료 해석의 정확성을 확인하고자 문의드립니다.

1. 공동주택 공용관리비 세부 항목 API의 `pay`, `cleanCost`, `guardCost` 값은 **해당 단지의 월별 총원 금액**인지, **원/㎡ 단가**인지, 또는 다른 단위인지 확인 부탁드립니다. 가능하면 공식 데이터사전·필드 설명서의 정확한 항목명과 문서 버전을 알려주시기 바랍니다.
2. K-apt의 공식 관리비 비교 화면이 표시하는 `원/㎡` 수치를 API 값에서 재현하려면 **어떤 면적 분모**를 사용해야 합니까? 주거전용면적 총합, 관리면적 또는 기타 표준면적 중 실제 적용되는 필드를 알려주시기 바랍니다.
3. `privArea`와 `kaptMarea`의 공식 정의 및 관계는 무엇입니까? 한 단지의 현재 시점 값이 과거 24개 관측 월에도 동일했다고 가정해도 되는지, **월별 당시의 면적 데이터**와 정정 이력을 조회할 수 있는지 확인 부탁드립니다.
4. 관리비 공개 화면의 '발생월·부과월·공개월'과 OpenAPI의 조회월 `searchDate`는 어떤 관계입니까? 월별 시점 정렬에 사용해야 할 기준은 무엇입니까?
5. 원자료의 누락, 미공개, 0원, 추후 정정은 API상 어떤 값 또는 상태로 구분됩니까? 이력이 수정되는 경우 기준일이나 변경내역을 조회할 수 있습니까?
6. 공식 공개 API 자료에 출처 표기와 분석 결과의 재이용·공개 범위를 명시하는 가이드가 있다면 URL을 안내 부탁드립니다.

이 문의의 목적은 공식 금액 단위와 관리비 비교 기준을 정확하게 인용하기 위한 **데이터 정의 검증**이며, 연구자료 홍보나 링크 요청이 아닙니다.

## Guardrails

- Do **not** send this request via an unrelated research-proposal or error-report channel.
- Do **not** treat unanswered questions as confirmation of a unit or normalization rule.
- Keep published component-change estimates labelled as exploratory, nonrepresentative, and not a household total-fee increase.
- Record the operator's response date, official document version and exact URL in the central N02 row, then assess whether a transparent Zenodo correction/new version is warranted. Do not silently alter the existing published archive.
- No duplicate N02 DOI; no institutional external submission or cold email without suitable channel and explicit approval.

**Source checks:** REB K-apt system introduction, REB advance public information on K-apt area/cost datasets, and the official K-apt site, all accessed 2026-10-22.

## Verified primary inquiry route — 2026-10-22

The actual **source API record** for this study is the Ministry of Land, Infrastructure and Transport's **공동주택관리비(공용관리비)정보제공서비스**: https://www.data.go.kr/data/15057937/openapi.do. Its public listing identifies provider **국토교통부**, managing division **주택건설운영과**, and offers the **데이터 개선요청 오류신고 및 문의** feature. The public catalog JSON-LD metadata explicitly lists a managing-division contact telephone **053-663-8263** (https://www.data.go.kr/catalog/15057937/openapi.json); confirm this is the appropriate API definitions inquiry point if using telephone rather than the record's online inquiry menu.

**First-choice channel:** Open the exact API record above while logged into data.go.kr; choose its data-improvement/error/inquiry pathway for a **field dictionary and unit clarification**. Do not file the matter as a confirmed error unless official inconsistency has been demonstrated. If the form permits category selection, choose a question/inquiry rather than an error report.

K-apt is operated by 한국부동산원, but the public API's formally named provider is 국토교통부. Direct the inquiry first through **the provider's own API record** instead of the separate REB quality-error channel, research-proposal desk, or publicity inbox.

**Prepared only:** No form was submitted and no message was sent. Record the case/ticket ID and the actual provider's response in the central research register after submission.

## Catalog metadata versus field dictionary — source audit 2026-10-22

- The official JSON-LD public catalog endpoint https://www.data.go.kr/catalog/15057937/openapi.json confirms the exact API title `국토교통부_공동주택관리비(공용관리비)정보제공서비스`, ministry as provider, managing division `주택건설운영과`, and contact `053-663-8263`.
- That metadata records service update date **2025-03-27** and licence **이용허락범위 제한 없음**. The catalog metadata does **not** specify the three API result fields' units, a historical month-specific area denominator, or correction semantics.
- K-apt public management-cost display and REB weekly pre-disclosure of complex-area data (https://www.reb.or.kr/reb/ad/bs/beffatinfosport/view/selectBeffatinfoList.do?mi=9624) establish the existence of area information, **not** that today's area equals all 24 historical monthly denominators.
- **Do not close** the official unit and historical denominator questions based on the metadata alone.
- No data-go.kr message, phone call or ticket was submitted in this audit.

## Public live API page cross-check — 2026-10-22

- The current public **API detail page** https://www.data.go.kr/data/15057937/openapi.do displays **수정일 2026-08-06**. This must be distinguished from the **2025-03-27 date found in a separate machine-readable catalog response**, which should **not** be labelled as the latest detail-page modification date.
- The detail page explicitly offers **데이터 개선요청 오류신고 및 문의** and identifies the provider as 국토교통부, 부서 주택건설운영과. Its rendered public detail view does not show the department phone number; a previously retrieved catalog value of 053-663-8263 should be revalidated with the provider before calling.
- Public read-only access was insufficient to open an authenticated enquiry submission form or obtain a case/ticket number. **No enquiry has been submitted**.
- Keep the substantive questions on `pay`, `cleanCost`, `guardCost` units, official monthly denominator, historic changes, reporting-month conventions and missing/zero/corrected amounts open until the ministry confirms them.

## Newly verified K-apt official statistics unit — 2026-10-22

K-apt's own thematic common-cost statistics page states: **발생 공용관리비 (단위: 원/㎡, 주거전용면적기준)**. It also says its statistics may change with complex-characteristic changes or management-cost corrections at later query dates. Source: https://www.k-apt.go.kr/apiinfo/index/apiIndexSearch.do (official K-apt public statistical page).

**Important interpretation boundary:** This establishes the presentation unit of that K-apt *statistics screen*, NOT necessarily the raw-return unit of the API fields `pay`, `cleanCost`, `guardCost`, and NOT the recorded area denominator on each of the 24 historic months. Do not assert that an API amount is already won/㎡, or divide an API value by today's area, based only on this display.

**Shortened provider questions:**
1. Are `pay`, `cleanCost` and `guardCost` raw API results monthly KRW totals or already unit-normalized won/㎡ values? Please refer to the version-specific official field dictionary.
2. What exact denominator does the K-apt official per-㎡ display use on each historical reporting month? Does it distinguish `privArea` from `kaptMarea` and retain month-specific area revisions?
3. How does the API mark and retain missing, non-disclosed, 0-valued and revised monthly records, including their reference month and last corrected date?

**Status:** Public documentation partially clarifies the statistics screen; individual API field definitions and historic denominators remain unanswered. No contact made or ticket issued.
