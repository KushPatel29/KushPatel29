# Hi, I'm Kush 👋

I'm a BI & Analytics specialist in Vancouver — 4+ years building
finance-grade (GL/P&L) and operations reporting across sales, finance, and
supply chain, most recently at a specialty food distributor. I work the whole
path from raw data to the number an executive acts on: pipelines, warehouse
models, semantic layers, DAX, and the dashboards on top.

**dharma.patel552@gmail.com** · Vancouver, BC · open to BI Analyst /
Analytics Engineer roles

## Eight repos, one rule

Everything below was built under a single rule: **no claim without a number,
and no number without a test that fails if it stops being true.** Every repo
generates its data from a fixed seed, rebuilds end-to-end in GitHub Actions,
and re-verifies its own claims on every push — **300+ automated tests across
the eight repos**. A green badge here means *it runs*, not just that it's
written down.

One of these repos used to be a Raspberry Pi voice assistant I built years
ago. I rebuilt it into the capstone of this portfolio and kept the git
history, because a portfolio that pretends its author sprang fully formed is
lying. Start there:

| Project | The one thing to know | Stack |
|---|---|---|
| 💬 [**Ask Your Data**](https://github.com/KushPatel29/IVA) | A grounded text-to-SQL assistant over all my portfolio datasets (36 tables, 6 business domains). The LLM never answers from memory — it writes SQL, the SQL runs, and it's shown next to the answer. Read-only guard, bounded self-correction proven in CI with a scripted fake model, golden-question accuracy contract. 64 tests. | Python, DuckDB, Claude API, Streamlit |
| 🏗️ [**Supply Chain Control Tower**](https://github.com/KushPatel29/supply-chain-control-tower-) | Medallion pipeline with a three-tier data defense — schema contracts before Bronze, row quarantine with replay, a DQ gate on Gold — each tier proven by CI injecting failures. 10M-row Delta benchmarks, dynamic RLS/OLS verified by impersonated DAX. 49 tests. | Fabric patterns, PySpark, Delta, Power BI |
| 🛒 [**Customer Recommendation Engine**](https://github.com/KushPatel29/Customer-Recommendation-Engine) | The fancy two-stage ranker scored 80.0% hit-rate@10; plain collaborative filtering scored 84.9%. The simple model ships, the loss is documented, and CI enforces that the winner keeps winning. FastAPI + Docker serving, A/B framework, 7-page Power BI. 38 tests. | Python, scikit-learn, FastAPI, MLflow |
| 🧑‍🤝‍🧑 [**HR Attrition Analytics**](https://github.com/KushPatel29/hr-attrition-analytics) | People analytics with the guardrails real employee data demands: k-anonymity masking, a disparate-impact CI gate (four-fifths rule + Fisher's exact), survival analysis with honest censoring. The flight-risk model uses zero protected attributes — and scores better without them. 52 tests. | T-SQL, Python, lifelines, Power BI |
| 🔄 [**Supply Chain Analytics (dbt)**](https://github.com/KushPatel29/supply-chain-analytics-dbt) | dbt Core, staging → marts on dual DuckDB/Snowflake profiles: incremental loads, SCD2 snapshots, MetricFlow semantic layer, Airflow DAG with DagBag validation. 53 dbt tests. | dbt, DuckDB/Snowflake, MetricFlow, Airflow |
| 🏥 [**Healthcare Claims Analytics**](https://github.com/KushPatel29/healthcare-claims-analytics) | Revenue-cycle analytics that goes past reporting into prediction: a Net Realizable Value model prices $3.6M of open AR at the ~$1.7M it will actually collect, with an expected-cash-yield worklist. CI enforces paid ≤ allowed ≤ submitted, NRV ceilings, and AR control totals to the penny. No PHI. 19 tests. | Python, Power BI, DAX |
| 💰 [**GL/P&L Reconciliation**](https://github.com/KushPatel29/gl-reconciliation-dashboard-) | ERP-vs-subledger reconciliation that detects four discrepancy classes and proves every dollar of variance ties to source — then re-runs the same engine, unmodified, over a FOCUS-format cloud bill for FinOps chargeback. 22 tests. | T-SQL, SQLite, Power BI, DAX |
| 🚚 [**Legacy-to-Fabric Migration**](https://github.com/KushPatel29/legacy-to-fabric-migration) | SSIS/SSRS → notebook pipeline with parallel-run validation and a GO/NO-GO cutover gate; negative tests prove the validator catches dropped rows, offsetting errors, and phantom keys. 11 tests. | SSIS, SSRS, T-SQL, PySpark |

## My favorite results are the losses

The two-stage ranker lost to plain collaborative filtering — documented, and
the simple model ships. The gradient-boosted forecaster lost to a moving
average — documented, and the moving average ships. The fairness screen
fired, and the follow-up analysis showed small-sample noise, not bias — so it
became a monitor, not a build-breaker.

Each repo also has a *"things I deliberately didn't build"* section: no
vector database where SQL is the right tool, no deep learning on 38 SKUs, no
cloud cosplay. Knowing when a technique would be decoration is, I think, the
actual skill.

## What I work with

**BI & semantic modeling** — Power BI (DAX, star schema, RLS/OLS,
calculation groups, TMDL/PBIR-as-code, VertiPaq tuning), SSRS ·
**Pipelines** — Microsoft Fabric, ADF/Synapse, PySpark, Delta Lake, dbt,
T-SQL, Python (pandas, scikit-learn) · **LLM apps** — Claude API,
grounded text-to-SQL, eval-driven development · **Governance** — Kimball
modeling, metric dictionaries, data contracts, reconciliation controls,
masking/anonymization · **Legacy MSBI** — SSIS, SQL Agent, and moving all of
it forward without breaking month-end

## Background

- MPS in Analytics (Applied Machine Intelligence), Northeastern University — GPA 3.76
- B.Eng. Computer Science, Gujarat Technological University
- Microsoft Fabric Analytics Engineer Associate (DP-600) — in progress
