from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATOS_VENTA_PATH = BASE_DIR / "data" / "datos_ventas.csv"


def load_data():
    return pd.read_csv(DATOS_VENTA_PATH)
