"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Tratamiento Lógico del Lenguaje ---> Gramática Causal Definida"""

import matplotlib.pyplot as plt

# Definimos una lista de eventos con sus relaciones causales
relaciones_causales = {
    "A": [("B", 0.8), ("C", 0.5)],  # El evento A causa los eventos B y C con ciertas probabilidades
    "B": [("D", 0.7)],              # El evento B causa el evento D con cierta probabilidad
    "C": [("D", 0.4)],              # El evento C causa el evento D con cierta probabilidad
    "D": []                          # El evento D no causa otros eventos
}

# Función para visualizar el grafo de relaciones causales
def visualizar_grafo(relaciones_causales):
    plt.figure(figsize=(8, 6))
    for evento, relaciones in relaciones_causales.items():
        for relacion in relaciones:
            destino, probabilidad = relacion
            plt.arrow(evento, destino, head_width=0.05, head_length=0.1, length_includes_head=True, label=f"{probabilidad:.2f}")
    plt.xlabel('Evento Causante')
    plt.ylabel('Evento Causado')
    plt.title('Grafo de Relaciones Causales')
    plt.grid(True)
    plt.show()

# Mostramos el grafo de relaciones causales
visualizar_grafo(relaciones_causales)
