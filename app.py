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

# ── Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Customer Churn Analysis",
    page_icon="📊",
    layout="wide"
)

# ── Colors ───────────────────────────────────────────────
CHURN_COLOR   = "#E24B4A"
RETAIN_COLOR  = "#1D9E75"
NEUTRAL_COLOR = "#378ADD"

# ── Load Data ────────────────────────────────────────────
@st.cache_data
def load_data():
    path = r"E:\Customer churn\Data\customer churn.csv"
    df = pd.read_csv(path)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)
    df["Churn_Flag"] = (df["Churn"] == "Yes").astype(int)
    return df

df = load_data()

# ── Sidebar ──────────────────────────────────────────────
st.sidebar.image("https://img.shields.io/badge/Churn-Analysis-E24B4A?style=for-the-badge")
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

st.sidebar.markdown("---")
st.sidebar.markdown("**Built by Sabari A S**")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/sabari3299)")

# ── Apply Filters ────────────────────────────────────────
filtered = df[
    (df["Contract"].isin(contract_filter)) &
    (df["InternetService"].isin(internet_filter)) &
    (df["tenure"].between(tenure_filter[0], tenure_filter[1]))
]

# ── Header ───────────────────────────────────────────────
st.title("📊 Customer Churn Analysis Dashboard")
st.markdown("**Telco Customer Churn — End-to-End Analytics by Sabari A S**")
st.markdown("---")

# ── KPI Cards ────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

total      = len(filtered)
churned    = filtered["Churn_Flag"].sum()
churn_rate = churned / total if total > 0 else 0
rev_risk   = filtered[filtered["Churn"]=="Yes"]["MonthlyCharges"].sum()

col1.metric("Total Customers",    f"{total:,}")
col2.metric("Churned Customers",  f"{churned:,}")
col3.metric("Churn Rate",         f"{churn_rate:.1%}")
col4.metric("Revenue at Risk",    f"${rev_risk:,.0f}/mo")

st.markdown("---")

# ── Row 1: Charts ────────────────────────────────────────
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

with col2:
    st.subheader("Churn by Contract Type")
    fig, ax = plt.subplots(figsize=(5, 3))
    data = filtered.groupby("Contract")["Churn_Flag"].mean().sort_values(ascending=False) * 100
    ax.barh(data.index, data.values,
            color=[CHURN_COLOR, "#FAC775", RETAIN_COLOR], edgecolor="white")
    for i, val in enumerate(data.values):
        ax.text(val + 0.5, i, f"{val:.1f}%", va="center", fontsize=9, fontweight="bold")
    ax.set_xlabel("Churn Rate (%)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)

# ── Row 2: Charts ────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("Churn by Internet Service")
    fig, ax = plt.subplots(figsize=(5, 3))
    data = filtered.groupby("InternetService")["Churn_Flag"].mean().sort_values(ascending=False) * 100
    ax.bar(data.index, data.values,
           color=[CHURN_COLOR, "#FAC775", RETAIN_COLOR], width=0.5, edgecolor="white")
    for bar, val in zip(ax.patches, data.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f"{val:.1f}%", ha="center", fontsize=9, fontweight="bold")
    ax.set_ylabel("Churn Rate (%)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("Churn by Payment Method")
    fig, ax = plt.subplots(figsize=(5, 3))
    data = filtered.groupby("PaymentMethod")["Churn_Flag"].mean().sort_values(ascending=False) * 100
    short = [p.replace(" (automatic)", "\n(auto)") for p in data.index]
    ax.barh(short, data.values,
            color=[CHURN_COLOR, "#FAC775", RETAIN_COLOR, RETAIN_COLOR], edgecolor="white")
    for i, val in enumerate(data.values):
        ax.text(val + 0.3, i, f"{val:.1f}%", va="center", fontsize=9, fontweight="bold")
    ax.set_xlabel("Churn Rate (%)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)

# ── Row 3: Heatmap + Tenure ──────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("Churn Heatmap — Contract × Internet")
    fig, ax = plt.subplots(figsize=(5, 3))
    pivot = filtered.pivot_table(
        values="Churn_Flag", index="Contract",
        columns="InternetService", aggfunc="mean") * 100
    sns.heatmap(pivot, annot=True, fmt=".1f",
                cmap="RdYlGn_r", linewidths=0.5, ax=ax)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("Tenure Distribution")
    fig, ax = plt.subplots(figsize=(5, 3))
    filtered[filtered["Churn"]=="No"]["tenure"].hist(
        ax=ax, bins=30, alpha=0.7, color=RETAIN_COLOR,
        label="Retained", edgecolor="white")
    filtered[filtered["Churn"]=="Yes"]["tenure"].hist(
        ax=ax, bins=30, alpha=0.7, color=CHURN_COLOR,
        label="Churned", edgecolor="white")
    ax.set_xlabel("Tenure (months)")
    ax.set_ylabel("Customers")
    ax.legend(fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)

# ── Raw Data ─────────────────────────────────────────────
st.markdown("---")
st.subheader("📋 Filtered Data")
st.dataframe(filtered.head(100), use_container_width=True)

st.markdown("---")
st.markdown("Built by **Sabari A S** · [LinkedIn](https://linkedin.com/in/sabari3299) · Open to analyst roles")