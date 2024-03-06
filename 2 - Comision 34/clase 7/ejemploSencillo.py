# listas y POO

class Estudiante:

    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def promedio_calificaciones(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0

# Crear un estudiante
estudiante1 = Estudiante("Juan", 20)

# agregando calificaciones
estudiante1.agregar_calificacion(8) # acá inicializo calificaciones
estudiante1.agregar_calificacion(10)
estudiante1.agregar_calificacion(7)


# Obtener el promedio de las calificaciones
# round() metodo para redondear los decimales (solo 2 decimales)s
print("Promedio: ", estudiante1.nombre , round(estudiante1.promedio_calificaciones(), 2))
