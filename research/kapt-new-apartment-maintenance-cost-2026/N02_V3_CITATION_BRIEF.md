# N02 v3 — Research citation and media brief (22 October 2026)

## Canonical research record

**Title:** Changes in Apartment Maintenance Cost Components During the First 24 Months: A 60-Complex Study in South Korea

**Version-specific DOI:** https://doi.org/10.5281/zenodo.23553560  
**Zenodo landing page:** https://zenodo.org/records/23553560  
**All-versions DOI:** https://doi.org/10.5281/zenodo.23393935  
**Previous v2 DOI:** https://doi.org/10.5281/zenodo.23432629  
**Readable Korean analysis:** https://resimanor.com/new-apartment-maintenance-cost-24-month-analysis/  
**Research protocol:** https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/research/kapt-new-apartment-maintenance-cost-2026/RESEARCH_PROTOCOL.md

The authorship and preferred citation string should follow the **metadata actually displayed in Zenodo v3**. Do not treat this brief as an independent publication or mint another DOI for it.

## What the study measured

- Selected **60 apartment complexes** in South Korea (20 earlier + 40 added)
- **24 consecutive observed reporting months** per complex, using **17 K-apt common-area cost API categories**
- **24,480 source-category request records**
- Strictly eligible units for each of three components: first 3 and last 3 monthly observations must all be present and nonzero
- For each eligible complex, relative change = (mean of months 22–24 / mean of months 1–3 − 1) × 100
- Study headline is the **median of these complex-level percentage changes**, **not** the increase in an average household bill

| Selected component | Strictly eligible complexes | Median change |
| --- | ---: | ---: |
| Labor/pay (`pay`) | 50 | +1.93% |
| Cleaning (`cleanCost`) | 50 | +2.24% |
| Security (`guardCost`) | 47 | +1.86% |

## Safe quotation / interpretation

Korean: “신축 아파트 60개 단지를 대상으로 준공 초기 24개월의 K-apt 공용관리비 세부 항목을 분석한 결과, 처음 3개월 대비 마지막 3개월의 단지별 변화율 중앙값은 급여 +1.93%(50단지), 청소비 +2.24%(50단지), 경비비 +1.86%(47단지)로 나타났다.”

English: “Among eligible complexes in a selected 60-complex K-apt sample, the median change in component costs from the first to the last three observed months was +1.93% for pay (n=50), +2.24% for cleaning (n=50), and +1.86% for security (n=47).”

## What it does **not** establish

- Not the change in total management fees or in any household's bill
- Not a nationally representative estimate
- Not proof that the first two years *cause* costs to stabilize or increase
- Not an inflation-adjusted or fully seasonally adjusted causal model
- Cannot freely add API categories to calculate a total, as categories can overlap
- The API's individual monetary-field unit and historical month-specific area denominator have not been independently established; **do not** quote the tentative per-㎡ values as official historical K-apt amounts
- Missing and zero amounts are distinct; sample sizes change with completeness rules

## For journalists, researchers and institutional resource curators

Link to the **existing** version-specific DOI above, preferably alongside the Korean explanatory article. Quote the sample, method, metric (median), eligibility counts and limitations when citing findings. Cross-reference the research protocol for study design and previous versions.

This page is an **attribution and re-use guide**, not an additional dataset deposit. It does not declare a separate open licence over the underlying K-apt raw responses.

## Discovery paths to check — not confirmed indexes or backlinks

- Google Dataset Search: Zenodo states that Dataset Search indexes Zenodo datasets. This does not prove that this individual v3 record is currently indexed.
- OpenAIRE EXPLORE: search the exact DOI and title before attempting any claim/link request. Do not create duplicate records.
- Institutional libraries and journalism data resource directories: use their **public editorial submission forms**, if relevant; respect curation policies. No bulk cold email, paid link placement, or fabricated citations.

**Last verified against:** Published Zenodo v3 screenshots and 60-complex independent statistical checks, 22 October 2026.

## Discovery verification — 22 October 2026

- Exact DOI `10.5281/zenodo.23553560` was searched on the public web with OpenAIRE and Google Dataset Search terms. **No N02-specific indexed entry was confirmed in those search results**. This is **not proof that it is absent from those indices**.
- Opening the DOI-specific OpenAIRE EXPLORE result URL and the Zenodo v3 record in the automated web reader failed with an access error. User-supplied Zenodo v3 screenshots had already verified that the record itself is published.
- **Google Scholar is not an appropriate index target for a Zenodo dataset**. Zenodo's official FAQ says Google Scholar does not index Zenodo; Google Dataset Search does index Zenodo datasets based on schema.org metadata, without guaranteeing immediate appearance of this individual record: https://support.zenodo.org/help/en-gb/18-general/61-is-zenodo-indexed-by-google-scholar
- OpenAIRE describes its source harvesting as approximately weekly: https://www.openaire.eu/faqs . Allow for indexing delay; query the exact DOI in EXPLORE again rather than creating an additional deposit.
- The OpenAIRE Link service is designed for genuine links among research results, ORCID and funding projects. It is **not** a generic backlink-submission tool; do not attach an unrelated funded project or create duplicate records: https://www.openaire.eu/claim-publication
- Check again after a reasonable harvesting interval. Record the exact public record URL if found; only then mark indexing **confirmed** in the central tracker.
