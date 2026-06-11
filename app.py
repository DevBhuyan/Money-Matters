#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:45:26 2026

@author: dev
"""


import streamlit as st
from calculators import CALCULATORS
import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
# Helper functions for dynamic result visualisation
# ---------------------------------------------------------------------
def _render_plain(result):
    """Fallback plain‑text rendering (unchanged from original logic)."""
    if isinstance(result, dict):
        for key, value in result.items():
            if isinstance(value, dict):
                st.markdown(f"### {key}")
                for subkey, subvalue in value.items():
                    st.write(f"**{subkey}:** {subvalue}")
            else:
                st.write(f"**{key}:** {value}")
    elif isinstance(result, list):
        st.dataframe(result, use_container_width=True)
    else:
        st.metric(label="Result", value=result)


def render_result(result, viz_cfg=None):
    """Render ``result`` according to an optional visualisation config.

    The ``viz_cfg`` dictionary is expected to be supplied by the calculator
    definition (see the documentation in the assistant's previous message).
    If the config is missing or the data shape does not match the requested
    visualisation, the function gracefully falls back to the plain‑text
    representation.
    """
    # -----------------------------------------------------------------
    # No visualisation requested – use the original plain‑text output.
    # -----------------------------------------------------------------
    if not viz_cfg:
        _render_plain(result)
        return

    vtype = viz_cfg.get("type")

    try:
        # -------------------------------------------------------------
        # Metric – single scalar value
        # -------------------------------------------------------------
        if vtype == "metric":
            label = viz_cfg.get("label", "Result")
            st.metric(label=label, value=result)

        # -------------------------------------------------------------
        # Pie chart – expects a dict where each entry contains a label and a value.
        # -------------------------------------------------------------
        elif vtype == "pie" and isinstance(result, dict):
            label_key = viz_cfg.get("label_key")
            value_key = viz_cfg.get("value_key")
            if label_key and value_key:
                labels = [v.get(label_key) for v in result.values()]
                values = [v.get(value_key) for v in result.values()]
                fig, ax = plt.subplots()
                ax.pie(values, labels=labels, autopct="%1.1f%%")
                st.pyplot(fig)
            else:
                _render_plain(result)

        # -------------------------------------------------------------
        # Bar / Line chart – expects a list of dicts (or a list of lists).
        # -------------------------------------------------------------
        elif vtype in {"bar", "line"} and isinstance(result, list):
            df = pd.DataFrame(result)
            # Allow the config to specify which column is the x‑axis.
            x_col = viz_cfg.get("x") or (
                df.columns[0] if not df.empty else None)
            if x_col and x_col in df.columns:
                df = df.set_index(x_col)
            if vtype == "bar":
                st.bar_chart(df)
            else:
                st.line_chart(df)

        # -------------------------------------------------------------
        # Dataframe – render any tabular data.
        # -------------------------------------------------------------
        elif vtype == "dataframe":
            if isinstance(result, (list, dict)):
                df = pd.DataFrame(result)
                st.dataframe(df, use_container_width=True)
            else:
                _render_plain(result)

        # -------------------------------------------------------------
        # Unknown type – fall back.
        # -------------------------------------------------------------
        else:
            _render_plain(result)
    except Exception:  # pragma: no cover – any visualisation error should not break the UI
        _render_plain(result)


def render_numeric_input(
    label,
    config,
    state_key
):
    expected_type = config.get("type", float)

    caster = float if expected_type is float else int

    value = caster(config["default"])

    if state_key in st.session_state:
        value = caster(st.session_state[state_key])

    slider_min = caster(config["slider_min"])
    slider_max = caster(config["slider_max"])
    step = caster(config["step"])

    col1, col2 = st.columns([4, 1])

    with col1:

        slider_value = st.slider(
            label,
            min_value=slider_min,
            max_value=slider_max,
            value=value,
            step=step,
            key=f"{state_key}_slider"
        )

    with col2:

        number_value = st.number_input(
            "Exact",
            min_value=slider_min,
            max_value=slider_max,
            value=slider_value,
            step=step,
            key=f"{state_key}_number",
            label_visibility="collapsed"
        )

    st.session_state[state_key] = caster(number_value)

    return caster(number_value)

# ==================================================
# Page Configuration
# ==================================================


st.set_page_config(
    page_title="Compound",
    page_icon="📈",
    layout="wide"
)


# ==================================================
# Sidebar
# ==================================================

st.sidebar.title("📈 Compound")

selected_calculator = st.sidebar.selectbox(
    "Select Calculator",
    list(CALCULATORS.keys())
)

tier = CALCULATORS[selected_calculator]

st.title(selected_calculator)


# ==================================================
# Input Rendering
# ==================================================

tabs = st.tabs(list(tier.keys()))

for idx, calculator in enumerate(tier.values()):

    with tabs[idx]:

        inputs = {}

        for input_name, config in calculator["inputs"].items():

            label = config.get(
                "label",
                input_name.replace("_", " ").title()
            )

            widget = config.get("widget", "number")

            default = config.get("default")

            # ----------------------------------------------
            # SELECT BOX
            # ----------------------------------------------

            if widget == "select":

                allowed_values = config.get("allowed_values", [])

                if not allowed_values:
                    st.warning(
                        f"{input_name} configured as select "
                        "but no allowed_values provided."
                    )
                    continue

                default_index = 0

                if default in allowed_values:
                    default_index = allowed_values.index(default)

                inputs[input_name] = st.selectbox(
                    label,
                    allowed_values,
                    index=default_index
                )

            # ----------------------------------------------
            # CHECKBOX
            # ----------------------------------------------

            elif widget == "checkbox":

                inputs[input_name] = st.checkbox(
                    label,
                    value=bool(default)
                )

            # ----------------------------------------------
            # NUMERIC INPUTS
            # ----------------------------------------------

            else:

                min_value = config.get("min")
                max_value = config.get("max")
                step = config.get("step", 1)

                if default is None:

                    if min_value not in [None, float("-inf")]:
                        default = min_value
                    else:
                        default = 0

                show_slider = config.get("show_slider", False)

                # ------------------------------------------
                # Slider Mode
                # ------------------------------------------

                if show_slider:

                    inputs[input_name] = render_numeric_input(
                        label,
                        config,
                        f"{selected_calculator}_{idx}_{input_name}"
                    )

                # ------------------------------------------
                # Number Input Mode
                # ------------------------------------------

                else:

                    kwargs = {
                        "label": label,
                        "value": default,
                        "step": step
                    }

                    if min_value not in [None, float("-inf")]:
                        kwargs["min_value"] = min_value

                    if max_value not in [None, float("inf")]:
                        kwargs["max_value"] = max_value

                    inputs[input_name] = st.number_input(**kwargs)

    # ==================================================
    # Calculation
    # ==================================================

        try:

            result = calculator["calculate"](**inputs)

            st.divider()
            st.subheader("Results")

            # Use the visualisation configuration supplied by the calculator (if any).
            viz_cfg = calculator.get("visualisation")
            render_result(result, viz_cfg)

        except Exception as e:

            st.error(
                f"Calculation failed:\n\n{type(e).__name__}: {e}"
            )
