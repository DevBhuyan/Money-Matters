#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:33:05 2026

@author: dev
"""


def calculate(
    property_price,
    downpayment,
    loan_interest_rate,
    years,
    monthly_rent,
    rent_inflation_rate,
    property_appreciation_rate
):

    future_property_value = (
        property_price
        * (1 + property_appreciation_rate / 100)
        ** years
    )

    annual_rent = monthly_rent * 12

    total_rent_paid = 0

    current_rent = annual_rent

    for _ in range(int(years)):

        total_rent_paid += current_rent

        current_rent *= (
            1 +
            rent_inflation_rate / 100
        )

    buy_net = future_property_value

    rent_net = property_price - downpayment

    recommendation = (
        "Buy"
        if buy_net > rent_net
        else "Rent"
    )

    return {
        "Future Property Value":
            round(future_property_value, 2),

        "Total Rent Paid":
            round(total_rent_paid, 2),

        "Recommendation":
            recommendation
    }



def get_inputs():
    """Return a dictionary describing the UI inputs for the *Rent vs Buy* calculator.

    The keys correspond to the argument names of :func:`calculate`.  Each entry
    follows the same schema used by the other calculators in the project –
    Streamlit will render the appropriate widget based on the ``widget`` field.
    ``show_slider`` is enabled for numeric fields where a sensible range is
    known, providing a more interactive experience.
    """

    return {
        "property_price": {
            "label": "Property Price (₹)",
            "widget": "number",
            "type": float,
            "default": 5000000,
            "min": 100000,
            "max": float("inf"),
            "show_slider": True,
            "slider_min": 500000,
            "slider_max": 20000000,
            "step": 50000,
            "allowed_values": []
        },
        "downpayment": {
            "label": "Down‑payment (₹)",
            "widget": "number",
            "type": float,
            "default": 1000000,
            "min": 0,
            "max": float("inf"),
            "show_slider": True,
            "slider_min": 0,
            "slider_max": 5000000,
            "step": 50000,
            "allowed_values": []
        },
        "loan_interest_rate": {
            "label": "Loan Interest Rate (%)",
            "widget": "number",
            "type": float,
            "default": 7.5,
            "min": 0,
            "max": 20,
            "show_slider": True,
            "slider_min": 0,
            "slider_max": 15,
            "step": 0.1,
            "allowed_values": []
        },
        "years": {
            "label": "Loan Tenure (years)",
            "widget": "number",
            "type": int,
            "default": 20,
            "min": 1,
            "max": 40,
            "show_slider": True,
            "slider_min": 1,
            "slider_max": 30,
            "step": 1,
            "allowed_values": []
        },
        "monthly_rent": {
            "label": "Current Monthly Rent (₹)",
            "widget": "number",
            "type": float,
            "default": 15000,
            "min": 0,
            "max": float("inf"),
            "show_slider": True,
            "slider_min": 5000,
            "slider_max": 50000,
            "step": 500,
            "allowed_values": []
        },
        "rent_inflation_rate": {
            "label": "Rent Inflation Rate (%)",
            "widget": "number",
            "type": float,
            "default": 5,
            "min": 0,
            "max": 20,
            "show_slider": True,
            "slider_min": 0,
            "slider_max": 15,
            "step": 0.1,
            "allowed_values": []
        },
        "property_appreciation_rate": {
            "label": "Property Appreciation Rate (%)",
            "widget": "number",
            "type": float,
            "default": 6,
            "min": 0,
            "max": 20,
            "show_slider": True,
            "slider_min": 0,
            "slider_max": 15,
            "step": 0.1,
            "allowed_values": []
        }
    }
