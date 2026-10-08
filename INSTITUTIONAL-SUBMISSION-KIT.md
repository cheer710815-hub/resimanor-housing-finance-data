# Institutional Resource Submission Kit

Updated: 2026-10-08

This page provides copy-ready descriptions for universities, lifelong-learning centers, financial-education providers, journalists, and public-interest resource pages that want to review Resimanor as an educational reference.

## New dataset submission package — 2026 H2 DSR scenarios (published 2026-10-08)

**This is a separate 160-row dataset, not a new version of the 2026-09-18 income/credit-debt reference dataset described below.** Its DOI must not replace the older dataset's DOI.

- **Korean title:** 2026년 하반기 소득·기존부채·지역별 주택담보대출 DSR 산출한도 160개 시나리오
- **English title:** 2026 H2 Korea Mortgage DSR Limit Scenario Dataset by Income, Existing Debt and Region
- **Publisher / author:** Resimanor
- **Publication date:** 2026-10-08
- **Version:** 1.0
- **Type:** Dataset (scenario-based calculated reference data; not observed borrower or lender approval records)
- **Coverage:** South Korea, 2026 H2 scenario assumptions
- **Format:** CSV, methodology, data dictionary, citation file, validation report
- **Size:** 160 scenario rows, 16 columns
- **License:** CC BY 4.0 for original Resimanor data and documentation
- **Version DOI:** https://doi.org/10.5281/zenodo.23231673
- **All-versions DOI:** https://doi.org/10.5281/zenodo.23231672
- **Zenodo record:** https://zenodo.org/records/23231673
- **Source repository:** https://github.com/cheer710815-hub/resimanor-housing-finance-data/tree/main/datasets/dsr-mortgage-limit-2026-h2
- **Structural validation:** https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/datasets/dsr-mortgage-limit-2026-h2/VALIDATION_REPORT.md
- **Related analysis:** https://resimanor.com/%ec%a3%bc%eb%8b%b4%eb%8c%80-%ed%95%9c%eb%8f%84/

**Keywords (KO):** 스트레스 DSR, 주택담보대출, 대출한도, 기존부채, 연소득, 주택금융, 시나리오 분석

**Keywords (EN):** Stress DSR, mortgage borrowing limit, debt service, existing debt, income, South Korea, scenario dataset

### Korean abstract

Resimanor가 2026년 하반기 대한민국 주택담보대출 DSR 산출한도를 비교하기 위해 구축한 160개 통제 시나리오 데이터입니다. 연소득 4개 구간, 기존 DSR 원리금 부담 5개 구간, 신규 주담대 금리 4개 구간, 지역별 스트레스금리 기준 2개를 조합했습니다. 은행권 DSR 40%, 30년 원리금균등상환 등의 공통 가정하에 DSR 기준 이론적 신규 주담대 산출한도를 제공합니다. 실제 금융기관 승인금액이나 실측 대출 통계가 아닙니다. 비수도권·비규제지역 0.75%는 비교를 위한 통제된 기준값이며 모든 대상 대출에 일률적으로 적용되는 공식 스트레스금리를 뜻하지 않습니다. CC BY 4.0으로 공개하며 CSV, 방법론, 변수 설명서, 검증 보고서 및 DOI를 제공합니다.

### English abstract

A 160-row controlled scenario dataset comparing theoretical DSR-based new-mortgage limits in South Korea under second-half 2026 assumptions. It crosses four annual income levels, five monthly-equivalent existing DSR debt-service burdens, four contractual mortgage rates, and two regional stress-rate scenarios, using a 40% DSR ceiling and 30-year equal-payment term. The outputs are illustrative calculated limits, not observed lending outcomes or bank approvals. The 0.75% regional stress-rate assumption is an analytical reference, not a universally applicable official rate. The release includes a CSV, methodology, data dictionary, structural validation report, CC BY 4.0 license, and Zenodo DOI.

### Preferred citation

Resimanor (2026). *2026 H2 Korea Mortgage DSR Limit Scenario Dataset by Income, Existing Debt and Region* (Version 1.0) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.23231673

### Submission and interpretation guardrails

- Check that the destination explicitly accepts unsolicited datasets or external resources before submitting.
- Do not describe a generic contact address as a dedicated dataset-submission channel.
- Check recent outreach history to avoid repeated contact with the same person or team.
- Do not claim external acceptance, indexing, citation, or endorsement without confirmation.
- Structural validation does not independently verify all financial formulas or regulatory applicability.
- The legacy dataset's DOI 10.5281/zenodo.22840870 remains associated with that older dataset only.

