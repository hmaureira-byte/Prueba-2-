import streamlit as st
import pandas as pd
import pickle

def mostrar():
    st.title("Predicción de Ventas")

    # Cargar modelo
    with open("models/model_lr.pkl", "rb") as f:
        model = pickle.load(f)

    st.subheader("Ingresa los datos para predecir:")

    precio = st.number_input("Precio del producto", min_value=500, max_value=3000, value=1500)
    temp = st.number_input("Temperatura (°C)", min_value=-5.0, max_value=40.0, value=20.0)
    promo = st.checkbox("¿Hay promoción?", value=False)

    # Valores faltantes automáticos:
    # día de la semana (0 = lunes)
    dia_semana = 0
    # is_weekend: fin de semana = 1 si dia_semana >=5
    is_weekend = 1 if dia_semana >= 5 else 0

    # Crear dataframe con EXACTAMENTE las columnas usadas al entrenar
    X = pd.DataFrame({
        "precio": [precio],
        "promocion": [1 if promo else 0],
        "temp_c": [temp],
        "dia_semana": [dia_semana],
        "is_weekend": [is_weekend]
    })

    # Predecir
    pred = model.predict(X)[0]

    st.subheader(f"Predicción estimada: **{pred:.0f} ventas**")
    st.write("Este valor corresponde a una estimación generada por un modelo de regresión lineal entrenado sobre datos históricos simulados.")
    st.write("El modelo intenta capturar relaciones entre precio, clima, promociones y ventas.")

    st.write("Nota: Esta predicción es una estimación basada en el modelo entrenado y puede variar según las condiciones reales.")  