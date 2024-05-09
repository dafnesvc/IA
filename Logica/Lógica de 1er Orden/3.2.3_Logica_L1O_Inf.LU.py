"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica 1er Orden ---> Inferencia Lógica: Unificación"""

import networkx as nx
import matplotlib.pyplot as plt

def unify(term1, term2):
    """
    Función para unificar dos términos lógicos.

    Args:
    - term1: Primer término a unificar.
    - term2: Segundo término a unificar.

    Returns:
    - Unificación de los términos.
    """
    # Verificar si los términos son iguales
    if term1 == term2:
        return term1

    # Si uno de los términos es una variable, unificarlo con el otro término
    elif isinstance(term1, str):
        return term2

    elif isinstance(term2, str):
        return term1

    # Si ambos términos son compuestos, unificar recursivamente
    elif isinstance(term1, tuple) and isinstance(term2, tuple):
        head1, *tail1 = term1
        head2, *tail2 = term2
        unified_head = unify(head1, head2)
        unified_tail = unify(tuple(tail1), tuple(tail2))
        if unified_head is None or unified_tail is None:
            return None
        else:
            return (unified_head,) + unified_tail

    # Si ninguno de los casos anteriores se cumple, los términos no se pueden unificar
    else:
        return None

# Definir términos lógicos para unificar
term1 = ("padre", "X", "Y")
term2 = ("padre", "Juan", "Maria")

# Realizar la unificación
unified_term = unify(term1, term2)

# Mostrar el resultado de la unificación
print("Resultado de la unificación:", unified_term)

# Crear un grafo dirigido para visualizar la unificación
G = nx.DiGraph()
G.add_nodes_from([str(term1), str(term2), str(unified_term)])
G.add_edges_from([(str(term1), str(unified_term)), (str(term2), str(unified_term))])

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=12, font_weight="bold", arrowsize=20)

# Mostrar el grafo
plt.title("Unificación de Términos Lógicos")
plt.show()
