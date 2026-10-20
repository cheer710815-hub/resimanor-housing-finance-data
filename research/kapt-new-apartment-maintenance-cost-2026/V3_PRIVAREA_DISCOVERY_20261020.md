# N02 new denominator candidate — privArea (2026-10-20)

## New finding
A historic description and sample output of the Ministry/K-apt apartment basic-information API (public portal: https://www.data.go.kr/data/15058453/openapi.do ) identifies three **different area fields**:

| Field | Label in historic examples | Sample A10027875 (m²) |
|---|---|---:|
| `kaptTarea` | 건축물대장상 연면적 | 19324.6751 |
| `kaptMarea` | 관리비부과면적 | 15040.1634 |
| **`privArea`** | **단지 전용면적합** | **9014.0338** |

Evidence: https://sijoo.tistory.com/420 and https://github-wiki-see.page/m/luritas/open-data-api/wiki/%EA%B3%B5%EB%8F%99%EC%A3%BC%ED%83%9D-%EA%B8%B0%EB%B3%B8-%EC%A0%95%EB%B3%B4 ; an independent raw response reproducing `privArea` in a different apartment appears at https://sir.kr/questions/390449?page=1705 .

**Confidence:** The field name and meaning are corroborated in several historical third-party captures but **the current official Swagger output schema and exact target-complex response have not yet been fetched**. Those historic values belong to A10027875 **and must not** be applied to A10020809 or any of the N02 60 complexes.

## Next reproducible check
1. Use the already-approved credentials for **국토교통부_공동주택 기본 정보제공 서비스** to request `getAphusBassInfoV3` (or the exact current method name listed by Swagger), with `kaptCode=A10020809`. Avoid publishing serviceKey or original JSON with secrets.
2. Extract raw `privArea`, `kaptMarea`, and `kaptTarea`. Record request time and whether the area is valid/positive. Note the risk of revision or historical area changes between month 202501 and current retrieval.
3. Retrieve the **same-complex same-month 202501** official cleaning component per m², in exclusive-area mode. Verify `cleanCost=3,667,763 / privArea` within published rounding precision, allowing for raw-cost category definitions and revisions.
4. Only if consistency confirmed, adapt N02 with **explicit conversion and area-denominator provenance**. Never assume `kaptMarea == privArea` or substitute sample values.
5. Make the area inference (rather than claimed official certification) clear until current government schema and response inspected.

K-apt official comparison UI https://www.k-apt.go.kr/apiinfo/goApiSearchCompare_detail.do describes `원/㎡` mode and warns other area bases are management-supplied. **No actual N02 per-square-meter numerical conversion has yet been verified.** 60-complex raw change analyses retained; v3 not published; Zenodo v2 DOI 10.5281/zenodo.23432629 unchanged.
