"""
class Usuario
    id
    mail
    nombre 
    apellido
    carrito de compras (varios productos)
    historias de compras (varios ordenes de compra)
    lista de favoritos (varios productos)
    - iniciar sesión
    - cambiar datos personales
    
class Producto
    id
    precio
    - agregar al carrito
    - agregar a favoritos
    class Libro
        titulo
        autor
        editorial
        cantPaginas
        generoLiterario
        pais
        idioma
    class Musica
        titulo
        autor
        discograficas
        generoMusica
        pais
        idioma
        formato (CD, Vinilos)
    class Peliculas
        titulo
        autor
        generosCine
        duracion

class Orders
    fecha
    comprador (usuario)
    lista de productos
    precio final (calcula)
    id
    medio de pago
"""
























# clase - "molde" con el cual voy a ir creando mis objetos Auto
# Objeto auto - UNA INSTANCIA DE LA CLASE AUTO


class Auto:
    # clase constructora
    # definiendo los atributos de mis objetos Auto
    def __init__(self, marca, modelo, color, anio, estadoMotor):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.estadoMotor = estadoMotor
    # METODOS - funciones restringidas a determinado contexto
    def tocarBocina(self):
        print("Pi piii")
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getAnio(self):
        return self.anio
    def mostrarAuto(self):
        print("Marca: " + self.getMarca())
        print("Modelo: " + self.getModelo())
        print("Color: " + self.getColor())
        print("Anio: " + self.getAnio())

    def cambiarEstadoMotor(self):
        if(self.estadoMotor):
            print("Estaba prendido")
            self.estadoMotor == False
            print("Lo apagué")
        else:
            print("Estaba apagado")
            self.estadoMotor = True
            print("Lo prendí")
    

# DNI, TELÉFONOS, CELULARES, - NO SE SUMAN -> NO HACE FALTA QUE SEAN NUMBER (INT)


"""
OBJETOS - DICCIONARIOS (SINÓNIMOS)
PARES KEY - VALUE (CLAVE - VALOR) (PROPIEDAD - ATRIBUTO)
"""


auto1 = Auto("Toyota", "Prius", "Rojo", "2017", False)
auto2 = Auto("Fiat", "Cronos", "Azul", "2020", True)
auto3 = Auto("Peugeot", "208", "Blanco", "2022", False)

auto1.mostrarAuto()
auto1.cambiarEstadoMotor()

auto2.mostrarAuto()
auto2.cambiarEstadoMotor()

auto3.mostrarAuto()
auto3.cambiarEstadoMotor()

auto3.