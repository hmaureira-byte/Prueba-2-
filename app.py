import streamlit as st

from ui.pantalla_principal import mostrar as pantalla_principal
from ui.analisis_datos import mostrar as analisis_datos
from ui.prediccion import mostrar as prediccion
from ui.preprocesar_y_entrenar import mostrar as preprocesar_y_entrenar

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Predicción de Ventas",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("📈 Sistema de Predicción de Ventas de Empanadas")

# Menú lateral
seccion = st.sidebar.selectbox(
    "Navegación",
    ["Inicio", "Análisis de datos", "Predicción", "Preprocesar y Entrenar"]
)

# Navegación
if seccion == "Inicio":
    pantalla_principal()

elif seccion == "Análisis de datos":
    analisis_datos()

elif seccion == "Predicción":
    prediccion()

elif seccion == "Preprocesar y Entrenar":
    preprocesar_y_entrenar()