# Narrativa del Proyecto: "Empanada" — Ventas y Predicción

**Problema:** Estimar la demanda diaria de empanadas para optimizar producción, reducir desperdicios y planificar promociones.

**Objetivo:** Construir una aplicación que permita:
- Explorar la serie histórica de ventas.
- Analizar cómo precio, promoción, temperatura y fin de semana afectan ventas.
- Predecir ventas diarias (unidades) para una combinación dada de condiciones.

**Datos:** dataset sintético (1 año) con variables: date, producto, precio, promocion, temp_c, dia_semana, is_weekend, ventas_diarias.

**Modelo:** Regresión lineal (interpretabilidad y robustez). Métricas calculadas: MAE, RMSE.

**Limitaciones:** Datos simulados; modelo simple. Recomendado: ampliar dataset con histórico real, incluir variables adicionales (competencia, stock, día festivo) y probar modelos no lineales.
