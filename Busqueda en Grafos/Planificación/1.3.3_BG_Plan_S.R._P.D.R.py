"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Satisfacción de restricciones--> Propagación de Restricciones

El resultado esperado es imprimir la solución encontrada para el problema de satisfacción de restricciones
(CSP, por sus siglas en inglés), que consiste en asignar colores a ciertas variables (en este caso, ciudades)
cumpliendo con ciertas restricciones. El resultado debe mostrar las asignaciones de colores para cada variable
si se encuentra una solución, o indicar que no se encontró solución si no es posible cumplir con todas las 
restricciones."""

class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones

    def propagacion_restricciones(self, asignacion={}):
        if len(asignacion) == len(self.variables):
            return asignacion

        var_no_asignada = [v for v in self.variables if v not in asignacion][0]

        for valor in self.dominios[var_no_asignada]:
            asignacion_nueva = asignacion.copy()
            asignacion_nueva[var_no_asignada] = valor

            if self.consistente(asignacion_nueva):
                restricciones_actualizadas = self.actualizar_restricciones(asignacion_nueva, var_no_asignada, valor)
                if restricciones_actualizadas is not None:
                    resultado = self.propagacion_restricciones(asignacion_nueva)
                    if resultado:
                        return resultado
        return None

    def actualizar_restricciones(self, asignacion, variable_asignada, valor_asignado):
        restricciones_actualizadas = []
        for restriccion in self.restricciones:
            if variable_asignada in restriccion:
                var1, var2 = restriccion
                if var1 == variable_asignada:
                    var1, var2 = var2, var1
                if var2 not in asignacion:
                    restricciones_actualizadas.append(restriccion)
                else:
                    if var1 in asignacion:  # Verificar si las variables están en la asignación
                        if (asignacion[var1], asignacion[var2]) == (valor_asignado, asignacion[var2]):
                            return None
            else:
                restricciones_actualizadas.append(restriccion)
        return restricciones_actualizadas

    def consistente(self, asignacion):
        for var1, var2 in self.restricciones:
            if var1 in asignacion and var2 in asignacion:
                if asignacion[var1] == asignacion[var2]:
                    return False
        return True


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

# Resolver el problema utilizando el algoritmo de Propagación de Restricciones
solucion = problema_csp.propagacion_restricciones()

# Imprimir la solución encontrada
if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")

