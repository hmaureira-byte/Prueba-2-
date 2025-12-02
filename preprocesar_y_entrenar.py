import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

# Cargar dataset
df = pd.read_csv("data/dataset.csv")

# Variables predictoras
X = df[["precio", "promocion", "temp_c", "dia_semana", "is_weekend"]]
y = df["ventas_diarias"]

# Dividir en train / test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir
y_pred = model.predict(X_test)

# RMSE CORREGIDO
rmse = (mean_squared_error(y_test, y_pred)) ** 0.5
print("RMSE:", rmse)

# Guardar modelo
with open("models/model_lr.pkl", "wb") as f:
    pickle.dump(model, f)

print("Modelo guardado correctamente.")
