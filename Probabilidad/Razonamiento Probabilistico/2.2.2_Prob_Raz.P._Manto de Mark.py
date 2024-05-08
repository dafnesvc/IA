"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razonamiento Probabilístico---> Manto de Markov
Este script simula la evolución de las probabilidades de dos estados a lo largo del tiempo utilizando 
el algoritmo del "Manto de Markov". Los resultados se visualizan gráficamente con matplotlib."""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la matriz de transición de estado
matriz_transicion = np.array([[0.7, 0.3],
                              [0.2, 0.8]])

# Definición de los estados iniciales y la cantidad de iteraciones
estado_inicial = np.array([0.5, 0.5])
num_iteraciones = 10

# Lista para almacenar las probabilidades de los estados en cada iteración
probabilidades_estados = [estado_inicial]

# Iteración para calcular las probabilidades de los estados en cada paso
for i in range(num_iteraciones):
    nuevo_estado = np.dot(probabilidades_estados[-1], matriz_transicion)
    probabilidades_estados.append(nuevo_estado)

# Convertir la lista de probabilidades de estados en un array para facilitar la manipulación
probabilidades_estados = np.array(probabilidades_estados)

# Visualización de los resultados
plt.figure(figsize=(10, 5))

# Graficar las probabilidades de los estados en cada iteración
for i in range(probabilidades_estados.shape[1]):
    plt.plot(probabilidades_estados[:, i], label=f'Estado {i+1}')

plt.title('Evolución de las Probabilidades de los Estados')
plt.xlabel('Iteración')
plt.ylabel('Probabilidad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
