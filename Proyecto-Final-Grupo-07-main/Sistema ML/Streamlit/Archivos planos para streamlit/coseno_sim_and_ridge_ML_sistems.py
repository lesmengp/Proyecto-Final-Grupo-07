### Import libraries:
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score
import matplotlib.pyplot as plt

### Apertura dataset:
prom_final_y_one_hot = pd.read_parquet('./prom_final_y_one_hot.parquet')
prom_final_y_one_hot.info()
prom_final_y_one_hot.head()
### Aplicacion Cosine Similarity:
# Seleccionar un restaurante aleatorio del conjunto de datos
restaurante_aleatorio = prom_final_y_one_hot.sample(random_state=41)

# Seleccionar solo las columnas numéricas relevantes para el cálculo de similitud
columnas_numericas_relevantes = restaurante_aleatorio.select_dtypes(include='number').values

# Calcular la similitud del coseno con respecto a todos los restaurantes
similitud_coseno = cosine_similarity(columnas_numericas_relevantes, prom_final_y_one_hot.select_dtypes(include='number'))

# Obtener los índices de los 10 restaurantes más similares, incluyendo el índice 0
indices_similares = np.argsort(similitud_coseno[0])[::-1][:10]


# Calcular el porcentaje de similitud para los 10 restaurantes más similares
for i, indice in enumerate(indices_similares):
    similitud = similitud_coseno[0][indice]  # Obtener la similitud del coseno para el restaurante en el índice
    porcentaje_similitud = (similitud * 100).round(2)  # Convertir a porcentaje y redondear a 2 decimales
    print(f"Porcentaje de similitud con restaurante {indice}: {porcentaje_similitud}%")

### Crear un DataFrame con los 10 restaurantes más similares
#*Analiza competencia de los 10 mas similares....*
# Obtener los índices de los restaurantes más similares (top 10)
indices_10_similares = np.argsort(similitud_coseno[0])[::-1][1:11]  # Tomamos los primeros 10

# Crear un DataFrame con los 10 restaurantes más similares
restaurantes_similares = prom_final_y_one_hot.iloc[indices_10_similares]

# Mostrar el DataFrame con los 10 restaurantes más similares
print("Restaurantes Más Similares (Top 10):")
print(restaurantes_similares.head())

restaurantes_similares.head(11)
restaurante_aleatorio.head()
### Metodo Ridge
### METODO RIDGE: EL QUE MEJORES RESULTADOS OBTUVO...
from sklearn.linear_model import Ridge

# Preprocesamiento de datos
prom_final_y_one_hot.drop(['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'BusinessParking'], axis=1, inplace=True)

# Separar datos
X = prom_final_y_one_hot.drop('stars_volume', axis=1)
y = prom_final_y_one_hot['stars_volume']

# Dividir datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=41)

# Entrenar el modelo con regularización Ridge
ridge_model = Ridge(alpha=0.1)  # Alpha controla la fuerza de la regularización
ridge_model.fit(X_train, y_train)

# Evaluar el modelo
y_pred_ridge = ridge_model.predict(X_test)
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
mae_ridge = mean_absolute_error(y_test, y_pred_ridge)
r2_ridge = r2_score(y_test, y_pred_ridge)
explained_var_ridge = explained_variance_score(y_test, y_pred_ridge)

# Imprimir métricas de evaluación con regularización Ridge
print('Ridge Regression:')
print('Mean Squared Error:', mse_ridge)
print('Mean Absolute Error:', mae_ridge)
print('R-squared:', r2_ridge)
print('Explained Variance Score:', explained_var_ridge)
