import streamlit as st

from core.formatting import format_metric
from core.metric_config import display_metrics, metrics


def get_metric(df, metric):
    return metric.func(df)


def metric_bar(main_df):
    with st.container(border=True):
        metric_cols = st.columns(len(display_metrics))
        for idx, metric_name in enumerate(display_metrics):
            metric = metrics[metric_name]
            with metric_cols[idx]:
                value = get_metric(main_df, metric)
                formated_value = format_metric(value, metric.type)
                c1, c2, c3 = st.columns([1, 3, 1])
                with c2:
                    st.metric(metric.title, formated_value)
