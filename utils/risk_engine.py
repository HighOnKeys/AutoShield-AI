"""
AutoShield AI
Supplier Risk Intelligence Engine

Provides helper functions for:

1. Supplier Risk Analysis
2. Risk Ranking
3. Commodity Risk Analysis
4. Executive Dashboard KPIs
"""

import pandas as pd


def load_supplier_data(path):

    return pd.read_csv(path)


def get_top_risk_suppliers(
    supplier_directory,
    top_n=10
):

    return (
        supplier_directory
        .groupby("Supplier")["avg_risk"]
        .mean()
        .reset_index()
        .sort_values(
            "avg_risk",
            ascending=False
        )
        .head(top_n)
    )


def get_top_safe_suppliers(
    supplier_directory,
    top_n=10
):

    return (
        supplier_directory
        .groupby("Supplier")["avg_risk"]
        .mean()
        .reset_index()
        .sort_values(
            "avg_risk",
            ascending=True
        )
        .head(top_n)
    )


def get_commodity_risk(
    supplier_directory
):

    return (
        supplier_directory
        .groupby("Commodity")["avg_risk"]
        .mean()
        .reset_index()
        .sort_values(
            "avg_risk",
            ascending=False
        )
    )


def get_kpis(
    supplier_directory
):

    total_suppliers = (
        supplier_directory["Supplier"]
        .nunique()
    )

    total_commodities = (
        supplier_directory["Commodity"]
        .nunique()
    )

    avg_risk = (
        supplier_directory["avg_risk"]
        .mean()
    )

    total_sales = (
        supplier_directory["sales"]
        .sum()
    )

    return {
        "suppliers": total_suppliers,
        "commodities": total_commodities,
        "avg_risk": avg_risk,
        "sales": total_sales
    }
