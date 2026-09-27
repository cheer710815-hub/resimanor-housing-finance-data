# Backlink Acquisition Tracker

Updated: 2026-09-26

This tracker records only legitimate editorial, institutional, open-data, and open-source adoption opportunities for AptToSell and Resimanor.

## Status legend

- ACTIVE — submitted or live opportunity
- PREPARED — submission package ready, external action still required
- WATCH — relevant but no action yet
- EXCLUDED — not suitable for backlink acquisition

## ACTIVE

### tae0y/real-estate-mcp
Type: Open-source data adoption
Status: ACTIVE
Issue:
https://github.com/tae0y/real-estate-mcp/issues/40
Assets:
- AptToSell subscription score data
- Resimanor stress DSR data
Goal:
Reference dataset / fixture / documentation adoption.

### ssuksak/cheongyak-rag-mcp
Type: Open-source data adoption
Status: ACTIVE
Issue:
https://github.com/ssuksak/cheongyak-rag-mcp/issues/1
Assets:
- AptToSell subscription score CSV/JSON
- AptToSell private-housing deposit data
Goal:
Static reference dataset for subscription guide / RAG / fixtures.

## PREPARED

### Awesome Public Datasets
Type: Public dataset catalog
Status: PREPARED
Submission method:
Fork + pull request required.
Rules:
- Direct dataset repository preferred over promotional landing page.
- High-quality, directly downloadable public data.
- Maintainer review required.
Prepared files:
- AptToSell: external-submissions/awesome-public-datasets.yml
- Resimanor: external-submissions/awesome-public-datasets.yml
Blocker:
Current GitHub connector cannot create forks.

### Universal Housing Dataset Catalog
Type: Housing dataset catalog
Status: EXCLUDED_FOR_CURRENT_LICENSE
Verified catalog:
https://housing.pubpub.org/datasets
Verified submission form:
Public Airtable form titled "Open-Source Housing Data"
Verified:
2026-09-27
Critical eligibility finding:
- The submission form explicitly says it is for "public-domain datasets centered around housing."
- Current AptToSell and Resimanor datasets are licensed CC BY 4.0, which is an open license but not public domain.
Decision:
- Do not submit either current dataset through this form.
- Do not change the dataset license merely to obtain a backlink.
Next step:
- Reconsider only if the catalog later accepts openly licensed non-public-domain datasets or a genuinely public-domain derivative/resource is created for an independent reason.
Priority: EXCLUDED

### Korea Banking Institute
Type: Financial education resource
Status: PREPARED
Fit:
Uses private proptech / real-estate information services in education.
Submission path:
Course proposal / institutional inquiry.
Constraint:
Login or human contact required.
Primary assets:
- AptToSell calculator/data center
- Resimanor DSR data center

### Seoul 50Plus
Type: Lifelong-learning resource
Status: PREPARED
Fit:
Real-estate and finance education with private real-estate tools.
Submission path:
Course/team inquiry.
Constraint:
Human contact required.
Primary asset:
Resimanor DSR / housing-finance data.

### Seoul Cyber University AI Real Estate Big Data
Type: University related-resource / education
Status: PREPARED
Fit:
Directly lists private real-estate/proptech tools.
Primary assets:
- AptToSell calculator
- AptToSell data center
- Resimanor DSR data center

### Mokwon University Real Estate Finance Insurance
Type: Broken-link replacement
Status: PREPARED
Candidate:
Speedbank legacy/outdated external link.
Replacement assets:
AptToSell data center / Resimanor data center.

## WATCH

- Shin Ansan University Real Estate
- Hallym University Community Education Center
- Pyeongtaek University Urban Planning & Real Estate
- Gangneung-Wonju National University Urban Planning & Real Estate
- Konkuk University Real Estate
- Korea Proptech Forum
- Seoul Eastern Women's Development Center



## Newly discovered Universal-Housing-like hubs

### National Housing Conference — Housing Resource Center
Type: Curated housing resource/data-tool hub
Status: SUBMITTED
Verified submission form:
https://hrc.nhc.org/contact-us/
Submitted:
2026-09-27
Submitted resource:
Resimanor South Korea Stress DSR Housing Finance Reference Data (2026)
Submitted link:
https://github.com/cheer710815-hub/resimanor-housing-finance-data
Suggested topic areas:
Homeownership; Research; Data Tools; Technology
Why it matters:
- Maintains a curated housing-policy resource center with a dedicated Data Tools type.
- Resource entries link users to the original external source.
- Official form explicitly accepts resource suggestions.
Submission notes:
- Submitted through the public web form, not by email.
- Confirmation shown: "Your submission was successful."
Next step:
- Wait for editorial review or inclusion.
- Do not send follow-up unless NHC requests clarification.
Priority: VERY HIGH

