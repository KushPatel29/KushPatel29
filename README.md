# Hi, I'm Kush 👋

I'm a BI & Analytics specialist in Vancouver — 4+ years delivering
finance-grade (GL/P&L) and operations reporting across sales, finance, and
supply chain, most recently at a specialty food distributor. I work the whole
path from raw data to the number an executive acts on: pipelines, warehouse
models, semantic layers, DAX, and the dashboards on top.

📫 **dharma.patel552@gmail.com** ·
🔗 [**LinkedIn**](https://www.linkedin.com/in/kush-patel-48885719b/) ·
📍 Vancouver, BC · ✅ open to **BI Analyst / Analytics Engineer / Decision Support** roles

## Nine repos, one rule

Everything below was built under a single rule: **no claim without a number,
and no number without a test that fails if it stops being true.** Every repo
generates its data from a fixed seed, rebuilds end-to-end in GitHub Actions,
and re-verifies its own claims on every push — **430+ automated tests across
the nine repos**. A green badge here means *it runs*, not just that it's
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
| 🏥 [**Health System Decision Support**](https://github.com/KushPatel29/healthcare-claims-analytics) | Two health systems, one standard. **Canadian side:** CIHI-DAD-shaped activity (CMG+/RIW, cost per weighted case, ALC, risk-adjusted readmission), SPC with Laney correction — where I found the metric everyone reports is 4.8× overdispersed and fires 41 false signals — and a health-economic evaluation that comes out *dominant* on one costing perspective and $192k/QALY on the other. Ends in a briefing note and a costed business case. **US side:** an NRV model pricing $3.6M of open AR at the ~$1.7M it will actually collect. Plus Safe Harbor + k-anonymity de-identification with a measured re-identification risk. No PHI. 97 tests. | Python, Power BI, DAX, SPC, HTA |
| 🧪 [**Clinical Data Management**](https://github.com/KushPatel29/clinical-data-management) | A trial database as code: CDASH CRF metadata, an executable Data Validation Specification, SDTM DM/AE/VS with conformance checks, MedDRA/WHODrug coding, and a UAT plan generated from the spec. The generator writes an exhaustive defect manifest — 49 injected, **49 detected, 0 missed, 0 false positives** — and that reconciliation caught a real bug where four protocol deviations went silently undetected. 51 tests. | Python, CDISC, CDASH/SDTM |
| 💰 [**GL/P&L Reconciliation**](https://github.com/KushPatel29/gl-reconciliation-dashboard-) | ERP-vs-subledger reconciliation that detects four discrepancy classes and proves every dollar of variance ties to source — then re-runs the same engine, unmodified, over a FOCUS-format cloud bill for FinOps chargeback. 22 tests. | T-SQL, SQLite, Power BI, DAX |
| 🚚 [**Legacy-to-Fabric Migration**](https://github.com/KushPatel29/legacy-to-fabric-migration) | SSIS/SSRS → notebook pipeline with parallel-run validation and a GO/NO-GO cutover gate; negative tests prove the validator catches dropped rows, offsetting errors, and phantom keys. 11 tests. | SSIS, SSRS, T-SQL, PySpark |

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

And two bugs found by reconciliation rather than by a person: a visit-window
check keyed on the wrong record, which let four protocol deviations through
silently, and a control chart whose contaminated baseline flagged the stable
months instead of the shifted ones. Neither crashed. Both are now tests.

Each repo also has a *"things I deliberately didn't build"* section: no
vector database where SQL is the right tool, no deep learning on 38 SKUs, no
cloud cosplay. Knowing when a technique would be decoration is, I think, the
actual skill.

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
  [control tower](https://github.com/KushPatel29/supply-chain-control-tower-).
- Secure-by-design delivery: RLS/RBAC, column-level security, masking for
  cost/margin and people data.

**Shivam Investments** — *Financial Analyst, Data & Reporting* (remote)
- GL/P&L reconciliations across sources — the discipline my
  [reconciliation repo](https://github.com/KushPatel29/gl-reconciliation-dashboard-)
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
breaking month-end

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
[**Ask Your Data**](https://github.com/KushPatel29/IVA), read "The rule: no
number without a query," and check that the badge is green. Everything else
here works the same way.*
