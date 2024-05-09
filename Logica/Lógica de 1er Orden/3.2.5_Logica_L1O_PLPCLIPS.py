"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica 1er Orden ---> Programación Lógica: Prolog y CLIPS"""

from pyswip import Prolog

# Inicializar el intérprete de Prolog
prolog = Prolog()

# Definir hechos y reglas en Prolog
prolog.assertz("hijo(juan, pedro)")
prolog.assertz("hijo(pedro, antonio)")
prolog.assertz("hijo(ana, pedro)")

prolog.assertz("hija(ana, pedro)")

# Consulta en Prolog
consulta = prolog.query("hijo(juan, pedro)")
print("¿Es Juan hijo de Pedro?", bool(list(consulta)))  # True si es hijo, False si no

consulta = prolog.query("hija(ana, pedro)")
print("¿Es Ana hija de Pedro?", bool(list(consulta)))  # True si es hija, False si no
