"""
============================================================
 Customer Churn Analysis — Streamlit Dashboard
 Author  : Sabari A S
 LinkedIn: linkedin.com/in/sabari3299
============================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

warnings.filterwarnings("ignore")

# ── Page Config ──────────────────────────────────────────
st.set_page_config(
    page_title="Customer Churn Analysis",
    page_icon="📡",
    layout="wide"
)

# ── Colors ───────────────────────────────────────────────
CHURN_COLOR   = "#E24B4A"
RETAIN_COLOR  = "#1D9E75"
NEUTRAL_COLOR = "#378ADD"
AMBER_COLOR   = "#FAC775"

# ── Load Data ────────────────────────────────────────────
@st.cache_data
def load_data():
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, "Data", "customer churn.csv")
    df = pd.read_csv(path)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())
    df["Churn_Flag"]   = (df["Churn"] == "Yes").astype(int)
    df["RiskScore"]    = (
        np.where(df["Contract"]        == "Month-to-month", 40, 0)
        + np.where(df["InternetService"] == "Fiber optic",   30, 0)
        + np.where(df["tenure"]          <= 12,              30, 0)
    )
    df["RiskCategory"] = pd.cut(
        df["RiskScore"],
        bins=[-1, 30, 60, 100],
        labels=["Low", "Medium", "High"]
    )
    df["TenureBand"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 72],
        labels=["0-12 Months", "13-24 Months", "25-48 Months", "49-72 Months"]
    )
    return df

df = load_data()

# ── Sidebar ──────────────────────────────────────────────
st.sidebar.title("🔍 Filters")

contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df["Contract"].unique(),
    default=df["Contract"].unique()
)
internet_filter = st.sidebar.multiselect(
    "Internet Service",
    options=df["InternetService"].unique(),
    default=df["InternetService"].unique()
)
tenure_filter = st.sidebar.slider(
    "Tenure Range (months)",
    min_value=int(df["tenure"].min()),
    max_value=int(df["tenure"].max()),
    value=(int(df["tenure"].min()), int(df["tenure"].max()))
)
risk_filter = st.sidebar.multiselect(
    "Risk Category",
    options=["Low", "Medium", "High"],
    default=["Low", "Medium", "High"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Built by Sabari A S**")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/sabari3299) · [GitHub](https://github.com/sabarias1999)")

# ── Apply Filters ────────────────────────────────────────
filtered = df[
    (df["Contract"].isin(contract_filter)) &
    (df["InternetService"].isin(internet_filter)) &
    (df["tenure"].between(tenure_filter[0], tenure_filter[1])) &
    (df["RiskCategory"].astype(str).isin(risk_filter))
]

# ── Header ───────────────────────────────────────────────
st.title("📡 Customer Churn Analysis Dashboard")
st.markdown("**Telco Customer Churn — End-to-End Analytics | Sabari A S**")
st.markdown("---")

# ── KPI Cards ────────────────────────────────────────────
total      = len(filtered)
churned    = int(filtered["Churn_Flag"].sum())
churn_rate = churned / total if total > 0 else 0
rev_risk   = filtered[filtered["Churn"] == "Yes"]["MonthlyCharges"].sum()
high_risk  = int((filtered["RiskCategory"] == "High").sum())

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total Customers",   f"{total:,}")
k2.metric("Churned",           f"{churned:,}")
k3.metric("Churn Rate",        f"{churn_rate:.1%}")
k4.metric("Revenue at Risk",   f"${rev_risk:,.0f}/mo")
k5.metric("High-Risk Customers", f"{high_risk:,}")

st.markdown("---")

# ── Tabs ─────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["📊 Overview", "🔬 Segment Analysis", "⚠️ Risk Profiling"])

# ════════════════════════════════════════
# TAB 1 — Overview
# ════════════════════════════════════════
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Churn Distribution")
        fig, ax = plt.subplots(figsize=(5, 3))
        counts = filtered["Churn"].value_counts()
        ax.bar(counts.index, counts.values,
               color=[RETAIN_COLOR, CHURN_COLOR], width=0.5, edgecolor="white")
        for i, (idx, val) in enumerate(counts.items()):
            ax.text(i, val + 20, f"{val:,}\n({val/total:.1%})",
                    ha="center", fontsize=9, fontweight="bold")
        ax.set_ylabel("Customers")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("Tenure Distribution")
        fig, ax = plt.subplots(figsize=(5, 3))
        filtered[filtered["Churn"] == "No"]["tenure"].hist(
            ax=ax, bins=30, alpha=0.7, color=RETAIN_COLOR,
            label="Retained", edgecolor="white")
        filtered[filtered["Churn"] == "Yes"]["tenure"].hist(
            ax=ax, bins=30, alpha=0.7, color=CHURN_COLOR,
            label="Churned", edgecolor="white")
        ax.set_xlabel("Tenure (months)")
        ax.set_ylabel("Customers")
        ax.legend(fontsize=9)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    st.subheader("Churn Heatmap — Contract × Internet Service")
    fig, ax = plt.subplots(figsize=(8, 3))
    pivot = filtered.pivot_table(
        values="Churn_Flag", index="Contract",
        columns="InternetService", aggfunc="mean") * 100
    sns.heatmap(pivot, annot=True, fmt=".1f",
                cmap="RdYlGn_r", linewidths=0.5, ax=ax,
                cbar_kws={"label": "Churn Rate (%)"})
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# ════════════════════════════════════════
# TAB 2 — Segment Analysis
# ════════════════════════════════════════
with tab2:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Churn by Contract Type")
        fig, ax = plt.subplots(figsize=(5, 3))
        data = filtered.groupby("Contract")["Churn_Flag"].mean().sort_values(ascending=False) * 100
        ax.barh(data.index, data.values,
                color=[CHURN_COLOR, AMBER_COLOR, RETAIN_COLOR], edgecolor="white")
        for i, val in enumerate(data.values):
            ax.text(val + 0.5, i, f"{val:.1f}%", va="center", fontsize=9, fontweight="bold")
        ax.set_xlabel("Churn Rate (%)")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("Churn by Internet Service")
        fig, ax = plt.subplots(figsize=(5, 3))
        data = filtered.groupby("InternetService")["Churn_Flag"].mean().sort_values(ascending=False) * 100
        ax.bar(data.index, data.values,
               color=[CHURN_COLOR, AMBER_COLOR, RETAIN_COLOR], width=0.5, edgecolor="white")
        for bar, val in zip(ax.patches, data.values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                    f"{val:.1f}%", ha="center", fontsize=9, fontweight="bold")
        ax.set_ylabel("Churn Rate (%)")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Churn by Payment Method")
        fig, ax = plt.subplots(figsize=(5, 3))
        data  = filtered.groupby("PaymentMethod")["Churn_Flag"].mean().sort_values(ascending=False) * 100
        short = [p.replace(" (automatic)", "\n(auto)") for p in data.index]
        ax.barh(short, data.values,
                color=[CHURN_COLOR, AMBER_COLOR, RETAIN_COLOR, RETAIN_COLOR], edgecolor="white")
        for i, val in enumerate(data.values):
            ax.text(val + 0.3, i, f"{val:.1f}%", va="center", fontsize=9, fontweight="bold")
        ax.set_xlabel("Churn Rate (%)")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("Churn by Tenure Band")
        fig, ax = plt.subplots(figsize=(5, 3))
        data = filtered.groupby("TenureBand", observed=True)["Churn_Flag"].mean().sort_index() * 100
        ax.bar(data.index.astype(str), data.values,
               color=[CHURN_COLOR, AMBER_COLOR, RETAIN_COLOR, RETAIN_COLOR],
               width=0.5, edgecolor="white")
        for bar, val in zip(ax.patches, data.values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                    f"{val:.1f}%", ha="center", fontsize=9, fontweight="bold")
        ax.set_ylabel("Churn Rate (%)")
        ax.tick_params(axis="x", labelsize=8)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ════════════════════════════════════════
# TAB 3 — Risk Profiling
# ════════════════════════════════════════
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Churn Rate by Risk Category")
        fig, ax = plt.subplots(figsize=(5, 3))
        risk_data   = filtered.groupby("RiskCategory", observed=True)["Churn_Flag"].mean().sort_index() * 100
        risk_colors = {"Low": RETAIN_COLOR, "Medium": AMBER_COLOR, "High": CHURN_COLOR}
        colors      = [risk_colors[str(x)] for x in risk_data.index]
        ax.bar(risk_data.index.astype(str), risk_data.values,
               color=colors, edgecolor="white", width=0.5)
        for bar, val in zip(ax.patches, risk_data.values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                    f"{val:.1f}%", ha="center", fontsize=10, fontweight="bold")
        ax.set_ylabel("Churn Rate (%)")
        ax.set_ylim(0, risk_data.max() * 1.25)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("Risk Category Distribution")
        fig, ax = plt.subplots(figsize=(5, 3))
        rc_counts   = filtered["RiskCategory"].value_counts().sort_index()
        risk_colors = {"Low": RETAIN_COLOR, "Medium": AMBER_COLOR, "High": CHURN_COLOR}
        colors      = [risk_colors[str(x)] for x in rc_counts.index]
        ax.bar(rc_counts.index.astype(str), rc_counts.values,
               color=colors, edgecolor="white", width=0.5)
        for bar, val in zip(ax.patches, rc_counts.values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10,
                    f"{val:,}", ha="center", fontsize=10, fontweight="bold")
        ax.set_ylabel("Number of Customers")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    st.subheader("⚠️ Top 20 Highest-Risk Customers")
    high_risk_df = filtered[
        (filtered["Contract"]        == "Month-to-month") &
        (filtered["tenure"]          <= 12) &
        (filtered["InternetService"] == "Fiber optic")
    ][["customerID", "Contract", "InternetService", "PaymentMethod",
       "tenure", "MonthlyCharges", "RiskCategory", "Churn"]
    ].sort_values("MonthlyCharges", ascending=False).head(20)

    st.dataframe(
        high_risk_df.style.apply(
            lambda col: ["background-color: #fde8e8" if v == "Yes" else "" for v in col],
            subset=["Churn"]
        ),
        use_container_width=True
    )

# ── Raw Data ─────────────────────────────────────────────
st.markdown("---")
with st.expander("📋 View Filtered Raw Data"):
    st.dataframe(filtered.head(200), use_container_width=True)
    st.caption(f"Showing first 200 of {len(filtered):,} filtered rows")

st.markdown("---")
st.markdown("Built by **Sabari A S** · [LinkedIn](https://linkedin.com/in/sabari3299) · [GitHub](https://github.com/sabarias1999) · Open to Data Analyst roles")
