"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica 1er Orden ---> Resolución: Skolem"""

from sympy import symbols, Not, Or, And
from sympy.logic.boolalg import to_cnf

def skolemization(sentence):
    """
    Realiza la skolemización de una sentencia lógica.
    """
    # Convertir a forma clausal
    cnf_sentence = to_cnf(sentence)

    # Símbolos existenciales
    existential_symbols = set()

    # Obtener todos los símbolos existenciales
    for sub_expr in cnf_sentence.args:
        if isinstance(sub_expr, Or):
            for arg in sub_expr.args:
                if isinstance(arg, Not):
                    existential_symbols.add(arg.args[0])
        elif isinstance(sub_expr, Not):
            existential_symbols.add(sub_expr.args[0])

    # Funciones Skolem
    skolem_funcs = {symbol: symbols(f'sk_{symbol}') for symbol in existential_symbols}

    # Sustituir símbolos existenciales por funciones Skolem
    skolemized_sentence = cnf_sentence.subs(skolem_funcs)

    return skolemized_sentence

# Ejemplo de uso
p, q, r = symbols('p q r')
sentence = Or(p, Not(q), Or(Not(r), q))
skolemized_sentence = skolemization(sentence)
print("Sentencia lógica original:", sentence)
print("Sentencia lógica skolemizada:", skolemized_sentence)
