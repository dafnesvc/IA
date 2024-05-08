"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Robótica---> Dinámica y Control
Este código simula el comportamiento de un sistema masa-resorte-amortiguador.
Calcula las derivadas de la posición y la velocidad en función del tiempo utilizando
las ecuaciones de movimiento del sistema y luego integra numéricamente estas ecuaciones
utilizando la función odeint de SciPy. Finalmente, grafica la posición y la velocidad en función del tiempo."""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1  # Masa del objeto
k = 1  # Constante del resorte
b = 0.5  # Coeficiente de amortiguamiento

# Función que calcula la derivada de la posición y la velocidad
def derivs(state, t):
    x, v = state[0], state[1]
    dxdt = v
    dvdt = (-k * x - b * v) / m
    return [dxdt, dvdt]

# Condiciones iniciales
x0 = 1.0  # Posición inicial
v0 = 0.0  # Velocidad inicial
initial_state = [x0, v0]

# Tiempo de integración
t = np.linspace(0, 10, 1000)

# Integración numérica de las ecuaciones de movimiento
from scipy.integrate import odeint
states = odeint(derivs, initial_state, t)

# Graficar la posición y la velocidad en función del tiempo
plt.figure(figsize=(10, 6))
plt.plot(t, states[:, 0], label='Posición (x)')
plt.plot(t, states[:, 1], label='Velocidad (v)')
plt.xlabel('Tiempo')
plt.ylabel('Magnitud')
plt.title('Dinámica de un sistema masa-resorte-amortiguador')
plt.legend()
plt.grid(True)
plt.show()
