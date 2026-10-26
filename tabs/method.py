import pandas as pd
import streamlit as st

from ui import section

def render(df):
    section(" What this brief refuses to do")
    st.markdown("1. UNHCR registered counts are never combined with the DHS modelled estimate (US-only, methodologically different).")
    st.markdown("2. Nulls are not zeros — except in conflict_intensity_index, where UCDP defines a genuine zero inside its 1989+ coverage.")
    st.markdown("3. The dataset is host-country framed: no origin-country claims are possible here.")

    section("📋 Coverage by year band")
    bands = pd.cut(df.year, [1950, 1970, 1990, 2010, 2025],
                   labels=["1951-69", "1970-89", "1990-2009", "2010-25"])
    cov_table = (df.groupby(bands, observed=True)[["refugees", "asylum_seekers", "idps"]]
                   .apply(lambda g: g.notna().mean().mul(100).round(0))
                   .astype(int))
    st.dataframe(cov_table, use_container_width=True)
    st.caption("Refugee coverage climbs from near-nothing in 1951-69 to near-complete in 2010-25. IDP series only begins around 1990, when UNHCR mandate began — the flatness before 1990 is a mandate artefact.")
