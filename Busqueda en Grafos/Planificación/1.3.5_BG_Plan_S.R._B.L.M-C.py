""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Satisfacción de restricciones--> Búsqueda Local: Mínimos-Conflictos
Este algoritmo busca una asignación de valores a las variables que satisfaga todas las restricciones del problema
minimizando el número de conflictos, es decir, la cantidad de restricciones violadas."""

import random

class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables del problema
        self.dominios = dominios    # Diccionario de dominios para cada variable
        self.restricciones = restricciones  # Lista de restricciones entre las variables

    def minimos_conflictos_search(self, max_iter=100):
        asignacion = {var: random.choice(self.dominios[var]) for var in self.variables}  # Asignación inicial aleatoria
        for _ in range(max_iter):
            if self.consistente(asignacion):  # Si la asignación es consistente, retornarla
                return asignacion
            conflicto_vars = self.obtener_conflictos(asignacion)  # Obtener variables en conflicto
            var = random.choice(conflicto_vars)  # Seleccionar una variable en conflicto aleatoriamente
            valor = self.min_conflict_value(var, asignacion)  # Asignar el valor con el mínimo conflicto
            asignacion[var] = valor
        return None  # Si no se encuentra solución después de un número máximo de iteraciones, retornar None

    def min_conflict_value(self, var, asignacion):
        min_conflictos = float('inf')
        mejor_valor = None
        for valor in self.dominios[var]:
            asignacion[var] = valor
            conflictos = self.num_conflictos(var, asignacion)
            if conflictos < min_conflictos:
                min_conflictos = conflictos
                mejor_valor = valor
        return mejor_valor

    def obtener_conflictos(self, asignacion):
        conflictos_vars = []
        for var in self.variables:
            conflictos = self.num_conflictos(var, asignacion)
            if conflictos > 0:
                conflictos_vars.append(var)
        return conflictos_vars

    def num_conflictos(self, variable, asignacion):
        conflictos = 0
        for restriccion in self.restricciones:
            if variable in restriccion:
                otra_variable = restriccion[1] if restriccion[0] == variable else restriccion[0]
                if otra_variable in asignacion and asignacion.get(variable) == asignacion.get(otra_variable):
                    conflictos += 1
        return conflictos

    def consistente(self, asignacion):
        for var1, var2 in self.restricciones:  # Iterar sobre todas las restricciones
            if var1 in asignacion and var2 in asignacion:  # Verificar si ambas variables tienen asignaciones
                if asignacion[var1] == asignacion[var2]:  # Si las asignaciones violan una restricción, retornar False
                    return False
        return True  # Si no se violan restricciones, retornar True

# Definir las variables, dominios y restricciones del problema
variables = ['A', 'B', 'C']
dominios = {
    'A': ['rojo', 'verde', 'azul'],
    'B': ['rojo', 'verde'],
    'C': ['rojo', 'verde']
}
restricciones = [('A', 'B'), ('A', 'C')]

# Crear una instancia del problema CSP
problema_csp = CSP(variables, dominios, restricciones)

# Resolver el problema utilizando el algoritmo de Búsqueda Local de Mínimos-Conflictos
solucion = problema_csp.minimos_conflictos_search()

# Imprimir la solución encontrada
if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")
