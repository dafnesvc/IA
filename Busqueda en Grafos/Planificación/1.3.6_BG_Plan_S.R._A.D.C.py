"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Satisfacción de restricciones--> Acondicionamiento del Corte

El acondicionamiento del corte es un enfoque para resolver problemas de satisfacción de restricciones (CSP)
mediante la modificación de los dominios de las variables para hacer que las restricciones sean más fáciles de satisfacer. """
class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables del problema
        self.dominios = dominios    # Diccionario de dominios para cada variable
        self.restricciones = restricciones  # Lista de restricciones entre las variables

    def cut_conditioning(self):
        while True:
            # Aplicar el acondicionamiento del corte a cada restricción
            cut_occurred = False  # Bandera para verificar si se ha realizado un corte
            for restriccion in self.restricciones:
                var1, var2 = restriccion  # Obtener las variables involucradas en la restricción
                for valor in self.dominios[var1][:]:  # Iterar sobre los valores del dominio de var1
                    if not any(valor2 for valor2 in self.dominios[var2] if (valor, valor2) not in restriccion):
                        # Si no hay ningún valor en el dominio de var2 que haga que la restricción sea falsa
                        continue  # No se realiza el corte
                    else:
                        # Si hay un valor en el dominio de var2 que hace que la restricción sea falsa
                        self.dominios[var1].remove(valor)  # Eliminar el valor del dominio de var1
                        cut_occurred = True  # Se ha realizado un corte
            if not cut_occurred:
                break  # Si no se ha realizado ningún corte, salir del bucle

        # Devolver los dominios actualizados
        return self.dominios


# Definir las variables, dominios y restricciones del problema
variables = ['A', 'B', 'C']
dominios = {
    'A': [1, 2, 3],
    'B': [1, 2],
    'C': [1, 2]
}
restricciones = [(['A', 'B']), (['A', 'C'])]

# Crear una instancia del problema CSP
problema_csp = CSP(variables, dominios, restricciones)

# Aplicar el acondicionamiento del corte
dominios_actualizados = problema_csp.cut_conditioning()

# Imprimir los dominios actualizados
print("Dominios actualizados después del acondicionamiento del corte:")
print(dominios_actualizados)
