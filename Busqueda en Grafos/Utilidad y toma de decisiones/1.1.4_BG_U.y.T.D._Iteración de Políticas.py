"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en grafos ---> Utilidad y Toma de Decisiones--->Iteración de Políticas"""

class Estado:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del estado
        self.utilidad = 0  # Utilidad del estado
        self.transiciones = {}  # Transiciones desde este estado

    def agregar_transicion(self, accion, estado_siguiente, probabilidad):
        """
        Agrega una transición desde este estado a otro estado con una acción y una probabilidad dada.
        """
        if accion not in self.transiciones:
            self.transiciones[accion] = []
        self.transiciones[accion].append((estado_siguiente, probabilidad))


def iteracion_politicas(estados, acciones, gamma=0.9, epsilon=0.01):
    """
    Implementa el algoritmo de Iteración de Políticas para encontrar la política óptima.
    """
    # Inicializar la política
    politica = {estado: acciones[0] for estado in estados}

    while True:
        delta = 0
        # Para cada estado en el conjunto de estados
        for estado in estados:
            # Calcular la utilidad actual del estado
            utilidad_actual = estado.utilidad
            # Calcular la utilidad máxima y la acción óptima para el estado
            max_utilidad = float("-inf")
            mejor_accion = None
            for accion in acciones:
                if accion in estado.transiciones:
                    utilidad_accion = sum(prob * (estado_siguiente.utilidad * gamma) for estado_siguiente, prob in estado.transiciones[accion])
                    if utilidad_accion > max_utilidad:
                        max_utilidad = utilidad_accion
                        mejor_accion = accion
            # Actualizar la utilidad del estado y la política si es necesario
            estado.utilidad = max_utilidad
            politica[estado] = mejor_accion
            delta = max(delta, abs(utilidad_actual - estado.utilidad))
        # Si la diferencia entre las utilidades de dos iteraciones consecutivas es menor que epsilon, terminar
        if delta < epsilon:
            break

    return politica


# Definir los estados y sus transiciones
estado_A = Estado("A")
estado_B = Estado("B")
estado_C = Estado("C")

estado_A.agregar_transicion("Ir a B", estado_B, 0.8)
estado_A.agregar_transicion("Ir a C", estado_C, 0.2)
estado_A.agregar_transicion("Ir a A", estado_A, 0.0)  # Agregar transición a sí mismo con probabilidad 0

estado_B.agregar_transicion("Ir a A", estado_A, 0.5)
estado_B.agregar_transicion("Ir a C", estado_C, 0.5)
estado_B.agregar_transicion("Ir a B", estado_B, 0.0)  # Agregar transición a sí mismo con probabilidad 0

estado_C.agregar_transicion("Ir a A", estado_A, 0.7)
estado_C.agregar_transicion("Ir a B", estado_B, 0.3)
estado_C.agregar_transicion("Ir a C", estado_C, 0.0)  # Agregar transición a sí mismo con probabilidad 0

# Definir el conjunto de estados y acciones
estados = [estado_A, estado_B, estado_C]
acciones = ["Ir a A", "Ir a B", "Ir a C"]

# Ejecutar la iteración de políticas para encontrar la política óptima
politica_optima = iteracion_politicas(estados, acciones)

# Imprimir la política óptima encontrada
for estado, accion in politica_optima.items():
    print(f"Para el estado {estado.nombre}, tomar la acción: {accion}")

