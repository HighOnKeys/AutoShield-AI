"""
AutoShield AI

Alternative Sourcing Engine

Identifies alternative suppliers
for disrupted sourcing locations.
"""

import pandas as pd


def get_alternatives(
    supplier_country,
    commodity,
    supplier_directory
):

    alternatives = supplier_directory[
        supplier_directory["Commodity"] == commodity
    ].copy()

    alternatives = alternatives[
        alternatives["Supplier"]
        != supplier_country
    ]

    alternatives = alternatives.sort_values(
        "Procurement_Score",
        ascending=False
    )

    return alternatives


def get_best_supplier(
    commodity,
    supplier_directory
):

    result = (
        supplier_directory[
            supplier_directory["Commodity"]
            == commodity
        ]
        .sort_values(
            "Procurement_Score",
            ascending=False
        )
        .head(1)
    )

    return result
