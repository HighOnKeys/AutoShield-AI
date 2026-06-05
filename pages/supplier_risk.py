"""
AutoShield AI

Supplier Risk Explorer

Provides:

1. Supplier-Level Risk Analysis
2. Commodity-Level Risk Analysis
3. Procurement Readiness Insights
"""

import streamlit as st
import pandas as pd
import plotly.express as px


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Supplier Risk Explorer",
    page_icon="⚠️",
    layout="wide"
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/final_supplier_directory.csv"
    )


supplier_directory = load_data()


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("⚠️ Supplier Risk Explorer")

st.caption(
    "Analyze supplier disruption risk and procurement readiness."
)


# --------------------------------------------------
# FILTERS
# --------------------------------------------------

col1, col2 = st.columns(2)

supplier_list = sorted(
    supplier_directory["Supplier"].unique()
)

commodity_list = sorted(
    supplier_directory["Commodity"].unique()
)

selected_supplier = col1.selectbox(
    "Select Supplier",
    supplier_list
)

selected_commodity = col2.selectbox(
    "Select Commodity",
    commodity_list
)


# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------

filtered = supplier_directory[
    (supplier_directory["Supplier"] == selected_supplier)
    &
    (supplier_directory["Commodity"] == selected_commodity)
]


# --------------------------------------------------
# SUPPLIER OVERVIEW
# --------------------------------------------------

st.subheader("📊 Supplier Overview")

if len(filtered) > 0:

    row = filtered.iloc[0]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Risk Score",
        round(row["avg_risk"], 3)
    )

    c2.metric(
        "Orders",
        int(row["orders"])
    )

    c3.metric(
        "Sales",
        f"${row['sales']:,.0f}"
    )

    c4.metric(
        "Procurement Score",
        round(
            row["Procurement_Score"],
            3
        )
    )

else:

    st.warning(
        "No data available."
    )


# --------------------------------------------------
# RISK DISTRIBUTION
# --------------------------------------------------

st.subheader(
    "📈 Supplier Risk Ranking"
)

risk_rank = (
    supplier_directory
    .groupby("Supplier")
    ["avg_risk"]
    .mean()
    .reset_index()
    .sort_values(
        "avg_risk",
        ascending=False
    )
    .head(20)
)

fig_risk = px.bar(
    risk_rank,
    x="Supplier",
    y="avg_risk",
    title="Top 20 Risk Suppliers"
)

st.plotly_chart(
    fig_risk,
    use_container_width=True
)


# --------------------------------------------------
# PROCUREMENT SCORE RANKING
# --------------------------------------------------

supplier_directory = supplier_directory[
    supplier_directory["orders"] >= 50
]

st.subheader(
    "🏆 Procurement Readiness Ranking"
)

procurement_rank = (
    supplier_directory
    .sort_values(
        "Procurement_Score",
        ascending=False
    )
    .head(20)
)

fig_procurement = px.bar(
    procurement_rank,
    x="Supplier",
    y="Procurement_Score",
    color="Commodity",
    title="Top Procurement Candidates"
)

st.plotly_chart(
    fig_procurement,
    use_container_width=True
)


# --------------------------------------------------
# RISK LEVEL BREAKDOWN
# --------------------------------------------------

st.subheader(
    "🚦 Risk Category Distribution"
)

risk_counts = (
    supplier_directory["Risk_Level"]
    .value_counts()
    .reset_index()
)

risk_counts.columns = [
    "Risk_Level",
    "Count"
]

fig_pie = px.pie(
    risk_counts,
    names="Risk_Level",
    values="Count",
    title="Supplier Risk Segmentation"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)


# --------------------------------------------------
# FULL DIRECTORY
# --------------------------------------------------

st.subheader(
    "📋 Supplier Intelligence Table"
)

st.dataframe(
    supplier_directory.sort_values(
        "avg_risk",
        ascending=False
    ),
    use_container_width=True
)


# --------------------------------------------------
# EXECUTIVE INSIGHT
# --------------------------------------------------

st.subheader(
    "🧠 Executive Insight"
)

highest_risk = (
    supplier_directory
    .sort_values(
        "avg_risk",
        ascending=False
    )
    .iloc[0]
)

st.warning(
    f"""
Highest Risk Supplier-Commodity Pair

Supplier: {highest_risk['Supplier']}

Commodity: {highest_risk['Commodity']}

Risk Score: {highest_risk['avg_risk']:.2f}

Recommendation:

• Closely monitor deliveries

• Increase safety stock

• Prepare alternative sourcing options
"""
)
