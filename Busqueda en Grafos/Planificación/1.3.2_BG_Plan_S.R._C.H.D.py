""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Satisfacción de restricciones--> Comprobación Hacia Delante 

Este programa define una clase CSP que representa un problema de Satisfacción de Restricciones. 
Implementa el algoritmo de Comprobación Hacia Delante (Forward Checking) para encontrar una asignación 
válida de valores a las variables del problema. """



class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables del problema
        self.dominios = dominios    # Diccionario de dominios para cada variable
        self.restricciones = restricciones  # Lista de restricciones entre las variables

    def forward_checking(self, asignacion={}):
        if len(asignacion) == len(self.variables):
            return asignacion  # Si todas las variables están asignadas, retornar la asignación completa

        var_no_asignada = [v for v in self.variables if v not in asignacion][0]  # Escoger una variable no asignada

        for valor in self.dominios[var_no_asignada]:  # Probar cada valor en el dominio de la variable
            asignacion_nueva = asignacion.copy()  # Crear una copia de la asignación actual
            asignacion_nueva[var_no_asignada] = valor  # Asignar el valor a la variable

            if self.consistente(asignacion_nueva):  # Verificar si la asignación es consistente
                dominios_reducidos = self.forward_checking_forward(asignacion_nueva, var_no_asignada, valor)
                if dominios_reducidos:
                    resultado = self.forward_checking(asignacion_nueva)  # Llamada recursiva con la asignación actualizada
                    if resultado:  # Si se encuentra una solución válida, retornarla
                        return resultado
        return None  # Si no se encuentra solución, retornar None

    def forward_checking_forward(self, asignacion, variable_asignada, valor_asignado):
        dominios_reducidos = {}  # Diccionario para almacenar los dominios reducidos
        for var, dominio in self.dominios.items():  # Iterar sobre todas las variables y sus dominios
            if var not in asignacion:  # Verificar si la variable no está asignada
                dominio_reducido = [valor for valor in dominio if (var, variable_asignada) not in self.restricciones or (var, valor_asignado) in self.restricciones]
                if not dominio_reducido:  # Si el dominio se reduce a un conjunto vacío, la asignación no es válida
                    return None
                dominios_reducidos[var] = dominio_reducido
        return dominios_reducidos  # Retornar los dominios reducidos

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

# Resolver el problema utilizando el algoritmo de Comprobación Hacia Delante
solucion = problema_csp.forward_checking()

# Imprimir la solución encontrada
if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")
