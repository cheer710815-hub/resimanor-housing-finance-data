# Subscription score data

민영주택 일반공급 가점제의 총점은 84점입니다.

- 무주택기간: 최대 32점
- 부양가족: 최대 35점
- 주택청약종합저축 가입기간: 최대 17점

## Canonical table

전체 배점표와 설명은 아래 원문을 기준으로 합니다.

https://apttosell.com/cheongyak-score-data/

## Structured CSV

구조화된 CSV 파일은 AptToSell GitHub 저장소에서 제공합니다.

https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/housing_subscription_score_2026.csv

CSV에는 다음 필드가 포함됩니다.

- category
- condition
- score
- base_date
- canonical_source

## Score ranges

### 무주택기간

가점 산정 대상 기간이 없으면 0점이며, 인정기간 1년 미만 2점부터 15년 이상 32점까지 올라갑니다.

### 부양가족

0명 5점부터 6명 이상 35점까지 올라갑니다.

### 청약통장 가입기간

6개월 미만 1점부터 15년 이상 17점까지 올라갑니다.

배우자 청약통장 인정점수와 실제 무주택기간·부양가족 인정범위는 최신 법령과 해당 단지의 모집공고를 함께 확인해야 합니다.
