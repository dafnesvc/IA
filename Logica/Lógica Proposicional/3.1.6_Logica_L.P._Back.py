"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica Proposicional---> Backtracking
Este script resuelve el problema de las 8 reinas utilizando el algoritmo de backtracking 
y muestra la solución encontrada en un tablero de ajedrez visualizado con Matplotlib."""

import matplotlib.pyplot as plt

def es_solucion(estado):
    """
    Verifica si el estado actual es una solución válida.
    """
    # En este ejemplo, la solución es una lista de números del 1 al 8 sin repeticiones
    return len(estado) == 8 and len(set(estado)) == 8

def es_valido(estado, fila, col):
    """
    Verifica si agregar una reina en la posición (fila, col) es válida en el estado actual.
    """
    for i in range(len(estado)):
        if estado[i] == col or abs(i - fila) == abs(estado[i] - col):
            return False
    return True

def backtracking(estado):
    """
    Implementa el algoritmo de backtracking para resolver el problema de las 8 reinas.
    """
    if es_solucion(estado):
        return estado
    
    for col in range(8):
        if es_valido(estado, len(estado), col):
            estado.append(col)
            resultado = backtracking(estado)
            if resultado is not None:
                return resultado
            estado.pop()
    return None

def visualizar_tablero(solucion):
    """
    Visualiza el tablero con la solución encontrada.
    """
    tablero = [[0] * 8 for _ in range(8)]
    for fila, col in enumerate(solucion):
        tablero[fila][col] = 1

    plt.imshow(tablero, cmap='binary')
    plt.title('Solución del problema de las 8 reinas')
    plt.xticks([])
    plt.yticks([])
    plt.show()

# Ejecutar el algoritmo de backtracking
solucion = backtracking([])
if solucion:
    print("Solución encontrada:", solucion)
    visualizar_tablero(solucion)
else:
    print("No se encontró solución.")
