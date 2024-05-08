"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razonamiento Probabilístico--->Regla de la Cadena

Este script calcula las probabilidades marginales de X y las probabilidades condicionales de Y dado X
a partir de un conjunto de datos dado, y luego visualiza estos resultados usando matplotlib."""

import numpy as np
import matplotlib.pyplot as plt

# Definición de los datos de entrada
datos = np.array([[0, 1], [1, 0], [0, 1], [1, 0], [0, 1]])

# Función para calcular la probabilidad marginal de X
def probabilidad_marginal_x(datos, valor_x):
    total_muestras = len(datos)
    conteo_valor_x = np.sum(datos[:, 0] == valor_x)
    return conteo_valor_x / total_muestras

# Función para calcular la probabilidad condicional de Y dado X
def probabilidad_condicional_y_dado_x(datos, valor_x, valor_y):
    muestras_con_x = datos[datos[:, 0] == valor_x]
    total_muestras_con_x = len(muestras_con_x)
    conteo_valor_y_con_x = np.sum(muestras_con_x[:, 1] == valor_y)
    return conteo_valor_y_con_x / total_muestras_con_x

# Definición de los valores de X e Y
valores_x = [0, 1]
valores_y = [0, 1]

# Cálculo de las probabilidades marginales de X
probabilidades_marginales_x = [probabilidad_marginal_x(datos, valor_x) for valor_x in valores_x]

# Cálculo de las probabilidades condicionales de Y dado X
probabilidades_condicionales_y_dado_x = np.array([[probabilidad_condicional_y_dado_x(datos, valor_x, valor_y) for valor_y in valores_y] for valor_x in valores_x])

# Visualización de los resultados
plt.figure(figsize=(10, 5))

# Graficar las probabilidades marginales de X
plt.subplot(1, 2, 1)
plt.bar(valores_x, probabilidades_marginales_x, color='blue', alpha=0.5)
plt.title('Probabilidad Marginal de X')
plt.xlabel('Valor de X')
plt.ylabel('Probabilidad')

# Graficar las probabilidades condicionales de Y dado X
plt.subplot(1, 2, 2)
for i, valor_x in enumerate(valores_x):
    plt.bar(np.array(valores_y) + i * 0.2, probabilidades_condicionales_y_dado_x[i], width=0.2, label=f'P(Y|X={valor_x})', alpha=0.5)
plt.title('Probabilidad Condicional de Y dado X')
plt.xlabel('Valor de Y')
plt.ylabel('Probabilidad')
plt.legend()

plt.tight_layout()
plt.show()
