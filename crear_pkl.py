import pandas as pd
import torch

df = pd.read_csv("data/dataset.csv")

X = torch.tensor(df[["precio"]].values, dtype=torch.float32)
y = torch.tensor(df["ventas_diarias"].values, dtype=torch.float32).view(-1, 1)

torch.save({"X": X, "y": y}, "data/procesado.pkl")

print("procesado.pkl generado correctamente.")