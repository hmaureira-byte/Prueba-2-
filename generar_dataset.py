# generar_dataset.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

start = datetime(2024, 1, 1)
days = 365

rows = []
base_price = 1500

for i in range(days):
    date = start + timedelta(days=i)
    dow = date.weekday()  # 0 Lunes .. 6 Domingo
    is_weekend = 1 if dow >= 5 else 0
    # Simula temperatura estacional: más frío en mitad de año (hemisferio sur)
    day_of_year = date.timetuple().tm_yday
    temp = 14 + 8 * np.sin(2 * np.pi * (day_of_year / 365.0)) + np.random.normal(0, 2)
    # precio con pequeña variación y eventos (oferta 1 vez por semana aprox)
    promotion = 1 if np.random.rand() < 0.12 else 0
    price = base_price * (1 - 0.12 * promotion) + np.random.normal(0, 50)

    # Generar ventas: base influenciada por precio (negativa), fin de semana (+), promo (+), temp pequeño efecto
    base_sales = 80 + 20 * is_weekend + 15 * promotion
    price_effect = -0.01 * (price - base_price)
    temp_effect = 0.5 * (max(0, 20 - temp)) / 10  # ligeramente más ventas si hace frío
    noise = np.random.normal(0, 8)
    ventas = max(0, int(base_sales + price_effect + temp_effect + noise))

    rows.append({
        "date": date.strftime("%Y-%m-%d"),
        "producto": "Empanada",
        "precio": int(round(price)),
        "promocion": promotion,
        "temp_c": round(temp, 1),
        "dia_semana": dow,
        "is_weekend": is_weekend,
        "ventas_diarias": ventas
    })

df = pd.DataFrame(rows)
df.to_csv("data/dataset.csv", index=False)
print("dataset.csv creado en data/ con", len(df), "filas")
