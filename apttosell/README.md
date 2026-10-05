# Overview

South Korea's 2026 housing-subscription reference data for private housing applications, including the 84-point subscription score structure, regional deposit requirements, subscription competition/follow-up supply analysis, and apartment pre-move-in funding data.

AptToSell의 청약·분양 데이터 문서 공간입니다. 주택공급 관련 공식 규정을 바탕으로 민영주택 청약가점 84점 구조, 지역·면적별 청약 예치금, 공고 확인 기준과 인용 가능한 공개 데이터 자산을 연결합니다.

## Quick reference

* **Canonical data center:** https://apttosell.com/housing-subscription-data/
* **Canonical GitHub repository:** https://github.com/cheer710815-hub/apttosell-subscription-data
* **Subscription score Zenodo DOI:** https://doi.org/10.5281/zenodo.22842058
* **Pre-move-in funding Zenodo DOI:** https://doi.org/10.5281/zenodo.23157055
* **Figshare DOI:** https://doi.org/10.6084/m9.figshare.33948556
* **Harvard Dataverse DOI:** https://doi.org/10.7910/DVN/TSALWZ
* **2026 경쟁률·후속공급 분석 DOI:** https://doi.org/10.6084/m9.figshare.34064439
* **License:** CC BY 4.0

This GitBook space is the documentation layer within Housing Data Korea Docs. For versioned machine-readable files, methodology, source metadata, and updates, use the canonical GitHub repository above.

## Featured derived datasets

### 2026 아파트 청약 경쟁률과 후속공급 분석

* [Canonical analysis](https://apttosell.com/%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/)
* Project-level cohort: **196 projects**
* Competition-rate coverage: **193 projects**
* First-priority competition ≥10:1: **44 projects**
* Follow-up supply observed among them: **19 projects (43.2%)**
* 60-day observed rate: **36.1%**
* Figshare DOI: https://doi.org/10.6084/m9.figshare.34064439
* Hugging Face: https://huggingface.co/datasets/eunguneun/korea-apartment-subscription-followup-supply-2026
* [Detailed documentation](FOLLOWUP-ANALYSIS-2026.md)

> 후속공급 발생은 미계약률 또는 계약 실패율을 의미하지 않습니다.

### 2026 아파트 입주 전 필요자금 데이터

* [Canonical analysis](https://apttosell.com/%ec%95%84%ed%8c%8c%ed%8a%b8-%ec%9e%85%ec%a3%bc-%ec%a0%84-%ed%95%84%ec%9a%94%ec%9e%90%ea%b8%88/)
* Validation universe: **196 projects**
* Payment structure + financing conditions verified: **82 projects**
* Pre-move-in funding ratio calculable: **81 projects**
* Conservative public subset: **41 projects**
* Zenodo Version 1.0 DOI: https://doi.org/10.5281/zenodo.23157055
* Zenodo all-versions DOI: https://doi.org/10.5281/zenodo.23157054
* [Detailed documentation](PRE-MOVE-IN-FUNDING-2026.md)

### 2026 Verified Project Registry — Pilot

* Working version: **0.4-pilot**
* Stable project IDs assigned: **196**
* Pre-move-in public subset crosswalk: **41/41 matched**
* DOI: not assigned
* [Detailed documentation](VERIFIED-PROJECT-REGISTRY-2026.md)

This identity layer is intended as a cross-dataset join key and does not alter previously frozen DOI releases.

### 2026 Follow-Up Event Registry — Pilot

* First-event rows: **103**
* Stable project-ID matches: **103/103**
* Evidence-review queue: **103/103 screened**
* Numeric first follow-up notice IDs recovered: **103/103**
* Primary-verified events: **5**
* DOI: not assigned
* [Detailed documentation](FOLLOWUP-EVENT-REGISTRY-2026.md)

This layer extends the existing competition/follow-up analysis into event chronology without changing the published DOI dataset.

## Canonical pages

* [2026 청약·분양 데이터센터](https://apttosell.com/housing-subscription-data/)
* [2026 아파트 입주 전 필요자금 분석](https://apttosell.com/%ec%95%84%ed%8c%8c%ed%8a%b8-%ec%9e%85%ec%a3%bc-%ec%a0%84-%ed%95%84%ec%9a%94%ec%9e%90%ea%b8%88/)
* [2026 청약가점 84점 데이터표](https://apttosell.com/cheongyak-score-data/)
* [민영주택 청약 예치금 데이터표](https://apttosell.com/private-housing-deposit-data/)
* [자료 이용·인용 정책](https://apttosell.com/citation-policy/)

## Repository

원본 데이터 저장소는 아래 GitHub Repository에서 관리합니다.

https://github.com/cheer710815-hub/apttosell-subscription-data

## Persistent identifiers

* Subscription score Zenodo version DOI: https://doi.org/10.5281/zenodo.22842058
* Subscription score Zenodo concept DOI: https://doi.org/10.5281/zenodo.22842057
* Pre-move-in funding Zenodo Version 1.0 DOI: https://doi.org/10.5281/zenodo.23157055
* Pre-move-in funding Zenodo all-versions DOI: https://doi.org/10.5281/zenodo.23157054
* Figshare DOI: https://doi.org/10.6084/m9.figshare.33948556
* Harvard Dataverse DOI: https://doi.org/10.7910/DVN/TSALWZ

## Scope

* 민영주택 청약가점 84점 구조
* 무주택기간 배점
* 부양가족 배점
* 청약통장 가입기간 배점
* 민영주택 예치금
* 입주자모집공고와 정정공고 확인 원칙
* 분양가·계약조건·제한사항 확인 절차
* 청약 경쟁률과 후속공급 연결 데이터
* 아파트 입주 전 필요자금과 금융지원 구조

실제 청약 신청 전에는 반드시 최신 입주자모집공고, 정정공고와 관계기관 안내를 다시 확인해야 합니다.

### Related housing-finance resource

* [Resimanor 2026 주택금융·DSR 데이터센터](https://resimanor.com/housing-finance-dsr-data/) — 스트레스 DSR, 주택담보대출 한도 예시와 주택금융 계산 기준을 정리한 관련 공개 데이터 문서입니다.

### Publisher identity

* ORCID: https://orcid.org/0009-0006-9445-4768
* About.me: https://about.me/eunk
* Gravatar: https://gravatar.com/vegadus2
* GitHub: https://github.com/cheer710815-hub


### Primary-promotion access blocker

The Follow-Up Event Registry has completed notice-ID discovery for **103/103** first events. One event is direct-primary verified; the remaining 102 have corroborated numeric notice IDs but still require direct official-artifact inspection before promotion.


### Primary-verified event subset

The Follow-Up Event Registry now has a conservative **5-event direct-primary subset** based on official project-hosted recruitment notice artifacts. The remaining 98 events are not promoted beyond corroborated status without direct official-artifact inspection.


The current primary subset also includes **드파인 아르티아**, where the official SK DEFINE notice corrected the first-event ID from a later secondary-recovered notice to `2026910214`.
