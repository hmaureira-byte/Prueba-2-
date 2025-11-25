import streamlit as st

def mostrar():
    st.title("🍽️ Sistema de Análisis de Ventas de Comida")

    st.markdown("""
    ### Bienvenido/a a la aplicación del proyecto  
    Esta herramienta permite:

    - 📊 Analizar ventas de productos de comida  
    - 🧮 Visualizar datos y relaciones importantes  
    - 🤖 Realizar predicciones mediante un modelo de aprendizaje automático  
      
    **Integrantes del grupo:**
    - 👩‍💻 *Helen Maureira* — Dataset, Preprocesamiento, Análisis de Datos  
    - 👨‍💻 *Francisco Provoste* — Modelo predictivo, Pantallas adicionales  
    """)

    st.info("Selecciona una sección desde el menú lateral.")

