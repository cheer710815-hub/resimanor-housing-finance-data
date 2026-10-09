# HUG presale guarantee dataset v1.0 — independent release audit

Audit date: 2026-10-09. Official source: https://www.data.go.kr/data/15002513/fileData.do

## Local deposit bundle checked
- Archive name: `HUG_Resimanor_DOI_deposit_v1.0.zip`
- ZIP SHA-256: `21de5107b5ce4ebd5a16f73972ad0b55e4a0a55d040b1c23bb244b7903810760`
- Archive entries: 13
- Manifest `SHA256_MANIFEST.json`: 12 listed files; **all 12 byte-size and SHA-256 checks passed**
- Detail: 818 data rows / 11 columns
- Quality exceptions: 31 data rows / 11 columns
- Period summary: 18 data rows / 7 columns
- Quarter summary: 42 data rows / 7 columns

Note: Manifest covers every member except the manifest itself. A self-hash of the manifest would be circular and is not expected.

## Public GitHub file read-back
- Full cleaned CSV: 819 lines including header; blob SHA `7c5c7963591eb1cfe261f199fefafc9f3f93cd97`
- Period summary: 19 lines including header; blob SHA `1dc99e511f812c9f5eff02108cf9c8f4989b3b18`
- Detailed CSV last record: source row 819, 2026 Q2, 충북, 6,689억원, 1,875 households

GitHub blob SHA confirms identity of the public file at retrieval; it is **not equivalent to an independent bit-by-bit comparison against the ZIP's CSV**, as their representations may differ in UTF-8 BOM or line endings. Comparing the complete public files to packaged source is a separate validation task.

## Release caveats
- Historical '48 periods' claim was wrong; validation JSON reports **49 distinct source labels**, while yearly/half-year summary includes 18 periods.
- Negative values and ambiguous original region names remain preserved, not modified.
- Quarterly region omissions are missing observations, not zero.
- 'Per-household guarantee issuance' is **not** mean presale price.
- 2026 is H1 only; avoid comparing against full-year totals as equal durations.

## External actions (still pending)
- No Zenodo/Figshare/Dataverse DOI deposit performed.
- No DOI registered.
- Resimanor WordPress draft blocked by WP Agent domain ownership restriction; WordPress untouched.
- No post published.

Dataset landing page: https://github.com/cheer710815-hub/resimanor-housing-finance-data/tree/main/research/hug-presale-guarantee-regional-series-2026
