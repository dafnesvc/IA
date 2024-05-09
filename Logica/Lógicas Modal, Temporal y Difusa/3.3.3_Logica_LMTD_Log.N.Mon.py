"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Lógicas Modal, Temporal y Difusa ---> Lógica No Monotónica"""
import matplotlib.pyplot as plt

# Definición de los hechos iniciales
hechos = {'p': True, 'q': False}

# Definición de las reglas
reglas = {
    'r1': {'si': ['p'], 'entonces': 'q'}
}

# Función para aplicar las reglas y actualizar los hechos
def aplicar_reglas(hechos, reglas):
    nuevos_hechos = dict(hechos)
    for regla, condiciones in reglas.items():
        if all(condicion in nuevos_hechos and nuevos_hechos[condicion] for condicion in condiciones['si']):
            nuevos_hechos[condiciones['entonces']] = True
    return nuevos_hechos

# Aplicar las reglas para obtener los nuevos hechos
nuevos_hechos = aplicar_reglas(hechos, reglas)

# Visualización de los hechos utilizando Matplotlib
plt.bar(nuevos_hechos.keys(), [int(hecho) for hecho in nuevos_hechos.values()], color=['green' if hecho else 'red' for hecho in nuevos_hechos.values()])
plt.title('Hechos después de aplicar las reglas')
plt.xlabel('Hechos')
plt.ylabel('Verdad')
plt.show()
