import streamlit as st
import torch
import torch.nn as nn

def mostrar():
    st.title("Predicción de Ventas con Red Neuronal")

    datos = torch.load("data/procesado.pkl")
    X = datos["X"]
    y = datos["y"]

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
    
    modelo = Modelo()
    modelo.eval()

    precio = st.number_input("Precio del producto a predecir", min_value=100, max_value=5000)

    if st.button("Predecir Ventas"):
        entrada = torch.tensor([[precio]], dtype=torch.float32)
        pred = modelo(entrada).item()
        st.success(f"Ventas estimadas: {pred:.1f} unidades por día")
