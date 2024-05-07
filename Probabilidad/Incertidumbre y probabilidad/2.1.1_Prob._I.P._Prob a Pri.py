"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Incertidumbre y Probabilidad--->Probabilidad a Priori

Este código genera datos ficticios de ejemplo y luego calcula la probabilidad a priori de 
cada categoría en base a la frecuencia de ocurrencia de cada categoría en los datos. 
Finalmente, grafica las probabilidades a priori para visualizarlas."""

import numpy as np
import matplotlib.pyplot as plt

# Datos ficticios de ejemplo
categories = ['A', 'B', 'C', 'D', 'E', 'F']
data = np.random.choice(categories, size=100, p=[0.2, 0.1, 0.15, 0.1, 0.25, 0.2])  # Generar datos aleatorios con probabilidades proporcionales

# Función para calcular la probabilidad a priori de cada categoría
def calculate_prior_prob(data, categories):
    total_samples = len(data)  # Calcular el número total de muestras
    unique, counts = np.unique(data, return_counts=True)  # Contar las ocurrencias de cada categoría
    prior_prob = {category: count / total_samples for category, count in zip(unique, counts)}  # Calcular la probabilidad a priori de cada categoría
    return prior_prob

# Función para graficar las probabilidades a priori
def plot_prior_prob(prior_prob):
    plt.bar(prior_prob.keys(), prior_prob.values(), color='skyblue')
    plt.xlabel('Categoría')
    plt.ylabel('Probabilidad a Priori')
    plt.title('Probabilidad a Priori de Cada Categoría')
    plt.show()

# Calcular las probabilidades a priori
prior_prob = calculate_prior_prob(data, categories)

# Graficar las probabilidades a priori
plot_prior_prob(prior_prob)
