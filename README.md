# Customer Churn Analysis

A complete end-to-end data analytics project identifying customer churn patterns and generating actionable business intelligence through automated dashboards, SQL pipelines, and executive reports.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Findings](#-key-findings)
- [Project Architecture](#-project-architecture)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Key Metrics](#-key-metrics)
- [Contributing](#-contributing)
- [Contact](#-contact)

---

## 🎯 Overview

This project analyses 7,043 Telco customer records to uncover what drives churn, quantify the revenue impact, and identify the highest-risk customer segments. It uses Python, SQL, and Power BI to produce professional reports and interactive dashboards.

**What it delivers:**
- 26.5% overall churn rate identified with $139,130/month revenue at risk
- 8 publication-ready visualisations across all key churn drivers
- 14 SQL analytical queries covering cohort analysis, window functions, and risk segmentation
- Interactive Streamlit dashboard with live filtering and 3 analysis tabs
- Excel report, HTML dashboard, and Power BI-ready CSV dataset

---

## 📊 Key Findings

| Driver | Finding | Churn Rate |
|---|---|---|
| Contract Type | Month-to-month customers churn at 15x the rate of 2-year contracts | 42.7% vs 2.8% |
| Internet Service | Fiber Optic drives the highest churn of any service | 41.9% |
| Payment Method | Electronic check users are the least committed | 45.3% |
| Tenure | First 12 months are critical — most churn happens here | ~47% |
| Combined Risk | M-t-M + Fiber Optic + Electronic Check + tenure ≤12 months | 60%+ |

> **Highest-risk profile:** Month-to-month contract + Fiber Optic + Electronic Check + tenure under 12 months — this segment churns at over **60%** and requires immediate intervention.
## 📊 Power BI Dashboard

An interactive Power BI dashboard is included in this repository.

### Dashboard Features

* Executive KPI Overview
* Customer Churn Analysis
* Revenue at Risk Tracking
* Customer Risk Segmentation
* Contract & Payment Method Analysis
* Internet Service Churn Analysis
* Interactive Filters and Drilldowns

### Open the Dashboard

1. Download `churn_dashboard.pbix`
2. Install Power BI Desktop (Free)
3. Open the `.pbix` file
4. If prompted, update the data source path to:

```text
Data/customer churn.csv
```

5. Refresh the dataset

### Key Metrics Included

* Total Customers
* Churned Customers
* Churn Rate %
* Revenue at Risk
* Revenue Retention Rate
* High-Risk Customer Count
* Average Customer Tenure
* Monthly Revenue

### Dashboard Pages

#### Page 1 — Executive Overview

Executive KPIs, churn trends, revenue impact, and retention summary.

#### Page 2 — Customer Segmentation

Contract analysis, internet service analysis, payment methods, and demographic breakdown.

#### Page 3 — Risk Analysis & Recommendations

Risk categories, high-risk customer segments, business impact analysis, and strategic recommendations.

---

**Built by Sabari A S**

This dashboard was developed as part of an end-to-end Customer Churn Analytics project using Python, SQL, Excel, and Power BI.

---

## 🔄 Project Architecture

```
customer churn.csv
      │
      ├── churn_analysis.ipynb      → EDA + 8 visuals saved to visuals/
      │
      ├── dashboard_automation.py  → All visuals + Excel + HTML + Power BI CSV
      │                               saved to dashboard_output/
      │
      ├── sql_automation.py        → 14 SQL queries exported to
      │                               sql_results/churn_sql_results.xlsx
      │
      └── app.py                   → Interactive Streamlit dashboard
                                      (reads Data/ directly)
```

---

## 📁 Project Structure

```
customer-churn-analysis/
├── Data/
│   └── customer churn.csv
├── dashboard_output/
│   ├── churn_dashboard_report.xlsx
│   ├── churn_dashboard.html
│   └── powerbi_dataset.csv
├── sql_results/
│   └── churn_sql_results.xlsx
├── visuals/
│   ├── 01_churn_distribution.png
│   ├── 02_churn_by_contract.png
│   ├── 03_tenure_distribution.png
│   ├── 04_monthly_charges.png
│   ├── 05_churn_by_internet.png
│   ├── 06_churn_by_payment.png
│   ├── 07_churn_heatmap.png
│   └── 08_risk_category.png
├── app.py
├── churn_analysis.ipynb
├── dashboard_automation.py
├── sql_automation.py
├── requirements.txt
├── README.md
└── CONTRIBUTING.md
```

---

## 📦 Requirements

- **Python**: 3.11+
- **MySQL**: 8.0+ (for sql_automation.py only)
- **RAM**: 2GB minimum

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/sabarias1999/customer-churn-analysis.git
cd customer-churn-analysis

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

> **Dataset:** Download `customer churn.csv` from [Kaggle — Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) and place it in the `Data/` folder.

---

## ⚡ Quick Start

### Run EDA Notebook
```bash
jupyter notebook "churn analysis.ipynb"
```

### Generate All Dashboards & Reports
```bash
python dashboard_automation.py
```

### Run SQL Pipeline (requires MySQL)
```bash
python sql_automation.py
```

### Launch Interactive Dashboard
```bash
streamlit run app.py
```

---

## 📊 Key Metrics

| Metric | Value |
|---|---|
| Total Customers | 7,043 |
| Churned | 1,869 (26.5%) |
| Retained | 5,174 (73.5%) |
| High-Risk Customers | 916 |
| Total Monthly Revenue | $139,130 |
| Revenue at Risk | $74,131/month |
| Revenue Retention Rate | 69.5% |

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

Licensed under the MIT License.

---

## 📬 Contact

- **Email**: sabariisalive@gmail.com
- **LinkedIn**: [sabari3299](https://linkedin.com/in/sabari3299)
- **GitHub**: [sabarias1999](https://github.com/sabarias1999)

---

**Last Updated:** June 2026 | **Version:** 2.1.0
