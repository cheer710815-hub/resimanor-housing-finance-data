# Attribution and interpretation boundaries

- **Original source:** 서울특별시 열린데이터광장, 「서울시 공동주택 잡수입,잡지출,장기수선충당금 정보」, `etc_income_2022.csv` and `etc_income_2023.csv`.
- **Official data page:** https://data.seoul.go.kr/dataList/OA-15819/S/1/datasetView.do
- **Identifier reference:** https://data.seoul.go.kr/dataList/OA-15818/A/1/datasetView.do (APT_CD / K-아파트코드). This does not prove codes correspond one-to-one to independently constituted legal properties.
- **Original source terms:** 공공누리 제1유형 (출처표시) shown on Seoul's dataset page; consult the official source for current terms.
- **Original source file SHA-256:** 2022 `c676b180bc507c2e2e70470c2176ef5ab0ff9aaef1dd2bd80de8ad1805f3aa5f`; 2023 `b4921ad52bd45ff74801874fe0a4434eeabe89dd591fe796325ff7f245a49db1`.
- **Method:** A collision is one unique (apartment name, date, income account) tuple associated with two or more distinct apartment codes. A collision is neither a demonstrated duplicate transaction nor a demonstrated official accounting error.
- **Disclosure boundaries:** No assertion of management-fee savings, accounting misconduct, monetary loss or policy causality; raw amount units, management-unit identities and payment details have not been independently validated.
- **Distributed scope:** Research code, aggregate indicators and explanatory documentation only. The original Seoul CSV records are not redistributed.
- **Code/text rights:** Separate from the Seoul government's source-data license. This project has not adopted an explicit open-source license for its original code and prose; publication does not itself license reuse or modification of those works.
- **Publication status:** Public GitHub methods release; no DOI assigned. Further repositories, archival services and DOI issuance require separate approval.
