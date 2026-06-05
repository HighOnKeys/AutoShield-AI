"""
AutoShield AI

Scenario Simulation Engine

Simulate supplier disruptions
and evaluate business impact.
"""

import streamlit as st
import pandas as pd

from utils.simulation_engine import (
    simulate_disruption
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Scenario Simulator",
    page_icon="⚡",
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

st.title("⚡ Scenario Simulator")

st.caption(
    "Simulate supplier failures and assess supply chain impact."
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
    "Impacted Commodity",
    commodity_list
)

# --------------------------------------------------
# RUN SIMULATION
# --------------------------------------------------

if st.button(
    "🚨 Simulate Disruption",
    use_container_width=True
):

    simulation = simulate_disruption(
        selected_supplier,
        selected_commodity,
        supplier_directory
    )

    impacted_sales = simulation[
        "impacted_sales"
    ]

    impacted_orders = simulation[
        "impacted_orders"
    ]

    alternatives = simulation[
        "alternatives"
    ]

    # ----------------------------------------------
    # IMPACT KPIs
    # ----------------------------------------------

    st.subheader(
        "📉 Business Impact Assessment"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Revenue Exposure",
        f"${impacted_sales:,.0f}"
    )

    c2.metric(
        "Impacted Orders",
        int(impacted_orders)
    )

    if impacted_sales > 300000:
        risk_level = "Critical"
    elif impacted_sales > 100000:
        risk_level = "High"
    elif impacted_sales > 50000:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    c3.metric(
        "Risk Level",
        risk_level
    )

    st.divider()

    # ----------------------------------------------
    # ALTERNATIVE SUPPLIERS
    # ----------------------------------------------

    st.subheader(
        "🔄 Alternative Suppliers"
    )

    if len(alternatives) > 0:

        st.dataframe(
            alternatives,
            use_container_width=True
        )

        best = alternatives.iloc[0]

        st.subheader(
            "⭐ Best Replacement Option"
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

    else:

        st.error(
            "No alternative suppliers available."
        )

    # ----------------------------------------------
    # EXECUTIVE RECOMMENDATION
    # ----------------------------------------------

    st.subheader(
        "🧠 Mitigation Strategy"
    )

    if len(alternatives) > 0:

        st.success(
            f"""
Disruption Scenario:

{selected_supplier} is unable to supply
{selected_commodity}.

Recommended Response:

1. Shift sourcing to {best['Supplier']}

2. Increase safety stock levels

3. Diversify supplier base

4. Monitor inventory buffers

Estimated Revenue Exposure:

${impacted_sales:,.0f}
"""
        )
