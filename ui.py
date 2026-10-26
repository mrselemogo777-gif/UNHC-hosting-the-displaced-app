import streamlit as st

from styles import CSS, HERO, BANNER, section_title, metric_card_html, so_what_html, footer_html
from config import PAGE_TITLE, PAGE_ICON, LAYOUT, AUTHOR, SNAPSHOT_DATE

def setup_page():
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=LAYOUT)
    st.markdown(CSS, unsafe_allow_html=True)
    st.markdown(HERO, unsafe_allow_html=True)
    st.markdown(BANNER, unsafe_allow_html=True)

def section(text):
    st.markdown(section_title(text), unsafe_allow_html=True)

def metric_row(cards, columns=4):
    cols = st.columns(columns)
    for i, (title, value, note) in enumerate(cards):
        with cols[i]:
            st.markdown(metric_card_html(title, value, note), unsafe_allow_html=True)

def so_what(year, overlap):
    st.markdown(so_what_html(year, overlap), unsafe_allow_html=True)

def footer():
    st.markdown(footer_html(AUTHOR, SNAPSHOT_DATE), unsafe_allow_html=True)