---

## Recommended resource

**Name:** 2026 스트레스 DSR 및 주택금융 데이터센터

**Canonical URL:**  
https://resimanor.com/housing-finance-dsr-data/

**One-sentence description:**  
2026년 스트레스 DSR 기준, 연소득별 주담대 한도 비교, 기존 신용대출에 따른 한도 변화, 계산 가정과 CSV·JSON 데이터를 함께 제공하는 공개 주택금융 참고자료입니다.

## Educational use

Suitable for:

- 주택금융·대출 교육
- 스트레스 DSR 설명
- 내집마련 자금계획 교육
- 금융권 고객상담·PB·WM 교육 보조자료
- 기사·보고서의 DSR 기준 확인
- 앱·MCP·AI Agent의 재현 가능한 reference data

## Copy-ready institutional description

> Resimanor는 금융당국의 스트레스 DSR 기준과 계산 가정을 바탕으로 연소득별 주택담보대출 한도와 기존 신용대출에 따른 변화 예시를 CSV·JSON으로 공개하고 있습니다. 실제 금융회사 승인한도를 대신하는 자료가 아니라 교육·연구·기사 작성에서 제도와 계산 구조를 재현하기 위한 참고자료입니다.

## Suggested link labels

- 스트레스 DSR 데이터센터
- 주택금융·DSR 데이터
- 2026 주담대 한도 비교자료
- 주택금융 교육 참고자료

## Public documentation

GitBook documentation:  
https://housing-data-korea.gitbook.io/housing-data-korea-docs/

The GitBook site is a public documentation layer for the canonical Resimanor data center and GitHub repository.

## Data access

JSON:
https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/stress_dsr_mortgage_examples_2026.json

Income CSV:
https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/income_mortgage_limits.csv

Credit-debt CSV:
https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/credit_debt_mortgage_limits.csv

Media brief:
https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/media/MEDIA-BRIEF-2026-09.md

Citation policy:
https://resimanor.com/citation-policy/


## DataON submission metadata (prepared)

Use this block when submitting the dataset to KISTI DataON. Do not treat DataON as an active distribution until the DataON record is approved and a DOI is issued.

- **Korean title:** 2026 스트레스 DSR 주택담보대출 한도 및 기존 신용대출 영향 데이터
- **English title:** South Korea 2026 Stress DSR Mortgage Limits and Existing Credit Debt Impact Data
- **Reference date:** 2026-09-18
- **Language:** Korean / English metadata
- **License:** CC BY 4.0
- **Recommended collection:** 국가연구데이터플랫폼
- **Suggested subject:** Economics / Finance / Housing / Real Estate
- **Keywords (KO):** 스트레스 DSR, 주택담보대출, 주담대 한도, 신용대출, 주택금융, 대한민국, 2026
- **Keywords (EN):** Stress DSR, mortgage limit, housing finance, credit debt, South Korea, 2026
- **Canonical source URL:** https://resimanor.com/housing-finance-dsr-data/
- **GitHub repository:** https://github.com/cheer710815-hub/resimanor-housing-finance-data
- **Primary CSV:** https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/income_mortgage_limits.csv
- **Machine-readable JSON:** https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/stress_dsr_mortgage_examples_2026.json
- **Existing DOI (Zenodo):** 10.5281/zenodo.22840870
- **Existing DOI (Figshare):** 10.6084/m9.figshare.33948214
- **Existing DOI (Harvard Dataverse):** 10.7910/DVN/Y4J5LD
- **Existing DOI (Mendeley Data):** 10.17632/xssjnmrhh4.1

**Description (KO):**
2026년 대한민국 스트레스 DSR 제도를 기준으로 연소득별 주택담보대출 한도 예시와 기존 신용대출 보유 시 한도 변화를 비교할 수 있도록 구조화한 공개 연구·교육용 데이터입니다. 금융위원회 등 공식 정책자료를 우선 근거로 하며 계산 기준, 가정, CSV·JSON 원본과 재사용 정보를 함께 제공합니다. 실제 금융회사의 대출 승인 결과를 의미하지 않으며 제도·계산 구조를 재현하고 비교하기 위한 참고자료입니다.

**Description (EN):**
An open research and educational dataset that structures example mortgage borrowing limits under South Korea's 2026 Stress DSR framework and illustrates how existing credit debt can affect borrowing capacity. The dataset prioritizes official policy sources and provides assumptions, machine-readable CSV/JSON files, methodology, and reuse information. It is intended for reproducible reference and comparison rather than as a prediction of actual lender approval.
