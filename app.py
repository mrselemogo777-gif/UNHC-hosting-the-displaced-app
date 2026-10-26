import streamlit as st

from ui import setup_page, footer
from data import load_data
from tabs import findings, method, data_tab, download

setup_page()
df = load_data()

tab_find, tab_meth, tab_data, tab_dl = st.tabs(
    ["📊 Findings", "🔬 Method", "🗂️ Data", "⬇️ Download"]
)

with tab_find:
    findings.render(df)
with tab_meth:
    method.render(df)
with tab_data:
    data_tab.render(df)
with tab_dl:
    download.render()

footer()
