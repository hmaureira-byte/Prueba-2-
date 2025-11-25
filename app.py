import streamlit as st
from ui import pantalla_principal, analisis_datos, prediccion

st.set_page_config(page_title="Ventas de Comida", layout="wide")

st.sidebar.title("Menú")

opcion = st.sidebar.radio(
    "Selecciona una sección:",
    ["Inicio", "Análisis de Datos", "Predicción de Ventas"]
)

if opcion == "Inicio":
    pantalla_principal.mostrar()

elif opcion == "Análisis de Datos":
    analisis_datos.mostrar()

elif opcion == "Predicción de Ventas":
    prediccion.mostrar()
