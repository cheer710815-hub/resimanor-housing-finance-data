# 자동차 할부금과 주택담보대출 DSR 한도 비교: 64개 가상 시나리오 (v1.0)

제작: Resimanor | 최초 작성일: 2026-10-09 | Zenodo 공개일: 2026-10-10

**Zenodo 정식 버전 DOI:** https://doi.org/10.5281/zenodo.23274478  
**전체 버전 DOI:** https://doi.org/10.5281/zenodo.23274477  
**라이선스:** CC BY 4.0

연소득(4천만·5천만·6천만·8천만 원) × 자동차 월 할부금(0·30만·60만·90만 원) × 가정 금리(4·5·6·7%)의 64개 가상 시나리오입니다.

## 산식
- 월 DSR 예산 = 연소득 × 0.40 / 12
- 월 주담대 상환 예산 = max(0, 월 DSR 예산 − 자동차 월 할부금)
- 월 이율 r = 연이율 / 12, 기간 n = 360개월
- 추정 대출원금 = 월 상환 예산 × (1 − (1+r)^(-n)) / r
- 한도 감소 = 동일 연소득·금리에서 자동차 할부 0원일 때 대출원금 − 해당 대출원금
- 금액은 원 단위 반올림

## 사용상 주의
자동차 월 할부금을 DSR 의무상환액으로 전액 차감하는 **연구용 단순화 모델**입니다. 실제 자동차 할부의 DSR 반영 여부와 방식은 금융기관·계약·규정에 따라 달라집니다. 기타 부채, 스트레스 DSR, LTV, 지역·주택가격 규제, 금융기관별 심사는 반영하지 않았습니다. 실제 대출 가능액이나 공식 규정 해석으로 사용하지 마십시오.

## 구성
- resimanor_auto_installment_mortgage_dsr_scenarios_2026_v1.csv (64행·11열)
- README.md
- CITATION.cff
- VALIDATION.md

## 인용
Kim, Eun (2026). *2026 Korea Mortgage DSR Scenarios: Impact of Monthly Car Installments on Loan Capacity (64 Cases)* (Version 1.0) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.23274478