### MorFi Open Source Housing & Mortgage Data
Type: Mortgage and housing open-data contribution hub
Status: UNDER_REVIEW
Submission route:
Email to support@morfi.com
Submitted:
2026-09-26
Why it matters:
- Explicitly invites users to suggest new housing/mortgage data sources and contribute to open datasets.
- Audience includes mortgage software developers, housing researchers and analysts.
Submission:
- Suggested Resimanor stress DSR / mortgage-limit data center and open CSV/JSON resources.
Next step:
- Monitor for reply, contribution guidance, or inclusion.
Priority: HIGH for Resimanor

Reply received: 2026-09-27
Update:
- Matthew Miller replied that MorFi mainly focuses on the U.S. mortgage industry but found the South Korean data interesting.
- MorFi said they will review the dataset and let us know if it is a fit.
- Sent a brief thank-you reply; no further follow-up until they respond.

### The Real Deal — Directory of Real Estate Data Sites
Type: Curated real-estate data-source directory
Status: SUBMITTED
Submission route:
Email to research@therealdeal.com
Submitted:
2026-09-26
Why it matters:
- Dedicated searchable directory of real-estate data sites.
- Public page explicitly invites suggestions.
Submission:
- Suggested AptToSell housing subscription data center.
- Suggested Resimanor housing-finance / stress-DSR data center.
Next step:
- Monitor for reply or directory inclusion.

### Data Is Plural
Type: Curated dataset discovery newsletter/archive
Status: SUBMITTED
Submission route:
Email to jsvine@gmail.com
Submitted:
2026-09-26
Why it matters:
- Prefers free, directly accessible, documented, downloadable datasets.
- AptToSell and Resimanor match many of its stated dataset-quality criteria.
Submission:
- Suggested AptToSell housing subscription data.
- Suggested Resimanor stress-DSR / housing-finance data.
Next step:
- Monitor for reply, newsletter inclusion, or archive citation.



### National Housing Data Exchange (Australia / AHDAP)
Type: Housing-specific CKAN data exchange
Status: WATCH
Why it matters:
- Dedicated housing data portal with datasets from government, industry and public sources.
- Supports external-source records, not only locally hosted files.
- CKAN registry exposes metadata, formats, licenses and API access.
Fit:
- Structural fit is strong for both repositories.
Constraint:
- Geographic mission is explicitly focused on Australia's housing future; Korean datasets may be outside scope.
Priority: MEDIUM-LOW unless international submissions are confirmed.

### Data Commons
Type: Global public-data knowledge graph / API / MCP
Status: WATCH
Why it matters:
- Accepts public-data contributions.
- Contributed data becomes accessible through Data Commons tools and APIs.
- Data Commons also provides MCP access for LLM/agent use.
Fit:
- Resimanor could fit only if converted into statistical variables joined to Korean places/institutions.
- AptToSell score/deposit lookup tables are less natural because they are rule/reference tables rather than place-based macro statistics.
Constraint:
- Best fit is public statistical macro data licensed CC BY and joinable to existing entities such as places or institutions.
Priority: MEDIUM for future derived regional statistics; LOW for current rule tables.



### Awesome Real Estate (etewiah/awesome-real-estate)
Type: Curated global real-estate / proptech resource list
Status: PR_READY
Why it matters:
- Actively maintained in 2026.
- Has an explicit Asia section with South Korea already represented.
- Includes Authoritative Research & Publications with open housing datasets.
- Contribution rules allow owner submissions if affiliation is disclosed.
Prepared file:
- external-submissions/awesome-real-estate-pr.md
Blocker:
- Pull request requires fork/edit flow not supported by the current GitHub connector.
Priority: HIGH

### Awesome Real Estate APIs (happyendpointhq/awesome-real-estate-apis)
Type: Country-by-country real-estate data source / API / dataset list
Status: PREPARED
Why it matters:
- Dedicated to property data sources, government open data, APIs and bulk datasets by country.
- Explicitly accepts additions through GitHub issues or pull requests.
- Has a Datasets section and Asia Pacific section.
- Free/open access status and access restrictions are part of its curation model.
Best fit:
- AptToSell: South Korea reference dataset (subscription score/deposit)
- Resimanor: South Korea reference dataset (stress DSR / mortgage-limit scenarios)
Constraint:
- GitHub App issue creation returned 403 even though the repo accepts issues/PRs; manual GitHub submission is still possible.

