#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:04:34 2026

@author: dev
"""

from finance import (
    emi,
    sip,
    loan_prepayment,
    lumpsum,
    repayment_schedule
)
from decision import (
    goal_based_sip,
    rent_vs_buy,
    loan_vs_invest,
    prepay_vs_invest
)


CALCULATORS = {
    "Finance":    {
        "EMI Calculator": {
            "inputs": emi.get_inputs(),
            "calculate": emi.calculate
        },
        "SIP Calculator": {
            "inputs": sip.get_inputs(),
            "calculate": sip.calculate
        },
        "Loan Prepayment Calculator": {
            "inputs": loan_prepayment.get_inputs(),
            "calculate": loan_prepayment.calculate
        },
        "Lumpsum Investment Calculator": {
            "inputs": lumpsum.get_inputs(),
            "calculate": lumpsum.calculate
        },
        "Loan Repayment Schedule": {
            "inputs": repayment_schedule.get_inputs(),
            "calculate": repayment_schedule.calculate
        }
    },
    "Decision Helpers": {
        "Goal based SIP": {
            "inputs": goal_based_sip.get_inputs(),
            "calculate": goal_based_sip.calculate
        },
        "Rent vs Buy": {
            "inputs": rent_vs_buy.get_inputs(),
            "calculate": rent_vs_buy.calculate
        },
        "Loan vs Invest": {
            "inputs": loan_vs_invest.get_inputs(),
            "calculate": loan_vs_invest.calculate
        },
        "Prepay vs Invest": {
            "inputs": prepay_vs_invest.get_inputs(),
            "calculate": prepay_vs_invest.calculate
        }
    }
}
