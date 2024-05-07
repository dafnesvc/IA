"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en grafos ---> Utilidad y Toma de Decisiones---> Valor de la información

Este programa define una red de decisión con varios nodos de decisión y nodos de resultado.
La función valor_informacion calcula el valor de la información para un nodo de decisión dado,
tomando en cuenta la diferencia en la utilidad promedio con y sin información adicional.
Finalmente, se calcula el valor de la información para cada nodo de decisión y se imprime.
"""

class NodoDecision:
    def __init__(self, nombre, utilidad=None):
        self.nombre = nombre
        self.utilidad = utilidad

def valor_informacion(utilidad_con_informacion, utilidad_actual):
    return utilidad_con_informacion - utilidad_actual  # Calcular el valor de la información

# Definir los nodos de decisión
comprar_auto = NodoDecision("Comprar Auto", utilidad=0)  # Asignar una utilidad inicial

# Calcular el valor de la información para la decisión de comprar un auto
utilidad_con_informacion = 8.6  # Utilidad con información
utilidad_actual = comprar_auto.utilidad  # Utilidad actual
valor_info_comprar_auto = valor_informacion(utilidad_con_informacion, utilidad_actual)

# Imprimir el valor de la información
print("Valor de la información para la decisión de comprar un auto:", valor_info_comprar_auto)