### SchemaFinder
Type: Public dataset search/index + API + MCP
Status: VERIFIED_READY_TO_SUBMIT
Submission:
https://schemafinder.com/submit
Verified:
2026-09-27
Verified fields:
- Publisher
- Category
- Format
- Geographic scope
- Update frequency
- API endpoint (optional)
- Documentation URL
- Tags
- Access: Open or Gated
- At least one column schema required, up to 100 columns
- Attribution: anonymous or credited
- Contact email optional/private
Fit:
- Resimanor is openly accessible without signup/payment.
- Direct CSV/JSON resources and documented methodology are available.
- Column schema can be supplied directly.
- South Korea geographic scope and housing-finance category are clear.
Submission rule:
- Search first to avoid duplicate URLs; duplicate URLs are rejected automatically.
Next step:
- Submit Resimanor first.
Priority: VERY HIGH

### Awesome Urban Datasets (urban-toolkit)
Type: Curated public urban-dataset list
Status: WATCH
Why it matters:
- Publicly maintained curated list of urban datasets.
- Contributions are explicitly welcomed.
- Includes property cadastre, buildings/lots, infrastructure and urban-analysis datasets.
Fit:
- Current AptToSell/Resimanor rule/reference tables are not a strong fit because they are not spatial urban datasets.
- Future regional datasets (local housing prices, supply, accessibility, regional finance indicators) could fit much better.
Priority: LOW for current datasets / HIGH for future geospatial-regional data.



### Number Cortex Financial Resources
Type: Curated finance education / calculator resource hub
Status: WATCH
Why it matters:
- Curates external financial websites, apps and calculators.
- Includes mortgage calculators as a dedicated calculator category.
- Public page exposes a “Suggest Resource” route.
Best fit:
- Resimanor housing-finance / stress-DSR data center and calculator-type resources.
Constraint:
- Submission form details and editorial standards need deeper verification before outreach.
Priority: MEDIUM

### PolicyMap Data Catalog
Type: Large housing / community-development / mortgage data catalog
Status: WATCH
Why it matters:
- Strong housing, affordability, mortgage and lending dataset coverage.
- High-value research audience.
Constraint:
- Current catalog appears to be internally curated / licensed data; no public external-dataset submission route verified.
Priority: LOW unless a contribution path is confirmed.

### Urban Institute Data Catalog
Type: Housing-policy / mortgage research data catalog
Status: WATCH
Why it matters:
- Strong topical overlap with mortgage, housing finance and neighborhood data.
- Research-grade catalog and citation environment.
Constraint:
- Appears focused on Urban Institute-produced/managed datasets; no open public submission path verified.
Priority: LOW unless external contributions are explicitly allowed.

### LucidAgent Data Catalog
Type: Agent-oriented public data catalog
Status: WATCH
Why it matters:
- Has a Real Estate category with Zillow, ACS Housing, HMDA, FHFA and HUD datasets.
- Oriented toward data applications and agents.
Constraint:
- No public external dataset submission path verified.
Priority: LOW unless contribution flow is found.



### GeetMark Search Hub
Type: Vertical resource search engine / API
Status: WATCH
Why it matters:
- Operates a dedicated Real Estate category.
- Public navigation exposes a Submit Resource route.
- Search API and item endpoints can make accepted resources discoverable programmatically, not only through a directory page.
- No-login browsing is available.
Best fit:
- AptToSell calculator/data center as a Real Estate resource
- Resimanor housing-finance/DSR data center as a Real Estate resource
Constraint:
- The public submission page is referenced in site navigation, but the detailed submission form and editorial criteria were not independently retrievable in follow-up verification.
Priority: MEDIUM pending form verification.

### Deal-Scale Awesome Real Estate Investing
Type: Curated real-estate investing resource list
Status: PR_READY
Contribution method:
Edit README.md and submit a pull request.
Why it matters:
- PRs are explicitly welcomed.
- Includes Analytics & Data Platforms, Foundational Geospatial & Data Sets, and Authoritative Research & Publications.
Prepared file:
- external-submissions/deal-scale-awesome-real-estate-investing-pr.md
Priority: MEDIUM

## EXCLUDED / DO NOT USE

