"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Lógicas Modal, Temporal y Difusa ---> Lógica por Defecto"""

import matplotlib.pyplot as plt

# Definición de los hechos iniciales
hechos = {'p': True, 'q': False}

# Definición de las reglas por defecto
reglas_por_defecto = {
    'r1': {'si': ['p'], 'entonces': 'q'}
}

# Función para aplicar las reglas y actualizar los hechos
def aplicar_reglas(hechos, reglas):
    nuevos_hechos = dict(hechos)
    for regla, condiciones in reglas.items():
        if all(condicion in nuevos_hechos and nuevos_hechos[condicion] for condicion in condiciones['si']):
            nuevos_hechos[condiciones['entonces']] = True
    return nuevos_hechos

# Aplicar las reglas por defecto para obtener los nuevos hechos
nuevos_hechos = aplicar_reglas(hechos, reglas_por_defecto)

# Visualización de los hechos utilizando Matplotlib
plt.bar(nuevos_hechos.keys(), [int(hecho) for hecho in nuevos_hechos.values()], color=['green' if hechos[hecho] else 'red' for hecho in nuevos_hechos.keys()])
plt.title('Hechos después de aplicar las reglas por defecto')
plt.xlabel('Hechos')
plt.ylabel('Verdad')
plt.show()
