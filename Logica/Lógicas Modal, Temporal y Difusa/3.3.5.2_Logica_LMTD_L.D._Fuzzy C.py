"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Lógicas Modal, Temporal y Difusa ---> Lógica Difusa---> Fuzzy CLIPS"""

import clips

# Crea un nuevo entorno CLIPS
environment = clips.Environment()

# Define las reglas difusas
environment.build('''
(defrule temperatura-alta
  (temperatura ?t&:(>= ?t 25))
  =>
  (assert (temperatura-alta))
)

(defrule temperatura-media
  (temperatura ?t&:(>= ?t 15&:(< ?t 25)))
  =>
  (assert (temperatura-media))
)

(defrule temperatura-baja
  (temperatura ?t&:(< ?t 15))
  =>
  (assert (temperatura-baja))
)

(defrule velocidad-alta
  (velocidad ?v&:(>= ?v 100))
  =>
  (assert (velocidad-alta))
)

(defrule velocidad-media
  (velocidad ?v&:(>= ?v 50&:(< ?v 100)))
  =>
  (assert (velocidad-media))
)

(defrule velocidad-baja
  (velocidad ?v&:(< ?v 50))
  =>
  (assert (velocidad-baja))
)
''')

# Inserta hechos de prueba
environment.assert_string('(temperatura 20)')
environment.assert_string('(velocidad 80)')

# Ejecuta el motor de inferencia
environment.run()

# Obtiene los resultados
temperatura_result = environment.find_fact('temperatura-alta') or \
                     environment.find_fact('temperatura-media') or \
                     environment.find_fact('temperatura-baja')

velocidad_result = environment.find_fact('velocidad-alta') or \
                   environment.find_fact('velocidad-media') or \
                   environment.find_fact('velocidad-baja')

# Imprime los resultados
print("Temperatura:", temperatura_result[1].name)
print("Velocidad:", velocidad_result[1].name)
