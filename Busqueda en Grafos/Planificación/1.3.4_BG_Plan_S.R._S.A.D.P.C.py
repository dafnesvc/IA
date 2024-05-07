"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Satisfacción de restricciones--> Salto Atrás Dirigido por Conflictos

Este programa implementa el algoritmo de Salto Atrás Dirigido por Conflictos para encontrar una solución al
problema de satisfacción de restricciones. Selecciona la variable no asignada que causa más conflictos y prueba
los valores en su dominio, utilizando la heurística de conflicto máximo para dirigir la búsqueda hacia la solución."""

class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables del problema
        self.dominios = dominios    # Diccionario de dominios para cada variable
        self.restricciones = restricciones  # Lista de restricciones entre las variables

    def backjumping_search(self, asignacion={}):
        if len(asignacion) == len(self.variables):
            return asignacion  # Si todas las variables están asignadas, retornar la asignación completa

        var_no_asignada = self.seleccionar_variable(asignacion)  # Seleccionar una variable no asignada

        for valor in self.dominios[var_no_asignada]:  # Probar cada valor en el dominio de la variable
            asignacion_nueva = asignacion.copy()  # Crear una copia de la asignación actual
            asignacion_nueva[var_no_asignada] = valor  # Asignar el valor a la variable

            if self.consistente(asignacion_nueva):  # Verificar si la asignación es consistente
                resultado = self.backjumping_search(asignacion_nueva)  # Llamada recursiva con la asignación actualizada
                if resultado:  # Si se encuentra una solución válida, retornarla
                    return resultado
        return None  # Si no se encuentra solución, retornar None

    def seleccionar_variable(self, asignacion):
        variables_no_asignadas = [v for v in self.variables if v not in asignacion]  # Variables que no están asignadas
        if variables_no_asignadas:
            return max(variables_no_asignadas, key=lambda v: self.num_conflictos(v, asignacion))  # Seleccionar la variable con más conflictos
        else:
            return None

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

# Resolver el problema utilizando el algoritmo de Salto Atrás Dirigido por Conflictos
solucion = problema_csp.backjumping_search()

# Imprimir la solución encontrada
if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")
