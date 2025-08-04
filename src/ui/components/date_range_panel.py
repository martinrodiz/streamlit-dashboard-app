from datetime import date, timedelta

import streamlit as st

# Hardcode this to the last date in dataset to ensure reproducibility
LATEST_DATE = date.fromisoformat("2024-08-31")
THIRTY_DAYS_AGO = LATEST_DATE - timedelta(days=30)


def date_range_panel():
    start = st.date_input("Fecha inicial", value=THIRTY_DAYS_AGO)
    end = st.date_input("Fecha final", value=LATEST_DATE)
    return start, end
