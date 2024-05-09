"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica Proposicional---> Algoritmos de Búsqueda Local"""

import numpy as np
import matplotlib.pyplot as plt

def funcion_objetivo(x):
    """
    Definición de la función objetivo.
    En este ejemplo, utilizamos una función cuadrática.
    """
    return -(x ** 2)

def hill_climbing(funcion_objetivo, x_inicial, paso, num_pasos):
    """
    Algoritmo de ascenso de colinas (hill climbing) para encontrar el máximo de una función.
    """
    x_actual = x_inicial
    maximo_global = funcion_objetivo(x_actual)

    for _ in range(num_pasos):
        # Generar un nuevo punto vecino dentro del rango [x_actual - paso, x_actual + paso]
        x_vecino = x_actual + np.random.uniform(-paso, paso)
        
        # Calcular el valor de la función objetivo en el nuevo punto vecino
        valor_vecino = funcion_objetivo(x_vecino)
        
        # Actualizar el punto actual si el valor del vecino es mayor
        if valor_vecino > maximo_global:
            maximo_global = valor_vecino
            x_actual = x_vecino

    return x_actual, maximo_global

# Parámetros del algoritmo
x_inicial = 2.0
paso = 0.1
num_pasos = 100

# Ejecutar el algoritmo
x_maximo, valor_maximo = hill_climbing(funcion_objetivo, x_inicial, paso, num_pasos)

# Mostrar resultados
print(f"El máximo encontrado es {valor_maximo} en x = {x_maximo}")

# Visualizar la función objetivo y el máximo encontrado
x = np.linspace(-5, 5, 100)
y = funcion_objetivo(x)

plt.plot(x, y, label='Función Objetivo')
plt.scatter(x_maximo, valor_maximo, color='red', label='Máximo Encontrado')
plt.title('Algoritmo de Búsqueda Local: Ascenso de Colinas')
plt.xlabel('x')
plt.ylabel('Valor de la Función Objetivo')
plt.legend()
plt.grid(True)
plt.show()
