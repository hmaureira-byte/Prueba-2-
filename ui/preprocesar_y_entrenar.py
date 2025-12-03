import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import os
import joblib

def mostrar():
    st.title("Entrenamiento del modelo de ventas (Random Forest)")

    if st.button("Entrenar modelo"):
        st.write("Cargando datos...")
        df = pd.read_csv("data/dataset.csv")
        X = df[["precio", "promocion", "temp_c", "dia_semana", "is_weekend"]].values
        y = df["ventas_diarias"].values

        st.write("Normalizando datos...")
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        st.write("Dividiendo datos...")
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=1)

        st.write("Entrenando modelo (Random Forest)...")
        model = RandomForestRegressor(n_estimators=100, random_state=1)
        model.fit(X_train, y_train)

        st.write("Evaluando modelo...")
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        st.metric("RMSE", f"{rmse:.2f}")
        st.metric("MAE", f"{mae:.2f}")
        st.metric("R²", f"{r2:.2f}")

        os.makedirs("data", exist_ok=True)
        joblib.dump(model, "data/modelo_entrenado_rf.pkl")
        joblib.dump(scaler, "data/scaler_rf.pkl")
        st.success("Modelo y scaler guardados correctamente en data/.")