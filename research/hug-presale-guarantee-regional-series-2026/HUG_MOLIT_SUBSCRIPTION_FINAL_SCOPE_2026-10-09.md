# Final scope and evidence audit: HUG guarantees, MOLIT presales, and subscription demand

**Status: HUG/MOLIT cross-source comparison completed; year-over-year subscription-demand hypothesis remains untested.** Date: 2026-10-09.

## 1. Confirmed official inputs
**Ministry of Land, Infrastructure and Transport (MOLIT)**, June 2026 housing statistics, released 2026-07-31:
- National H1 presale housing units: 2025 **67,965**, 2026 **109,186** (+41,221, approximately +60.7%).
- Capital region: 2025 **40,986**, 2026 **63,586** (+22,600, approximately +55.1%).
- Primary source: https://molit.go.kr/USR/NEWS/m_71/dtl.jsp?id=95092274
- Secondary source describing government release: https://eiec.kdi.re.kr/policy/materialView.do?num=284940

**HUG** public guarantee-issuance dataset:
- Official portal: https://www.data.go.kr/data/15002513/fileData.do
- Cleaned 818-row processed dataset: [GitHub](./hug_presale_guarantee_clean_2009_2026q2.csv)
- 2025 H1 reported-region guarantee amount **202,579억원**, 2026 H1 **431,426억원**.
- 2025 H1 reported-region guaranteed units **45,023**, 2026 H1 **90,160**.
- **29 matched region-quarter cells**: 2025 **202,601억원** vs 2026 **426,340억원**, net difference **+223,739억원**; see [matched records](./hug_2025_2026_h1_matched_region_quarter.csv).

## 2. Interpretation allowed by evidence
Two separately defined official series have positive H1 year-over-year changes. The HUG geographic coverage is inconsistent between periods and has quality exceptions; matching observed region-quarter pairs mitigates some but not all bias.

**Disallowed inference:** No proof of higher subscription application volume, subscription competition ratios, real sales contracts, sales prices, housing-market recovery, or a causal HUG/MOLIT association. Never divide HUG households by MOLIT presale housing units and call it a guarantee rate or contract rate.

## 3. 2025 vs 2026 H1 subscription-demand verification: blocked on comparable data
AptToSell GitHub contains 2026 recruitment/subscription work; as of this audit a **complete, independently validated 2025 H1 comparison series using the same recruitment-notice period, rank, housing type, project identifiers, and application-count/eligible-supply rules has not been identified**.

Do **not** assert a 2025–2026 change in competition or applicant counts. Zero and missing cases must be kept separate; multi-type projects need explicit denominators; amendment dates and initial announcements must be reconciled; matched and unmatched cohorts should be reported separately.

### Exact research acceptance criteria if revisited
1. Collect 2025-01-01 to 2025-06-30 and 2026-01-01 to 2026-06-30 initial recruitment notices using the same official Applyhome endpoint/snapshot rules.
2. Map complex identifiers and all eligible housing types, competition/application categories, and initial announcement dates.
3. Preserve non-primary recruitment, cancellations, corrections and missing API responses in a documented exclusion log.
4. Publish one CSV for the complete comparable cohort and separate region/type analyses, with counts of source projects, analyzed projects, missing projects and negative/zero cases.
5. Compute applications and per-type applicants-per-eligible-unit; only then compare by same period, geography and supply category.
6. Do not claim causality without a design controlling confounders.

## 4. Completed public outputs
- [Source-aligned comparison CSV](./hug_molit_2025_2026_h1_cross_source_summary.csv)
- [Cross-source summary and caveats](./HUG_MOLIT_CROSS_SOURCE_H1_2026.md)
- [Official-2025/2026 matched HUG comparison](./H1_2025_2026_SUMMARY.md)
- [Canonical HUG DOI](https://doi.org/10.5281/zenodo.23262918) (**DOI covers HUG 818-row v1.0 deposit, NOT the newer cross-source table or matched panel**).

## 5. Release conclusion
**Final editorial conclusion:** 'In the first half of 2026, separately defined official housing presale and HUG guarantee issuance figures rose from H1 2025 levels. Whether the total number of housing subscription applicants or the intensity of competition increased is not established by these datasets.'

Avoid announcing a proven subscription-demand rebound. This document closes the present cross-source workstream at its defensible evidence boundary, pending acquisition of an appropriate 2025 baseline.

Resimanor WordPress post: **not published**; prior connector create attempt blocked by account/domain restrictions. Do not describe GitHub publication as WordPress publication.
