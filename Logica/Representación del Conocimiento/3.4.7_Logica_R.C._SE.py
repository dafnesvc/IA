"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Representación del Conocimiento ---> Sistemas Expertos"""
import random

# Definimos la base de conocimiento como una lista de reglas
base_conocimiento = [
    ("tiene_fiebre", "tiene_gripe"),
    ("tiene_tos", "tiene_gripe"),
    ("tiene_fiebre", "tomar_paracetamol"),
    ("tiene_tos", "tomar_jarabe"),
]

# Definimos las reglas de producción como una función
def sistema_experto(sintomas):
    diagnostico = set()
    recomendaciones = set()
    
    # Aplicamos las reglas de la base de conocimiento
    for condicion, conclusion in base_conocimiento:
        if condicion in sintomas:
            diagnostico.add(conclusion)
            if conclusion.startswith("tomar_"):
                recomendaciones.add(conclusion.replace("tomar_", "").replace("_", " "))
    
    return diagnostico, recomendaciones

# Ejemplo de síntomas
sintomas_paciente = ["tiene_fiebre", "tiene_tos"]

# Ejecutamos el sistema experto
diagnostico, recomendaciones = sistema_experto(sintomas_paciente)

# Mostramos el diagnóstico y las recomendaciones
print("Diagnóstico:", diagnostico)
print("Recomendaciones:", recomendaciones)
