""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Satisfacción de restricciones--> Búsqueda de Vuelta Atrás

Este programa utiliza el algoritmo de Búsqueda de Vuelta Atrás para encontrar una solución a un problema
de satisfacción de restricciones (CSP). Se define una clase CSP que representa el problema, con métodos 
para realizar la búsqueda de vuelta atrás y verificar la consistencia de una asignación parcial."""

class CSP:
    def __init__(self, variables, dominios, restricciones):
        """
        Inicializa el problema de satisfacción de restricciones (CSP).

            variables (list): Lista de variables del problema.
            dominios (dict): Diccionario de dominios para cada variable.
            restricciones (list): Lista de restricciones entre las variables.
        """
        self.variables = variables  # Lista de variables del problema
        self.dominios = dominios    # Diccionario de dominios para cada variable
        self.restricciones = restricciones  # Lista de restricciones entre las variables

    def backtrack_search(self, asignacion={}):
       
        if len(asignacion) == len(self.variables):
            return asignacion  # Si todas las variables están asignadas, retornar la asignación completa

        var_no_asignada = [v for v in self.variables if v not in asignacion][0]  # Escoger una variable no asignada

        for valor in self.dominios[var_no_asignada]:  # Probar cada valor en el dominio de la variable
            asignacion_nueva = asignacion.copy()  # Crear una copia de la asignación actual
            asignacion_nueva[var_no_asignada] = valor  # Asignar el valor a la variable

            if self.consistente(asignacion_nueva):  # Verificar si la asignación es consistente
                resultado = self.backtrack_search(asignacion_nueva)  # Llamada recursiva con la asignación actualizada
                if resultado:  # Si se encuentra una solución válida, retornarla
                    return resultado
        return None  # Si no se encuentra solución, retornar None

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

# Resolver el problema utilizando el algoritmo de Búsqueda de Vuelta Atrás (Backtracking)
solucion = problema_csp.backtrack_search()

# Imprimir la solución encontrada
if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")
