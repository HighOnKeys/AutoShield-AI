"""
AutoShield AI

Alternative Sourcing Engine

Identify replacement suppliers
for disrupted sourcing locations.
"""

import streamlit as st
import pandas as pd

from utils.sourcing_engine import (
    get_alternatives
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Alternative Sourcing",
    page_icon="🔄",
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

st.title("🔄 Alternative Sourcing Engine")

st.caption(
    "Identify alternative suppliers for critical automotive commodities."
)

# --------------------------------------------------
# INPUTS
# --------------------------------------------------

col1, col2 = st.columns(2)

supplier_list = sorted(
    supplier_directory["Supplier"].unique()
)

commodity_list = sorted(
    supplier_directory["Commodity"].unique()
)

selected_supplier = col1.selectbox(
    "Disrupted Supplier",
    supplier_list
)

selected_commodity = col2.selectbox(
    "Commodity",
    commodity_list
)

# --------------------------------------------------
# CURRENT SUPPLIER
# --------------------------------------------------

current_supplier = supplier_directory[
    (supplier_directory["Supplier"] == selected_supplier)
    &
    (supplier_directory["Commodity"] == selected_commodity)
]

st.subheader("📍 Current Supplier Profile")

if len(current_supplier) > 0:

    row = current_supplier.iloc[0]

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
        "Supplier-Commodity combination not found."
    )

# --------------------------------------------------
# ALTERNATIVES
# --------------------------------------------------

alternatives = get_alternatives(
    selected_supplier,
    selected_commodity,
    supplier_directory
)

# remove tiny suppliers

alternatives = alternatives[
    alternatives["orders"] >= 50
]

st.subheader(
    "🏆 Recommended Alternative Suppliers"
)

st.dataframe(
    alternatives.head(10),
    use_container_width=True
)

# --------------------------------------------------
# BEST ALTERNATIVE
# --------------------------------------------------

if len(alternatives) > 0:

    best = alternatives.iloc[0]

    st.subheader(
        "⭐ Recommended Supplier"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Supplier",
        best["Supplier"]
    )

    col2.metric(
        "Procurement Score",
        round(
            best["Procurement_Score"],
            3
        )
    )

    col3.metric(
        "Risk Score",
        round(
            best["avg_risk"],
            3
        )
    )

# --------------------------------------------------
# TOP 10 PROCUREMENT SCORES
# --------------------------------------------------

st.subheader(
    "📊 Procurement Score Comparison"
)

comparison = alternatives.head(10)

if len(comparison) > 0:

    import plotly.express as px

    fig = px.bar(
        comparison,
        x="Supplier",
        y="Procurement_Score",
        color="avg_risk",
        title=f"Top Alternative Suppliers for {selected_commodity}"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# EXECUTIVE RECOMMENDATION
# --------------------------------------------------

if len(alternatives) > 0:

    st.subheader(
        "🧠 Executive Recommendation"
    )

    st.success(
        f"""
Primary Alternative Supplier:
{best['Supplier']}

Commodity:
{selected_commodity}

Procurement Score:
{best['Procurement_Score']:.3f}

Risk Score:
{best['avg_risk']:.3f}

Recommended Actions:

• Begin supplier qualification

• Diversify sourcing portfolio

• Reduce dependency on single supplier

• Establish contingency sourcing strategy
"""
    )
