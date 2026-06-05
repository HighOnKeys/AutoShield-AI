"""
AutoShield AI

War Room Dashboard

Provides a real-time view of:

1. Supply Chain Risk
2. Supplier Landscape
3. Commodity Exposure
4. Executive KPIs
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.risk_engine import (
    get_kpis,
    get_top_risk_suppliers,
    get_commodity_risk
)


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="War Room",
    page_icon="🚨",
    layout="wide"
)


# ---------------------------------------------------
# DATA LOADING
# ---------------------------------------------------

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/final_supplier_directory.csv"
    )


supplier_directory = load_data()


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🚨 Supply Chain War Room")

st.caption(
    "Automotive Supply Chain Risk Intelligence Dashboard"
)


# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

kpis = get_kpis(
    supplier_directory
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Suppliers",
    kpis["suppliers"]
)

col2.metric(
    "Commodities",
    kpis["commodities"]
)

col3.metric(
    "Average Risk",
    round(
        kpis["avg_risk"],
        2
    )
)

col4.metric(
    "Revenue Exposure",
    f"${kpis['sales']:,.0f}"
)


st.divider()


# ---------------------------------------------------
# TOP RISK SUPPLIERS
# ---------------------------------------------------

supplier_directory = supplier_directory[
    supplier_directory["orders"] >= 50
]

st.subheader(
    "⚠️ Highest Risk Suppliers"
)

risk_suppliers = get_top_risk_suppliers(
    supplier_directory
)

fig_risk = px.bar(
    risk_suppliers,
    x="Supplier",
    y="avg_risk",
    title="Top Risk Suppliers"
)

st.plotly_chart(
    fig_risk,
    use_container_width=True
)


# ---------------------------------------------------
# COMMODITY RISK
# ---------------------------------------------------

st.subheader(
    "📦 Commodity Risk Analysis"
)

commodity_risk = get_commodity_risk(
    supplier_directory
)

fig_commodity = px.bar(
    commodity_risk,
    x="Commodity",
    y="avg_risk",
    title="Commodity Risk Profile"
)

st.plotly_chart(
    fig_commodity,
    use_container_width=True
)


# ---------------------------------------------------
# SUPPLIER DIRECTORY
# ---------------------------------------------------

st.subheader(
    "🌍 Supplier Intelligence Directory"
)

st.dataframe(
    supplier_directory,
    use_container_width=True
)


# ---------------------------------------------------
# EXECUTIVE INSIGHTS
# ---------------------------------------------------

st.subheader(
    "🧠 Executive Insights"
)

highest_risk_supplier = (
    risk_suppliers.iloc[0]["Supplier"]
)

highest_risk_commodity = (
    commodity_risk.iloc[0]["Commodity"]
)

st.warning(
    f"""
Highest Risk Supplier: {highest_risk_supplier}

Highest Risk Commodity: {highest_risk_commodity}

Recommended Action:

• Monitor supplier performance

• Increase safety stock

• Prepare alternative sourcing plans
"""
)
