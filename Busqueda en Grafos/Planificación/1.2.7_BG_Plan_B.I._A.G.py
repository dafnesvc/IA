""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Búsqueda informada --> Algoritmos Genéticos
Este código implementa un algoritmo genético para resolver el Problema del Viajante (TSP),
donde se busca encontrar la ruta más corta que visite todas las ciudades exactamente una vez
y regrese al punto de partida. """

import random

class GeneticoTSP:
    def __init__(self, ciudades, distancias, tamano_poblacion=100, prob_mutacion=0.1, elitismo=True):
        self.ciudades = ciudades
        self.distancias = distancias
        self.tamano_poblacion = tamano_poblacion
        self.prob_mutacion = prob_mutacion
        self.elitismo = elitismo

    def generar_ruta_aleatoria(self):
        # Genera una ruta aleatoria que visita todas las ciudades exactamente una vez
        return random.sample(self.ciudades, len(self.ciudades))

    def calcular_distancia_total(self, ruta):
        # Calcula la distancia total de una ruta dada
        distancia_total = 0
        for i in range(len(ruta)):
            ciudad_actual = ruta[i]
            ciudad_siguiente = ruta[(i + 1) % len(ruta)]  # Para cerrar el ciclo
            distancia_total += self.distancias[ciudad_actual][ciudad_siguiente]
        return distancia_total

    def generar_poblacion_inicial(self):
        # Genera una población inicial de rutas aleatorias
        poblacion = []
        for _ in range(self.tamano_poblacion):
            ruta = self.generar_ruta_aleatoria()
            poblacion.append(ruta)
        return poblacion

    def cruzar_padres(self, padre1, padre2):
        # Cruza dos padres para producir un hijo
        punto_corte = random.randint(0, len(padre1) - 1)
        hijo = padre1[:punto_corte]
        for ciudad in padre2:
            if ciudad not in hijo:
                hijo.append(ciudad)
        return hijo

    def mutar_ruta(self, ruta):
        # Realiza una mutación en una ruta con una cierta probabilidad
        if random.random() < self.prob_mutacion:
            indices = random.sample(range(len(ruta)), 2)
            ruta[indices[0]], ruta[indices[1]] = ruta[indices[1]], ruta[indices[0]]
        return ruta

    def seleccionar_padres(self, poblacion):
        # Selecciona los padres para la próxima generación basados en la ruleta
        padres = random.choices(poblacion, k=2)
        return padres

    def generar_siguiente_generacion(self, poblacion):
        # Genera la próxima generación de rutas
        nueva_generacion = []

        if self.elitismo:
            poblacion.sort(key=self.calcular_distancia_total)
            nueva_generacion.append(poblacion[0])  # Conserva al mejor individuo

        while len(nueva_generacion) < self.tamano_poblacion:
            padre1, padre2 = self.seleccionar_padres(poblacion)
            hijo = self.cruzar_padres(padre1, padre2)
            hijo = self.mutar_ruta(hijo)
            nueva_generacion.append(hijo)

        return nueva_generacion

    def encontrar_mejor_ruta(self, generaciones):
        # Encuentra la mejor ruta después de un número dado de generaciones
        poblacion = self.generar_poblacion_inicial()
        for _ in range(generaciones):
            poblacion = self.generar_siguiente_generacion(poblacion)
        mejor_ruta = min(poblacion, key=self.calcular_distancia_total)
        return mejor_ruta

# Ejemplo de uso
# Definir ciudades y distancias entre ellas
ciudades = ['A', 'B', 'C', 'D']
distancias = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

# Crear una instancia de GeneticoTSP y ejecutar el algoritmo genético
genetico = GeneticoTSP(ciudades, distancias)
mejor_ruta = genetico.encontrar_mejor_ruta(generaciones=1000)

# Imprimir la mejor ruta encontrada
print("Mejor ruta encontrada:", mejor_ruta)
print("Distancia total:", genetico.calcular_distancia_total(mejor_ruta))
