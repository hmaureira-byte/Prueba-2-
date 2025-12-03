import streamlit as st
import pandas as pd
import joblib
import numpy as np

def mostrar():
    st.title("Predicción de Ventas (Random Forest)")

    # Cargar modelo y scaler
    scaler = joblib.load("data/scaler_rf.pkl")
    model = joblib.load("data/modelo_entrenado_rf.pkl")

    st.subheader("Ingresa los datos para predecir:")

    precio = st.number_input("Precio del producto", min_value=500, max_value=3000, value=1500)
    temp = st.number_input("Temperatura (°C)", min_value=-5.0, max_value=40.0, value=20.0)
    promo = st.checkbox("¿Hay promoción?", value=False)
    dia_semana = st.selectbox(
        "Día de la semana",
        options=[0, 1, 2, 3, 4, 5, 6],
        format_func=lambda x: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"][x]
    )
    is_weekend = 1 if dia_semana >= 5 else 0

    X = np.array([[precio, 1 if promo else 0, temp, dia_semana, is_weekend]])
    X_scaled = scaler.transform(X)

    pred = model.predict(X_scaled)[0]

    st.subheader(f"Predicción estimada: **{pred:.0f} ventas**")
    st.write("Este valor corresponde a una estimación generada por un modelo Random Forest entrenado sobre datos históricos simulados.")
    st.write("El modelo intenta capturar relaciones entre precio, clima, promociones y ventas.")
    st.write("Nota: Esta predicción es una estimación basada en el modelo entrenado y puede variar según las condiciones reales.")