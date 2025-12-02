import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def mostrar():
	st.title("Visualización de Datos")
	df = pd.read_csv("data/dataset.csv")

	st.metric("Promedio de ventas", round(df["ventas_diarias"].mean(), 1))
	st.metric("Venta mínima", df["ventas_diarias"].min())
	st.metric("Venta máxima", df["ventas_diarias"].max())


	# Gráficos aquí...

	# Convertir fecha
	df["date"] = pd.to_datetime(df["date"])

	# ---- Gráfico de tendencia ----
	st.subheader("Tendencia de ventas diarias")
	fig, ax = plt.subplots()
	ax.plot(df["date"], df["ventas_diarias"])
	ax.set_xlabel("Fecha")
	ax.set_ylabel("Ventas diarias")
	st.pyplot(fig)

	# ---- Ventas por temperatura ----
	st.subheader("Relación entre temperatura y ventas")
	fig2, ax2 = plt.subplots()
	ax2.scatter(df["temp_c"], df["ventas_diarias"], alpha=0.7)
	ax2.set_xlabel("Temperatura (°C)")
	ax2.set_ylabel("Ventas diarias")
	st.pyplot(fig2)

	# ---- Promociones ----
	st.subheader("Promociones vs ventas")
	fig3, ax3 = plt.subplots()
	ax3.boxplot([df[df["promocion"] == 0]["ventas_diarias"],
	df[df["promocion"] == 1]["ventas_diarias"]],
	labels=["Sin promo", "Con promo"])
	st.pyplot(fig3)
