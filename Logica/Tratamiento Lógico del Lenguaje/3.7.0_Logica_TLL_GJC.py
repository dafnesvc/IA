"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Tratamiento Lógico del Lenguaje ---> Gramáticas: Jerarquía de Chomsky"""

import nltk
import matplotlib.pyplot as plt

# Definir una gramática libre de contexto
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V | V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'boy' | 'girl' | 'dog' | 'cat'
    V -> 'chased' | 'saw' | 'bit' | 'loved'
    P -> 'with' | 'in'
""")

# Crear un parser para la gramática
parser = nltk.ChartParser(grammar)

# Obtener todas las producciones de la gramática
productions = grammar.productions()

# Visualizar las producciones de la gramática
print("Producciones de la gramática:")
for production in productions:
    print(production)

# Generar algunas cadenas de texto a partir de la gramática
sentences = [
    "the boy chased the dog",
    "a girl saw a cat with a telescope",
    "a dog bit a girl in the park"
]

# Parsear las cadenas de texto
for sentence in sentences:
    print("\nAnalizando la oración:", sentence)
    for tree in parser.parse(sentence.split()):
        print(tree)

# Visualizar una producción de la gramática
nltk.draw.Tree.fromstring("(S (NP (Det the) (N boy)) (VP (V chased) (NP (Det the) (N dog))))").pretty_print()

# Visualizar otra producción de la gramática
nltk.draw.Tree.fromstring("(S (NP (Det a) (N girl)) (VP (V saw) (NP (Det a) (N cat) (PP (P with) (NP (Det a) (N telescope))))))").pretty_print()

# Visualizar otra producción de la gramática
nltk.draw.Tree.fromstring("(S (NP (Det a) (N dog)) (VP (V bit) (NP (Det a) (N girl) (PP (P in) (NP (Det the) (N park))))))").pretty_print()
