# Resimanor Housing Finance Data

South Korea's 2026 Stress DSR housing-finance reference data, including income-based mortgage borrowing examples and the effect of existing credit obligations on borrowing capacity.

이 저장소는 대한민국의 2026 스트레스 DSR 제도를 기준으로 연소득별 주택담보대출 한도와 기존 신용대출에 따른 한도 변화를 검증할 수 있도록 정리한 공개 자료입니다. 계산 근거는 금융위원회 등 공식 정책자료를 우선하며, CSV·JSON, 방법론, 출처 정책과 인용 메타데이터를 함께 제공합니다.

## Quick reference

- **Canonical data center:** https://resimanor.com/housing-finance-dsr-data/
- **Canonical GitHub repository:** https://github.com/cheer710815-hub/resimanor-housing-finance-data
- **Reference release:** 2026-09-18
- **Canonical DOI (Zenodo):** https://doi.org/10.5281/zenodo.22840870
- **License:** CC BY 4.0

For current methodology, machine-readable files, updates, and citation information, use the canonical data center and GitHub repository above.

## Website

- https://resimanor.com/

## Canonical data source

- [2026 스트레스 DSR 주택담보대출 데이터](https://resimanor.com/housing-finance-dsr-data/)
- 기준 공개본: 2026-09-18
- Canonical DOI (Zenodo): https://doi.org/10.5281/zenodo.22840870
- Zenodo concept DOI: https://doi.org/10.5281/zenodo.22840869
- Zenodo Community: https://zenodo.org/communities/resimanor-housing-finance-data/
- Hugging Face dataset: https://huggingface.co/datasets/eunguneun/korea-stress-dsr-mortgage-limit-2026
- Kaggle dataset: https://www.kaggle.com/datasets/resimanor/korea-stress-dsr-mortgage-limit-2026

## Legacy DOI mirrors

The exact dataset was also deposited in several DOI-minting repositories before the canonical-DOI policy was adopted. These records are retained as legacy mirrors only and should not be used as the preferred citation.

- Figshare: https://doi.org/10.6084/m9.figshare.33948214
- Harvard Dataverse: https://doi.org/10.7910/DVN/Y4J5LD
- Mendeley Data: https://doi.org/10.17632/xssjnmrhh4.1

**Preferred citation DOI:** https://doi.org/10.5281/zenodo.22840870

이 저장소는 위 원문 데이터 페이지의 계산 기준, 출처 정책과 재사용 정보를 보조하기 위한 공개 저장소입니다. 최신 설명과 수정 사항은 canonical data source를 우선합니다.

## Educational & institutional resource

- [INSTITUTIONAL-RESOURCE.md](./INSTITUTIONAL-RESOURCE.md) — 대학·연구기관·교육기관용 자료 안내
- [INSTITUTIONAL-LINK-PLAYBOOK.md](./INSTITUTIONAL-LINK-PLAYBOOK.md) — 기관형 링크 획득 운영 기준
- 추천 링크명: 스트레스 DSR 데이터센터 / 주택금융·DSR 데이터

## Media & citation kit

- [PRESS-KIT.md](./PRESS-KIT.md)
- [EMBED.md](./EMBED.md) — 복사해서 붙여넣을 수 있는 차트·출처 링크 코드
- [2026 하반기 스트레스 DSR 미디어 브리프](./MEDIA-BRIEF-2026-H2-STRESS-DSR.md)
- [기사·리포트용 비교 CSV](./media_stress_dsr_h2_2026.csv)


## Research indexing

- RePEc archive: https://cheer710815-hub.github.io/resimanor-housing-finance-data/RePEc/gyv/
- Archive handle: `RePEc:gyv`
- Series handle: `RePEc:gyv:resfin`
- Series: Resimanor Housing Finance Research Notes

The RePEc archive directory contains the archive template, series template, and paper templates used for research-indexing and mirroring. The public archive URL has been submitted to the RePEc archive maintainer for inclusion.

## Public documentation

- [DagsHub public repository](https://dagshub.com/cheer710815-hub/resimanor-housing-finance-data)
- [GitLab public mirror](https://gitlab.com/housing-data-korea-group/resimanor-housing-finance-data)
- [GitBook public documentation](https://housing-data-korea.gitbook.io/housing-data-korea-docs/)

## Reference and citation pages

- [2026 주택금융·DSR 데이터센터](https://resimanor.com/housing-finance-dsr-data/)
- [자료 이용·인용 정책](https://resimanor.com/citation-policy/)
- [2026 전세안전 데이터센터](https://resimanor.com/jeonse-safety-data/)

외부 데이터 저장소에서 이 자료를 인용하거나 재사용할 때는 가능한 경우 위 원문 데이터 페이지와 인용 정책을 함께 확인해 주세요.

## Related public datasets

### Korea Bogeumjari Loan Rates 2026

- Canonical source: https://resimanor.com/%eb%b3%b4%ea%b8%88%ec%9e%90%eb%a6%ac%eb%a1%a0/
- Kaggle dataset: https://www.kaggle.com/datasets/resimanor/korea-bogeumjari-loan-rates-2026

보금자리론 만기별 금리와 주요 조건을 비교할 수 있도록 정리한 공개 데이터입니다.

## Purpose

이 저장소는 주택금융 정보를 단순 요약하는 데 그치지 않고, 공식 자료를 바탕으로 계산 기준과 판단 과정을 공개하기 위해 운영합니다.

## Coverage

- 주택담보대출과 스트레스 DSR
- 보금자리론, 디딤돌대출 등 정책대출
- 주택가격별 필요 자기자금
- 금리와 상환기간별 월 상환액
- 취득세 등 주택 구입 부대비용

## Repository structure

- `METHODOLOGY.md`: 자료 수집, 계산, 검수 원칙
- `SOURCE_POLICY.md`: 허용 출처와 인용 원칙
- `CITATION.cff`: GitHub·연구도구용 인용 메타데이터
- `datapackage.json`: 원문 URL, DOI, 라이선스와 주제 키워드를 담은 기계판독형 데이터 패키지 메타데이터

## Data policy

1. 정부기관과 공공기관의 원문을 우선합니다.
2. 계산에 사용한 기준일, 금리, 기간과 가정을 함께 표시합니다.
3. 정책 변경 가능성이 있는 수치는 기준일을 명시합니다.
4. 계산 결과는 개별 금융기관의 실제 심사 결과와 다를 수 있습니다.

## Citation

자료를 인용할 때는 저장소 이름, 문서 제목, 기준일과 원문 URL을 함께 표시해 주세요.

권장 원문 표기:

> Resimanor, "2026 스트레스 DSR 주택담보대출 데이터", https://resimanor.com/housing-finance-dsr-data/

## Disclaimer

본 저장소는 정보 제공을 목적으로 하며 대출 승인, 투자 수익 또는 특정 금융상품의 적합성을 보장하지 않습니다. 실제 의사결정 전에는 관계기관과 금융기관의 최신 기준을 확인해야 합니다.


## Developer access

Machine-readable JSON:
https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/stress_dsr_mortgage_examples_2026.json

CSV:
https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/income_mortgage_limits.csv

Use the JSON endpoint for apps, MCP servers, agents, and web tools that need reproducible example scenarios for stress DSR and mortgage-limit comparisons.


## Monthly reference snapshots

- September 2026: https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/reports/2026-09-reference-snapshot.md


## Media brief

- September 2026: https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/media/MEDIA-BRIEF-2026-09.md


## Institutional submission kit

- https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/INSTITUTIONAL-SUBMISSION-KIT.md


## Machine-readable catalog metadata

DCAT 3 JSON-LD:
https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/dcat.jsonld

This file describes the repository's public datasets and distributions using the W3C Data Catalog Vocabulary (DCAT), so data catalogs, research tools, and agents can discover the dataset metadata in a standard machine-readable form.

## Related housing-subscription resource

- [AptToSell 2026 청약·분양 데이터센터](https://apttosell.com/housing-subscription-data/) — 청약가점, 예치금, 입주자모집공고 확인 기준을 정리한 관련 공개 데이터 문서입니다.

## Publisher identity

- ORCID: https://orcid.org/0009-0006-9445-4768
- About.me: https://about.me/eunk
- Gravatar: https://gravatar.com/vegadus2
- GitHub: https://github.com/cheer710815-hub



## Research pilot: recruitment notice correction history

- [South Korea Housing Recruitment Notice Correction History 2026 — Pilot](./datasets/recruitment-notice-corrections-2026/README.md)
- Version: **0.1-pilot**
- Snapshot: **2026-10-05**
- Public-ready events: **6**
- Public-ready projects: **3**
- DOI: **not assigned — pilot coverage is intentionally bounded and non-exhaustive**

This pilot preserves before/after values from official correction notices as event-level change history instead of overwriting the original recruitment-notice state.

## Dataset — 2026 H2 DSR mortgage-limit scenarios

- [2026 H2 Korea Mortgage DSR Limit Scenario Dataset](./datasets/dsr-mortgage-limit-2026-h2/README.md)
- Version: **1.0**
- Release date: **2026-10-07**
- Scenario rows: **160**
- License: **CC BY 4.0**
- Version 1.0 DOI: **https://doi.org/10.5281/zenodo.23231673**
- All-versions DOI: **https://doi.org/10.5281/zenodo.23231672**
- Zenodo publication date: **2026-10-08**
- [CSV](./datasets/dsr-mortgage-limit-2026-h2/resimanor_dsr_mortgage_limit_scenarios_2026_h2_v1.csv)
- [Methodology](./datasets/dsr-mortgage-limit-2026-h2/METHODOLOGY.md)
- [Data dictionary](./datasets/dsr-mortgage-limit-2026-h2/DATA_DICTIONARY.md)
- [Media / research summary](./datasets/dsr-mortgage-limit-2026-h2/MEDIA_RESEARCH_SUMMARY.md)

The dataset reports **DSR-based theoretical calculated limits**, not actual bank approval amounts. The 0.75% non-metropolitan/non-regulated value is a controlled analytical reference scenario and must not be interpreted as a universal fixed official stress rate.


## Dataset — Car installment impact on modeled mortgage DSR (64 scenarios)

- [Dataset documentation](./datasets/auto-installment-mortgage-dsr-2026/README.md)
- [CSV (64 scenarios)](./datasets/auto-installment-mortgage-dsr-2026/resimanor_auto_installment_mortgage_dsr_scenarios_2026_v1.csv)
- [Validation notes](./datasets/auto-installment-mortgage-dsr-2026/VALIDATION.md)
- [Citation metadata](./datasets/auto-installment-mortgage-dsr-2026/CITATION.cff)
- Version: **1.0** | Published: **2026-10-10** | License: **CC BY 4.0**
- Version DOI: **https://doi.org/10.5281/zenodo.23274478**
- All-versions DOI: **https://doi.org/10.5281/zenodo.23274477**

**Modeling caveat:** Monthly car installments are deducted in full as an illustrative DSR obligation. This assumption is not a statement of actual regulatory treatment or lender underwriting; stress DSR, LTV, other debts, and bank-specific criteria are excluded.
