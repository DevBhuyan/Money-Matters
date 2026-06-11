#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:33:26 2026

@author: dev
"""


from finance.lumpsum import calculate as lumpsum_calculate


def calculate(
    available_amount: float,
    loan_interest_rate: float,
    investment_return_rate: float,
    remaining_years: float
):

    loan_savings = available_amount * (
        (1 + loan_interest_rate / 100) ** remaining_years
        - 1
    )

    invest_result = lumpsum_calculate(
        available_amount,
        investment_return_rate,
        remaining_years
    )

    investment_gain = invest_result["Estimated Returns"]

    recommendation = (
        "Invest"
        if investment_gain > loan_savings
        else "Prepay Loan"
    )

    return {
        "Loan Interest Saved": round(loan_savings, 2),
        "Investment Gain": round(investment_gain, 2),
        "Advantage": round(
            abs(investment_gain - loan_savings),
            2
        ),
        "Recommendation": recommendation
    }



def get_inputs():
    """Return a dictionary describing the UI inputs for the *Prepay vs Invest* calculator.

    The keys correspond to the arguments of :func:`calculate`.  The structure
    follows the same convention used throughout the project so Streamlit can
    automatically generate the appropriate widgets.
    """

    return {
        "available_amount": {
            "label": "Available Amount (₹)",
            "widget": "number",
            "type": float,
            "default": 200000,
            "min": 0,
            "max": float("inf"),
            "show_slider": True,
            "slider_min": 50000,
            "slider_max": 2000000,
            "step": 5000,
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
        "remaining_years": {
            "label": "Remaining Years",
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
