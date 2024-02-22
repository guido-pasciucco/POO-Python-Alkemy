from enum import Enum
"""
    Clase 5 - POO Python
    Librería
    Producto - PADRE
    HIJOS 3 CLASS (Libro, disco, pelicula)
"""
# enums

class TipoLibro(Enum):
    FISICO = "Fisico"
    DIGITAL = "Ebook"

class FormatoDisco(Enum):
    CD = "Compact Disc"
    VINILO = "Vinilo"

class Clasificaciones(Enum):
    ATP = "Apto Todo Publico"
    MAS13 = "+13"
    MAS16 = "+16"
    MAS18 = "+18"

class GeneroCine(Enum):
    DOCU = "Documental"
    TERROR = "Terror"
    ACCION = "Accion"


class Producto:
    def __init__(self, id, titulo, autor, precio, stock):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock
    def mostrarProducto(self):
        pass # delegar el cuerpo del método a la clase hijo correspondiente

class Libro(Producto): # la clase libro extiende a producto
    def __init__(
            self,
            id,
            titulo,
            autor, 
            precio,
            stock,
            formatoLibro,
            cantHojas
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.formatoLibro = formatoLibro
        self.cantHojas = cantHojas
    def mostrarProducto(self):
        print(f'ID: {self.id}')
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'precio: {self.precio}')
        print(f'stock: {self.stock}')
        print(f'formato: {self.formatoLibro}') # fisico o ebook
        print(f'cantHojas: {self.cantHojas}')

class Musica(Producto):
    def __init__(
            self,
            id,
            titulo,
            autor, 
            precio,
            stock,
            formatoDisco, # CD o Vinilo o Cassette
            sello
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.formatoDisco = formatoDisco
        self.sello = sello
    def mostrarProducto(self):
        print(f'ID: {self.id}')
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'precio: {self.precio}')
        print(f'stock: {self.stock}')
        print(f'formatoDisco: {self.formatoDisco}')
        print(f'selloDiscografico: {self.sello}')

class Pelicula(Producto):
    def __init__(
            self,
            id,
            titulo,
            autor, 
            precio,
            stock,
            calificacion,
            generoCine
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.calificacion = calificacion # ATP +13 +16 +18
        self.generoCine = generoCine # documental terror accion
    def mostrarProducto(self):
        print(f'ID: {self.id}')
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'precio: {self.precio}')
        print(f'stock: {self.stock}')
        print(f'calificacion: {self.calificacion}')
        print(f'generoCine: {self.generoCine}')

# Creamos las instancias (3 por cada clase = 9 productos)

libro1 = Libro("1", "1984", "George Orwell", 12000, 8, TipoLibro.FISICO.value, 250)
libro2 = Libro("2", "Don Quijote", "Miguel de Cervantes", 19000, 10, TipoLibro.DIGITAL.value, 1000)
libro3 = Libro("3", "Un mundo feliz", "Aldous Huxley", 5000, 42, TipoLibro.DIGITAL.value, 300)

musica1 = Musica("4", "Fix you", "Coldplay", 3000, 12, FormatoDisco.CD.value, "Sony")
musica2 = Musica("5", "The Scientist", "Coldplay", 2700, 32, FormatoDisco.CD.value, "Sony")
musica3 = Musica("6","In my place", "Coldplay", 3100, 43, FormatoDisco.CD.value, "Sony")

pelicula1 = Pelicula("7","Spiderman", "Sam Raimi", 15000, 43, Clasificaciones.MAS16.value, GeneroCine.ACCION.value)
pelicula2 = Pelicula("8","El exorcista", "John Borman", 14500, 43, Clasificaciones.MAS16.value, GeneroCine.ACCION.value)
pelicula3 = Pelicula("9","Matrix", "Hermanas Wachowski", 16500, 12, Clasificaciones.MAS16.value, GeneroCine.ACCION.value)

libro1.mostrarProducto()
print("-------------------------")
libro2.mostrarProducto()
print("-------------------------")
libro3.mostrarProducto()
print("-------------------------")
musica1.mostrarProducto()
print("-------------------------")
musica2.mostrarProducto()
print("-------------------------")
musica3.mostrarProducto()
print("-------------------------")
pelicula1.mostrarProducto()
print("-------------------------")
pelicula2.mostrarProducto()
print("-------------------------")
pelicula3.mostrarProducto()
