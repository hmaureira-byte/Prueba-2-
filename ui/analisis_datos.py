import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

def mostrar():
    st.title("Análisis Exploratorio de Ventas de Comida")

    # --- Cargar dataset ---
    data = pd.read_csv("data/dataset.csv")

    st.subheader("Vista general del dataset")
    st.dataframe(data)

    # --- Análisis 1: Histograma ---
    st.subheader("Distribución de variables numéricas")
    numeric_cols = data.select_dtypes("number").columns
    variable = st.selectbox("Selecciona una variable", numeric_cols)

    fig, ax = plt.subplots()
    ax.hist(data[variable], bins=10)
    ax.set_title(f"Distribución de {variable}")
    ax.set_xlabel(variable)
    ax.set_ylabel("Frecuencia")
    st.pyplot(fig)

    # --- Análisis 2: Ventas promedio por categoría ---
    st.subheader("Ventas promedio por categoría")
    cat_avg = data.groupby("categoria")["ventas_diarias"].mean()

    fig2, ax2 = plt.subplots()
    ax2.bar(cat_avg.index, cat_avg.values)
    ax2.set_title("Ventas Promedio por Categoría")
    ax2.set_ylabel("Ventas diarias promedio")
    ax2.set_xticklabels(cat_avg.index, rotation=20)
    st.pyplot(fig2)

    # --- Análisis 3: Relación precio vs ventas ---
    st.subheader("Relación entre precio y ventas")
    fig3, ax3 = plt.subplots()
    ax3.scatter(data["precio"], data["ventas_diarias"])
    ax3.set_xlabel("Precio")
    ax3.set_ylabel("Ventas diarias")
    ax3.set_title("Precio vs Ventas")
    st.pyplot(fig3)
    st.write("Se observa cómo varían las ventas diarias en función del precio de los productos.")
    st.write("Este análisis ayuda a entender mejor el comportamiento de las ventas en relación con los precios.")
