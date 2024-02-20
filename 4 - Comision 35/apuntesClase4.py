# librerías

"""
class Producto 
    id
    precio
    titulo
    director
    categoría (Libro, Musica, Cine)
        class Libros
            editorial
            cantPaginas
            generoLiterario (novela, policial, ensayo)
            + Hojear
            + leerContratapa
        class Musica
            sello 
            duracion
            formato (CD, VINILO, CASETTE)
            generoMusical (Rock, Trap)
            + probarDisco
        class Cine
            duracion
            generoCine (Terror, infantiles, documental)

class Usuario
    id
    nombre
    apellido
    email
    contrasenia
    username
    dni
    carrito de compras (LISTA DE PRODUCTOS)
    lista de favoritos (LISTA DE PRODUCTOS)
    historial de compras (LISTA DE ORDENES DE COMPRA PASADAS)

class OrdenDeCompra
    id
    precioFinal
    productos (LISTA DE PRODUCTOS)
    comprador (usuario, id)


""" 























# POO - 

# Un objeto es una Entidad
# 1. ATRIBUTOS/PROPIEDADES - que tiene determinadas características
# 2. MÉTODOS - puede realizar acciones, tener x comportamiento
# 3. ESTADOS - puede tener un estado
# CLASES
# un OBJETO puede ser una INSTANCIA de una CLASE
# el auto es un ejemplar de el "molde" de autos que seria la clase

class Auto:
    # constructor - acá definimos los atributos 
    def __init__(
            self, 
            marca, 
            modelo, 
            color, 
            estadoMotor, 
            estadoCambios, 
            velocidades
        ):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.estadoMotor = estadoMotor
        self.estadoCambios = estadoCambios
        self.velocidades = velocidades
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getAuto(self):
        print("Marca: " + self.getMarca())
        print("Modelo: " + self.getModelo())
        print("Color: " + self.getColor())
    def tocarBocina(self):
        print(f'Soy un {self.getModelo()}: pi piiii')
    def cambiarEstadoMotor(self):
        if(self.estadoMotor):
            print("Motor del " + self.getModelo() + " prendido, lo voy a apagar")
            self.estadoMotor = False
            print("Motor apagado")
        else:
            print("Motor del " + self.getModelo() + " apagado, lo voy a encender")
            self.estadoMotor = True
            print("Motor encendido")
    def subirVelocidad(self):
        if(self.estadoCambios < self.velocidades):
            self.estadoCambios += 1
            print(f'el {self.getModelo()} estaba en {self.estadoCambios - 1 } ahora esta en {self.estadoCambios}')
        else:
            print("No podes subir mas")
    def bajarVelocidad(self):
        if(self.estadoCambios > -1):
            self.estadoCambios -= 1
            print(f'el {self.getModelo()} estaba en {self.estadoCambios + 1 } ahora esta en {self.estadoCambios}')
        else:
            print("No podes bajar mas")


auto1 = Auto("Toyota", "Prius", "Blanco", True, 1,6) 
auto2 = Auto("Fiat", "Cronos", "Rojo", False, 0, 5) 
auto3 = Auto("Peugeot", "208", "Verde", False, -1, 5)

obj = {"Nombre": "Juan", "Apellidos": "Perez"}

# par clave-valor key-value propiedades-atributos

auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()




