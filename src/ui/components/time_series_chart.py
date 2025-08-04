import plotly.graph_objects as go
import streamlit as st

from core.data_wrangling import get_metric_time_series
from core.metric_config import display_metrics, metrics


def get_time_series_chart(df, metric):
    data = get_metric_time_series(df, metric)
    fig = go.Figure()
    # go.Scatter crea un grafico de dispersión
    fig.add_trace(
        go.Scatter(
            x=data["Dia"],
            y=data["Valor"],
            mode="lines+markers",
        )
    )

    fig.update_layout(
        title=f"{metric.title}",
        xaxis_title="Dia",
        yaxis_title=metric.title,
    )

    return fig


def time_series_chart(df):
    with st.container(border=True):
        chart_tabs = st.tabs(display_metrics)
        for idx, met in enumerate(display_metrics):
            with chart_tabs[idx]:
                chart = get_time_series_chart(df, metrics[met])
                st.plotly_chart(chart, use_container_width=True)
