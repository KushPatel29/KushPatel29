# Hi, I'm Kush 👋

I'm a data analyst and BI / analytics engineer in Vancouver. For 4+ years,
Finance, Sales and Operations brought me the report that didn't tie out — most
recently as the sole analyst at a specialty food distributor, before that as a
financial analyst running month-end GL/P&L reconciliations. I find the cause,
fix it at the source, and build the SQL, pipelines (Microsoft Fabric, Azure
Data Factory, PySpark) and Power BI reporting that keep it fixed.

📫 **dharma.patel552@gmail.com** ·
🔗 [**LinkedIn**](https://www.linkedin.com/in/kush-patel-48885719b/) ·
📍 Vancouver, BC · ✅ open to **Data Analyst · BI Developer · Analytics Engineer · Data Engineer · Business Analyst · Financial / Supply Chain Analyst** roles across Canada

**Hiring for one of those?** The portfolio ties each role's usual requirements
to evidence, line by line:
[data analyst](https://kushpatel29.github.io/?role=data-analyst#fit) ·
[BI developer](https://kushpatel29.github.io/?role=bi-developer#fit) ·
[analytics engineer](https://kushpatel29.github.io/?role=analytics-engineer#fit) ·
[data engineer](https://kushpatel29.github.io/?role=data-engineer#fit) ·
[business analyst](https://kushpatel29.github.io/?role=business-analyst#fit) ·
[financial analyst](https://kushpatel29.github.io/?role=financial-analyst#fit) ·
[supply chain analyst](https://kushpatel29.github.io/?role=supply-chain-analyst#fit) ·
[data scientist](https://kushpatel29.github.io/?role=data-scientist#fit)

## Sixteen public repos, one rule

Everything below was built under a single rule: **no claim without a number,
and no number without a test that fails if it stops being true.** Every repo
but two generates its data from a fixed seed — the wildfire forecast reads
Canada's public fire and weather records, and the utility model reads US federal filings — rebuilds end-to-end in
GitHub Actions and re-verifies its own claims on every push —
**12,558 automated tests across the sixteen featured repos below**. A green badge here means *it runs*, not
just that it's written down.

Twelve of them have **hosted destinations you can click** — no local install:
[retail analytics platform](https://kushpatel29.github.io/wholesale-analytics-platform/) ·
[transaction monitoring](https://aml-transaction-monitoring.streamlit.app) ·
[cross-sell console](https://cross-sell-rep-console.streamlit.app) ·
[Ask Your Data](https://ask-your-data-kp.streamlit.app) ·
[pricing & costing analytics](https://cost-to-price-calculator.streamlit.app) ·
[attribution vs truth](https://attribution-vs-truth.streamlit.app) ·
[clinical evidence console](https://kush-clinical-data-dashboard.streamlit.app/) ·
[inventory decision studio](https://inventory-analytics-app.onrender.com/) ·
[network risk decision room](https://kush-network-risk-decision-room.streamlit.app/) ·
[workforce decision room](https://kush-workforce-decision-room.streamlit.app/) ·
[wildfire risk forecast](https://wildfire-prediction-app1.streamlit.app) ·
[asset-management decision board](https://kush-asset-management-decision-board.streamlit.app/).
The first is a prerendered static site, so it opens instantly. Inventory
Analytics runs on Render; the other ten interactive destinations run on
Streamlit Community Cloud, where a job visits every one of them every three
hours so a link does not land on a sleeping app. A first load can still take a
moment, or ask for a Streamlit sign-in if the host's visibility setting changes.

**Hiring for business analysis, asset management, or operational decision
support?** Start with the
[Inventory Analytics live decision studio](https://inventory-analytics-app.onrender.com/)
and its [requirements-to-UAT interview case](https://github.com/KushPatel29/inventory-analytics-app/blob/main/docs/business-analysis-and-interview-guide.md),
then review the
[live asset-management decision board](https://kush-asset-management-decision-board.streamlit.app/),
its [portfolio case](https://kushpatel29.github.io/#asset-management-proof),
the [asset lifecycle, condition/criticality, renewal and capital-scenario evidence](https://github.com/KushPatel29/legacy-to-fabric-migration/tree/master/examples/asset_management)
and its [five-year asset capital programme business case](https://github.com/KushPatel29/legacy-to-fabric-migration/blob/master/docs/business-analysis/ASSET_CAPITAL_PROGRAM_BUSINESS_CASE.md)
and the [public-sector decision and procurement brief](https://github.com/KushPatel29/legacy-to-fabric-migration/blob/master/docs/business-analysis/PUBLIC_SECTOR_DECISION_AND_PROCUREMENT_BRIEF.md).
All asset records, coordinates, costs, conditions and scenarios are synthetic;
the evidence demonstrates transferable methods, not municipal employment or
an approved capital plan.

One of these repos used to be a Raspberry Pi voice assistant I built years
ago. I rebuilt it into the capstone of this portfolio and kept the git
history, because a portfolio that pretends its author sprang fully formed is
lying. Start there:

| Project | The one thing to know | Stack |
|---|---|---|
| 💬 [**Ask Your Data**](https://github.com/KushPatel29/ask-your-data) · [**live ▶**](https://ask-your-data-kp.streamlit.app) | Grounded text-to-SQL over 71 tables in 11 business domains, asked by voice or text, with **two engines**. The live demo has no API key and needs none: a **deterministic compiler** profiles the warehouse (column roles, grains, join graph, a 797-phrase value lexicon read straight out of the data) and binds your words to it, so it answers questions nobody pre-registered. On its 58-question contract it is **46 right, 0 wrong, 12 refused** — refusing is the feature. Add a key and Claude writes the SQL instead, through the same read-only guard, structural verifier and default-deny access policy; its prose is then **checked back against the returned rows**, so a sentence cannot quote a number the query never produced. Six certified metrics carry an owner and a CI-asserted value. Speech runs **in-process on open models** — faster-whisper and Piper, checksum-pinned — so it listens and answers aloud with no account. I found half its early answers wrong by attacking my own eval four times over, and the README says so. 1,128 tests. | Python, DuckDB, ONNX, Claude API, Streamlit |
| 💵 [**Pricing & Costing Analytics**](https://github.com/KushPatel29/pricing-costing-analytics) · [**live ▶**](https://cost-to-price-calculator.streamlit.app) | The list price is not the price: **18.2% of it never arrives**, once every rebate, payment term, freight allowance and return is counted. Margin is expressed on *pocket* price throughout, because a margin quoted on list is the number that lets a deal look healthy while losing money. The output is not an elasticity, it is a sentence — six ordered actions across 240 products **worth $2.65M of annual gross margin**, each carrying the reason and a confidence about the *evidence* rather than the size of the prize. The part worth asking about: **the dataset is built so the analysis can be caught being wrong.** Elasticity, cost pass-through and segment price sensitivity are seeded deliberately and taken back out through the real code — estimated category elasticities preserve the seeded ordering at **rank correlation 0.95**, every pass-through estimate attenuated toward zero. Underneath, an SAP-shaped ERP extract with defects injected on purpose: all twelve quality rules find something and the reconciliation balances to **$0.00 unexplained**. Six marts computed a second time in DuckDB and held to the pandas ones at 1e-8 — which is how the price-band median was caught five percent apart under the same column name. A **nineteen-page Power BI project generated from spec** — opened in Desktop, refreshed and exported page by page with **0 broken visuals**, which is how nine defects no structural test could see were found and fixed, each one now a check in the generator. A **governed decision room** registers all 240 proposals, routes each material one to a named authority and leaves 161 decisions for a human; of 2,075 approved historical changes, 1,132 stay on an explanation queue rather than becoming a benefit claim. 3,182 tests. | Python, DuckDB, Power BI (PBIR/TMDL), Streamlit |
| ⚡ [**Finance Decision Models in Excel and Power BI**](https://github.com/KushPatel29/excel-fpa-model) · [**utility workbook ↓**](https://github.com/KushPatel29/excel-fpa-model/raw/main/workbook/PGE_Utility_FPA_Model.xlsx) · [**B.C. model ↓**](https://github.com/KushPatel29/excel-fpa-model/raw/main/examples/bc-local-government/BC_Local_Government_Finance_Model.xlsx) · [**Kestrel Bay ↓**](https://github.com/KushPatel29/excel-fpa-model/raw/main/examples/kestrel-bay/Kestrel_Bay_FPA_Model.xlsx) · [**Power BI**](https://github.com/KushPatel29/excel-fpa-model#the-same-numbers-in-power-bi) | Three complementary models: Portland General Electric plan-vs-actual from EIA, FERC and NOAA, published in Excel and a seven-page PBIP/TMDL report; a B.C. local-government model that contracts 66 official workbooks into six years of history for 161 municipalities plus five-year operating, capital, debt and reserve scenarios; and the preserved Kestrel Bay distributor model for channel economics, PVM and working capital. Source drift, accounting identities and workbook surfaces are covered by 1,218 tests. | Excel, Power Query, Power Pivot, DAX, LINEST, scenario modelling, public-sector finance, Power BI (PBIP/TMDL) |
| 🔎 [**Transaction Monitoring**](https://github.com/KushPatel29/aml-transaction-monitoring) · [**live ▶**](https://aml-transaction-monitoring.streamlit.app) | A flat $10,000 reporting threshold finds 38 of 60 planted cases and raises 555 alerts doing it. Five explainable rules over an unsupervised model find **all 60 on a third fewer alerts**, at 2.4× the precision. The honest half: ablation shows the anomaly model lifts ranking 49% but saves 1.8% at the operating point — so the README says it earns its place on triage *order*, not on the accept/reject decision. 17 SQL features proven equal to their Python twins on all 100,299 rows. 183 tests. | Python, SQLite, scikit-learn, Streamlit |
| 🏪 [**Retail Analytics Platform**](https://github.com/KushPatel29/wholesale-analytics-platform) · [**live ▶**](https://kushpatel29.github.io/wholesale-analytics-platform/) | Sixteen pages that between them printed **three different HHI values at the same time**, because every page did its own arithmetic. One catalogue now governs **62 definitions: 47 implemented and 15 explicitly unavailable without a named source system**. Every implemented metric carries a formula, grain, source table, owner page and **gross-or-net basis**, pinned by a hand-computed test. The demand planner used to produce a forecast nobody scored; it now leads with **WAPE 11.6% and a 40% hit rate** from a rolling-origin backtest, and demotes MAPE to a labelled diagnostic because small SKU-month denominators make it least reliable where it looks most alarming. Finance adds statements whose revenue and COGS are read from the sales fact (net margin 2.8%, current ratio 1.02×, ROA 2.3%); marketing adds CAC $17,667 on an 11.0-month payback. Inventory turnover appears twice on two honest bases, and ROMI is withheld outright — spend and wins exist, exposure and a counterfactual do not. Prerendered: 100 charts frozen to SVG, every page verified with networking blocked. 1,423 tests. | Python, Flask, DuckDB, Plotly, Playwright, Docker |
| 🏗️ [**Supply Chain Control Tower**](https://github.com/KushPatel29/supply-chain-control-tower) · [**live ▶**](https://kush-network-risk-decision-room.streamlit.app/) | Medallion pipeline with a three-tier data defense — schema contracts before Bronze, row quarantine with replay, a DQ gate on Gold — each tier proven by CI injecting failures. The live Network Risk Decision Assurance Studio opens with an executive decision brief and adds governed GIS evidence: 34 synthetic WGS 84 reference points, QGIS/ArcGIS-ready GeoJSON, nearest-node screening, traceable requirements and UAT, accountable handoff, and a reproducible evidence pack. The map deliberately labels straight-line proximity as screening rather than route, capacity, or execution approval. 10M-row Delta benchmarks and dynamic RLS/OLS verified by impersonated DAX. 826 tests. | Fabric patterns, PySpark, Delta, Power BI, Streamlit, GIS |
| 📦 [**Inventory Analytics**](https://github.com/KushPatel29/inventory-analytics-app) · [**live ▶**](https://inventory-analytics-app.onrender.com/) · [**BA case**](https://github.com/KushPatel29/inventory-analytics-app/blob/main/docs/business-analysis-and-interview-guide.md) | A six-workspace operations decision studio that turns nine WMS/ERP extracts into demand forecasts, replenishment decisions, ABC-XYZ policy, network-transfer screening, supplier performance, inventory-accuracy controls, and a financially ranked action register. Seven forecasting methods compete in rolling-origin backtests; Python calculations are held to DuckDB marts by 14 parity tests; every page ends in a decision, export, or named handoff rather than another chart. The deterministic demo covers 420 SKUs across 7 nodes and produces 1,170 prioritized actions. Its reviewable BA case adds stakeholders, current/future state, 11 traced requirements, 10 UAT scenarios, a pilot/adoption plan, and an eight-minute interview walkthrough. 316 tests. | Python, Flask, DuckDB, forecasting, inventory planning, BA delivery, Render |
| 🛒 [**Customer Recommendation Engine**](https://github.com/KushPatel29/Customer-Recommendation-Engine) · [**live ▶**](https://cross-sell-rep-console.streamlit.app) | The fancy two-stage ranker scored 81.2% recall@10; plain collaborative filtering scored 84.9%. The simple model ships, the loss is documented, and CI enforces that the winner keeps winning. The live rep console turns that into what a salesperson actually needs: what to pitch next, why, and what it's worth. A **decision room** now scores it on seven objectives, not one — relevance, reach, novelty, diversity, calibration, eligibility — breaks results out by five slices (the weakest warm slice sits at 67.6%), audits all 791 served items against the eligibility rules, and falls back to a labelled regional default that invents no dollar opportunity. It recommends a human-reviewed pilot and a pre-registered experiment, because offline recall does not measure sales lift. FastAPI + Docker serving, 9-page Power BI. 814 tests. | Python, scikit-learn, FastAPI, MLflow |
| 📈 [**Marketing Attribution & Incrementality**](https://github.com/KushPatel29/marketing-attribution-analytics) · [**live ▶**](https://attribution-vs-truth.streamlit.app) | Attribution is the one analytics discipline where everyone argues and nobody can check the answer, because the counterfactual isn't in the data. So I generated one: each user carries a fixed random draw, and a channel's true contribution is measured by re-running that draw with its touches deleted. Six models compete against it and **none wins** — the exact Shapley value and a Markov chain both lose to a heuristic that fits in a `CASE` expression. Last-touch hands *direct* 24.5% of conversions against a true 1.9%. Then a geo holdout settles it: naive pre/post reads 11.0% against a planted 5.5%, difference-in-differences returns 4.0% with an interval that covers it. A second act asks the same questions of a **B2B SaaS motion** — CRM pipeline, ARR waterfall, NRR vs GRR, quota and capacity, a LookML semantic layer — and finds the segment with the fastest cycle and the best pipeline coverage is the one that loses money on every customer. The **investment decision room** on top chooses between attribution, a lift test and experiment-calibrated MMM per question, refuses to fit MMM to twelve months of data, and reallocates a constant $37.2K budget across diminishing-return curves — with only one of four channel moves experiment-calibrated, and the other three shown as test-gated. 128 tests. | Python, SQL, causal inference, LookML, Streamlit |
| 🔥 [**Canada Wildfire Risk**](https://github.com/KushPatel29/wildfire-prediction-app) · [**live ▶**](https://wildfire-prediction-app1.streamlit.app) · [**this week ▶**](https://kushpatel29.github.io/wildfire/) | The one project here that runs on real data. It began as a 2024 hackathon win — a random forest on hectares burned per month — and is now a daily seven-day ignition forecast for Canada's 753 one-degree cells, over 4.0M cell-days of the National Fire Database and 3,198 CWFIS stations. The Fire Weather Index is implemented from Van Wagner and replayed against CWFIS's own published codes. Two boosters (a classifier and a Poisson count) are averaged and isotonically calibrated, trained to 2016, tuned on 2017–2019 and scored **once** on 2020–2024: **ROC-AUC 0.881** against 0.822 for each cell's own rate for the month, with **57.5% of 27,147 fires inside the riskiest tenth re-ranked every morning**. The part I would read first is the bug behind those numbers: a pandas index misalignment had put **97.7% of fires in another fire's cell**, and the model trained, calibrated and scored 0.807 on the scrambled record without an error anywhere. The one score it could not fake — this season, graded against satellites — was the one where the plain Fire Weather Index beat it; a map of the grid's provinces, with Nova Scotia's fires in the Yukon, gave it away. Fixed, it beats FWI there too, 0.743 to 0.724. GitHub Actions rebuilds the forecast twice a day; an eight-page Power BI project is generated from spec. 111 tests. | Python, XGBoost, FWI System, GIS, Power BI, GitHub Actions |
| 🧑‍🤝‍🧑 [**HR Attrition Analytics**](https://github.com/KushPatel29/hr-attrition-analytics) · [**live ▶**](https://kush-workforce-decision-room.streamlit.app/) | People analytics with the guardrails real employee data demands: k-anonymity masking, a disparate-impact CI gate (four-fifths rule + Fisher's exact), survival analysis with honest censoring. The flight-risk model uses zero protected attributes — and scores better without them. The live **workforce decision room** shows none of it per person: six cohort-level proposals, each with an owner, approval path and rollback trigger, small cohorts suppressed, and a release docket held at *review required* while two of its eight controls wait for named human review. 822 tests. | T-SQL, Python, lifelines, Power BI |
| 🔄 [**Supply Chain Analytics (dbt)**](https://github.com/KushPatel29/supply-chain-analytics-dbt) | dbt Core, staging → marts on dual DuckDB/Snowflake profiles: incremental loads, SCD2 snapshots, MetricFlow semantic layer, Airflow DAG with DagBag validation. **6 unit tests** run the model SQL against fixed inputs, so a change to the OTIF threshold or a partly shipped line priced on the wrong quantity fails the build — the data tests would not notice either. 157 dbt data tests across 15 models. | dbt, DuckDB/Snowflake, MetricFlow, Airflow |
| 🏥 [**Health System Decision Support**](https://github.com/KushPatel29/healthcare-claims-analytics) | Two health systems, one standard. **Canadian side:** CIHI-DAD-shaped activity (CMG+/RIW, cost per weighted case, ALC, risk-adjusted readmission), SPC with Laney correction — where I found the metric everyone reports is 4.6× overdispersed and fires 41 signals in 19 of 24 months — and a health-economic evaluation that comes out *dominant* on one costing perspective and $192k/QALY on the other. Ends in a briefing note and a costed business case. **US side:** an NRV model pricing $5.2M of open AR at the ~$2.2M it will actually collect. Plus Safe Harbor + k-anonymity de-identification with a measured re-identification risk. The Canadian layer now leads the Power BI report — activity and the ALC/flow/SPC page come first, because that is the order a health authority reads them in. No PHI. 819 tests. | Python, Power BI, DAX, SPC, HTA |
| 🧪 [**Clinical Data Management**](https://github.com/KushPatel29/clinical-data-management) · [**live ▶**](https://kush-clinical-data-dashboard.streamlit.app/) | A trial database as code: CDASH CRF metadata, an executable Data Validation Specification, SDTM DM/AE/VS with conformance checks, MedDRA/WHODrug coding, and a UAT plan generated from the spec. The generator writes an exhaustive defect manifest — 49 injected, **49 detected, 0 missed, 0 false positives** — and that reconciliation caught a real bug where four protocol deviations went silently undetected. The status board is hand-generated SVG, because "stdlib only" is a claim and a chart is not a good enough reason to break it. 281 tests. | Python, CDISC, CDASH/SDTM |
| 💰 [**GL/P&L Reconciliation**](https://github.com/KushPatel29/gl-reconciliation-dashboard) | ERP-vs-subledger reconciliation that detects four discrepancy classes and proves every dollar of variance ties to source — then re-runs the same engine, unmodified, over a FOCUS-format cloud bill for FinOps chargeback. 710 tests. | T-SQL, SQLite, Power BI, DAX, Tableau |
| 🏗️ [**Asset Management & Legacy-to-Fabric**](https://github.com/KushPatel29/legacy-to-fabric-migration) · [**live decision board ▶**](https://kush-asset-management-decision-board.streamlit.app/) · [**capital business case**](https://github.com/KushPatel29/legacy-to-fabric-migration/blob/master/docs/business-analysis/ASSET_CAPITAL_PROGRAM_BUSINESS_CASE.md) | The live board connects a governed 96-record, six-service asset/GIS portfolio to three investment postures, a cash- and capacity-constrained ten-year plan, capital PV, cost/funding sensitivities, indicative funding, owned risk/benefit/requirement registers and delivery gates. Nine bad source records stay blocked. The wider repo adds SSIS/SSRS → Fabric parallel-run validation, requirements/process/RAID/UAT/adoption evidence, Microsoft 365 design and public-sector procurement controls. The recommendation authorizes validation—not spending, engineering approval or a municipal claim. 440 tests. | Asset management, capital business case, BA delivery, GIS, Streamlit, Fabric, SSIS/SSRS, Python |

## My favorite results are the losses

The two-stage ranker lost to plain collaborative filtering — documented, and
the simple model ships. The gradient-boosted forecaster lost to a moving
average — documented, and the moving average ships. The fairness screen
fired, and the follow-up analysis showed small-sample noise, not bias — so it
became a monitor, not a build-breaker. The health-economics model came out
*dominant* under one costing perspective and not worth funding under the
other — so the business case recommends approval explicitly **not** as a
savings initiative, because saying both is what makes the first half
believable.

The layered transaction-monitoring detector is the same shape: blending an
anomaly model into the score lifts ranking by 49%, and saves 1.8% at the
threshold you would actually run. Both numbers are in the README, because
only quoting the first one is how a model gets credit for work the rules did.

The biggest loss is the attribution project, where I built a dataset with a
known answer and then watched **every model fail to find it** — including the
exact Shapley value and a Markov chain, both beaten by a 40/20/40 heuristic.
The reason turned out to be structural rather than fixable: every model that
reads only a journey log can see how often a channel was *present*, never
whether it *caused* anything. That is also where the nicest piece of nuance in
the portfolio lives — last-touch is the worst model in the table and the least
damaging one for splitting paid budget, because its catastrophic error lands
on a channel nobody can buy.

And three bugs found by reconciliation rather than by a person: a visit-window
check keyed on the wrong record, which let four protocol deviations through
silently; a control chart whose contaminated baseline flagged the stable
months instead of the shifted ones; and a p′ chart that **rendered completely
empty while passing every test it had** — the tests checked the maths, and
nothing checked that the thing drew. None of them crashed. All three are now
tests.

Each repo also has a *"things I deliberately didn't build"* section: no vector
search over business rows where SQL is the right tool (Ask Your Data embeds only
schema descriptions), no deep learning on 38 SKUs, no cloud cosplay. Knowing
when a technique would be decoration is, I think, the actual skill.

## Where I've done this for real

The repos above aren't hypotheticals — they're sharpened versions of problems
I've worked professionally:

**Two Rivers Specialty Meats** — *Data Analyst: Operations, Logistics &
Enterprise Reporting* (Vancouver)
- Defined governed KPIs for P&L/GL and operations (OTIF, inventory turns,
  days on hand) with Sales, Finance, and Supply Chain; built the Power BI
  star-schema models and DAX behind them.
- Developed Fabric / ADF / Synapse pipelines (SQL, PySpark) on
  Bronze→Silver→Gold patterns while owning the legacy SSIS/SSRS estate — the
  same modernization my [migration repo](https://github.com/KushPatel29/legacy-to-fabric-migration)
  rehearses with a GO/NO-GO parallel-run gate.
- Automated data-quality and reconciliation controls with logging and
  exception reporting — cutting recurring discrepancies by ~45% and reporting
  errors by ~30%. FEFO/expiry-risk and lot-traceability analytics for
  perishable inventory — the direct ancestor of my
  [control tower](https://github.com/KushPatel29/supply-chain-control-tower).
- Secure-by-design delivery: RLS/RBAC, column-level security, masking for
  cost/margin and people data.

**Shivam Investments** — *Financial Analyst, Data & Reporting* (remote)
- GL/P&L reconciliations across sources — the discipline my
  [reconciliation repo](https://github.com/KushPatel29/gl-reconciliation-dashboard)
  turns into a tested engine.
- Automated recurring analysis with Python + SQL feeding Power BI, cutting
  manual effort ~40%.

## What I work with

**BI & semantic modeling** — Power BI (DAX, star schema, RLS/OLS,
calculation groups, TMDL/PBIR-as-code, VertiPaq tuning), SSRS ·
**Pipelines** — Microsoft Fabric, ADF/Synapse, PySpark, Delta Lake, dbt,
Airflow, T-SQL, Python (pandas, scikit-learn) — ETL/ELT patterns that carry
directly to Talend and equivalent enterprise integration platforms ·
**Health analytics** — CIHI DAD/CMG+/RIW, cost per weighted case, ALC and
patient flow, risk adjustment by indirect standardisation, SPC (p/u charts,
Western Electric, Laney), health economics (ICER, budget impact, PSA/CEAC),
CDISC CDASH/SDTM · **LLM apps** — Claude API, grounded text-to-SQL,
eval-driven development · **Governance** — Kimball modeling, metric
dictionaries, data contracts, reconciliation controls, HIPAA Safe Harbor and
k-anonymity de-identification, PHI/PII-safe pipeline design ·
**Legacy MSBI** — SSIS, SQL Agent, and moving all of it forward without
breaking month-end · **Business analysis** — stakeholder and requirements
work, current/future-state process, business cases, charters, traceability,
RAID/status, UAT, change/adoption, executive decision briefs and vendor-option
evaluation · **Asset and spatial information (portfolio evidence)** — governed
asset registers, lifecycle, condition, criticality, inspections, renewal need,
multi-year options, capital affordability/PV, sensitivity, funding, risk,
benefits, delivery gates, GIS reconciliation, GeoJSON and WGS 84 · **Microsoft
365** — Word, Excel, PowerPoint and Teams; SharePoint information architecture
and Power Automate workflow design are clearly labelled portfolio blueprints,
not production administration

## Background

- 🎓 MPS in Analytics (Applied Machine Intelligence), Northeastern
  University, Vancouver — GPA 3.76
- 🎓 B.Eng. Computer Science, Gujarat Technological University
- 📜 Microsoft Fabric Analytics Engineer Associate (DP-600) — in progress
- 🏆 First prize at a wildfire-prediction hackathon — Python + Azure + live
  sensor data (DHT22/LM393), because sometimes the dashboard needs hardware

<details>
<summary>📚 More certifications & coursework</summary>

- Google Data Analytics
- IBM Python for Data Science, AI and Development
- Power BI Data Modelling with DAX · Advanced SQL
- SQL for Data Science: Data Pipelines, DBMS, Data Modeling

</details>

---

*If you only have five minutes: open
[**Ask Your Data**](https://ask-your-data-kp.streamlit.app) and type a question
of your own — no API key needed. The SQL that produced the number is shown
underneath it, along with the table, the measure and the filter it bound, and
which words in your question paid for each. Ask it something it cannot compile
and it refuses rather than guessing. Then read
["The rule: no number without a query"](https://github.com/KushPatel29/ask-your-data)
and check the badge is green. Everything else here works the same way.*
