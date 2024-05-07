"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en grafos ---> Utilidad y Toma de Decisiones---> Red Bayesiana Dinámica
Este script genera muestras de una Red Bayesiana Dinámica que modela el tiempo y el tráfico 
a lo largo de varios pasos de tiempo y visualiza los resultados utilizando Matplotlib. """

import numpy as np
import matplotlib.pyplot as plt

# Definir las variables aleatorias
X = np.array([0, 1])  # Estado del tiempo: 0 para soleado, 1 para lluvioso
Y = np.array([0, 1])  # Estado del tráfico: 0 para ligero, 1 para denso

# Definir las probabilidades condicionales
# Probabilidad de cambio de tiempo
P_X = np.array([0.7, 0.3])  # Soleado -> Lluvioso
# Probabilidad de tráfico dado el tiempo
P_Y_given_X = np.array([[0.8, 0.2],  # Soleado -> Ligero, Soleado -> Denso
                        [0.4, 0.6]]) # Lluvioso -> Ligero, Lluvioso -> Denso

# Inicializar la Red Bayesiana Dinámica (DBN)
def dbn(X, Y, P_X, P_Y_given_X, n_steps):
    X_samples = [np.random.choice(X, p=P_X)]
    Y_samples = [np.random.choice(Y, p=P_Y_given_X[X_samples[0]])]

    # Realizar las transiciones para n_steps
    for _ in range(1, n_steps):
        # Actualizar el estado del tiempo
        X_samples.append(np.random.choice(X, p=P_X))
        # Actualizar el estado del tráfico basado en el tiempo actual
        Y_samples.append(np.random.choice(Y, p=P_Y_given_X[X_samples[-1]]))

    return X_samples, Y_samples

# Generar muestras de la DBN
n_steps = 10
X_samples, Y_samples = dbn(X, Y, P_X, P_Y_given_X, n_steps)

# Visualizar los resultados
plt.figure(figsize=(10, 6))
plt.plot(X_samples, label='Tiempo (X)')
plt.plot(Y_samples, label='Tráfico (Y)')
plt.xlabel('Paso de tiempo')
plt.ylabel('Estado')
plt.title('Ejemplo de Red Bayesiana Dinámica')
plt.xticks(range(n_steps))
plt.yticks([0, 1], ['Soleado/Ligero', 'Lluvioso/Denso'])
plt.legend()
plt.grid(True)
plt.show()

