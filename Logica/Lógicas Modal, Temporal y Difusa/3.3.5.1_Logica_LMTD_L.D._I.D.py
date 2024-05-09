"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Lógicas Modal, Temporal y Difusa ---> Lógica Difusa---> Inferencia Difusa"""

import numpy as np
import matplotlib.pyplot as plt

# Función de membresía para un conjunto difuso "bajo"
def membresia_bajo(x, a, b):
    return np.where(x <= a, 1, np.where(x >= b, 0, (b - x) / (b - a)))

# Función de membresía para un conjunto difuso "medio"
def membresia_medio(x, a, b, c, d):
    return np.maximum(np.minimum((x - a) / (b - a), 1, (d - x) / (d - c)), 0)

# Función de membresía para un conjunto difuso "alto"
def membresia_alto(x, a, b):
    return np.where(x >= b, 1, np.where(x <= a, 0, (x - a) / (b - a)))

# Inferencia difusa utilizando operadores de Mamdani
def inferencia_difusa(x, bajo, medio, alto):
    # Reglas difusas
    regla1 = np.fmin(bajo, medio)
    regla2 = np.fmin(medio, alto)
    
    # Resultado de la inferencia
    resultado = np.fmax(regla1, regla2)
    return resultado

# Definición del universo del discurso
x = np.linspace(0, 10, 1000)

# Definición de los conjuntos difusos de entrada
bajo = membresia_bajo(x, 2, 5)
medio = membresia_medio(x, 3, 5, 7, 9)
alto = membresia_alto(x, 5, 8)

# Inferencia difusa
resultado = inferencia_difusa(x, bajo, medio, alto)

# Visualización del resultado
plt.figure(figsize=(8, 6))

plt.plot(x, resultado, label='Resultado')
plt.fill_between(x, 0, resultado, alpha=0.1)

plt.title('Inferencia Difusa')
plt.xlabel('Universo del Discurso')
plt.ylabel('Función de Membresía')
plt.legend()
plt.grid(True)
plt.show()

