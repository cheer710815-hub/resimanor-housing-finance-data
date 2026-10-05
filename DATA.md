# Data downloads

이 공간은 Resimanor가 공개하는 주택금융 계산 데이터의 문서 허브입니다.

## Canonical source

- [Resimanor 2026 주택금융·DSR 데이터센터](https://resimanor.com/housing-finance-dsr-data/)
- [자료 이용·인용 정책](https://resimanor.com/citation-policy/)

## CSV files

### 연소득별 스트레스 DSR 주담대 한도 예시

- [income_mortgage_limits.csv](./income_mortgage_limits.csv)
- 원문 데이터센터: https://resimanor.com/housing-finance-dsr-data/

포함 항목:

- 연소득
- 비교 시나리오
- 심사금리
- DSR 한도
- 주담대 추정 한도
- 실제금리 가정
- 만기와 상환방식
- 기준일

### 신용대출 잔액별 주담대 한도 예시

- [credit_debt_mortgage_limits.csv](./credit_debt_mortgage_limits.csv)
- 원문 데이터센터: https://resimanor.com/housing-finance-dsr-data/

포함 항목:

- 연소득
- 기존 신용대출 잔액
- 기존 대출의 연간 원리금
- 신규 주담대에 남는 연간 원리금
- 주담대 심사금리
- 주담대 추정 한도
- 기준일

## Important note

이 데이터는 동일한 가정에서 제도 효과를 비교하기 위한 계산 예시입니다. 실제 금융기관의 대출 승인한도는 LTV, 인정소득, 기존 부채, 주택가격, 규제지역, 금리유형, 만기와 금융기관 내부 심사에 따라 달라질 수 있습니다.


## 입주자모집공고 정정 이력 파일럿

2026-10-05 기준 공식 정정공고의 변경 전/후 값을 이벤트 단위로 보존한 연구 파일럿입니다.

- [파일럿 문서](./datasets/recruitment-notice-corrections-2026/README.md)
- [공개 가능 6개 검증 이벤트 CSV](./datasets/recruitment-notice-corrections-2026/correction-events-public-pilot-2026-10-05.csv)
- [전체 작업 seed](./datasets/recruitment-notice-corrections-2026/correction-events-seed-2026-10-05.csv)
- [방법론](./datasets/recruitment-notice-corrections-2026/METHODOLOGY.md)
- [품질검사 기준](./datasets/recruitment-notice-corrections-2026/QUALITY-CHECKS.md)

이 파일럿은 전국 2026년 정정공고 전체를 대표한다고 주장하지 않으며, DOI를 부여하지 않은 방법론 검증용 스냅샷입니다.
