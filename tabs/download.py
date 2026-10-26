import streamlit as st

from config import CSV_PATH, NOTEBOOK_URL
from ui import section

def render():
    section("⬇️ Download the underlying data")
    st.markdown("The exact CSV behind every number in this brief. Static snapshot retrieved 2026-07-31.")
    with open(CSV_PATH, "rb") as f:
        st.download_button(
            label="⬇️ Download CSV (4 MB)",
            data=f,
            file_name="global_refugee_asylum_irregular_migration_2026.csv",
            mime="text/csv",
            use_container_width=True,
        )
    section("📓 Companion notebook")
    st.markdown("The full policy brief lives in the companion notebook repository.")
    st.markdown(NOTEBOOK_URL)
