# Methods, data dictionary and permitted interpretations

**Observation unit.** An LH dataset row is an auction/notice record, not a unique physical shop, completed sale, or occupancy event. Repeated bids and re-offerings can yield several rows for the same shop. The strict notice–shop key is formed by \`공고명\`, \`공고게시일\`, \`상가명\`, \`호\`, and \`전용면적\`. A shop-level **research composite**, not an official LH asset ID, uses \`사업지구\`, \`블록\`, \`상가명\`, \`호\`, and \`전용면적\`.

**Dates.** The earlier-labelled CSV's nonblank entry-date values use day 01; the comparison is therefore limited to year-month. The later-labelled CSV contains \`2025-MM-YY 00:00:00\`. A separate derived \`20YY-MM\` is computed for diagnostics; the original value is retained unchanged. Two LH exports could be derived from a shared internal system and are **not independent evidence** of physical occupancy.

**Data ethics and scope.** Original public files are not redistributed. No personal or tenant-level records, confirmed occupancy dates, defect cause, data revision sequence, LH acknowledgment, or implication of wrongdoing are claimed.

**Reproducibility.** Requires CP949 CSVs with byte-identical SHA-256 from the source pages. Uses Python 3.9+ standard library. Verification stops on unexpected file hashes or schemas. Outputs are machine-generated and must be interpreted with reference to the two official source definitions. Do not infer that the 2025-labelled dataset replaced the 2020-labelled dataset.

**Counts.** Notice key: shared 1,825, comparable 1,822, agree 1,820, disagree 2. Shop composite: shared 1,210, comparable 1,207, agree 1,206, disagree 1. The two notice differences are associated with one composite, Entrarium unit 101. Multi-notice composites with constant entry-date string: 381 (2020-labelled dataset) and 476 (2025-labelled dataset); listed prices differ across notices for 107 and 131 composites respectively.

**Citation / distribution.** Research note by Resimanor / ARHRN, 2026-11-21, identifier \`ARHRN-LH-SHOP-PAYMENT-TERMS-GRAIN-QA-20261115\`. **No DOI has been minted. Zenodo submission remains on hold.** Reproduce using the original records rather than treating this report as a new official LH statement.
