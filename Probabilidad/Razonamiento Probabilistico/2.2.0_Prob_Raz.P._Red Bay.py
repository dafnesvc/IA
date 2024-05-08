"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razonamiento Probabilístico--->Red Bayesiana

Este script generará un grafo dirigido que representa una Red Bayesiana básica 
y lo visualizará utilizando matplotlib."""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo dirigido para representar la Red Bayesiana
red_bayesiana = nx.DiGraph()

# Definir los nodos de la red
nodos = ['A', 'B', 'C', 'D', 'E']

# Añadir los nodos al grafo
red_bayesiana.add_nodes_from(nodos)

# Definir las conexiones entre los nodos (aristas)
aristas = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('B', 'D')]

# Añadir las aristas al grafo
red_bayesiana.add_edges_from(aristas)

# Dibujar la Red Bayesiana
pos = nx.spring_layout(red_bayesiana)  # Calcular la disposición de los nodos
nx.draw(red_bayesiana, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', arrowsize=20)
plt.title('Red Bayesiana')
plt.show()

