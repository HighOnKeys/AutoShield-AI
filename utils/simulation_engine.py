"""
AutoShield AI

Scenario Simulation Engine

Simulates supplier disruptions
and estimates business impact.
"""

from utils.sourcing_engine import (
    get_alternatives
)


def simulate_disruption(
    supplier_country,
    commodity,
    supplier_directory
):

    affected = supplier_directory[
        (
            supplier_directory["Supplier"]
            == supplier_country
        )
        &
        (
            supplier_directory["Commodity"]
            == commodity
        )
    ]

    impacted_sales = (
        affected["sales"]
        .sum()
    )

    impacted_orders = (
        affected["orders"]
        .sum()
    )

    alternatives = get_alternatives(
        supplier_country,
        commodity,
        supplier_directory
    )

    return {
        "supplier": supplier_country,
        "commodity": commodity,
        "impacted_sales": impacted_sales,
        "impacted_orders": impacted_orders,
        "alternatives": alternatives
    }
