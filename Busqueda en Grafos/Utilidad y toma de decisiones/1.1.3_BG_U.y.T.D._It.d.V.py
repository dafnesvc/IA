"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en grafos ---> Utilidad y Toma de Decisiones--->Iteración de Valores"""

class NodoDecision:
    def __init__(self, nombre, utilidad):
        self.nombre = nombre  # Nombre del nodo de decisión
        self.utilidad = utilidad  # Utilidad asociada al elegir este nodo

def iteracion_valores(nodos_decision, descuentos, epsilon=0.01):
    # Inicializar las utilidades de todos los nodos a 0
    utilidades_previas = {nodo: 0 for nodo in nodos_decision}
    
    while True:
        # Crear un diccionario para almacenar las nuevas utilidades calculadas
        nuevas_utilidades = {}
        
        # Para cada nodo de decisión, calcular su nueva utilidad
        for nodo in nodos_decision:
            # Calcular la utilidad máxima para este nodo
            utilidad_maxima = max(calcular_utilidad(nodo, utilidades_previas, descuentos) for nodo in nodos_decision)
            
            # Actualizar el diccionario de nuevas utilidades
            nuevas_utilidades[nodo] = utilidad_maxima
        
        # Verificar si las nuevas utilidades convergen
        if all(abs(nuevas_utilidades[nodo] - utilidades_previas[nodo]) < epsilon for nodo in nodos_decision):
            break
        
        # Actualizar las utilidades previas con las nuevas utilidades calculadas
        utilidades_previas = nuevas_utilidades.copy()
    
    return utilidades_previas

def calcular_utilidad(nodo, utilidades_previas, descuentos):
    # Si el nodo de decisión tiene una utilidad definida, retornarla directamente
    if isinstance(nodo.utilidad, (int, float)):
        return nodo.utilidad
    
    # Si el nodo de decisión tiene una función para calcular la utilidad
    # Llamar a esa función con las utilidades previas y los descuentos
    elif callable(nodo.utilidad):
        return nodo.utilidad(utilidades_previas, descuentos)

# Definir los nodos de decisión y sus utilidades
comprar_auto = NodoDecision("Comprar Auto", 0)
nodos_decision = [comprar_auto]

# Definir los descuentos para cada iteración
descuentos = [0.9, 0.9]  # Descuentos para las dos iteraciones

# Realizar la iteración de valores para calcular las utilidades finales
utilidades_finales = iteracion_valores(nodos_decision, descuentos)

# Imprimir las utilidades finales calculadas para cada nodo de decisión
for nodo, utilidad in utilidades_finales.items():
    print(f"Utilidad de '{nodo.nombre}': {utilidad}")

