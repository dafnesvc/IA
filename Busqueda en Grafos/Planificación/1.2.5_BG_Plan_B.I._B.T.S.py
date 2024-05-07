""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Búsqueda no informada --> Busqueda de Template simulado."""

import random  # Importamos el módulo random para generar números aleatorios
import math    # Importamos el módulo math para funciones matemáticas

class TempleSimuladoTSP:
    def __init__(self, distancia_matrix, temperatura_inicial=1000, factor_enfriamiento=0.95, iteraciones_por_temp=100):
        # Constructor de la clase TempleSimuladoTSP
        # Inicializa los parámetros del algoritmo
        self.distancia_matrix = distancia_matrix  # Matriz de distancias entre ciudades
        self.num_ciudades = len(distancia_matrix)  # Número de ciudades en el problema
        self.temperatura_inicial = temperatura_inicial  # Temperatura inicial del temple simulado
        self.factor_enfriamiento = factor_enfriamiento  # Factor de enfriamiento por iteración
        self.iteraciones_por_temp = iteraciones_por_temp  # Número de iteraciones a realizar por temperatura

    def distancia_total(self, recorrido):
        # Calcula la distancia total de un recorrido dado
        distancia_total = 0
        for i in range(self.num_ciudades - 1):
            distancia_total += self.distancia_matrix[recorrido[i]][recorrido[i+1]]
        distancia_total += self.distancia_matrix[recorrido[-1]][recorrido[0]]  # Volver a la ciudad inicial
        return distancia_total

    def generar_vecino(self, recorrido):
        # Genera un vecino intercambiando dos ciudades aleatorias en el recorrido
        vecino = recorrido[:]
        i, j = random.sample(range(self.num_ciudades), 2)  # Seleccionamos dos índices aleatorios para intercambiar ciudades
        vecino[i], vecino[j] = vecino[j], vecino[i]  # Intercambiamos las ciudades
        return vecino

    def temple_simulado(self):
        # Implementación del algoritmo Temple Simulado para resolver el problema del TSP
        mejor_recorrido = list(range(self.num_ciudades))  # Generamos un recorrido inicial
        mejor_distancia = self.distancia_total(mejor_recorrido)  # Calculamos su distancia total

        temperatura_actual = self.temperatura_inicial  # Inicializamos la temperatura actual

        # Bucle principal del Temple Simulado
        while temperatura_actual > 1:
            for _ in range(self.iteraciones_por_temp):
                # Generamos un vecino y calculamos su distancia
                vecino = self.generar_vecino(mejor_recorrido)
                distancia_vecino = self.distancia_total(vecino)

                # Calculamos el delta (diferencia de distancias)
                delta = distancia_vecino - mejor_distancia

                # Si el vecino es mejor o se acepta según la probabilidad de aceptación, lo actualizamos
                if delta < 0 or random.random() < math.exp(-delta / temperatura_actual):
                    mejor_recorrido = vecino
                    mejor_distancia = distancia_vecino

            # Actualizamos la temperatura actual multiplicándola por el factor de enfriamiento
            temperatura_actual *= self.factor_enfriamiento

        return mejor_recorrido, mejor_distancia

# Ejemplo de uso
# Matriz de distancia entre ciudades (en este caso, una matriz de ejemplo)
distancia_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Crear una instancia de TempleSimuladoTSP y ejecutar el Temple Simulado
temple_simulado = TempleSimuladoTSP(distancia_matrix)
mejor_recorrido, mejor_distancia = temple_simulado.temple_simulado()

# Imprimir resultados
print("Mejor recorrido encontrado:", mejor_recorrido)
print("Distancia del mejor recorrido:", mejor_distancia)

#Donde la lista representa el orden de las ciudades visitadas en el recorrido y el valor numérico es la distancia total del recorrido.