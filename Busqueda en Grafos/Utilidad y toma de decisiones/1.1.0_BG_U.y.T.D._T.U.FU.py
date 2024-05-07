"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en grafos ---> Utilidad y Toma de Decisiones--->Teoría de la Utilidad: Función de Utilidad

El objetivo de este código es implementar la teoría de la utilidad utilizando una función de utilidad.
La teoría de la utilidad es un concepto fundamental en la toma de decisiones, que se utiliza para evaluar
y comparar diferentes opciones en función de su utilidad esperada. La función de utilidad asigna un valor
numérico a cada posible resultado o conjunto de atributos, lo que permite tomar decisiones informadas sobre
cuál es la opción más favorable"""

import numpy as np

class FuncionUtilidad:
    def __init__(self, pesos):
        self.pesos = np.array(pesos)  # Los pesos que representan la importancia de cada atributo en la función de utilidad

    def calcular_utilidad(self, atributos):
        """Calcula la utilidad utilizando la función de utilidad y los atributos dados."""
        # Convertir los atributos en un arreglo numpy
        atributos = np.array(atributos)
        # Multiplicar los atributos por los pesos y sumar el resultado para obtener la utilidad
        utilidad = np.dot(self.pesos, atributos)
        return utilidad

# Definir los pesos para la función de utilidad
pesos = [0.5, 0.3, 0.2]

# Crear una instancia de la función de utilidad con los pesos dados
funcion_utilidad = FuncionUtilidad(pesos)

# Definir los atributos para calcular la utilidad
atributos = [10, 8, 6]

# Calcular la utilidad utilizando la función de utilidad y los atributos dados
utilidad = funcion_utilidad.calcular_utilidad(atributos)

# Imprimir la utilidad calculada
print("Utilidad calculada:", utilidad)
