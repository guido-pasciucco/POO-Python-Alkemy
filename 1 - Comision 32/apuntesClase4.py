"""
class Biblioteca
    class Libros
        titulo, anio, cantHojas
    class Autores
        nombre, apellido, fecha nacimiento, lista (libros)
    class Generos
        titulo, lista (libros, autores)
    class Clientes
        nombre, apellido, dni, tdc, listas (compras, libros)
    class Ventas
        lista ventas ()

"""












"""

class VEHICULO
    mostrar vehiculo
    tipoVehiculo = 
        Auto
            props
            metodos
            : abrir puertas
        Moto
            props
            metodos
        Avion
            props
            metodos
            : metodo: aterrizar
        Barco
            metodo: anclar
"""
class Auto:
    # PROPIEDADES - "que caracteriza a mi objeto?"
    def __init__(
            self,
            marca,
            modelo,
            color,
            tipoCombustible,
            cantPuertas,
            estado
        ):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipoCombustible = tipoCombustible
        self.cantPuertas = cantPuertas
        self.estado = estado
    # MÉTODOS - "que acciones caracterizan a mi objeto?"
    def mostrarAuto(self):
        print(f'Marca: {self.getMarca()}')
        print(f'Modelo: {self.getModelo()}')
        print(f'Color: {self.getColor()} ')
        print(f'Tipo de Combustible: {self.getTipoCombustible()}')
        print(f'Cantidad de Puertas: {self.getCantPuertas()}')
        print(f'Estado: {self.getEstado()}')
    # Getters
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getTipoCombustible(self):
        return self.tipoCombustible
    def getCantPuertas(self):
        return self.cantPuertas
    def getEstado(self):
        return self.estado

inputMarca = input("Ingrese la marca: ")
inputModelo = input("Ingrese el modelo: ")
inputColor = input("Ingrese el color: ")
inputTipoCombustible = input("Ingrese tipo de combustible: ")
inputCantPuertas = input("Ingrese la cantidad de puertas: ")
inputEstado = input("Ingrese Estado: ")

miAuto = Auto(
    inputMarca,
    inputModelo,
    inputColor,
    inputTipoCombustible,
    inputCantPuertas,
    inputEstado
)

miAuto.mostrarAuto()