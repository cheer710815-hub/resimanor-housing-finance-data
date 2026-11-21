# Seoul apartment miscellaneous income: join-key reproducibility audit (2022–2023)

**Research ID:** `ARHRN-SEOUL-APT-MISC-INCOME-QUALITY-20261109`  
**Publisher:** ARHRN Research / Resimanor  
**Status:** Public methods and aggregate-result release; **no DOI assigned**.  
**Source:** Seoul Metropolitan Government, [Seoul Open Data Plaza — apartment miscellaneous income, expenditure and long-term repair reserve](https://data.seoul.go.kr/dataList/OA-15819/S/1/datasetView.do).

## Research question

Can apartment names serve as unique identifiers when joining Seoul apartment miscellaneous-income records by apartment name, date and account? **Not reliably.** Different apartment codes appear under the same name/date/account combination. We call these *join-key collisions* — **not proven accounting errors, duplicate transactions, or separate legal apartment entities**.

## Independently reproduced findings

| Audit metric | 2022 | 2023 |
|---|---:|---:|
| Source records | 735,394 | 719,513 |
| Distinct apartment codes | 2,351 | 2,358 |
| Distinct apartment names | 2,372 | 2,375 |
| Income account labels | 15 | 15 |
| Codes with multiple names | 28 | 22 |
| Names associated with multiple codes | 7 | 5 |
| **Name + date + account groups spanning multiple codes** | **349** | **207** |
| Negative amount rows | 3,058 | 2,777 |
| Empty or nonnumeric amount rows | 2 | 10 |

Across both years, **2,309 apartment codes** occur in both source files. The collision metric counts *unique name/date/account groups* each containing more than one distinct apartment code; it does not count allegedly erroneous accounting entries.

## Reproduce

**Source availability as checked 2026-11-21:** the Seoul Open Data Plaza OA-15819 dataset page currently displays **"해당 데이터는 종료된 서비스입니다"** ("This data service has ended") and an invalid-URL warning. The historical 2022/2023 CSVs were used for this audit, but fresh downloads of the identical originals from that page are **not currently verified**. The repository intentionally does **not** redistribute those raw files. No substitute download URL is asserted.

1. Obtain archived copies of the original `etc_income_2022.csv` and `etc_income_2023.csv` from a lawfully accessible source, without altering their bytes. If you do not have the originals, you can inspect the published aggregate results and code, but **you cannot independently re-run the strict raw-data audit**.
2. From the **repository root**, enter this research directory: `cd research/seoul-apartment-misc-income-join-key-audit-2022-2023` and create a local `source/` subdirectory there. Put the two original CSVs in that `source/` folder.
3. From this research directory, run `python scripts/reproduce.py --source-dir source --output audit_results.json --strict` using Python 3.9+ (standard library only; source CSV decoding assumes CP949).
4. Compare the JSON output with `results/audit_summary.csv`. Strict mode checks source-file SHA-256 digests, published metrics, and shared-code count. If the same originals are unavailable, do **not** report a successful independent strict reproduction.

The original published findings remain historical findings, not evidence that today's official download interface is available. No change to the 2022–2023 calculated values or original hashes is made by this notice.

**Original SHA-256:**  
2022: `c676b180bc507c2e2e70470c2176ef5ab0ff9aaef1dd2bd80de8ad1805f3aa5f`  
2023: `b4921ad52bd45ff74801874fe0a4434eeabe89dd591fe796325ff7f245a49db1`

## Interpretation and limitations

- An apartment name is not a safe unique join key. Use the official apartment code as the primary linkage key, while independently auditing its stability and the level of management entity it denotes.
- One apartment code can be associated with different displayed names. The extracts cannot establish the administrative cause.
- Negative income entries do **not** establish errors or misconduct.
- Miscellaneous income does **not** directly measure a reduction in resident management fees.
- A reduction in `고용안정사업수익` rows after June 2022 coincides with the scheduled end of a government assistance program; this is **not a causal conclusion and not part of this release's main claim**.
- Monetary units, distinct legal/physical apartment identities and actual payments are **not independently verified**.

## Scope, provenance and reuse

The historical source dataset was published by Seoul Metropolitan Government and was marked as **공공누리 제1유형 (출처표시)** on its data page. The public download interface currently states that the service has ended; check any surviving official record for current access and reuse terms. These scripts and aggregate statistics are derived research materials. **Original raw CSV files are not redistributed.**

Source and code identifiers: [Seoul Open Data Plaza dataset](https://data.seoul.go.kr/dataList/OA-15819/S/1/datasetView.do); [Seoul apartment code reference](https://data.seoul.go.kr/dataList/OA-15818/A/1/datasetView.do). See [attribution and limitations](docs/ATTRIBUTION_AND_LIMITATIONS.md).

**Rights notice:** No additional open-source license for the original research code/text is granted by this release. Contact the publisher before redistributing or modifying those original contributions; use of underlying Seoul government data is governed by its own stated terms. An open-code license can be adopted later with separate approval.

**Suggested citation:** ARHRN Research / Resimanor (2026). *Seoul apartment miscellaneous-income join-key reproducibility audit (2022–2023)*. GitHub research release, `ARHRN-SEOUL-APT-MISC-INCOME-QUALITY-20261109`. Cite the repository URL and access date. **No DOI.**
