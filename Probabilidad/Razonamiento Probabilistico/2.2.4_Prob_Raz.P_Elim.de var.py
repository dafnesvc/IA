"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razonamiento Probabilístico---> Eliminación de Variables

Este script realiza eliminación de variables para calcular las probabilidades marginales P(X) y P(Y)
utilizando las probabilidades a priori y condicionales proporcionadas. Los resultados se visualizan
gráficamente con matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt

# Definición de las probabilidades condicionales y las probabilidades a priori
prob_a_priori = {'A': 0.3, 'B': 0.7}
prob_condicional = {'A': {'X': 0.9, 'Y': 0.2}, 'B': {'X': 0.1, 'Y': 0.8}}

# Función para realizar la eliminación de variables
def eliminacion_de_variables(variables_observadas, prob_a_priori, prob_condicional):
    # Calcular la probabilidad marginal de las variables observadas
    prob_marginal = 0
    for val in prob_a_priori.keys():
        prob_marginal += prob_a_priori[val] * prob_condicional[val][variables_observadas]
    return prob_marginal

# Calcular la probabilidad marginal P(X)
prob_marginal_X = eliminacion_de_variables('X', prob_a_priori, prob_condicional)

# Calcular la probabilidad marginal P(Y)
prob_marginal_Y = eliminacion_de_variables('Y', prob_a_priori, prob_condicional)

# Visualización de los resultados
plt.figure(figsize=(8, 6))
plt.bar(['P(X)', 'P(Y)'], [prob_marginal_X, prob_marginal_Y], color=['blue', 'green'])
plt.title('Eliminación de Variables')
plt.xlabel('Variable')
plt.ylabel('Probabilidad Marginal')
plt.ylim(0, 1)
plt.show()

