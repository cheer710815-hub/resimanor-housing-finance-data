# N02 v3: official K-apt source date and region-label reconciliation

Date: 2026-10-19. Status: prepublication source audit; Zenodo v2 is unchanged.

Official K-apt management market statistics page: https://www.k-apt.go.kr/apiinfo/index/aptMarketSize.do?tabId=tabAvg3

The page says statistics are taken from backup data, its chart database refreshes monthly on the first day, and recent-month results can vary by the time of query as collection coverage improves. It also directs readers to source apartment-level monthly records. This demonstrates a risk of publication-time revision, not proof that any particular N02 monthly API response was changed.

The page's regional selector currently displays `전남광주특별시`. The archived N02 candidate master uses `전남광주통합특별시`. These are different literal labels; preserve the source string, record the source date, and map the two to a common analysis geography only after verifying the official statutory nomenclature and the underlying municipality. The 2024 historic approval address should never be silently overwritten by a 2026 regional label.

N02 must distinguish: (1) archived source reporting month, (2) actual API collection timestamp, (3) analysis execution date, (4) K-apt published display date, and (5) administrative boundary reference date. Archived raw JSON was not live refetched in this review.

K-apt regional and national statistics may display per-area amounts, but that alone does not establish the unit or denominator for each of the 35 AptCmnuseManageCostServiceV3 raw numeric fields. Official field-level definitions are still pending ministry response. Do not convert, sum overlapping fields, or assert nationally representative estimates.

Next gate: create a sourced mapping of current official region names and historical labels; request field-unit definitions through existing agency enquiry. Keep N02 v3 unpublished until review and explicit approval.
