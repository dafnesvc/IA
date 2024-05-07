"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Incertidumbre y Probabilidad--->Regla de Bayes

Este script calculará y mostrará la probabilidad de tener una enfermedad dado un resultado
positivo en un test, utilizando la Regla de Bayes. Luego, generará un gráfico de barras que 
muestra estas probabilidades para tener o no tener la enfermedad.
"""

import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
# Probabilidad de una enfermedad, P(D)
prob_enfermedad = 0.01
# Sensibilidad del test, P(+|D)
prob_positivo_dado_enfermedad = 0.95
# Probabilidad de un falso positivo, P(+|¬D)
prob_positivo_dado_no_enfermedad = 0.01

# Calculando la probabilidad de tener la enfermedad dado un resultado positivo, P(D|+)
# Utilizando la Regla de Bayes: P(D|+) = (P(+|D) * P(D)) / P(+)
# P(+) = P(+|D) * P(D) + P(+|¬D) * P(¬D)
prob_positivo = (prob_positivo_dado_enfermedad * prob_enfermedad) + (prob_positivo_dado_no_enfermedad * (1 - prob_enfermedad))
prob_enfermedad_dado_positivo = (prob_positivo_dado_enfermedad * prob_enfermedad) / prob_positivo

# Visualización de resultados
labels = ['Enfermedad', 'No Enfermedad']
probabilidades = [prob_enfermedad_dado_positivo, 1 - prob_enfermedad_dado_positivo]

# Graficar el resultado
plt.bar(labels, probabilidades, color=['blue', 'green'])
plt.title('Probabilidad de tener la enfermedad dado un resultado positivo')
plt.xlabel('Condición')
plt.ylabel('Probabilidad')
plt.ylim(0, 1)  # Limitar el eje y entre 0 y 1 para la probabilidad
plt.show()
