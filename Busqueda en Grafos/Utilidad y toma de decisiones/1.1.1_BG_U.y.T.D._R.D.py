"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en grafos ---> Utilidad y Toma de Decisiones--->Redes de Decisión
Este programa define una red de decisión con varios nodos de decisión y nodos de resultado.
Cada nodo de decisión tiene opciones disponibles, y cada opción conduce a un resultado.
La función calcular_utilidad calcula la utilidad total de una secuencia de decisiones.
Finalmente, se toman algunas decisiones y se calcula la utilidad total resultante."""

class NodoDecision:
    def __init__(self, nombre, utilidad=None):
        self.nombre = nombre  # Nombre del nodo de decisión
        self.utilidad = utilidad  # Utilidad asociada al tomar esta decisión
        self.opciones = {}  # Opciones disponibles para tomar decisiones
        self.resultados = {}  # Resultados asociados a cada opción

    def agregar_opcion(self, opcion, resultado):
        self.opciones[opcion] = resultado  # Agregar una opción y su resultado asociado

    def tomar_decision(self, opcion):
        return self.opciones[opcion]  # Tomar una decisión y devolver el resultado asociado

class NodoResultado:
    def __init__(self, nombre, utilidad):
        self.nombre = nombre  # Nombre del nodo de resultado
        self.utilidad = utilidad  # Utilidad asociada a este resultado

# Construir la red de decisión
comprar_auto = NodoDecision("Comprar Auto")
comprar_auto.agregar_opcion("Sí", NodoResultado("Auto Nuevo", 20))
comprar_auto.agregar_opcion("No", NodoResultado("Sin Auto", 0))

comprar_casa = NodoDecision("Comprar Casa")
comprar_casa.agregar_opcion("Sí", NodoResultado("Casa Propia", 30))
comprar_casa.agregar_opcion("No", NodoResultado("Alquilar", 10))

viajar = NodoDecision("Viajar")
viajar.agregar_opcion("Sí", NodoResultado("Vacaciones", 15))
viajar.agregar_opcion("No", NodoResultado("En Casa", 5))

# Función para calcular la utilidad total de una secuencia de decisiones
def calcular_utilidad(decisiones):
    utilidad_total = 0
    for decision in decisiones:
        utilidad_total += decision.utilidad
    return utilidad_total

# Tomar decisiones y calcular la utilidad total
decisiones = [comprar_auto.tomar_decision("Sí"), comprar_casa.tomar_decision("Sí"), viajar.tomar_decision("Sí")]
utilidad_total = calcular_utilidad(decisiones)

# Imprimir la utilidad total calculada
print("Utilidad Total:", utilidad_total)

