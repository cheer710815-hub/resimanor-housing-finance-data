# N02: K-apt cost-field hierarchy and citation guide (2026-10-17)

**Status:** Official taxonomy cross-check; not a fresh re-download of every 2023–2025 monthly record.  
**Canonical research series:** [v2 20-complex report (DOI 10.5281/zenodo.23432629)](https://doi.org/10.5281/zenodo.23432629); historical [v1 pilot](https://doi.org/10.5281/zenodo.23393936).

## Official evidence and meaning

1. K-apt presents management expenses as a **hierarchy** rather than 17 freely additive independent totals. The official audit reconciliation interface lists common management costs, their main headings (general management, cleaning, security, disinfection, elevators, home-network upkeep, repairs/maintenance, management agency fees) and subheadings. Source: https://www.k-apt.go.kr/audt/ext/audtExtForm.do.
2. In particular, **labor cost (인건비)** is nested under **general management cost (일반관리비)**, and includes **salary/pay (급여)** plus allowances, bonuses, retirement costs, statutory insurance and welfare-related subcategories. Neither salary nor labor subcategories should be summed again on top of their parent general-management value.
3. **Repairs and maintenance (수선유지비)** is a parent of repairs (수선비), facilities upkeep (시설유지비), safety inspections (안전점검비) and disaster prevention (재해예방비). An official K-apt comparison table exposes parent code **1700** and its children **1701–1704**. Source: https://www.k-apt.go.kr/apiinfo/goApiSearchCompare_detail.do?bjdCodeR=11200114&bjdCodeT=1120010200&kaptCodeR=A13372101&kaptCodeT=A13302201&searchDate=201501.
4. Cleaning cost (청소비, code 1200), security cost (경비비, code 1300), disinfection (1400), elevator upkeep (1500), and home network upkeep (1600) appear as distinct headings within common management expenses in that official view. However, this alone does not prove that every API response field shares a common denominator/unit, or that the entire 17-endpoint collection can be summed to produce monthly total management charges.
5. K-apt also separates **common-area management costs**, **individual utility/use charges**, and **long-term repair reserve charges** in its management-cost displays. Source: https://www.k-apt.go.kr/.

## Rules for analysis

- **Do not sum all 17 API responses or all monetary fields.** Endpoint counts are data-acquisition/coverage measures (20 × 24 × 17 = 8,160 response records), not 8,160 independent total-cost observations.
- Report individual cost components (e.g. **pay**, **cleanCost**, **guardCost**) separately with their own documented API JSON field names; never label pay as all labor cost or all management cost.
- Treat API `null` and missing keys as **missing**; recorded `0` is a separate category that may represent no charge, non-reporting, or an initial occupancy condition. Never silently replace missing with 0.
- The strict sensitivity approach requires six usable nonzero values for a given component (first three and last three observed months), and comparisons are made at **complex level** before computing the **median** across complexes. Published v2 strict subset: 16 complexes, pay −8.00%, cleaning +0.30%, security −0.76%. These are descriptive, nonrepresentative estimates.
- Management floor area (`kaptMarea`) is preferred as the area denominator if analyzing area-adjusted cost **only after matching the official field's unit and source denominator**. Do not mix per-unit and per-square-meter API fields.
- Do not infer that source API figures have been freshly rechecked for subsequent amendments; latest audit checked archived 20-complex raw CSV against the derived tables, not contemporaneous K-apt live updates.
- Distinguish the source provider's data rights from the author's rights over the analytic report. Original raw API payloads are not included in the Zenodo report releases.

## Publication-quality checklist

| Check | Status |
|---|---|
| Official source category hierarchy | **Verified for representative official K-apt presentation** |
| Repair parent-child relationship | **Verified (1700, 1701–1704)** |
| General-management / labor / pay nesting | **Confirmed by official audit category listing; require endpoint field dictionary to validate all JSON keys** |
| Exact per-field units for each of 17 N02 API methods | **Open; do not claim validated** |
| Nationwide applicability / random sample | **Not supported** |
| Reuse license of all raw K-apt API data as redistributable dataset | **Not established; do not redistribute raw responses** |

**Citation wording:** “Eun Kim (Resimanor). *Early-stage apartment maintenance-cost trajectories in South Korea: Expanded 20-complex, 24-month observational analysis (2023–2026).* Zenodo v2 (2026). DOI: [10.5281/zenodo.23432629](https://doi.org/10.5281/zenodo.23432629).”
