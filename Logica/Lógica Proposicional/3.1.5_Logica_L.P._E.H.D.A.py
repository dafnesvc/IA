"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica Proposicional---> Encadenamiento: Hacia Delante y Atrás"""

import matplotlib.pyplot as plt
import networkx as nx

def encadenamiento_hacia_adelante(hechos_iniciales, reglas):
    """
    Implementa el algoritmo de encadenamiento hacia adelante.
    """
    agenda = hechos_iniciales.copy()  # Inicializar la agenda con los hechos iniciales
    while agenda:
        hecho_actual = agenda.pop(0)
        print("Analizando hecho:", hecho_actual)
        for regla in reglas:
            if all(premisa in hecho_actual for premisa in regla[0]):
                nuevo_hecho = regla[1]
                if nuevo_hecho not in agenda:
                    agenda.append(nuevo_hecho)
                    print("Se ha inferido:", nuevo_hecho)
    return agenda

def encadenamiento_hacia_atras(hechos_finales, reglas):
    """
    Implementa el algoritmo de encadenamiento hacia atrás.
    """
    agenda = hechos_finales.copy()  # Inicializar la agenda con los hechos finales
    while agenda:
        hecho_actual = agenda.pop(0)
        print("Analizando hecho:", hecho_actual)
        for regla in reglas:
            if hecho_actual == regla[1]:
                premisas = regla[0]
                for premisa in premisas:
                    if premisa not in agenda:
                        agenda.append(premisa)
                        print("Se ha inferido:", premisa)
    return agenda

# Definir las reglas y hechos iniciales/finales
reglas = [(['a'], 'b'), (['b'], 'c'), (['c'], 'd'), (['d'], 'e'), (['e'], 'f')]
hechos_iniciales = ['a']
hechos_finales = ['f']

# Aplicar encadenamiento hacia adelante y hacia atrás
hechos_inferidos_adelante = encadenamiento_hacia_adelante(hechos_iniciales, reglas)
hechos_inferidos_atras = encadenamiento_hacia_atras(hechos_finales, reglas)

# Visualización gráfica
G = nx.DiGraph()

# Agregar nodos
for hecho in hechos_iniciales + hechos_finales + hechos_inferidos_adelante + hechos_inferidos_atras:
    G.add_node(hecho)

# Agregar aristas
for regla in reglas:
    for premisa in regla[0]:
        G.add_edge(premisa, regla[1])

# Visualizar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold")
plt.title("Grafo de Encadenamiento Lógico")
plt.show()
