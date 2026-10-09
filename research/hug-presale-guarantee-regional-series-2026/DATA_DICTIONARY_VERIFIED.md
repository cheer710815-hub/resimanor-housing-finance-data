# Data dictionary
- source_row: CSV 원본의 1-based 행번호(헤더=1)
- period: 원본 기간 표현
- year / quarter / period_type: 연도 및 분기 구분
- region_original / region_standard: 원본지역명 및 정규화한 17개 시도명(미확인 '전라'는 공란)
- guarantee_amount_100m_krw: 보증실적, 억원, 음수도 보존
- households: 세대수, 음수도 보존
- amount_per_household_100m_krw: 보증실적/세대수. 두 값 모두 양수인 경우만 표시. 실제 분양가 아님
- quality_flags: unmapped_region, negative_amount, negative_households, zero_households

Period summary는 정규화 가능한 17개 지역만 합산하며 없는 행은 0으로 보정하지 않습니다.
