"""
AutoShield AI

Main Application Entry Point
"""

import streamlit as st

st.set_page_config(
    page_title="AutoShield AI",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 AutoShield AI")

st.subheader(
    "Predict. Simulate. Mitigate."
)

st.markdown(
    """
Welcome to AutoShield AI.

An AI-powered automotive supply chain
risk intelligence platform.

Use the sidebar to navigate through:

- War Room Dashboard
- Supplier Risk Explorer
- Alternative Sourcing
- Scenario Simulator
- Executive Copilot
"""
)
