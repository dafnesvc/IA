"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica 1er Orden ---> Reglas de Diagnóstico y Causales"""

import matplotlib.pyplot as plt

# Definición de las reglas de diagnóstico y causales
reglas_diagnosticas = {
    "Síntoma1": ["Enfermedad1", "Enfermedad2"],
    "Síntoma2": ["Enfermedad1", "Enfermedad3"],
    "Síntoma3": ["Enfermedad2", "Enfermedad3"],
}

# Visualización de las reglas de diagnóstico y causales
plt.figure(figsize=(8, 6))

for i, (sintoma, enfermedades) in enumerate(reglas_diagnosticas.items()):
    for enfermedad in enfermedades:
        plt.arrow(i + 0.1, 0.1, 0, 0.4, head_width=0.1, head_length=0.1, fc='black', ec='black')
        plt.text(i + 0.1, 0.5, f"{sintoma} -> {enfermedad}", fontsize=10)

plt.xticks(range(len(reglas_diagnosticas)), list(reglas_diagnosticas.keys()))
plt.yticks([])  # Desactivar los ticks del eje Y
plt.xlabel('Síntomas')
plt.title('Reglas de Diagnóstico y Causales')
plt.grid(False)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
