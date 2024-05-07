"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Percepción---> Gráficas por computador """
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = sin(x)', color='blue', linestyle='-')
plt.title('Gráfica por Computadora: Ejemplo de Función Seno')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
 