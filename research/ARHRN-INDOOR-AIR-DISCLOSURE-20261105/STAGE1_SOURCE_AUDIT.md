# Stage 1: Government-source attachment discovery and licensing gate

**Study:** ARHRN-INDOOR-AIR-DISCLOSURE-20261105  
**Audited:** 2026-11-05  
**Status:** SOURCE DISCOVERY PASSED for September and October 2025 only; **DATA RELEASE BLOCKED**

## Verified primary-source attachments

| Source page | Government attachment URL | Observed PDF length | Verification |
| --- | --- | --- | --- |
| [Seoul September 2025](https://news.seoul.go.kr/env/archives/565412) | https://news.seoul.go.kr/env/files/2025/11/69140ab3033867.75787033.pdf | 1 page | Official HTML linked PDF; machine-readable extracted text visible |
| [Seoul October 2025](https://news.seoul.go.kr/env/archives/566501) | https://news.seoul.go.kr/env/files/2025/12/692d52afee9dd5.27398510.pdf | 2 pages | Official HTML linked PDF; machine-readable extracted text visible |

The source web tool returned document text including room-level readings, measurement dates, analytes and units. **Independent PDF screenshot rendering and local binary acquisition both failed due source-access/tool restrictions.** This is a source-discovery milestone, not a fully audited row-level numerical dataset.

## Methodologically important preliminary findings

- The source-page month is **not necessarily the measurement month**: the September posting's attached text includes July 14 and August 26 readings; the October posting includes October 23 readings and November 3 follow-up entries.
- A single listed apartment development can contain multiple dwellings and multiple measurement dates. Hence the unit of observation must be established as **building/development × dwelling × analyte × measurement date × test status**, with linked versions, rather than counting one project or one calendar listing as one measurement.
- Missing-looking cells represented by a dash cannot automatically be converted to zero. Subsequent test rows may report only the analytes retested.
- City-published tables include both **radon closed-space and ventilated readings**, not a single interchangeable radon measure.
- Reported concentrations must not be treated as independent of resampling or retesting without the original layout and row alignment being checked.

## Copyright, redistribution and safety gate

The government source pages display **KOGL Type 4 (attribution + non-commercial + no modification)**. Consequently, **do not upload their source PDFs to GitHub, Figshare or other mirrors and do not release a transformed measurement-row dataset without a documented licensing assessment or specific additional reuse permission**. This is especially important when linking research to monetized websites. This README contains only original research-method commentary and hyperlinks to the primary sources.

The links above do not constitute a license grant for derivative numeric data. Researchers can consult the originals at the linked government pages.

## Next checks

1. Retrieve all five August–December PDFs as verified source bytes in an appropriately restricted work environment and inspect visual tables manually before any row extraction.
2. Record stable names, street addresses where available, dwelling IDs (internally only), measurement date, analyte, unit, retest flag, and PDF page/row position, avoiding unnecessary publication of household-level details.
3. Reconcile repeating apartment names across months using both development identity and measurement dates. Do not equate recurring publication to duplicate source observations.
4. Evaluate reuse permission for numeric extracts before releasing any curated dataset, code-derived tables or figures.
5. Decide **PUBLISH / IMPROVE / SITE-ONLY / STOP** based on independent public use value and documented permission. No DOI or Figshare record at this stage.

## Platform status

- GitHub: Stage 0 research design and this Stage 1 source/rights audit only.
- Figshare: user authorization granted but **no registration completed**; source values/reuse rights not cleared.
- Zenodo: excluded per user decision.
- DOI: not assigned.

**Caution:** No pollutant standard exceedance percentages, building rankings, health impacts or regional comparisons have been independently calculated or approved.
