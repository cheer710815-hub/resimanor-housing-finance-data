# N02 v3 technical specification audit — 2026-10-20

Official source: https://www.data.go.kr/data/15057937/openapi.do

The public service lists the Ministry of Land, Infrastructure and Transport, housing-construction operations department, REST/JSON transport and unrestricted portal-use scope. The directly accessible page contains an Open API specification viewing guide, but did not expose a verifiable response-property table or authoritative units for the 35 observed numeric JSON fields.

External indexing confirms the AptCmnuseManageCostServiceV3 service and a getHsmpLaborCostInfoV3 example operation. This does NOT determine the units or area denominators of pay, cleanCost, and guardCost.

The October 19 helpdesk response only confirmed forwarding the inquiry to the responsible ministry. No field-specific technical response was established.

Maintain all 35 field units as UNVERIFIED. The normalized K-apt public website display does not establish the raw API field denominators. Continue field-level numeric sensitivity research as exploratory only; no national-cost, total monthly KRW, KRW-per-square-meter or causal claim is authorized by this evidence.

Next provider response action: populate V3_35_FIELDS_PROVIDER_RESPONSE_MATRIX_20261019.md field by field with exact government documentation and effective date. Require study coordinator approval before a new version of existing N02 Zenodo series. Existing v2 DOI remains 10.5281/zenodo.23432629; v3 remains unpublished.