"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Redes Neuronales ---> Redes Multicapa
En este ejemplo, creamos una red neuronal multicapa con dos capas ocultas, cada una con 10 neuronas 
y una función de activación ReLU. Utilizamos TensorFlow para construir y entrenar el modelo. Luego, 
visualizamos la pérdida durante el entrenamiento para verificar cómo se está ajustando el modelo a los datos. """

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(0)
X = np.linspace(-1, 1, 100).reshape(-1, 1)
y = 2 * X + np.random.normal(0, 0.2, size=X.shape)

# Definir la arquitectura de la red neuronal
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mse')

# Entrenar el modelo
history = model.fit(X, y, epochs=100, verbose=0)

# Visualizar la pérdida durante el entrenamiento
plt.plot(history.history['loss'])
plt.title('Pérdida durante el entrenamiento')
plt.xlabel('Época')
plt.ylabel('Pérdida')
plt.show()

# Visualizar la predicción del modelo
plt.scatter(X, y, label='Datos de entrenamiento')
plt.plot(X, model.predict(X), color='red', label='Predicción del modelo')
plt.title('Predicción del modelo vs Datos de entrenamiento')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
