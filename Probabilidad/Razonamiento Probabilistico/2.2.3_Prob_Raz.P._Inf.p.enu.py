"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razonamiento Probabilístico---> Inferencia por Enumeración
"""
import numpy as np
import matplotlib.pyplot as plt

# Definición de las probabilidades condicionales y las probabilidades a priori
prob_a_priori = {'A': 0.3, 'B': 0.7}
prob_condicional = {'A': {'X': 0.9, 'Y': 0.2}, 'B': {'X': 0.1, 'Y': 0.8}}

# Función para realizar la inferencia por enumeración
def inferencia_por_enumeracion(variables_observadas, prob_a_priori, prob_condicional):
    total_prob = 0
    # Iterar sobre todas las posibles combinaciones de valores de las variables no observadas
    for val1 in prob_a_priori.keys():
        prob_val1 = prob_a_priori[val1]
        for val2 in prob_a_priori.keys():
            prob_val2 = prob_a_priori[val2]
            # Calcular la probabilidad conjunta de las variables observadas y no observadas
            prob_conjunta = prob_val1 * prob_val2 * prob_condicional[val1][variables_observadas[0]] * prob_condicional[val2][variables_observadas[1]]
            total_prob += prob_conjunta
    return total_prob

# Calcular la probabilidad condicional P(A|X)
prob_A_dado_X = prob_condicional['A']['X'] * prob_a_priori['A'] / (prob_condicional['A']['X'] * prob_a_priori['A'] + prob_condicional['B']['X'] * prob_a_priori['B'])

# Calcular la probabilidad condicional P(B|Y)
prob_B_dado_Y = prob_condicional['B']['Y'] * prob_a_priori['B'] / (prob_condicional['B']['Y'] * prob_a_priori['B'] + prob_condicional['A']['Y'] * prob_a_priori['A'])

# Visualización de los resultados
plt.figure(figsize=(8, 6))
plt.bar(['P(A|X)', 'P(B|Y)'], [prob_A_dado_X, prob_B_dado_Y], color=['blue', 'green'])
plt.title('Inferencia por Enumeración')
plt.xlabel('Variable')
plt.ylabel('Probabilidad')
plt.ylim(0, 1)
plt.show()
