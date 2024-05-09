"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica Proposicional--->Sintaxis y Semántica: Tablas de Verdad"""
import numpy as np
import matplotlib.pyplot as plt

# Función para evaluar una expresión lógica dada una lista de valores de entrada
def evaluate_expression(expression, values):
    truth_values = []
    for v in values:
        truth_values.append(eval(expression, {'__builtins__': None}, {'x': v}))
    return truth_values

# Función para generar una tabla de verdad para una expresión lógica dada
def generate_truth_table(expression):
    values = np.array([0, 1])
    truth_table = np.array([values, evaluate_expression(expression, values)])
    return truth_table

# Función para visualizar la tabla de verdad
def plot_truth_table(truth_table, expression):
    plt.figure(figsize=(5, 3))
    plt.axis('off')
    plt.title(f'Tabla de verdad para {expression}')
    plt.table(cellText=truth_table.T, colLabels=['x', expression], loc='center')
    plt.show()

# Expresión lógica a evaluar
expression = 'not x or x'

# Generar y visualizar la tabla de verdad
truth_table = generate_truth_table(expression)
plot_truth_table(truth_table, expression)
