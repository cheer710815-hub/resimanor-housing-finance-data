# N02 original API amount scale vs K-apt public area-based display — 2026-10-20

## Direct archived JSON check

Read the 40-complex `cohort_results.zip` directly. Each numeric value below came from the original flat `result_json` for its corresponding `operation`, excluding null and nonpositive values. These are **raw numeric amounts without any conversion**:

| Field | Positive numeric observed months | Median raw numeric amount | Min positive | Max positive |
|---|---:|---:|---:|---:|
| `pay` | 926 | 24,352,135 | 2,500,000 | 125,404,900 |
| `cleanCost` | 925 | 18,108,690 | 178,300 | 94,891,356 |
| `guardCost` | 883 | 16,321,340 | 505,400 | 94,325,610 |

The order of magnitude of the observed raw values is **consistent with Korean-won monthly complex-total components**, not values already in KRW per square meter. This is an evidence-based **inference**, not a provider-certified field unit.

## Distinct official output basis

The K-apt [official regional common-maintenance statistics](https://www.k-apt.go.kr/apiinfo/index/apiIndexSearch.do) explicitly display **원/㎡, 주거전용면적기준**. The [regional detailed monthly averages](https://www.k-apt.go.kr/apiinfo/goApiInfoBySido.do) likewise display **원/㎡, 주거전용면적기준**. Those public display units **do not automatically define** the archived REST API raw field units or denominator.

## Correct next conversion test

For a particular **same complex, same reporting month, same item**, retrieve verified monthly residential exclusive-floor-area total (㎡), and compare `raw monthly cost KRW / verified residential exclusive-floor-area total` with the K-apt official displayed item (원/㎡). Verify the rounding rule, whether reported values are current revisions, and whether the display represents precisely the same cost subfield. Do **not** use `kaptMarea` without verifying its precise area definition; do not divide by a single household's 84㎡ unit area when attempting to calculate a whole-complex per-㎡ value.

Before this crosscheck, record units as **strongly suggested monthly KRW total by observed magnitude, not officially verified**. The previously published percent-change analysis is invariant to dividing all 24 observations of a complex by the same positive constant, **but not invariant to a denominator that changes across months**. Report v3 results as raw-field trajectories with source-unit caveats until such validation is completed.

Existing Zenodo v2 DOI `10.5281/zenodo.23432629` retained; v3 not published.