from enum import Enum

# genero cine
# genero musica
# genero libros
# clasificacionCine
# formatoMusica

class GeneroCine(Enum):
    ACCION = "Accion"
    TERROR = "Terror"
    DOCU = "Documental"

class GeneroMusica(Enum):
    A = "Rock"
    B = "POP"
    C = "Clasica"

class GeneroLibros(Enum):
    NOVELA = "Novela"
    BIO = "Biografia"
    ENSAYO = "Ensayo"

class ClasificacionCine(Enum):
    ATP = "Apto Todo Publico"
    MAS13 = "+13"
    MAS16 = "+16"
    MAS18 = "+18"

class FormatoMusica(Enum):
    CD = "Compact Disc"
    VINILO = "Disco de vinilo"
    CASSETTE = "Cassette"

class Producto:
    def __init__(self, id, titulo, autor, precio, stock):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock
    def mostrarProducto(self): # metodo el mismo para los 3 hijos
        pass # delegar el cuerpo del método a cada hijo

# creamos clases de los 3 hijos


class Libro(Producto): # la clase libro EXTIENDE A PRODUCTO
    def __init__(
            self,
            id,
            titulo,
            autor,
            precio,
            stock,
            editorial, # propio de Libro
            generoLiterario # propio de Libro - enum
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.editorial = editorial
        self.generoLiterario = generoLiterario
    def mostrarProducto(self):
        print(f'id: {self.id}')
        print(f'titulo: {self.titulo}')
        print(f'autor: {self.autor}')
        print(f'precio: {self.precio}')
        print(f'stock: {self.stock}')
        print(f'editorial: {self.editorial}')
        print(f'generoLiterario: {self.generoLiterario}')

class Pelicula(Producto):
    def __init__(
            self,
            id,
            titulo,
            autor,
            precio,
            stock,
            clasificacion, # propio de Pelicula
            generoCine # propio de Pelicula - enum
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.clasificacion = clasificacion
        self.generoCine = generoCine
    def mostrarProducto(self):
        print(f'id: {self.id}')
        print(f'titulo: {self.titulo}')
        print(f'autor: {self.autor}')
        print(f'precio: {self.precio}')
        print(f'stock: {self.stock}')
        print(f'clasificacion: {self.clasificacion}')
        print(f'generoCine: {self.generoCine}')

class Musica(Producto): 
    def __init__(
            self,
            id,
            titulo,
            autor,
            precio,
            stock,
            formato, # CD / VINILO / Cassette
            generoMusica # Rock / Pop / Clasica / Trap
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.formato = formato
        self.generoMusica = generoMusica
    def mostrarProducto(self):
        print(f'id: {self.id}')
        print(f'titulo: {self.titulo}')
        print(f'autor: {self.autor}')
        print(f'precio: {self.precio}')
        print(f'stock: {self.stock}')
        print(f'formato: {self.formato}')
        print(f'generoMusica: {self.generoMusica}')


miLibro = Libro("1", "1984", "George Orwell", 13000, 19, "Anagrama", GeneroLibros.NOVELA.value)

miLibro.mostrarProducto()

miPeli = Pelicula("2", "Cars", "Pixar", 5000, 23, ClasificacionCine.ATP.value, GeneroCine.ACCION.value)
miPeli2 = Pelicula("5", "Cars2", "Pixar", 5000, 23, ClasificacionCine.MAS18.value, GeneroCine.DOCU.value)

miPeli.mostrarProducto()
miPeli2.mostrarProducto()

miDisco = Musica(
    "3",
    "Dark side of the moon",
    "Pink Floyd",
    8500,
    43,
    FormatoMusica.VINILO.value,
    GeneroMusica.A.value
)

miDisco.mostrarProducto()




""" class Algo:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre # atributo privado setters y getters
        self.apellido = apellido # publico 

algo = Algo("juan", "perez")

print(algo.__nombre)
print(algo.apellido)
"""

# POO - Python

""" class Auto:
    def acelera(self):
        print("Me transporto en 4 ruedas")

class Moto:
    def acelera(self):
        print("Me transporto en 2 ruedas")

class Camion:
    def acelera(self):
        print("Me transporto en 18 ruedas")

miVehiculo = Camion()

def vehiculoAcelera(vehiculo):
    vehiculo.acelera()

vehiculoAcelera(miVehiculo) """