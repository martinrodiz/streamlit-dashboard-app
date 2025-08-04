from core.metric import Metric


def margin_percent(df):
    total_sales = df["Ventas"].sum()
    return df["Margen bruto"].sum() / total_sales if total_sales > 0 else 0


def average_transaction_value(df):
    total_sales = df["Ventas"].sum()
    return total_sales / df["Transacciones"].sum() if total_sales > 0 else 0


metrics = {
    "Ventas totales": Metric(
        title="Ventas totales",
        func=lambda df: df["Ventas"].sum(),
        type="dollars",
    ),
    "Margen bruto": Metric(
        title="Margen bruto",
        func=lambda df: df["Margen bruto"].sum(),
        type="dollars",
    ),
    "Margen %": Metric(
        title="Margen %",
        func=margin_percent,
        type="percent",
    ),
    "VPT": Metric(
        title="Valor promedio por transaccion",
        func=average_transaction_value,
        type="dollars",
    ),
}

display_metrics = ["Ventas totales", "Margen bruto", "Margen %", "VPT"]

pie_chart_display_metrics = ["Ventas totales", "Margen bruto"]
