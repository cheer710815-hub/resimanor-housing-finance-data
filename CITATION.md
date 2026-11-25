# Citation guide

Resimanor 주택금융 데이터를 인용할 때는 가능한 경우 **원문 데이터 페이지와 보존 DOI를 함께 표시**해 주세요.

## Recommended citation

> Resimanor, "2026 스트레스 DSR 주택담보대출 데이터", https://resimanor.com/housing-finance-dsr-data/. DOI: https://doi.org/10.5281/zenodo.22840870

## Canonical identifiers

- Zenodo version DOI: https://doi.org/10.5281/zenodo.22840870
- Zenodo concept DOI: https://doi.org/10.5281/zenodo.22840869

## Archival mirrors and related public records

- Figshare DOI: https://doi.org/10.6084/m9.figshare.33948214
- Harvard Dataverse DOI: https://doi.org/10.7910/DVN/Y4J5LD
- Mendeley Data DOI: https://doi.org/10.17632/xssjnmrhh4.1
- Mendeley Data: https://data.mendeley.com/datasets/xssjnmrhh4/1
- GitHub: https://github.com/cheer710815-hub/resimanor-housing-finance-data
- GitBook documentation: https://housing-data-korea.gitbook.io/housing-data-korea-docs/
- Hugging Face: https://huggingface.co/datasets/eunguneun/korea-stress-dsr-mortgage-limit-2026
- Kaggle: https://www.kaggle.com/datasets/resimanor/korea-stress-dsr-mortgage-limit-2026
- Zenodo Community: https://zenodo.org/communities/resimanor-housing-finance-data/

## Reuse policy

재사용 범위와 출처 표시 원칙은 [Resimanor 자료 이용·인용 정책](https://resimanor.com/citation-policy/)을 확인해 주세요. 저장소의 라이선스 표기는 CC BY 4.0입니다.


## Research pilot citation

> Kim, Eun. (2026). *South Korea Housing Recruitment Notice Correction History 2026 — Pilot* (Version 0.1-pilot). Resimanor GitHub repository.

- Pilot documentation: https://github.com/cheer710815-hub/resimanor-housing-finance-data/tree/main/datasets/recruitment-notice-corrections-2026
- Public-ready pilot CSV: https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/datasets/recruitment-notice-corrections-2026/correction-events-public-pilot-2026-10-05.csv
- Snapshot date: 2026-10-05
- DOI: not assigned because this is a bounded, non-exhaustive pilot
- License for Resimanor-created metadata/derived fields: CC BY 4.0


## Dataset-level license and version boundaries (checked 2026-11-22)

- **CC BY 4.0 scope:** reuse the publisher-created dataset tables, explanatory metadata, and derived reference materials that are explicitly marked CC BY 4.0, following attribution and change-notice requirements. A repository-level license declaration does **not** automatically relicense original government data, linked third-party materials, separately licensed subprojects, photographs, or entire website articles. Check the source and each dataset folder first.
- **Where to start:** [canonical data center](https://resimanor.com/housing-finance-dsr-data/) · [site reuse/citation policy](https://resimanor.com/citation-policy/) · [CC BY 4.0 text](https://creativecommons.org/licenses/by/4.0/).
- **GitHub is mutable:** cite the exact file path, checked date, and preferably the commit SHA when reusing a changing `main` branch file. A revised README or a green CI workflow does not create a new dataset version or amend any previously archived DOI release.
- **Citation identity:** cite the dataset actually used. DOI references elsewhere in this repository may point to *distinct* studies and archived versions. An untested DOI link must not be described as confirmed publicly accessible.
- **Quality limitations:** the public checks validate structure, formula assumptions, and/or CSV-widget equality, not the current legal validity of housing eligibility, loan approvals, or a particular project notice.

## Distinct mortgage scenario datasets

- [2026 H2 DSR mortgage limit scenarios (160 cases)](./datasets/dsr-mortgage-limit-2026-h2/): archived version identifier `10.5281/zenodo.23231673`; [methodology](./datasets/dsr-mortgage-limit-2026-h2/METHODOLOGY.md) and [validation](./datasets/dsr-mortgage-limit-2026-h2/VALIDATION_REPORT.md).
- [Auto installment mortgage DSR scenarios (64 cases)](./datasets/auto-installment-mortgage-dsr-2026/): archived version identifier `10.5281/zenodo.23274478`; [calculation assumptions](./datasets/auto-installment-mortgage-dsr-2026/README.md) and [validation](./datasets/auto-installment-mortgage-dsr-2026/VALIDATION.md).

These identifiers refer to different datasets, not alternate identifiers for the basic DSR dataset above. Use the dataset-specific citation metadata, identify the exact version or Git revision used, and distinguish modeled scenarios from actual lending outcomes. Current DOI accessibility was not tested. The documentation clarification does not constitute a new dataset release.
