# 2025 Korea Newlywed Special Supply: Announcement-Level Allocation Audit

**ARHRN study:** `ARHRN-INDEPENDENT-BRIDAL-SPECIAL-SUPPLY-REFORM-20261108`  
**Release:** 2026-11-17 · **Status:** Public descriptive replication note; **not peer reviewed; no DOI**.

## Research question
Did the *observed share of newlywed special-supply allocations* in sampled private-apartment subscription notices change around the 2025-03-31 revision of Article 41 of the Housing Supply Rules?

**Historical rule:** the 2025-03-31 amendment changed the specified newlywed percentage from 18% to 23%. Subsequent revisions, including in 2026, must not be confused with this historical comparison. The observation below is **not an estimate of the amendment's causal effect**.

## Dataset and scope
- Official origin: Korea Real Estate Board (한국부동산원), 청약홈 APT 분양정보 and APT 주택형별 분양정보; **2025-11-28 snapshots**, locally retained.
- Private-sale APT notices, notice dates 2024-01-01–2024-11-28 and 2025-01-01–2025-11-28; housing types whose numeric type designation is ≤85㎡.
- **502 unique notices:** 276 in 2024, 226 in 2025; observations are **partial-year** and are neither a census of 2025 nor of all housing deliveries.
- Unit-weighted allocation share = newlywed special-supply units / (general + special-supply units) for included types × 100.
- The denominator is the ApplyHome *subscription-eligible supply volume in the included type rows*, **not** a development's full construction quantity.
- The grouping boundary is **notice date**, not the unknown approval application date.

## Four observed cohorts
| Period | Notices | Included supply units | Newlywed units | Allocation share |
|---|---:|---:|---:|---:|
| 2024 before March 31 | 64 | 25,924 | 4,559 | 17.58602% |
| 2024 March 31 onward | 212 | 93,456 | 16,311 | 17.45313% |
| 2025 before March 31 | 32 | 10,965 | 1,889 | 17.22754% |
| 2025 March 31 onward | 194 | 81,404 | 18,168 | 22.31831% |

The difference between the **2025 before/after change** and the analogous **2024 calendar split** is **+5.22366 percentage points**. It is a *descriptive four-cohort contrast*, **not causal difference-in-differences identification**; no parallel-trends assumption was established.

**Sensitivity:** each notice weighted equally gives +6.87572 percentage points. A 5,000-replicate notice-level within-cohort resampling yielded a descriptive interval of +4.01864 to +6.66144 points; this is *not a confidence interval for causal policy effects*.

## Reproduce from original official files
1. Download the official **2025-11-28 snapshot** notice and housing-type CSVs from the corresponding public-data catalog or request the historic version from the provider. The exact snapshot is necessary: later extracts can differ.
2. Verify SHA-256:
   - Notice CSV: `da0722409157619242fb614c145541051e1584aadfd1176f946910c5085d4ae2`
   - Type CSV: `f6a71618eee61414d9cc401f047192ea218f711927396fc5c1786060406d8642`
3. Run `python reproduce_from_official.py "NOTICE.csv" "TYPE.csv"` (standard library only; CP949 encoding). The script asserts all four totals and the contrast.
4. Aggregated data: [four_cohort_summary.csv](./four_cohort_summary.csv). **Original raw official CSVs are not redistributed in this repository.** License/redistribution rights of the source must be checked separately.

## Material limitations / citation guidance
- The selection of notices and projects changes over time and across regions; this study does **not** estimate additional homes allocated **because of** the rule.
- Full original project approval/exception documentation and correction history were **not verified for all 502 notices**; 8 of 10 targeted PDFs were secured during internal audit.
- Legal mandated allocation percentage and this calculated ratio use different denominators.
- These data cannot measure application behavior, successful applications, contract execution, or actual occupancy.
- No DOI has been issued and publication here does not imply journal acceptance or independent expert review.

**Suggested citation:** ARHRN (2026). *2025 Korea Newlywed Special Supply: Announcement-Level Allocation Audit*. GitHub descriptive replication note, release 2026-11-17. Cite the exact repository path and accessed revision.

## Source and prior work
- [2025-03-31 Housing Supply Rules amendment, Article 41](https://law.go.kr/LSW/lsRvsDocListP.do?chrClsCd=010202&lsId=008243&lsRvsGubun=all)
- [2025-03-31 Newlywed Special Supply Operational Guidance](https://www.law.go.kr/LSW/admRulInfoP.do?admRulSeq=2100000256910)
- [Korea Real Estate Board housing subscription data portal](https://www.data.go.kr/)
- Korea Construction Economy Research Institute (CERIK), *특별공급 청약제도의 운영 실태와 과제* (2025-04), important related prior study: https://www.cerik.re.kr/uploads/report/2962/%ED%8A%B9%EB%B3%84%EA%B3%B5%EA%B8%89%20%EC%B2%AD%EC%95%BD%EC%A0%9C%EB%8F%84%EC%9D%98%20%EC%9A%B4%EC%98%81%20%EC%8B%A4%ED%83%9C%EC%99%80%20%EA%B3%BC%EC%A0%9C.pdf

**Correction pathway:** GitHub Issues in the parent repository, referencing this research ID and the source snapshot.
