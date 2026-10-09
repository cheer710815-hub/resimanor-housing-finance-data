# HUG 지역별 분양보증 발급현황 — 공식 CSV 검증 결과 (2026-10-09)

## 데이터 확보·검증 완료
- 공식 원본: `주택도시보증공사_분양보증 발급현황_20260630.csv`
- 공식 데이터 출처: https://www.data.go.kr/data/15002513/fileData.do
- 원본 CSV: CP949, **818행, 4열**: 연도 / 지역 / 보증실적(억원) / 세대수
- 2009~2015 연간, 2016~2026년 2분기까지 분기 기록
- 기간 종류 48개, 지역 표기 18종
- 누락 셀 0, 기간-지역 중복 0
- 음수 보증실적 13행, 음수 세대수 3행, 세대수 0인 21행(서로 중복될 수 있음)
- 미정규화 지역 1행: **2023년 4분기 ‘전라’** (원본 CSV 655행)
- 정규 17개 시도 합계에서는 '전라' 1행(보증실적 10,689억원, 세대수 3,509)을 보류·제외하고 별도 원본 보존

## 집계 결과 (17개 시도에 명확하게 분류되는 행만)
| 기간 | 보증실적 합계 (억원) | 세대수 합계 | 주의 |
|---|---:|---:|---|
| 2023 연간 | 1,033,193 | 267,242 | ‘전라’ 1행 제외 |
| 2024 연간 | 748,890 | 163,721 | 일부 분기 지역 행 누락 |
| 2025 연간 | 602,194 | 124,480 | 일부 분기 지역 행 누락 |
| 2026 1~2분기 | 431,426 | 90,160 | **반기 실적**, 연간 비교 금지 |

**주의:** 누락 지역 행은 0으로 채우지 않으며, 음수 원본값은 삭제하지 않았습니다. 음수값의 행정·회계적 의미는 별도 공식 해명이 필요합니다.

## 산출물
- Cleaned table: 818행, 원본값·품질 플래그 보존
- Quality-flags table: 이상 징후가 발견된 행만 분리
- Period summary and quarter summary, periods never mixed indiscriminately
- Methodology, data dictionary, validation report and executable build script

The complete verified dataset artifact was prepared in this analysis session; **this repository entry is a verification summary, not the CSV upload**. Do not claim the source data or derived CSV were committed to GitHub until they are actually uploaded.

## 인용 및 해석
HUG의 분양보증 발급현황은 실제 분양계약 체결량이나 아파트 시세 자료가 아닙니다. 가구당 보증실적은 단순 비율이지 평균 분양가격이 아닙니다. 원본: HUG; 분석 및 재구성: Resimanor, 2026. 원본 이용조건과 별개로 자체 가공 해설은 CC BY 4.0.

**DOI: 미발급. Resimanor 포스팅: 미발행.**