- Mass email outreach
- Random profile backlinks
- Free posting boards
- Paid guest posts
- Reciprocal link schemes
- Automated backlink packages
- Government “suggest a dataset” forms that only request new government datasets
- Irrelevant GitHub repositories without a clear data-use case
- Duplicate submissions to multiple repositories by the same developer

## Core linkable assets

### AptToSell
Data center:
https://apttosell.com/housing-subscription-data/

Calculator:
https://apttosell.com/cheongyak-score-calculator/

JSON:
https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/housing_subscription_score_2026.json

Repository:
https://github.com/cheer710815-hub/apttosell-subscription-data

### Resimanor
Data center:
https://resimanor.com/housing-finance-dsr-data/

JSON:
https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/stress_dsr_mortgage_examples_2026.json

Repository:
https://github.com/cheer710815-hub/resimanor-housing-finance-data

## Next action rule

Prioritize in this order:
1. Existing submitted open-source proposals
2. Public dataset catalogs
3. Institutional related-resource pages
4. Broken-link replacement
5. Educational resource adoption
6. Research / journalism citation

Do not create new outreach targets merely to increase the count.


### tae0y/real-estate-mcp PR #41
Type: Editorial open-source integration / reference-data inclusion
Status: PR_OPEN
PR:
https://github.com/tae0y/real-estate-mcp/pull/41
Issue:
https://github.com/tae0y/real-estate-mcp/issues/40
Opened:
2026-09-27
Changes:
- Added Korea housing subscription and stress DSR reference examples under resources/
- Linked AptToSell and Resimanor CSV/JSON datasets and methodology pages
- Updated custom instructions and README/README-ko discovery links
Why it matters:
- Maintainer explicitly requested a PR.
- If merged, links become part of an actively used Korean real-estate MCP project rather than a generic directory.
Next step:
- Wait for maintainer review after their stated availability window.
Priority: VERY HIGH


### etewiah/awesome-real-estate PR #81
Type: Curated global real-estate / proptech resource list
Status: PR_OPEN
PR:
https://github.com/etewiah/awesome-real-estate/pull/81
Opened:
2026-09-27
Changes:
- Added AptToSell Korea Housing Subscription Data under Asia > Authoritative Research & Publications
- Added Resimanor Korea Stress DSR Housing Finance Data in the same section
Why it matters:
- South Korea is already represented in the Asia section.
- The section already includes CC BY 4.0 housing datasets with downloadable CSV/JSON and documented methodology.
- Affiliation was disclosed in the PR as required by the contribution rules.
Next step:
- Wait for maintainer review / CI feedback.
Priority: VERY HIGH


### Deal-Scale/awesome-real-estate-investing PR #17
Type: Curated real-estate investing resource list
Status: PR_OPEN
PR:
https://github.com/Deal-Scale/awesome-real-estate-investing/pull/17
Opened:
2026-09-27
Changes:
- Added AptToSell Korea Housing Subscription Data under Authoritative Research & Publications
- Added Resimanor Korea Stress DSR Housing Finance Data in the same section
Why it matters:
- The repository explicitly welcomes PR contributions.
- The list includes analytics, foundational data, and authoritative research resources.
- Both submissions disclose maintainer affiliation and link directly to public data repositories.
Next step:
- Wait for maintainer review / CI feedback.
Priority: HIGH


### awesomedata/apd-core PR #731
Type: Awesome Public Datasets / Finance dataset catalog
Status: PR_OPEN
PR:
https://github.com/awesomedata/apd-core/pull/731
Opened:
2026-09-27
Changes:
- Added core/Finance/Resimanor-Korea-Stress-DSR-2026.yml
- Homepage points directly to the public GitHub dataset repository
- Included direct CSV/JSON sources, methodology, source policy, FSC reference, CC BY 4.0, and Zenodo DOI
Why it matters:
- Awesome Public Datasets explicitly requires direct dataset/repository links and rejects advertising/spam.
- The submission matches the Finance category and research/education use criteria.
- Reviewers were assigned automatically after PR creation.
Next step:
- Wait for maintainer/reviewer feedback; do not add follow-up comments unless requested.
Priority: VERY HIGH


### jasonniebauer/awesome-public-data-sources PR #6
Type: Curated public data source list
Status: PR_OPEN
PR:
https://github.com/jasonniebauer/awesome-public-data-sources/pull/6
Opened:
2026-09-27
Changes:
- Added Resimanor South Korea Housing Finance Data under Finance & Economics
- Linked directly to the public GitHub data repository
- Description highlights CSV/JSON, methodology, and official-source references
Why it matters:
- The repository explicitly welcomes public data source PRs.
- Finance & Economics had an open contribution slot.
- The contribution is a direct data repository, not a promotional landing page.
Next step:
- Wait for maintainer review; no follow-up comment unless requested.
Priority: HIGH


