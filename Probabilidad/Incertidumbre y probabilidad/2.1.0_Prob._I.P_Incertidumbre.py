"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Incertidumbre y Probabilidad--->Incertidumbre
Este código simula el lanzamiento de una moneda num_flips veces y luego calcula la frecuencia
de aparición de cada resultado (cara o sello). Finalmente, grafica los resultados para visualizar
la incertidumbre asociada con el lanzamiento de la moneda.
"""
import numpy as np
import matplotlib.pyplot as plt

# Simulación del lanzamiento de una moneda
def flip_coin(num_flips):
    results = np.random.choice(['Cara', 'Sello'], size=num_flips)  # Lanzar la moneda 'num_flips' veces
    return results

# Función para calcular la frecuencia de cada resultado
def calculate_frequency(results):
    unique, counts = np.unique(results, return_counts=True)  # Contar la frecuencia de cada resultado
    return dict(zip(unique, counts))

# Función para graficar los resultados
def plot_results(frequency_dict):
    labels = list(frequency_dict.keys())
    counts = list(frequency_dict.values())
    
    plt.bar(labels, counts, color=['blue', 'green'])
    plt.xlabel('Resultado')
    plt.ylabel('Frecuencia')
    plt.title('Resultados del Lanzamiento de la Moneda')
    plt.show()

# Parámetros
num_flips = 1000  # Número de veces que se lanzará la moneda

# Simular el lanzamiento de la moneda
results = flip_coin(num_flips)

# Calcular la frecuencia de cada resultado
frequency = calculate_frequency(results)

# Graficar los resultados
plot_results(frequency)
