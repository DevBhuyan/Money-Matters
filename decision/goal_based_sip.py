#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:31:24 2026

@author: dev
"""


def calculate(
    target_corpus: float,
    annual_return_rate: float,
    tenure_years: float
):

    monthly_rate = annual_return_rate / 12 / 100

    total_months = int(tenure_years * 12)

    growth_factor = (
        ((1 + monthly_rate) ** total_months - 1) / monthly_rate
    ) * (1 + monthly_rate)

    required_sip = target_corpus / growth_factor

    return {
        "Target Corpus": round(target_corpus, 2),
        "Required Monthly SIP": round(required_sip, 2),
        "Investment Duration (Years)": tenure_years
    }


def get_inputs():

    return {

        "target_corpus": {
            "label": "Target Corpus (₹)",
            "widget": "number",
            "type": float,
            "default": 10000000,
            "min": 1000,
            "max": float("inf"),
            "show_slider": True,
            "slider_min": 100000,
            "slider_max": 100000000,
            "step": 100000,
            "allowed_values": []
        },

        "annual_return_rate": {
            "label": "Expected Return (%)",
            "widget": "number",
            "type": float,
            "default": 12,
            "min": 0,
            "max": 100,
            "show_slider": True,
            "slider_min": 0,
            "slider_max": 25,
            "step": 0.1,
            "allowed_values": []
        },

        "tenure_years": {
            "label": "Years Available",
            "widget": "number",
            "type": float,
            "default": 15,
            "min": 1,
            "max": 50,
            "show_slider": True,
            "slider_min": 1,
            "slider_max": 40,
            "step": 1,
            "allowed_values": []
        }
    }
