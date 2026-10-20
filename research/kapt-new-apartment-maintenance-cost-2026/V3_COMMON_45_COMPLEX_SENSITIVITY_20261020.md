# N02 v3 matched 45-complex sensitivity — 2026-10-20

**Source:** 180 observed complex-field eligibility rows from the 60-complex archived-source calendar continuity rerun. This was a new direct reaggregation of per-complex percentage differences, not an imputation or a new API collection.

The intersection of valid complexes for all three fields is **45**. Comparing the prior field-specific medians with medians computed over precisely the same 45 complex IDs:

| Field | Field-specific eligible n | Field-specific median change | Identical complexes n | Matched median change | Difference in percentage points |
|---|---:|---:|---:|---:|---:|
| pay | 50 | +1.925659% | 45 | +1.902384% | -0.023275 |
| cleanCost | 50 | +2.242365% | 45 | **-2.094951%** | **-4.337316** |
| guardCost | 47 | +1.859155% | 45 | +1.166539% | -0.692616 |

**Material sensitivity:** cleanCost reverses sign when analysis uses the same 45 complexes across all three fields. Do not report a robust positive trajectory for this field without exposing this sensitivity. It does not show which analytical cohort is more representative or prove an actual national cost decline.

Method: inner join the field-level `eligible` statuses by complex ID for `pay`, `cleanCost`, and `guardCost`. Calculate the unweighted median of already-computed per-complex first-three versus last-three-month percentages for each field within the matched set. The field-specific and matched estimates are both descriptive.

Outputs: `N02_동일45단지_3항목_표본민감도_20261020.zip` contains the 45-row matched ID/change table, summary, script and explanation. No raw API JSON redistributed. Official API numeric units and denominators remain unverified. Existing N02 v2 DOI `10.5281/zenodo.23432629` unchanged; N02 v3 **not published**.
