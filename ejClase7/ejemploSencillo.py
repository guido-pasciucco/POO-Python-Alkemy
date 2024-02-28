

""" fabrica de instrumentos musicales
la fabrica tiene multiples sucursales

Fabrica
- Sucursales sucursales = []

Sucursal 
- Instrumento instrumentos = []
+ agregarInstrumento

"""

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def promedio_calificaciones(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

# Crear un estudiante
estudiante1 = Estudiante("Juan", 20)

# Agregar algunas calificaciones
estudiante1.agregar_calificacion(8)
estudiante1.agregar_calificacion(10)
estudiante1.agregar_calificacion(7)

# Obtener el promedio de las calificaciones
print("Promedio: ", estudiante1.nombre , round(estudiante1.promedio_calificaciones(), 2))
