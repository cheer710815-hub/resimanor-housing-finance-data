# N02 — K-apt API field-unit clarification request (2026-10-22)

Status: **draft inquiry, not sent**. Source record: https://www.data.go.kr/data/15057937/openapi.do

Official catalog identifies the publisher as the Ministry of Land, Infrastructure and Transport, the service as “공동주택관리비(공용관리비)정보제공서비스,” and usage terms as “이용허락범위 제한 없음.” The public catalog does **not** resolve response-field units for `pay`, `cleanCost`, and `guardCost` or define historical reporting-area denominators. An unrelated K-apt UI display labelled 원/㎡ must not be imported as the raw API unit without an authoritative mapping.

## Inquiry text (Korean)

제목: 공동주택관리비(공용관리비)정보제공서비스 API 응답 필드 단위 및 과거 면적 기준 확인 요청

안녕하세요. 국토교통부 공공데이터포털의 「공동주택관리비(공용관리비)정보제공서비스」(데이터 ID 15057937)를 활용해 공동주택 60개 단지의 월별 관리비 항목 변화를 연구하고 있습니다. 연구 결과의 단위 오류를 방지하기 위해 다음 사항에 대한 공식 명세 또는 답변을 요청드립니다.

1. 응답 필드 `pay`, `cleanCost`, `guardCost` 각각의 정확한 단위는 무엇입니까? 단지 전체 원화 총액, 원/㎡, 또는 기타 기준인가요?
2. 면적 기준 값이라면 사용되는 분모는 관리비 부과면적, 관리면적, 주거전용면적 또는 별도의 면적인가요? 각 필드에 동일하게 적용됩니까?
3. 과거 월별 API 값은 당시 신고면적을 기준으로 산정된 값인가요? 현재 제공되는 `privArea` 또는 `kaptMarea` 값을 과거 24개월에 일괄 적용할 수 있나요?
4. API의 0 또는 누락 값은 실측 0원, 미보고, 비적용 가운데 어떻게 구별하나요? 정정된 과거 자료가 다시 제공되는지 확인 부탁드립니다.
5. 공식 필드 정의서/활용가이드(버전과 개정일 포함)를 받을 수 있을까요? 공공데이터포털의 ‘이용허락범위 제한 없음’에 해당하는 API 응답 원자료를 연구용 CSV/ZIP에 포함해 재배포하는 경우 별도로 확인할 조건이 있는지도 부탁드립니다.

감사합니다.

## Handling

- No assertion that raw API financial fields are denominated in KRW or KRW/m² until source authority confirms.
- Preserve current v3 DOI and relative endpoint changes, and keep legal/units caveats.
- Send only after user approval, through the official portal inquiry or provider contact channel. Do not use press outreach.
