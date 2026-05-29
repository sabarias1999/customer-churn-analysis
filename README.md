# Customer Churn Analysis — Telco

> End-to-end automated churn analysis pipeline — from raw data to interactive dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat)

---

## Business Problem

A telecom company is losing customers every month.
Each churned customer = lost recurring revenue that is expensive to recover.

This project answers:
- **Who** is most likely to churn?
- **Why** are they churning?
- **When** do they churn in their lifecycle?
- **What** can the business do to prevent it?

---

## Pipeline Architecture
---

## Key Findings

| Insight | Finding |
|---|---|
| Overall churn rate | 26.5% of customers churned |
| Highest risk contract | Month-to-month → 42.7% churn rate |
| Highest risk internet | Fiber Optic → 41.9% churn rate |
| Highest risk payment | Electronic Check → 45.3% churn rate |
| Avg tenure at churn | Only 18 months vs 37 months retained |
| Revenue at risk | $139K+/month from churned customers |
| Highest risk segment | Month-to-month + Fiber Optic + tenure ≤12mo |

---

## Project Structure
---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Jupyter Notebook
```bash
jupyter notebook "churn analysis.ipynb"
```

### 3. Launch Streamlit Dashboard
```bash
streamlit run app.py
```

### 4. Run SQL Automation Pipeline
```bash
python "sql automation.py"
```

---

## Business Recommendations

| # | Action | Impact |
|---|---|---|
| 1 | Target month-to-month customers with upgrade offers | Churn drops from 42.7% to 2.8% |
| 2 | Investigate Fiber Optic pricing and quality | 41.9% churn — likely dissatisfaction |
| 3 | Migrate electronic check users to auto-pay | 45.3% to 15% churn reduction |
| 4 | Onboarding program for first 12 months | Most churn happens in year 1 |
| 5 | Bundle Tech Support into new customer plans | Significantly reduces churn |
| 6 | Senior citizen dedicated retention program | 40% churn vs 22% non-senior |

---

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3.x |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| SQL Analytics | MySQL, Window Functions |
| BI Dashboard | Power BI |
| Web App | Streamlit |
| Database | MySQL |

---

## Dashboard

[![Power BI Dashboard](https://img.shields.io/badge/Power_BI-View_Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://linkedin.com/in/sabari3299)

---

*Built by [Sabari A S](https://linkedin.com/in/sabari3299) · Open to Data Analyst roles*