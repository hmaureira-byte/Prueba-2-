# Instrucciones para ejecutar

1. Clonar repo.
2. Crear entorno virtual (opcional):
   - `python -m venv .venv`
   - `.\.venv\Scripts\activate` (Windows)
3. Instalar dependencias:
   - `python -m pip install -r requirements.txt`
4. Generar dataset:
   - `python generar_dataset.py`  (crea data/dataset.csv)
5. Preprocesar y entrenar:
   - `python preprocesar_y_entrenar.py` (crea data/procesado.pkl y models/model_lr.pkl)
6. Ejecutar app:
   - `python -m streamlit run app.py`
