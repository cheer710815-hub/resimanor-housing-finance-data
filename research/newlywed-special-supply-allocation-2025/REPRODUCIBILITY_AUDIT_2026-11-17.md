# Public replication audit — 2026-11-17

**Study ID:** ARHRN-INDEPENDENT-BRIDAL-SPECIAL-SUPPLY-REFORM-20261108  
**Audit scope:** confirmation of previously published 2025-11-28 official CSV snapshot, deterministic reproduction of four cohort totals; no causal inference and no independent legal compliance adjudication.

## Inputs and exact fingerprints

| Official source | Bytes | SHA-256 |
|---|---:|---|
| 한국부동산원_청약홈_APT 분양정보_20251128 (5).csv | 1,592,459 | `da0722409157619242fb614c145541051e1584aadfd1176f946910c5085d4ae2` |
| 한국부동산원_청약홈_APT 주택형별 분양정보_20251128 (2).csv | 1,155,851 | `f6a71618eee61414d9cc401f047192ea218f711927396fc5c1786060406d8642` |

The filenames above include local duplicate-name suffixes (`(5)`, `(2)`), which are **not official version indicators**. Exact byte hashes, rather than file names, identify the inputs. Raw official files were used locally but were **not redistributed**.

## Procedure and observed output

Executed the public `reproduce_from_official.py` via Python 3 with the two above files:

```text
2024,pre,64,25924,4559,17.58602
2024,post,212,93456,16311,17.45313
2025,pre,32,10965,1889,17.22754
2025,post,194,81404,18168,22.31831
descriptive_difference_pp=5.22366 (NOT causal)
```

**Exit status:** 0. The script verifies both source hashes, the four cohort counts and supply totals, the 502-notice count, and the descriptive contrast.

**Formula:** for each cohort, newlywed allocation units divided by eligible general + special supply units across included type rows. Descriptive contrast = (2025 post − 2025 pre) − (2024 post − 2024 pre), all in percentage points.

## Limitations not resolved by this pass

- Official notices from 2025-11-29 onward are excluded. This is a snapshot-bound **partial-year** comparison.
- Notice dates do not establish underlying housing construction approval application dates.
- The original 502 individual notice amendment histories, special-case eligibility, and compliance with transitional rules have **not** been independently completed.
- Changes in location, project composition and other contemporaneous interventions are not isolated. **No causal identification.**
- This audit confirms arithmetic reproducibility for the specified inputs, **not independent academic peer review** and not DOI readiness.
- The analytical panel and official inputs are distinct; source redistribution permissions are not asserted.

**Status:** verified reproducibility of public descriptive materials; HOLD for DOI minting or causal-policy interpretation. Future external publication should retain these qualifications.
