#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:33:13 2026

@author: dev
"""


def calculate(
    purchase_cost,
    loan_interest_rate,
    investment_return_rate,
    years
):

    loan_cost = purchase_cost * (
        (1 + loan_interest_rate / 100)
        ** years
    )

    invested_value = purchase_cost * (
        (1 + investment_return_rate / 100)
        ** years
    )

    recommendation = (
        "Invest First"
        if invested_value > loan_cost
        else "Take Loan"
    )

    return {
        "Future Loan Cost": round(loan_cost, 2),
        "Future Investment Value": round(
            invested_value,
            2
        ),
        "Recommendation": recommendation
    }



def get_inputs():
    """Return a dictionary describing the UI inputs for the *Loan vs Invest* calculator.

    The structure mirrors the ``get_inputs`` functions used by the other
    calculators in the project.  Each key matches a parameter of
    :func:`calculate` and provides Streamlit with the necessary metadata to
    render an appropriate widget.
    """

    return {
        "purchase_cost": {
            "label": "Purchase Cost (₹)",
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
        "investment_return_rate": {
            "label": "Investment Return Rate (%)",
            "widget": "number",
            "type": float,
            "default": 12,
            "min": 0,
            "max": 30,
            "show_slider": True,
            "slider_min": 0,
            "slider_max": 25,
            "step": 0.1,
            "allowed_values": []
        },
        "years": {
            "label": "Investment Horizon (years)",
            "widget": "number",
            "type": int,
            "default": 10,
            "min": 1,
            "max": 40,
            "show_slider": True,
            "slider_min": 1,
            "slider_max": 30,
            "step": 1,
            "allowed_values": []
        }
    }
