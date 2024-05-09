"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Lógicas Modal, Temporal y Difusa ---> Lógica Modal"""
import matplotlib.pyplot as plt

# Definición de los mundos posibles y sus relaciones
worlds = {
    'w1': {'p': True, 'q': False},
    'w2': {'p': True, 'q': True},
    'w3': {'p': False, 'q': True},
    'w4': {'p': False, 'q': False}
}

# Definición de la relación de accesibilidad entre los mundos
accessibility_relations = {
    'w1': ['w1', 'w2', 'w4'],
    'w2': ['w1', 'w2', 'w3'],
    'w3': ['w2', 'w3', 'w4'],
    'w4': ['w1', 'w3', 'w4']
}

# Función para determinar si una fórmula modal es verdadera en un mundo dado
def evaluate_formula(world, formula):
    if formula[0] == 'p':
        return worlds[world][formula[0]]
    elif formula[0] == 'q':
        return worlds[world][formula[0]]
    elif formula[0] == '¬':
        return not evaluate_formula(world, formula[1])
    elif formula[0] == '□':
        return all(evaluate_formula(w, formula[1]) for w in accessibility_relations[world])
    elif formula[0] == '◊':
        return any(evaluate_formula(w, formula[1]) for w in accessibility_relations[world])

# Definición de la fórmula modal a evaluar
modal_formula = ('□', ('p',))

# Evaluación de la fórmula modal en cada mundo posible
results = {world: evaluate_formula(world, modal_formula) for world in worlds}

# Visualización de los resultados utilizando Matplotlib
plt.figure(figsize=(6, 4))
plt.bar(results.keys(), [int(result) for result in results.values()], color=['green' if result else 'red' for result in results.values()])
plt.title('Evaluación de la Fórmula Modal ' + str(modal_formula))
plt.xlabel('Mundos Posibles')
plt.ylabel('Verdad')
plt.xticks(rotation=45)
plt.show()
