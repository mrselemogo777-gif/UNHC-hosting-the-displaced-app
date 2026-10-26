import pandas as pd
import streamlit as st

from config import CSV_PATH

@st.cache_data
def load_data():
    return pd.read_csv(CSV_PATH)

def prepare_snapshot(df, year, threshold):
    snap = df[df.year == year].dropna(subset=["refugees"]).copy()
    cov = snap.dropna(subset=["population", "gdp_per_capita"]).copy()
    cov["refugees_per_1k"] = cov["refugees"] / cov["population"] * 1000
    big = cov[cov.refugees >= threshold]
    return cov, big

def compute_overlap(big):
    abs_top = set(big.nlargest(10, "refugees").country_name)
    pc_top = set(big.nlargest(10, "refugees_per_1k").country_name)
    return len(abs_top & pc_top)
