"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica Proposicional---> Resolución y Forma Normal Conjuntiva
Este código implementa el algoritmo de resolución y la conversión a Forma Normal Conjuntiva (FNC)
de un conjunto de cláusulas proposicionales. También verifica si las cláusulas están en FNC y si son 
satisfacibles. """

import matplotlib.pyplot as plt
import networkx as nx

def resolucion(clausula1, clausula2):
    """
    Realiza la resolución de dos cláusulas.
    """
    for literal in clausula1:
        if literal[0] == '-':
            complemento = literal[1:]
        else:
            complemento = '-' + literal
        if complemento in clausula2:
            nueva_clausula = [lit for lit in clausula1 if lit != literal] + [lit for lit in clausula2 if lit != complemento]
            return nueva_clausula
    return None

def forma_normal_conjuntiva(clausulas):
    """
    Convierte una lista de cláusulas en Forma Normal Conjuntiva (FNC).
    """
    nuevas_clausulas = clausulas[:]
    for i in range(len(nuevas_clausulas)):
        for j in range(i + 1, len(nuevas_clausulas)):
            res = resolucion(nuevas_clausulas[i], nuevas_clausulas[j])
            if res is not None:
                if len(res) == 0:
                    return True  # La resolución da una cláusula vacía, lo que significa que es insatisfacible
                nuevas_clausulas.append(res)
    return False  # No se encontró ninguna cláusula vacía, por lo que es satisfacible

# Clausulas de ejemplo
clausulas = [['P', 'Q'], ['P', '-Q'], ['-P', 'R'], ['-R']]

# Verificar si las clausulas están en FNC y si son satisfacibles
es_fnc = forma_normal_conjuntiva(clausulas)

# Mostrar el resultado
if es_fnc:
    print("Las cláusulas están en Forma Normal Conjuntiva (FNC) y son satisfacibles.")
else:
    print("Las cláusulas no están en Forma Normal Conjuntiva (FNC) o no son satisfacibles.")