### Mokwon University broken-link target
Type: .ac.kr academic resource-page replacement
Status: VERIFIED_TARGET
Target page:
https://www.mokwon.ac.kr/refic/html/sub05/0507.html
Verified:
2026-09-27
Finding:
- The Department of Real Estate, Finance and Insurance maintains a public related-sites page.
- The page still lists "스피드뱅크" with an old real21.kr destination.
- The university's homepage modification board is staff-only, so external users cannot submit the edit directly there.
Replacement fit:
- Resimanor housing-finance / stress-DSR dataset is a stronger current educational/reference resource than the obsolete commercial portal link.
Next step:
- Hold for a non-email public submission/contact route or a direct institutional relationship.
Priority: VERY HIGH


### Seoul Cyber University AI Real Estate Big Data resource inclusion target
Type: .ac.kr academic data-resource inclusion
Status: VERIFIED_TARGET
Target pages:
https://redate.iscu.ac.kr/lab/lab04.asp
https://redate.iscu.ac.kr/lab/lab01.asp
https://redate.iscu.ac.kr/lab/lab02.asp
Verified:
2026-09-27
Finding:
- The AI Real Estate Big Data department actively maintains AI Lab resource, market-trend, and AI/PropTech platform pages.
- The platform page curates public and private real-estate data sources such as Korea Real Estate Board R-One, HF housing-finance statistics, Seoul Open Data, public transaction data, court auction data, and major proptech services.
- The department also operates its own real-estate data center and posts externally supplied market materials.
- A stale legacy HousePalm real-estate platform link remains in the PropTech list, providing a possible replacement angle for AptToSell.
Resource fit:
- Resimanor offers structured South Korea housing reference data with CSV/JSON, methodology, and citation metadata suitable for education and analysis.
Submission route:
- No dedicated public external resource-submission form was verified.
- Do not use admissions-only channels unless the department explicitly accepts resource-maintenance requests there.
Next step:
- Look for a department-managed public contact, research-lab contact, partner/contact form, or other non-email route suitable for data-resource suggestions.
Priority: VERY HIGH


### European Housing Coop Community Library
Type: Curated housing research/resource library
Status: SUBMITTED_UNDER_REVIEW
Target:
https://www.housingcoop.eu/resources
Submitted:
2026-09-27
Submitted resource:
South Korea Stress DSR Housing Finance Reference Data (2026)
Submitted link:
https://github.com/cheer710815-hub/resimanor-housing-finance-data
Resource type:
Knowledge
Share method:
Link to a Website
Submission confirmation:
"Resource Submitted Successfully!" and "Your submission is now under review and will be published once approved by our team."
Why it matters:
- European Housing Coop operates an open housing knowledge library for research, policy resources, organisations, projects and events.
- The housing-finance topic is a direct fit for Resimanor's stress-DSR reference data.
- Submission linked directly to the public GitHub repository with CSV/JSON, methodology, official-source references and DOI-backed archives.
Next step:
- Wait for editorial review and publication.
- Do not send follow-up unless requested.
Priority: VERY HIGH


### MIT Orbit resource submission
Type: .edu entrepreneurship resource directory
Status: READY_TO_SUBMIT
Target:
https://orbit.mit.edu/resources/new
Verified:
2026-09-27
Finding:
- MIT Orbit explicitly invites submission of resources that could benefit the MIT entrepreneurship community.
- The form supports category "Outside Org" and "Resources".
- Relevant interests include FinTech, Real Estate, Global, AI and Education.
- Relevant needs include Research and Advice.
- The form includes "Not an MIT student", so external-resource relevance is contemplated.
Resource fit:
- Resimanor is a public South Korea housing-finance reference dataset with direct CSV/JSON, documented methodology, official FSC references, CC BY 4.0 licensing and DOI archives.
Best framing:
- Open research/reference resource for founders, researchers and analysts exploring South Korea housing finance, mortgage affordability and stress-DSR policy.
Next step:
- Submit through the public MIT Orbit resource form.
- Use the GitHub repository as the primary URL.
- Do not present Resimanor as an MIT-affiliated resource.
Priority: VERY HIGH
