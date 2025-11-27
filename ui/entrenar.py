import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import os

df = pd.read_csv("data/dataset.csv")

precio_min = df["precio"].min()
precio_max = df["precio"].max()
ventas_min = df["ventas_diarias"].min()
ventas_max = df["ventas_diarias"].max()

X = (df[["precio"]].values - precio_min) / (precio_max - precio_min)
y = (df["ventas_diarias"].values.reshape(-1, 1) - ventas_min) / (ventas_max - ventas_min)

X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32)

class Modelo(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(1, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.ReLU()
        )
    def forward(self, x):
        return self.fc(x)

modelo = Modelo()
criterio = nn.MSELoss()
optimizador = optim.Adam(modelo.parameters(), lr=0.01)

for epoch in range(2000):
    modelo.train()
    salida = modelo(X)
    loss = criterio(salida, y)
    optimizador.zero_grad()
    loss.backward()
    optimizador.step()

os.makedirs("data", exist_ok=True)
torch.save({
    "state_dict": modelo.state_dict(),
    "precio_min": precio_min,
    "precio_max": precio_max,
    "ventas_min": ventas_min,
    "ventas_max": ventas_max
}, "data/modelo_streamlit.pth")
print("Modelo entrenado y guardado.")