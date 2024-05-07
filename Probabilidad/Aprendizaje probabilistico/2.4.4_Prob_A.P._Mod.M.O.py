"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Aprendizaje Probabilístico ---> Modelos de Markov Ocultos"""
import numpy as np
import matplotlib.pyplot as plt
from hmmlearn import hmm

# Creamos y entrenamos el modelo HMM
model = hmm.GaussianHMM(n_components=2, covariance_type="full", random_state=42)

# Definimos los parámetros del modelo (probabilidades de transición y emisión)
model.startprob_ = np.array([0.5, 0.5])  # Probabilidad inicial de los estados
model.transmat_ = np.array([[0.7, 0.3],   # Probabilidades de transición entre estados
                            [0.3, 0.7]])
model.means_ = np.array([[0.0, 0.0],      # Medias de las distribuciones gaussianas para cada estado
                         [3.0, 3.0]])
model.covars_ = np.tile(np.identity(2), (2, 1, 1))  # Covarianza de las distribuciones gaussianas

# Generamos secuencias de observaciones a partir del modelo
observed, states = model.sample(100)

# Graficamos las secuencias observadas
plt.figure(figsize=(10, 6))
plt.plot(observed[:, 0], observed[:, 1], ".-", label="Observado")
plt.title("Secuencia de Observaciones Generadas por el Modelo HMM")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.grid(True)
plt.show()

# Graficamos los estados ocultos
plt.figure(figsize=(10, 2))
plt.plot(states, "o-", label="Estado Oculto")
plt.title("Estados Ocultos Generados por el Modelo HMM")
plt.xlabel("Tiempo")
plt.ylabel("Estado")
plt.yticks([0, 1], ["Estado 1", "Estado 2"])
plt.legend()
plt.grid(True)
plt.show()
