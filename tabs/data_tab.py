import pandas as pd
import streamlit as st

from ui import section, metric_row

def render(df):
    section("🗂️ Dataset at a glance")
    metric_row([
        ("Rows", "{:,}".format(len(df)), "Country-year obs"),
        ("Countries", str(df.iso3.nunique()), "ISO3 codes"),
        ("Years", str(df.year.min()) + "-" + str(df.year.max()), "Full span"),
        ("Snapshot", "2026-07-31", "Static, not live"),
    ], columns=4)

    section(" Column reference")
    cols = [
        ("iso3", "Country of asylum (ISO3)"),
        ("country_name", "Country name"),
        ("year", "Year"),
        ("refugees", "UNHCR registered refugees"),
        ("asylum_seekers", "Pending asylum claims"),
        ("idps", "Internally displaced persons"),
        ("stateless_persons", "Stateless persons of concern"),
        ("returned_refugees", "Refugees returned"),
        ("unauthorized_migrant_estimate", "DHS modelled estimate (US only)"),
        ("population", "World Bank total population"),
        ("gdp_per_capita", "World Bank GDP per capita"),
        ("conflict_intensity_index", "UCDP/PRIO conflict deaths"),
    ]
    col_ref = pd.DataFrame(cols, columns=["Column", "Description"])
    st.dataframe(col_ref, use_container_width=True, hide_index=True)
