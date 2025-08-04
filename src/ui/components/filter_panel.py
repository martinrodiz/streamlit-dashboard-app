import streamlit as st

from core.data_wrangling import get_unique_values

filter_dims = [
    "Grupo edad",
    "Género",
    "Categoría",
    "Segmento",
    "Nombre producto",
    "Fecha",
]


def filter_panel(df):
    filters = {}
    with st.expander("Filtros"):
        filter_cols = st.columns(len(filter_dims))
        for idx, dim in enumerate(filter_dims):
            with filter_cols[idx]:
                unique_vals = get_unique_values(df, dim)
                filters[dim] = st.multiselect(dim, unique_vals)
    return filters
