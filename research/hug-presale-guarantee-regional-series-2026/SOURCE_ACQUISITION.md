# Official source acquisition record — pending

Catalog: https://www.data.go.kr/data/15002513/fileData.do

Official catalog values verified 2026-10-09:
- Title: 주택도시보증공사_분양보증 발급현황_20260630
- Provider: 주택도시보증공사 (HUG)
- Source data date: 2026-06-30
- Catalog modified: 2026-09-30
- Format: CSV; portal reports 818 rows
- Columns: 연도 / 지역 / 보증실적(억원) / 세대수
- Update cycle: quarterly
- Reuse restriction: none, as indicated by catalog

## Acquisition status
**NOT DOWNLOADED**. The catalog is accessible but its download control did not expose a downloadable attachment through available retrieval methods. No source file has been ingested, and no derived data have been calculated. Do not present catalog row counts as observed CSV row counts.

## Manual acquisition procedure
1. Open the catalog above and select the CSV Download control.
2. Preserve the **original downloaded CSV** without editing it.
3. Feed that CSV to `analyze_hug.py`; retain SHA-256 in the validation report.
4. Investigate any mismatch with the portal-reported 818 records, unknown periods, duplicates, subtotals and zero denominators.
5. Publish cleaned tables only after source-vs-derived spot checks and an explicit validation report.

**No DOI or dataset version should be registered before real values are validated.**
