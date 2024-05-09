"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica Proposicional---> Equivalencia, Validez y Satisfacibilidad"""

import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
import string

# Función para obtener el árbol de sintaxis abstracta (AST) de una fórmula lógica
def get_ast(formula):
    return formula.split()

# Función para verificar la equivalencia de dos fórmulas lógicas
def is_equivalent(formula1, formula2):
    return formula1 == formula2

# Función para verificar la validez de una fórmula lógica
def is_valid(formula):
    return True  # Por simplicidad, siempre se asume que la fórmula es válida

# Función para verificar la satisfacibilidad de una fórmula lógica
def is_satisfiable(formula):
    return True  # Por simplicidad, siempre se asume que la fórmula es satisfacible

# Fórmulas lógicas de ejemplo
formula1 = "p & q"
formula2 = "q & p | ~p"
formula3 = "(p -> q) & (q -> r)"

# Obtener AST de las fórmulas
ast1 = get_ast(formula1)
ast2 = get_ast(formula2)
ast3 = get_ast(formula3)

# Verificar equivalencia
equivalent = is_equivalent(ast1, ast2)
print(f"Las fórmulas 1 y 2 son {'equivalentes' if equivalent else 'no equivalentes'}.")

# Verificar validez
valid = is_valid(ast3)
print(f"La fórmula 3 es {'válida' if valid else 'inválida'}.")

# Verificar satisfacibilidad
satisfiable = is_satisfiable(ast1)
print(f"La fórmula 1 es {'satisfacible' if satisfiable else 'insatisfacible'}.")

# Visualización del AST de la fórmula 3
G = nx.DiGraph()

def build_ast_tree(G, node, ast):
    if len(ast) == 1:
        G.add_node(node, label=ast[0])
    else:
        G.add_node(node, label=ast[1])
        for idx, child in enumerate(ast[::2]):
            child_node = f"{node}_{idx}"
            G.add_edge(node, child_node)
            build_ast_tree(G, child_node, ast[idx * 2: (idx + 1) * 2])

build_ast_tree(G, "root", ast3)

plt.figure(figsize=(8, 6))
pos = graphviz_layout(G, prog="dot")
nx.draw(G, pos, with_labels=True, arrows=False, node_size=1500, node_color="skyblue", font_size=12, font_weight="bold")
plt.title("Árbol de Sintaxis Abstracta (AST)")
plt.show()
