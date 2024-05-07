""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Búsqueda no informada --> Busqueda de haz local

 implementa el algoritmo de búsqueda de haz local para encontrar un máximo local de una función objetivo.
El tamaño del haz y el número máximo de iteraciones se pueden ajustar según sea necesario. La función objetivo 
y la generación de vecinos se pueden definir según el problema específico que se esté abordando"""

import random  # Importamos el módulo random para generar números aleatorios

class BusquedaHazLocal:
    def __init__(self, funcion_objetivo, generar_vecino, tamano_haz=10, iteraciones_maximas=1000):      
        # Constructor de la clase BusquedaHazLocal
        # funcion_objetivo: La función objetivo que queremos maximizar
        # generar_vecino: La función que genera un vecino aleatorio dado un estado
        # tamano_haz: El tamaño del haz (cantidad de estados candidatos a considerar en cada iteración)
        # iteraciones_maximas: El número máximo de iteraciones a realizar
        self.funcion_objetivo = funcion_objetivo
        self.generar_vecino = generar_vecino
        self.tamano_haz = tamano_haz
        self.iteraciones_maximas = iteraciones_maximas

    def busqueda_haz_local(self, estado_inicial):
        # Inicializamos el mejor estado y su valor
        mejor_estado = estado_inicial
        mejor_valor = self.funcion_objetivo(estado_inicial)

        iteracion = 0
        while iteracion < self.iteraciones_maximas:
            # Generamos un haz de estados vecinos aleatorios
            haz = [self.generar_vecino(mejor_estado) for _ in range(self.tamano_haz)]

            # Evaluamos la función objetivo en cada estado del haz
            valores = [self.funcion_objetivo(estado) for estado in haz]

            # Seleccionamos el mejor estado del haz
            indice_mejor = valores.index(max(valores))
            mejor_vecino = haz[indice_mejor]
            valor_mejor_vecino = valores[indice_mejor]

            # Actualizamos el mejor estado y su valor si es mejor que el actual
            if valor_mejor_vecino > mejor_valor:
                mejor_estado = mejor_vecino
                mejor_valor = valor_mejor_vecino

            iteracion += 1

        return mejor_estado, mejor_valor

# Ejemplo de uso
# Definimos una función objetivo de ejemplo (puede ser cualquier función que deseemos maximizar)
def funcion_objetivo(x):
    # En este ejemplo, maximizamos una función cuadrática
    return -(x ** 2)  # Negamos el cuadrado para maximizar

# Definimos una función que genera un vecino aleatorio (en este caso, sumando o restando un pequeño valor)
def generar_vecino(estado):
    return estado + random.uniform(-0.1, 0.1)

# Creamos una instancia de BusquedaHazLocal y ejecutamos la búsqueda
busqueda_haz_local = BusquedaHazLocal(funcion_objetivo, generar_vecino)
mejor_estado, mejor_valor = busqueda_haz_local.busqueda_haz_local(0)

# Imprimimos el resultado
print("Mejor estado encontrado:", mejor_estado)
print("Valor del mejor estado:", mejor_valor)

