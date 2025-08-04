import plotly.graph_objects as go
import streamlit as st

from core.data_wrangling import get_metric_grouped_by_dimension
from core.metric_config import metrics, pie_chart_display_metrics


def get_pie_chart(df, metric, dimension):
    data = get_metric_grouped_by_dimension(df, metric, dimension)
    fig = go.Figure()
    fig.add_trace(
        go.Pie(
            labels=data[dimension],
            values=data["Valor"],
            hole=0.4,
        )
    )
    return fig


def pie_chart(df):
    with st.container(border=True):
        split_dimension = st.selectbox(
            "Por grupo",
            [
                "Grupo edad",
                "Género",
                "Estado",
                "Categoría",
                "Segmento",
                "Nombre producto",
            ],
        )
        metric_tabs = st.tabs(pie_chart_display_metrics)
        for idx, met in enumerate(pie_chart_display_metrics):
            with metric_tabs[idx]:
                chart = get_pie_chart(df, metrics[met], split_dimension)
                st.plotly_chart(chart, use_container_width=True)
