"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Lógicas Modal, Temporal y Difusa ---> Lógica Difusa---> Conjuntos Difusos"""
import numpy as np
import matplotlib.pyplot as plt

# Definición de las funciones de membresía
def membresia_baja(x, a, b):
    # Función de membresía para un conjunto difuso "bajo"
    return np.where(x <= a, 1, np.where(x >= b, 0, (b - x) / (b - a)))

def membresia_media(x, a, b, c, d):
    # Función de membresía para un conjunto difuso "medio"
    return np.maximum(np.minimum((x - a) / (b - a), 1, (d - x) / (d - c)), 0)

def membresia_alta(x, a, b):
    # Función de membresía para un conjunto difuso "alto"
    return np.where(x >= b, 1, np.where(x <= a, 0, (x - a) / (b - a)))

# Definición del universo del discurso
x = np.linspace(0, 10, 1000)

# Definición de los conjuntos difusos
bajo = membresia_baja(x, 2, 5)
medio = membresia_media(x, 3, 5, 7, 9)
alto = membresia_alta(x, 5, 8)

# Visualización de los conjuntos difusos
plt.figure(figsize=(8, 6))

plt.plot(x, bajo, label='Bajo')
plt.plot(x, medio, label='Medio')
plt.plot(x, alto, label='Alto')

plt.title('Conjuntos Difusos')
plt.xlabel('Universo del Discurso')
plt.ylabel('Función de Membresía')
plt.legend()
plt.grid(True)
plt.show()
