import pandas as pd
import streamlit as st

from core.data_loeader import load_data


def get_unique_values(df, column):
    return list(df[column].unique())


def clean_columns_names(df):
    df.columns = df.columns.str.replace("_", " ").str.capitalize()
    return df


def apply_filters(df, filters):
    for col, values in filters.items():
        if values:
            df = df[df[col].isin(values)]
    return df


@st.cache_data(show_spinner="Leyendo datos de ventas...", ttl="1d")
def prep_data() -> pd.DataFrame:
    df = clean_columns_names(load_data())
    df["Dia"] = pd.to_datetime(df["Fecha"])
    return df


def get_data_within_date_range(df, start, end):
    if start is not None and end is not None:
        dt_start, dt_end = pd.to_datetime(start), pd.to_datetime(end)
        return df[(df["Dia"] >= dt_start) & (df["Dia"] <= dt_end)]
    return df


def get_filtered_data_within_date_range(df, start, end, filters):
    df_within_range = get_data_within_date_range(df.copy(), start, end)
    return apply_filters(df_within_range, filters)


def get_metric_time_series(df, metric):
    grouped = df.groupby("Dia")
    data = grouped.apply(metric.func, include_groups=False).reset_index()
    data.columns = ["Dia", "Valor"]
    return data


def get_metric_grouped_by_dimension(df, metric, dimension):
    grouped = df.groupby(dimension)
    data = grouped.apply(metric.func, include_groups=False).reset_index()
    data.columns = [dimension, "Valor"]
    return data
