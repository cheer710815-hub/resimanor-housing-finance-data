# 2026 Pre-Move-In Funding Dataset

**Korea Apartment Pre-Move-In Funding Dataset 2026** is a public South Korea apartment presale reference dataset built from initial housing recruitment notices published from January through September 2026. It standardizes contract deposits, interim-payment schedules, financing support, balance structure, and explicitly self-paid interim payments so projects can be compared on the same pre-move-in funding basis.

The validation universe covers **196 projects**. Payment structure and financing conditions are verified for **82 projects**, the standardized pre-move-in funding ratio is calculable for **81 projects**, and a conservative **41-project public subset** is released for external reuse under **CC BY 4.0**.

AptToSell의 **Korea Apartment Pre-Move-In Funding Dataset 2026**은 2026년 1월부터 9월까지의 아파트 최초 모집공고를 기준으로 계약금, 중도금, 잔금과 중도금 금융지원 구조를 검증한 공개 데이터셋입니다.

## Release summary

- Validation universe: **196 projects**
- Payment structure + financing conditions verified: **82 projects**
- Pre-move-in funding ratio calculable: **81 projects**
- Conservative public subset: **41 projects**
- Verification date: **2026-10-05**
- License: **CC BY 4.0**

## Core metric

**Pre-move-in funding ratio = total contract deposit rate + explicitly self-paid interim-payment rate**

Confirmed interest-free interim payments, deferred-interest financing, or arranged group lending are excluded from the standardized pre-move-in funding metric. The metric does not estimate an individual buyer's loan eligibility, actual bank approval, or total funds required at closing.

중도금 무이자, 이자후불, 집단대출 알선 등 사업주체의 금융지원이 확인된 중도금은 표준화된 입주 전 필요자금에서 제외합니다. 이 지표는 개인별 실제 대출 가능액이나 금융기관 승인 결과를 의미하지 않습니다.

## Initial conditions vs later promotions

Later residual-unit, first-come sales, reduced-deposit, cashback, or revised financing conditions are kept separate from the original recruitment conditions and are not retroactively applied to the initial-condition metric.

최초 모집공고 이후의 잔여세대, 선착순 공급, 계약금 인하, 페이백, 중도금 무이자 전환 등의 조건은 최초 모집공고 조건과 분리합니다. 이후 조건을 초기 지표에 소급 적용하지 않습니다.

## Persistent identifiers

- **Zenodo Version 1.0 DOI:** https://doi.org/10.5281/zenodo.23157055
- **Zenodo all-versions DOI:** https://doi.org/10.5281/zenodo.23157054
- **Canonical AptToSell page:** https://apttosell.com/%ec%95%84%ed%8c%8c%ed%8a%b8-%ec%9e%85%ec%a3%bc-%ec%a0%84-%ed%95%84%ec%9a%94%ec%9e%90%ea%b8%88/
- **Dataset repository:** https://github.com/cheer710815-hub/apttosell-subscription-data/tree/main/datasets/initial-contract-cash-2026
- **Public CSV:** https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/datasets/initial-contract-cash-2026/apttosell-initial-cash-publication-ready-2026-10-05.csv
- **Frictionless metadata:** https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/initial-contract-cash-2026/datapackage.json
- **Schema.org Dataset JSON-LD:** https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/initial-contract-cash-2026/schemaorg-dataset.jsonld

## Documentation

- Methodology: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/initial-contract-cash-2026/METHODOLOGY.md
- Data dictionary: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/initial-contract-cash-2026/DATA-DICTIONARY.md
- Media brief: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/initial-contract-cash-2026/MEDIA-BRIEF.md
- External submission kit: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/datasets/initial-contract-cash-2026/SUBMISSION-KIT.md

## Recommended citation

> Kim, Eun. (2026). *Korea Apartment Pre-Move-In Funding Dataset 2026* (Version 1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23157055

Use the Version 1.0 DOI for a fixed citation to the current release. Use the all-versions DOI when a link should resolve to the latest future release.

현재 공개본을 고정 인용할 때는 Version 1.0 DOI를 사용하고, 향후 최신 버전을 추적하려면 all-versions DOI를 사용합니다.
