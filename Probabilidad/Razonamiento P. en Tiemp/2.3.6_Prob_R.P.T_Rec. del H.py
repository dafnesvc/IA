"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razon. Probabil. en el Tiempo---> Reconocimiento del Habla

Este script simula un sistema de reconocimiento de habla simple, donde se calcula la probabilidad de
que haya habla en cada segmento de audio en función de su magnitud media. Los resultados se visualizan
en un gráfico donde se muestran los datos de audio, el umbral de habla y la probabilidad de habla en cada segmento"""

import numpy as np
import matplotlib.pyplot as plt

# Simulación de datos de audio
np.random.seed(0)
audio_data = np.random.randn(1000)  # Datos de audio simulados

# Parámetros del modelo de reconocimiento de habla
threshold = 0.5  # Umbral para detectar la presencia de habla

# Función para calcular la probabilidad de habla en una ventana de tiempo
def calculate_speech_probability(audio_segment):
    # Simplemente tomamos la magnitud media del segmento de audio y la comparamos con el umbral
    avg_magnitude = np.mean(np.abs(audio_segment))
    speech_probability = 1.0 if avg_magnitude > threshold else 0.0
    return speech_probability

# Procesamiento del audio por segmentos
segment_length = 100  # Longitud de cada segmento de audio
num_segments = len(audio_data) // segment_length
speech_probabilities = []

for i in range(num_segments):
    start_idx = i * segment_length
    end_idx = start_idx + segment_length
    segment = audio_data[start_idx:end_idx]
    
    # Calculamos la probabilidad de habla para este segmento
    speech_probability = calculate_speech_probability(segment)
    speech_probabilities.append(speech_probability)

# Visualización de los resultados
plt.figure(figsize=(10, 6))
plt.plot(audio_data, label='Datos de Audio', color='blue')
plt.axhline(threshold, linestyle='--', color='red', label='Umbral de Habla')
plt.scatter(np.arange(0, len(audio_data), segment_length), speech_probabilities, color='green', marker='o', label='Probabilidad de Habla')
plt.title('Reconocimiento del Habla')
plt.xlabel('Tiempo')
plt.ylabel('Magnitud / Probabilidad')
plt.legend()
plt.grid(True)
plt.show()
