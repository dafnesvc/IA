"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en grafos ---> Utilidad y Toma de Decisiones---> MDP Parcialmente Observable (POMDP)
Este programa implementa la iteración de valor para POMDP. Cada estado tiene transiciones asociadas 
con acciones y observaciones, y la utilidad de cada estado se actualiza iterativamente hasta que se 
alcanza una convergencia dentro de un cierto umbral de diferencia."""

import numpy as np

class Estado:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del estado
        self.utilidad = 0  # Utilidad del estado
        self.transiciones = {}  # Transiciones desde este estado

    def agregar_transicion(self, accion, observacion, estado_siguiente, probabilidad):
        """
        Agrega una transición desde este estado a otro estado con una acción, una observación y una probabilidad dada.
        """
        if accion not in self.transiciones:
            self.transiciones[accion] = {}
        if observacion not in self.transiciones[accion]:
            self.transiciones[accion][observacion] = []
        self.transiciones[accion][observacion].append((estado_siguiente, probabilidad))

def iteracion_valor_pomdp(estados, acciones, observaciones, gamma=0.9, epsilon=0.01):
    """
    Implementa el algoritmo de Iteración de Valor para POMDP para encontrar la utilidad óptima de los estados.
    """
    # Inicializar las utilidades de los estados a 0
    utilidades_previas = {estado: 0 for estado in estados}

    while True:
        delta = 0
        # Para cada estado en el conjunto de estados
        for estado in estados:
            # Calcular la utilidad actual del estado
            utilidad_actual = estado.utilidad
            # Calcular la utilidad máxima para este estado
            max_utilidad = float("-inf")
            for accion in acciones:
                for observacion in observaciones:
                    utilidad_accion_observacion = sum(prob * (estado_siguiente.utilidad * gamma) for estado_siguiente, prob in estado.transiciones[accion][observacion])
                    max_utilidad = max(max_utilidad, utilidad_accion_observacion)
            # Actualizar la utilidad del estado y delta si es necesario
            estado.utilidad = max_utilidad
            delta = max(delta, abs(utilidad_actual - estado.utilidad))
        # Si la diferencia entre las utilidades de dos iteraciones consecutivas es menor que epsilon, terminar
        if delta < epsilon:
            break

    return utilidades_previas

# Definir los estados y acciones
estado_A = Estado("A")
estado_B = Estado("B")
estados = [estado_A, estado_B]
acciones = ["accion1", "accion2"]

# Definir las observaciones y las transiciones para cada acción y observación
observaciones = ["obs1", "obs2"]
for estado in estados:
    for accion in acciones:
        for observacion in observaciones:
            estado.agregar_transicion(accion, observacion, estado, 1.0)

# Ejecutar la iteración de valor para encontrar las utilidades óptimas de los estados
utilidades_optimas = iteracion_valor_pomdp(estados, acciones, observaciones)

# Imprimir las utilidades óptimas de los estados
for estado, utilidad in utilidades_optimas.items():
    print(f"Utilidad óptima de '{estado.nombre}': {utilidad}")
