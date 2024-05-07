""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Búsqueda informada --> Búsqueda de Ascensión de Colinas

Este código encuentra el máximo de una función objetivo utilizando la estrategia de 
búsqueda ascendente de colinas. Genera un punto inicial aleatorio en el dominio de la
función y luego explora vecinos cercanos, moviéndose hacia arriba si encuentra un vecino
con un valor más alto. Si no encuentra un vecino mejor después de un número limitado de
iteraciones, termina y devuelve el punto donde se encontró el máximo y su valor correspondiente."""

import random

def funcion_objetivo(x):
    # Función de ejemplo (puede ser cualquier función que deseemos maximizar)
    return -(x ** 2)  # Negamos el cuadrado para maximizar

def busqueda_ascendente_colinas(funcion_objetivo, limite_iteraciones=1000, paso=0.01):
    # Empezamos desde un punto aleatorio en el dominio de la función
    x_actual = random.uniform(-10, 10)
    valor_actual = funcion_objetivo(x_actual)

    for _ in range(limite_iteraciones):
        # Generamos un nuevo punto vecino agregando un pequeño valor aleatorio al punto actual
        vecino = x_actual + random.uniform(-paso, paso)
        valor_vecino = funcion_objetivo(vecino)

        # Si el valor en el vecino es mayor, nos movemos hacia él
        if valor_vecino > valor_actual:
            x_actual = vecino
            valor_actual = valor_vecino

    return x_actual, valor_actual

# Ejemplo de uso
resultado_x, resultado_valor = busqueda_ascendente_colinas(funcion_objetivo)

print("Máximo encontrado en x =", resultado_x)
print("Valor máximo encontrado =", resultado_valor)
