"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Lógicas Modal, Temporal y Difusa ---> Lógica Temporal"""

import matplotlib.pyplot as plt

# Definición de los mundos posibles y sus relaciones de transición
worlds = {
    'w1': {'p': True, 'q': False},
    'w2': {'p': True, 'q': True},
    'w3': {'p': False, 'q': True},
    'w4': {'p': False, 'q': False}
}

# Definición de la relación de transición entre los mundos
transition_relations = {
    'w1': ['w2', 'w3'],
    'w2': ['w1', 'w4'],
    'w3': ['w2', 'w4'],
    'w4': ['w1', 'w3']
}

# Función para determinar si una fórmula temporal es verdadera en un mundo dado
def evaluate_formula(world, formula):
    if formula[0] == 'p':
        return worlds[world][formula[0]]
    elif formula[0] == 'q':
        return worlds[world][formula[0]]
    elif formula[0] == '¬':
        return not evaluate_formula(world, formula[1])
    elif formula[0] == 'X':
        return any(evaluate_formula(next_world, formula[1]) for next_world in transition_relations[world])
    elif formula[0] == 'F':
        return evaluate_formula(world, formula[1]) or any(evaluate_formula(next_world, ('F', formula[1])) for next_world in transition_relations[world])
    elif formula[0] == 'G':
        return evaluate_formula(world, formula[1]) and all(evaluate_formula(next_world, ('G', formula[1])) for next_world in transition_relations[world])
    elif formula[0] == 'U':
        return evaluate_formula(world, formula[2]) or (evaluate_formula(world, formula[1]) and any(evaluate_formula(next_world, ('U', formula[1], formula[2])) for next_world in transition_relations[world]))

# Definición de la fórmula temporal a evaluar
temporal_formula = ('F', ('p',))

# Evaluación de la fórmula temporal en cada mundo posible
results = {world: evaluate_formula(world, temporal_formula) for world in worlds}

# Visualización de los resultados utilizando Matplotlib
plt.figure(figsize=(6, 4))
plt.bar(results.keys(), [int(result) for result in results.values()], color=['green' if result else 'red' for result in results.values()])
plt.title('Evaluación de la Fórmula Temporal ' + str(temporal_formula))
plt.xlabel('Mundos Posibles')
plt.ylabel('Verdad')
plt.xticks(rotation=45)
plt.show()
