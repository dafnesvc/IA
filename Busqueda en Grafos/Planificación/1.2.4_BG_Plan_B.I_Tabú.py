""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Búsqueda informada --> Tabú
El objetivo de este código es resolver el problema del Viajante de Comercio (TSP)
utilizando el algoritmo de búsqueda tabú. El TSP es un problema de optimización
combinatoria en el que se busca encontrar el recorrido más corto que visite cada 
ciudad exactamente una vez y regrese al punto de partida."""

import random

class TabuSearchTSP:
    def __init__(self, distancia_matrix, tamano_tabu=10, iteraciones_maximas=1000):
        self.distancia_matrix = distancia_matrix
        self.num_ciudades = len(distancia_matrix)
        self.tamano_tabu = tamano_tabu
        self.iteraciones_maximas = iteraciones_maximas

    def inicializar_solucion(self):
        # Genera una solución inicial aleatoria
        return random.sample(range(self.num_ciudades), self.num_ciudades)

    def evaluar_solucion(self, solucion):
        # Calcula la distancia total de la solución dada
        distancia_total = 0
        for i in range(self.num_ciudades - 1):
            distancia_total += self.distancia_matrix[solucion[i]][solucion[i+1]]
        distancia_total += self.distancia_matrix[solucion[-1]][solucion[0]]  # Volver a la ciudad inicial
        return distancia_total

    def generar_vecindario(self, solucion):
        # Genera vecinos intercambiando dos ciudades en la solución actual
        vecindario = []
        for i in range(self.num_ciudades):
            for j in range(i + 1, self.num_ciudades):
                vecino = solucion[:]
                vecino[i], vecino[j] = vecino[j], vecino[i]
                vecindario.append(vecino)
        return vecindario

    def buscar_mejor_vecino(self, solucion_actual, tabu_list):
        mejor_vecino = None
        mejor_valor = float('inf')

        vecindario = self.generar_vecindario(solucion_actual)
        for vecino in vecindario:
            valor_vecino = self.evaluar_solucion(vecino)
            if valor_vecino < mejor_valor and vecino not in tabu_list:
                mejor_vecino = vecino
                mejor_valor = valor_vecino

        return mejor_vecino, mejor_valor

    def busqueda_tabu(self):
        solucion_actual = self.inicializar_solucion()
        mejor_solucion = solucion_actual[:]
        mejor_valor = self.evaluar_solucion(mejor_solucion)
        tabu_list = []

        iteracion = 0
        while iteracion < self.iteraciones_maximas:
            mejor_vecino, valor_vecino = self.buscar_mejor_vecino(solucion_actual, tabu_list)

            if mejor_vecino is None:
                break

            solucion_actual = mejor_vecino
            if valor_vecino < mejor_valor:
                mejor_solucion = solucion_actual[:]
                mejor_valor = valor_vecino

            tabu_list.append(solucion_actual)
            if len(tabu_list) > self.tamano_tabu:
                tabu_list.pop(0)

            iteracion += 1

        return mejor_solucion, mejor_valor

# Ejemplo de uso    
# Matriz de distancia entre ciudades (en este caso, una matriz de ejemplo)
distancia_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Crear una instancia de TabuSearchTSP y ejecutar la búsqueda tabú
tabu_search = TabuSearchTSP(distancia_matrix)
mejor_solucion, mejor_valor = tabu_search.busqueda_tabu()

print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la mejor solución:", mejor_valor)
