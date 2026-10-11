# HUG Regional Presale Guarantee Data, 2009–2026 Q2

**Resimanor research dataset and supplementary analysis**  
**Canonical archived dataset:** [Zenodo v1.0, DOI 10.5281/zenodo.23262918](https://doi.org/10.5281/zenodo.23262918)  
**Research article:** [2026 H1 presale statistics and HUG guarantee comparison](https://resimanor.com/2026-h1-presale-hug-guarantee-analysis/)  
**Official HUG source:** [Public Data Portal — HUG presale guarantee issuances](https://www.data.go.kr/data/15002513/fileData.do)

## Scope

A reproducible, attributed analysis of 818 original HUG source rows covering regional presale-guarantee issuances from 2009 through 2026 Q2, including annual and quarterly observations. The repository preserves source irregularities rather than silently correcting or zero-filling them.

Known data-quality caveats include 13 negative guarantee amounts, 3 negative household values, 21 zero-household records, one ambiguous original region label (`전라`), and missing region-quarter cells. These conditions must be considered when comparing periods.

## Data files and follow-up material

- [`hug_presale_guarantee_clean_2009_2026q2.csv`](./hug_presale_guarantee_clean_2009_2026q2.csv): cleaned 818-row research dataset with traceable source rows and quality flags.
- [`HUG_MOLIT_CROSS_SOURCE_H1_2026.md`](./HUG_MOLIT_CROSS_SOURCE_H1_2026.md): cross-source interpretation of HUG guarantee issuance and MOLIT housing presales in 2025 H1 vs 2026 H1.
- [`hug_molit_2025_2026_h1_cross_source_summary.csv`](./hug_molit_2025_2026_h1_cross_source_summary.csv): reproducible cross-source summary of 2025/2026 H1.
- [`hug_2025_2026_h1_matched_region_quarter.csv`](./hug_2025_2026_h1_matched_region_quarter.csv): 29 matched region-quarter observations for a more comparable HUG issuance comparison.
- [`HUG_MOLIT_SUBSCRIPTION_FINAL_SCOPE_2026-10-09.md`](./HUG_MOLIT_SUBSCRIPTION_FINAL_SCOPE_2026-10-09.md): evidence audit and limits of inference.
- [`MEDIA_INSTITUTIONAL_BRIEF_2026-10-09.md`](./MEDIA_INSTITUTIONAL_BRIEF_2026-10-09.md): institutional and media brief, prepared only; **no external outreach has been authorized**.

**Version distinction:** The Zenodo v1.0 deposit is an archived 13-file dataset package. Later HUG–MOLIT cross-source analysis and the 29 matched-record supplement are hosted on GitHub and **are not part of the Zenodo v1.0 ZIP**. Cite their individual GitHub file URLs in addition to the Zenodo DOI when relying on these supplementary analyses.

## Interpretation safeguards

- HUG guarantee issuances are not completed presale contracts, average transaction prices, or evidence of increases in subscription demand.
- MOLIT housing presales and HUG issuances have different populations and units; they must not be merged into a contract/guarantee rate.
- Missing regional observations must not be imputed as zero without an explicit justified method.
- The 29 matched region-quarter observations reduce some coverage inconsistency but do not establish causation.
- A validated comparable 2025-vs-2026 first-half subscription application series was **not** established by this analysis.

## Citation

For the archived data package, cite:

> Eun Kim (2026). *HUG Regional Presale Guarantee Issuance in South Korea, 2009–2026 Q2: Verified Dataset and Regional Analysis* (Version 1.0). Zenodo. https://doi.org/10.5281/zenodo.23262918

For any post-deposit GitHub analysis, also cite that specific document or CSV by its stable GitHub URL and access date. Do not describe GitHub-only supplemental work as archived inside Zenodo v1.0.

## Licensing and provenance

Original government/HUG source data retains its applicable source terms. Resimanor's original curation, explanatory text, and other independently copyrightable derivative material may be reused under **CC BY 4.0** with attribution. This statement does not claim ownership or exclusive rights over the official source data.
