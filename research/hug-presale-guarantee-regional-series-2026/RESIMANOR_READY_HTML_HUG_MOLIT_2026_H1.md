# Resimanor 게시 전 최종 초안 — HUG×국토부 2026 상반기

- **Status:** prepared; NOT saved to WordPress; NOT published.
- **Title:** 2026 상반기 분양실적 60.7% 증가, HUG 분양보증도 늘었지만 청약 수요는?
- **Slug:** 2026-h1-presale-hug-guarantee-subscription-demand
- **SEO title:** 2026 상반기 분양실적과 HUG 분양보증 비교 | 청약 수요는?
- **Meta description:** 국토부 공동주택 분양실적 60.7% 증가와 HUG 분양보증 발급실적 변화를 2025·2026년 상반기 기준으로 비교했습니다. 청약 수요 검증의 한계도 설명합니다.
- **Focus keyword:** 2026 상반기 분양실적
- **Excerpt:** 2026년 상반기 분양실적은 전년 대비 60.7% 증가했습니다. HUG 보증실적과 나란히 비교하고, 청약 경쟁률 증가 여부는 왜 별도로 검증해야 하는지 살펴봅니다.
- **Featured image ALT (when a real image is created):** 2025년과 2026년 상반기 전국 공동주택 분양실적과 HUG 보증발급액의 비교
- **Featured image:** not yet created or uploaded. Do not claim one.
- **Publishing gate:** user approval required, WordPress connector domain lock unresolved.

## HTML custom block
```html
<!-- wp:html -->
<article>
<p><strong>2026년 상반기 전국 공동주택 분양실적은 10만9,186호로 전년 상반기 6만7,965호보다 60.7% 늘었습니다.</strong> 같은 기간 주택도시보증공사(HUG)의 지역별 분양보증 발급실적도 증가했습니다. 그러나 이것만으로 청약 경쟁률이나 청약 신청자 수가 증가했다고 말할 수는 없습니다. 실제 공급실적과 분양보증 발급실적은 서로 다른 통계이기 때문입니다.</p>
<h2>2026년 상반기 공동주택 분양실적은 얼마나 늘었나</h2>
<p><a href="https://molit.go.kr/USR/NEWS/m_71/dtl.jsp?id=95092274">국토교통부 2026년 6월 주택통계</a>에 따르면 전국 분양실적은 2025년 1~6월 67,965호에서 2026년 같은 기간 109,186호로 41,221호 증가했습니다. 수도권은 40,986호에서 63,586호로 22,600호 증가했습니다. 국토부가 집계한 분양실적은 계약 완료 세대수나 청약 신청 건수와 동일한 수치가 아닙니다.</p>
<h2>같은 기간 HUG 분양보증 발급실적은</h2>
<table><thead><tr><th>지표</th><th>2025년 상반기</th><th>2026년 상반기</th></tr></thead><tbody>
<tr><td>국토부 전국 공동주택 분양실적</td><td>67,965호</td><td>109,186호</td></tr>
<tr><td>국토부 수도권 공동주택 분양실적</td><td>40,986호</td><td>63,586호</td></tr>
<tr><td>HUG 기록상 보증발급액</td><td>202,579억원</td><td>431,426억원</td></tr>
<tr><td>HUG 기록상 세대수</td><td>45,023세대</td><td>90,160세대</td></tr>
</tbody></table>
<p>HUG 수치는 <a href="https://doi.org/10.5281/zenodo.23262918">Zenodo에 공개한 818행 데이터셋</a>을 같은 기간 기준으로 재집계한 것입니다. 원본에는 일부 지역·분기 기록이 없으며, 음수 보증실적이나 불분명한 지역명이 포함됩니다. 따라서 HUG 집계와 국토부 분양실적을 직접 나누거나 동일한 주택에 대한 수치로 연결할 수 없습니다.</p>
<h2>지역 누락을 고려해 29개 비교 관측치만 추출</h2>
<p>2025년과 2026년 모두 기록이 존재하는 동일 지역·동일 분기 29개 조합을 비교한 결과, HUG 분양보증 발급액은 202,601억원에서 426,340억원으로 223,739억원 증가했습니다. 이 수치는 <a href="https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/research/hug-presale-guarantee-regional-series-2026/hug_2025_2026_h1_matched_region_quarter.csv">공통 지역·분기 29행 CSV</a>에서 확인할 수 있습니다. 비교대상으로 잡히지 않은 관측치는 0으로 보정하지 않았습니다.</p>
<h2>청약 경쟁률도 높아졌을까</h2>
<p><strong>이번 데이터만으로는 판단할 수 없습니다.</strong> 청약 수요 증가 여부는 같은 기준으로 집계한 2025년과 2026년 상반기의 청약 모집 세대수와 신청 건수, 단지별·주택형별 경쟁률을 검증해야 합니다. 기존에 확보한 2026년 청약자료만으로 전년과의 증감률을 산출하지 않았습니다.</p>
<h2>공식 데이터와 분석 방법 다운로드</h2>
<p>원본 출처는 <a href="https://www.data.go.kr/data/15002513/fileData.do">HUG 분양보증 발급현황</a> 및 <a href="https://molit.go.kr/USR/NEWS/m_71/dtl.jsp?id=95092274">국토부 주택통계</a>입니다. Resimanor가 재구성한 <a href="https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/research/hug-presale-guarantee-regional-series-2026/hug_molit_2025_2026_h1_cross_source_summary.csv">두 통계의 비교 CSV</a>와 <a href="https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/research/hug-presale-guarantee-regional-series-2026/HUG_MOLIT_SUBSCRIPTION_FINAL_SCOPE_2026-10-09.md">검증 범위 및 제한사항</a>도 공개합니다. DOI 10.5281/zenodo.23262918은 HUG 원본 가공 데이터셋 v1.0에 부여된 번호이며 이번 교차분석 CSV에 별도로 발급된 DOI는 아닙니다.</p>
<h2>자주 묻는 질문</h2>
<h3>분양실적이 늘었으면 청약 신청도 늘었다는 뜻인가요?</h3>
<p>아닙니다. 분양실적과 청약 신청 건수는 다른 지표입니다. 동일기간 청약홈 신청자료를 확보해 별도로 비교해야 합니다.</p>
<h3>HUG 분양보증 발급액은 실제 분양가격인가요?</h3>
<p>아닙니다. 보증 발급실적이며 실제 분양가격·매매거래액과 동일하지 않습니다.</p>
<h3>왜 HUG 29개 지역·분기 조합만 비교했나요?</h3>
<p>일부 분기에는 특정 지역 기록이 누락돼 두 해에 공통으로 존재하는 조합만 비교했기 때문입니다.</p>
</article>
<!-- /wp:html -->

```
