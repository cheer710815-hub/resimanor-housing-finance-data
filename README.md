# Resimanor Housing Finance Data

주택 구입에 필요한 자기자금, 대출 한도, 월 상환액과 총비용을 계산하고 검증하기 위한 공개 자료 저장소입니다.

## Website

- https://resimanor.com/

## Canonical data source

- [2026 스트레스 DSR 주택담보대출 데이터](https://resimanor.com/housing-finance-dsr-data/)
- 기준 공개본: 2026-09-18
- Zenodo DOI: https://doi.org/10.5281/zenodo.22840870
- Zenodo concept DOI: https://doi.org/10.5281/zenodo.22840869
- Zenodo Community: https://zenodo.org/communities/resimanor-housing-finance-data/
- Figshare DOI: https://doi.org/10.6084/m9.figshare.33948214
- Harvard Dataverse DOI: https://doi.org/10.7910/DVN/Y4J5LD
- Hugging Face dataset: https://huggingface.co/datasets/eunguneun/korea-stress-dsr-mortgage-limit-2026
- Kaggle dataset: https://www.kaggle.com/datasets/resimanor/korea-stress-dsr-mortgage-limit-2026

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
