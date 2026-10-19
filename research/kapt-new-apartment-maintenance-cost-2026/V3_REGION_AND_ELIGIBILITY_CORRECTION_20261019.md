# N02 v3 prepublication correction (2026-10-19)

## Region label correction

**Do not mark `전남광주통합특별시` as an administrative-name error in 2026.** The Ministry of the Interior and Safety announced a July 1, 2026 launch under this official name: https://www.korea.kr/news/policyNewsView.do?newsId=148960435 . Archived candidate `A10022567` (힐스테이트오룡1단지, 무안군, approved May 30 2024) shows the 2026 name; historical references for its 2024 approval date should say `전라남도 무안군`. Retain 2026 name for contemporary regional reporting; do not exclude the complex merely on this label. This **supersedes** assertions of a malformed region name in prior N02 study notes.

## Reproducible field-specific six-point rule

Audit used existing `component_comparison.csv` early-three + late-three raw values and required all six field observations numeric and strictly positive. In **new40**:

| Cost field | Eligible | Excluded with null | Excluded with zero |
|---|---:|---:|---:|
| pay | 34 | 6 | 0 |
| cleanCost | 34 | 6 | 0 |
| guardCost | 31 | 6 | 3 |

For **prior20** each field has 16 eligible, two null-excluded and two zero-excluded. These criteria yield 60-complex eligible totals 50 / 50 / 47. Historic October 18 new40 summary 28 / 28 / 27 is **not reproduced**; since original intermediate code was not preserved, its exact cause cannot be asserted. Do not substitute a guessed explanation. The complete 180-row per-field decision table and exclusion summary are in the working ZIP `N02_v3_지역명_표본수_검증정정_20261019.zip`.

The government has not yet specified official source monetary units or denominator. This is a prepublication correction only; no new Zenodo v3 version is released, and N02 v2 is untouched.
