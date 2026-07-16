# Hi, I'm Kush 👋

I'm a BI & Analytics specialist in Vancouver — 4+ years building
finance-grade (GL/P&L) and operations reporting across sales, finance, and
supply chain, most recently at a specialty food distributor. I work across
the whole path from raw data to the number an executive acts on: pipelines,
warehouse models, semantic layers, DAX, and the dashboards on top.

**dharma.patel552@gmail.com** · Vancouver, BC · open to BI Analyst /
Analytics Engineer roles

## The portfolio, and the rule behind it

Everything below was built under one rule: **no claim without a number, and
no number without a test that fails if it stops being true.** Every repo
generates its data from a fixed seed, rebuilds end-to-end in GitHub
Actions, and re-verifies its own claims on every push — a green badge means
it runs, not just that it's written down.

| Project | The one thing to know | Stack |
|---|---|---|
| [**Supply Chain Control Tower**](https://github.com/KushPatel29/supply-chain-control-tower-) | Medallion pipeline with a three-tier data defense — schema contracts before Bronze, row quarantine with replay, a DQ gate on Gold — each tier proven by CI injecting failures. 10M-row Delta benchmarks, dynamic RLS/OLS verified by impersonated DAX. 49 tests. | Fabric patterns, PySpark, Delta, Power BI |
| [**Customer Recommendation Engine**](https://github.com/KushPatel29/Customer-Recommendation-Engine) | The fancy two-stage ranker scored 80.0% hit-rate@10; plain collaborative filtering scored 84.9%. The simple model ships, the loss is documented, and CI enforces the winner keeps winning. FastAPI + Docker serving, A/B framework, 7-page Power BI. 38 tests. | Python, scikit-learn, FastAPI, MLflow |
| [**HR Attrition Analytics**](https://github.com/KushPatel29/hr-attrition-analytics) | People analytics with the guardrails real employee data demands: k-anonymity masking, a disparate-impact CI gate (four-fifths rule + Fisher's exact), survival analysis with honest censoring. The flight-risk model uses zero protected attributes — and scores better without them. 52 tests. | T-SQL, Python, lifelines, Power BI |
| [**Supply Chain Analytics (dbt)**](https://github.com/KushPatel29/supply-chain-analytics-dbt) | dbt Core, staging → marts on dual DuckDB/Snowflake profiles: incremental loads, SCD2 snapshots, MetricFlow semantic layer, Airflow DAG with DagBag validation. 53 dbt tests. | dbt, DuckDB/Snowflake, MetricFlow, Airflow |
| [**GL/P&L Reconciliation**](https://github.com/KushPatel29/gl-reconciliation-dashboard-) | ERP-vs-subledger reconciliation that detects four discrepancy classes and proves every dollar of variance ties to source. Month-end close scorecard in Power BI. | T-SQL, SQLite, Power BI, DAX |
| [**Healthcare Claims Analytics**](https://github.com/KushPatel29/healthcare-claims-analytics) | Revenue-cycle dashboard over 12k synthetic claims; CI enforces paid ≤ allowed ≤ submitted and AR control totals to the penny. No PHI. | Python, Power BI, DAX |
| [**Legacy-to-Fabric Migration**](https://github.com/KushPatel29/legacy-to-fabric-migration) | SSIS/SSRS → notebook pipeline with parallel-run validation and a GO/NO-GO cutover gate; negative tests prove the validator catches dropped rows, offsetting errors, and phantom keys. | SSIS, SSRS, T-SQL, PySpark |

A pattern you'll notice: the results I'm proudest of are losses. The
two-stage ranker lost to plain CF. The gradient-boosted forecaster lost to
a moving average. The fairness screen fired, and the follow-up showed it
was small-sample noise, not bias. Each repo also has a *"things I
deliberately didn't build"* section — knowing when a vector database or a
deep-learning layer would be decoration is, I think, the actual skill.

## What I work with

**BI & semantic modeling** — Power BI (DAX, star schema, RLS/OLS,
calculation groups, TMDL/PBIR-as-code, VertiPaq tuning), SSRS ·
**Pipelines** — Microsoft Fabric, ADF/Synapse, PySpark, Delta Lake, dbt,
T-SQL, Python (pandas, scikit-learn) · **Governance** — Kimball modeling,
metric dictionaries, data contracts, reconciliation controls,
masking/anonymization · **Legacy MSBI** — SSIS, SQL Agent, and moving all
of it forward without breaking month-end

## Background

- MPS in Analytics (Applied Machine Intelligence), Northeastern University — GPA 3.76
- B.Eng. Computer Science, Gujarat Technological University
- Microsoft Fabric Analytics Engineer Associate (DP-600) — in progress
