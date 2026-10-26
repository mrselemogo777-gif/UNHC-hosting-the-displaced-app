[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://unhc-hosting-the-displaced-app.streamlit.app)

# Hosting the Displaced — Streamlit brief

An interactive policy brief built from the *Global Refugee & Migration Dataset 2026*
(UNHCR · World Bank · UCDP/PRIO · DHS).

**Author:** Legakwa Selemogo

Toggle **absolute** refugee host counts against **per-1,000-residents** counts for
2022–2024. The finding that survives the toggle: the countries hosting the most
refugees and the countries hosting the most per capita overlap in **≤ 2 of the
top 10** in every year shown.

## Run locally

    pip install -r requirements.txt
    streamlit run app.py

## Data

`data/global_refugee_asylum_irregular_migration_2026_FINAL.csv` — static snapshot
(retrieved 2026-07-31), bundled here so the app is fully reproducible.

## Methodological guardrails

- UNHCR registered counts are never combined with the DHS modelled estimate
  (US-only, methodologically different).
- Nulls are not zeros, except in `conflict_intensity_index` where UCDP defines a
  genuine zero inside its 1989+ coverage.
- Dataset is host-country framed; no origin-country claims are made.
