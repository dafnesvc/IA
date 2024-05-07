"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Percepción---> Preprocesado: Filtros"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Generar una señal de ejemplo
t = np.linspace(0, 10, 1000, endpoint=False)
x = np.sin(2 * np.pi * 1 * t) + 0.5 * np.sin(2 * np.pi * 3 * t)

# Aplicar un filtro paso bajo (filtro promedio)
b = signal.firwin(30, 0.05)
y = signal.lfilter(b, 1, x)

# Graficar la señal original y la señal filtrada
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Señal original')
plt.plot(t, y, label='Señal filtrada', linestyle='--')
plt.title('Filtro Paso Bajo: Ejemplo de Preprocesado')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()

