import streamlit as st

from config import (YEAR_MIN, YEAR_MAX, THRESHOLD_MIN, THRESHOLD_MAX,
                    THRESHOLD_DEFAULT, THRESHOLD_STEP)
from data import prepare_snapshot, compute_overlap
from charts import top_hosts_chart
from ui import section, metric_row, so_what

def render(df):
    section(" Comparison settings")
    c1, c2 = st.columns(2)
    with c1:
        year = st.selectbox("Comparison year", list(range(YEAR_MIN, YEAR_MAX + 1)),
                            index=(YEAR_MAX - YEAR_MIN))
    with c2:
        view = st.radio("View", ["Absolute", "Per 1,000 residents"], horizontal=True)
    threshold = st.slider("Minimum refugees hosted", THRESHOLD_MIN, THRESHOLD_MAX,
                          THRESHOLD_DEFAULT, step=THRESHOLD_STEP)

    cov, big = prepare_snapshot(df, year, threshold)
    overlap = compute_overlap(big)

    section(" At a glance")
    metric_row([
        ("Year", str(year), "Snapshot shown"),
        ("Countries with covariates", str(len(cov)), "Pop + GDP available"),
        ("Hosts ≥ threshold", str(len(big)), "Passing min-host filter"),
        ("Top-10 overlap", str(overlap) + " / 10", "Abs vs per-capita"),
    ], columns=4)

    metric = "refugees" if view == "Absolute" else "refugees_per_1k"
    label = "Registered refugees" if view == "Absolute" else "Refugees per 1,000 residents"
    section("📈 Top 12 hosts — " + label + ", " + str(year))

    if len(big) == 0:
        st.warning("No countries pass the current threshold. Lower the slider.")
    else:
        fig, _ = top_hosts_chart(big, metric, view)
        st.pyplot(fig)

    so_what(year, overlap)
