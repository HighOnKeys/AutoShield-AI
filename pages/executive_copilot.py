"""
AutoShield AI

Executive AI Copilot

Natural language decision support for
automotive supply chain executives.

Supported Queries:

1. Highest Risk Suppliers
2. Commodity Risk Analysis
3. Alternative Sourcing
4. China Semiconductor Disruption Scenario
"""

import streamlit as st
import pandas as pd


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Executive AI Copilot",
    page_icon="🤖",
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


df = load_data()


# --------------------------------------------------
# QUERY CLASSIFIER
# --------------------------------------------------

def classify_query(question):

    q = question.lower()

    if "risk" in q and "supplier" in q:
        return "risk"

    elif "commodity" in q:
        return "commodity"

    elif (
        "china" in q
        or "semiconductor" in q
        or "disruption" in q
    ):
        return "scenario"

    elif (
        "alternative" in q
        or "replacement" in q
    ):
        return "alternative"

    return "unknown"


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🤖 Executive AI Copilot")

st.caption(
    "Natural language decision support for automotive supply chains."
)

st.info(
    """
Example Questions

• Which suppliers are highest risk?

• Which commodities are highest risk?

• Recommend alternative suppliers

• What happens if China semiconductor supply fails?
"""
)


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

question = st.chat_input(
    "Ask AutoShield AI..."
)


# --------------------------------------------------
# QUERY HANDLING
# --------------------------------------------------

if question:

    intent = classify_query(question)

    with st.chat_message("user"):

        st.write(question)

    with st.chat_message("assistant"):

        # ------------------------------------------
        # SUPPLIER RISK
        # ------------------------------------------

        if intent == "risk":

            top_risk = (
                df.groupby("Supplier")
                ["avg_risk"]
                .mean()
                .reset_index()
                .sort_values(
                    "avg_risk",
                    ascending=False
                )
                .head(10)
            )

            st.subheader(
                "⚠️ Highest Risk Suppliers"
            )

            st.dataframe(
                top_risk,
                use_container_width=True
            )

            st.metric(
                "High Risk Suppliers",
                len(top_risk)
            )

            st.warning(
                """
High disruption probability detected.

Potential Impact:

• Logistics delays

• Supply shortages

• Procurement instability

• Increased operational risk
"""
            )

            st.success(
                """
Recommended Actions

• Diversify supplier portfolio

• Increase safety stock

• Monitor supplier performance

• Establish contingency sourcing plans
"""
            )

        # ------------------------------------------
        # COMMODITY RISK
        # ------------------------------------------

        elif intent == "commodity":

            commodity_risk = (
                df.groupby("Commodity")
                ["avg_risk"]
                .mean()
                .reset_index()
                .sort_values(
                    "avg_risk",
                    ascending=False
                )
            )

            highest = (
                commodity_risk.iloc[0]
                ["Commodity"]
            )

            st.subheader(
                "📦 Commodity Risk Analysis"
            )

            st.dataframe(
                commodity_risk,
                use_container_width=True
            )

            st.metric(
                "Highest Risk Commodity",
                highest
            )

            st.error(
                f"""
Highest Risk Commodity:

{highest}

This commodity should receive priority attention
during procurement planning.
"""
            )

            st.success(
                """
Recommended Actions

• Identify backup suppliers

• Increase inventory buffers

• Monitor market volatility

• Improve sourcing diversification
"""
            )

        # ------------------------------------------
        # SCENARIO SIMULATION
        # ------------------------------------------

        elif intent == "scenario":

            affected = df[
                (df["Commodity"] == "Semiconductors")
            ]

            revenue = (
                affected["sales"]
                .sum()
            )

            alternatives = (
                affected
                .sort_values(
                    "Procurement_Score",
                    ascending=False
                )
                .head(5)
            )

            st.subheader(
                "⚡ China Semiconductor Disruption Scenario"
            )

            col1, col2 = st.columns(2)

            col1.metric(
                "Revenue Exposure",
                f"${revenue:,.0f}"
            )

            col2.metric(
                "Risk Level",
                "Critical"
            )

            st.subheader(
                "🔄 Recommended Alternatives"
            )

            st.dataframe(
                alternatives[
                    [
                        "Supplier",
                        "orders",
                        "sales",
                        "avg_risk",
                        "Procurement_Score"
                    ]
                ],
                use_container_width=True
            )

            best = alternatives.iloc[0]

            st.success(
                f"""
Primary Alternative Supplier:

{best['Supplier']}

Recommended Response:

• Activate contingency sourcing

• Increase inventory coverage

• Diversify semiconductor sourcing

• Reduce supplier concentration risk
"""
            )

        # ------------------------------------------
        # ALTERNATIVE SOURCING
        # ------------------------------------------

        elif intent == "alternative":

            alternatives = (
                df.sort_values(
                    "Procurement_Score",
                    ascending=False
                )
                .head(10)
            )

            best = alternatives.iloc[0]

            st.subheader(
                "🔄 Alternative Supplier Recommendations"
            )

            st.dataframe(
                alternatives[
                    [
                        "Supplier",
                        "Commodity",
                        "Procurement_Score",
                        "avg_risk"
                    ]
                ],
                use_container_width=True
            )

            st.metric(
                "Best Alternative",
                best["Supplier"]
            )

            st.success(
                f"""
Recommended Supplier:

{best['Supplier']}

Procurement Score:

{best['Procurement_Score']:.3f}

Recommended Actions

• Begin supplier qualification

• Diversify sourcing portfolio

• Establish contingency contracts

• Reduce dependency on single suppliers
"""
            )

        # ------------------------------------------
        # HELP
        # ------------------------------------------

        else:

            st.info(
                """
Supported Questions

• Which suppliers are highest risk?

• Which commodities are highest risk?

• Recommend alternative suppliers

• What happens if China semiconductor supply fails?
"""
            )
