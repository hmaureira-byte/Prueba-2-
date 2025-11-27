import streamlit as st
import torch
import torch.nn as nn
import os

def mostrar():
    st.title("Predicción de Ventas con Red Neuronal")

    class Modelo(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc = nn.Sequential(
                nn.Linear(1, 16),
                nn.ReLU(),
                nn.Linear(16, 1)
            )
        def forward(self, x):
            return self.fc(x)

    modelo_path = "data/modelo_streamlit.pth"

    if os.path.exists(modelo_path):
        checkpoint = torch.load(modelo_path, weights_only=False)
        modelo = Modelo()
        modelo.load_state_dict(checkpoint["state_dict"])
        modelo.eval()

        precio_min = checkpoint["precio_min"]
        precio_max = checkpoint["precio_max"]
        ventas_min = checkpoint["ventas_min"]
        ventas_max = checkpoint["ventas_max"]

        precio = st.number_input("Precio del producto a predecir", min_value=100, max_value=5000)

        if st.button("Predecir Ventas"):
            precio_norm = (precio - precio_min) / (precio_max - precio_min)
            entrada = torch.tensor([[precio_norm]], dtype=torch.float32)
            pred_norm = modelo(entrada).item()
            pred = pred_norm * (ventas_max - ventas_min) + ventas_min
            pred_entero = max(1, int(round(pred)))
            st.success(f"Ventas estimadas: {pred_entero} unidades por día")
    else:
        st.warning("Primero debes entrenar y guardar el modelo.")