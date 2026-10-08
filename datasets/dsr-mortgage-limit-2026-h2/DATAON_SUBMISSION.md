# DataON submission worksheet — 2026 H2 DSR scenarios

Status: **Prepared only — not submitted or approved** (2026-10-08).

## Official route

- DataON: https://dataon.kisti.re.kr/
- Official submission guide: https://dataon.gitbook.io/dataon-user-guide/registration/how_to_register
- Sign in, go to 연구데이터 등록 → 제출, review notices, select an eligible collection, complete metadata, license and file/source URL fields, then review and request approval.
- Collection eligibility and the service's current mandatory fields must be confirmed during submission. Do not invent a grant, institutional affiliation, research ID or ORCID.

## Metadata

- Title (KO): 2026년 하반기 소득·기존부채·지역별 주택담보대출 DSR 산출한도 160개 시나리오
- Title (EN): 2026 H2 Korea Mortgage DSR Limit Scenario Dataset by Income, Existing Debt and Region
- Creator: Resimanor
- Publication date: 2026-10-08
- Language: English dataset documentation, Korean and English descriptive metadata
- Type: Controlled scenario dataset; 160 rows, 16 columns
- License: CC BY 4.0
- Keywords (KO): 스트레스 DSR, 주택담보대출, 연소득, 기존부채, 대출한도, 주택금융
- Keywords (EN): Stress DSR, mortgage limit, existing debt, annual income, housing finance, South Korea
- Version DOI: https://doi.org/10.5281/zenodo.23231673
- Concept DOI: https://doi.org/10.5281/zenodo.23231672
- Source URL: https://github.com/cheer710815-hub/resimanor-housing-finance-data/tree/main/datasets/dsr-mortgage-limit-2026-h2
- Direct CSV URL: https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/datasets/dsr-mortgage-limit-2026-h2/resimanor_dsr_mortgage_limit_scenarios_2026_h2_v1.csv
- Validation: https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/datasets/dsr-mortgage-limit-2026-h2/VALIDATION_REPORT.md

## Abstract (KO)

2026년 하반기 대한민국 주택담보대출의 DSR 기준 이론적 신규 대출 산출한도를 비교하는 160개 통제 시나리오 데이터입니다. 연소득 4개 수준, 기존 대출의 월환산 DSR 원리금 부담 5개 수준, 신규 주담대 약정금리 4개 수준, 지역별 스트레스금리 분석 가정 2개를 조합했습니다. 은행권 DSR 상한 40%, 만기 30년, 원리금균등상환 조건을 가정한 계산 결과를 제공합니다. 실제 차주의 관측 데이터나 금융기관 대출 승인금액이 아니며, 비수도권·비규제지역의 0.75% 스트레스금리 값은 모든 대출에 적용되는 공식 일률 금리가 아닌 통제된 비교 가정입니다. CSV, 방법론, 변수 설명서, 구조 검증 보고서와 영구 식별자 DOI를 함께 제공합니다.

## Abstract (EN)

A controlled 160-row scenario dataset comparing theoretical DSR-based new mortgage limits under 2026 H2 South Korean assumptions. It combines four income levels, five monthly-equivalent existing DSR debt-service levels, four contractual mortgage rates and two regional stress-rate analytical scenarios, with a 40% bank DSR ceiling and 30-year equal-payment mortgage term. These are illustrative calculated limits, not observed borrower data or actual bank approvals. The 0.75% regional stress-rate scenario is a controlled analytical reference, not a universally applicable official rate. The release includes a CSV, methodology, data dictionary, structural validation report and Zenodo DOI.

## Before requesting approval

1. Check whether the selected collection accepts independently produced public scenario datasets.
2. Check that Zenodo DOI is entered as an **existing related identifier**, not falsely represented as a DataON-assigned DOI.
3. If uploading the CSV, comply with DataON filename constraints; retain original versioned filename in the canonical GitHub/Zenodo release.
4. Confirm the correct creator and contact details from the authenticated account.
5. Confirm CC BY 4.0 and the explicit analytical limitations.
6. Record DataON submission ID and approval status only after the platform returns them.

Legacy dataset DOI 10.5281/zenodo.22840870 belongs to a different dataset and must not be substituted.
