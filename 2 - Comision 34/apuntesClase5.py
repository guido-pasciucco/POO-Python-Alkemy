from enum import Enum
"""

LIBRERÍA

Productos
    LIBROS - DISCOS - PELICULAS

HERENCIA
ENCAPSULAMIENTO

"""

class CalificacionesCine(Enum):
    ATP = "ATP"
    MAS13 = "+13"
    MAS16 = "+16"
    MAS18 = "+18"

class FormatoDiscos(Enum):
    CD = "CD"
    VINILO = "VINILO"

class GeneroLiterario(Enum):
    NOVELA = "Novela"
    ENSAYO = "Ensayo"
    BIOGRAFIA = "Biografia"

class GenerosCine(Enum):
    POLICIAL = "Policial"
    DOCUMENTAL = "Documental"
    INFANTIL = "Infantil"

class GenerosMusica(Enum):
    ROCK = "Rock"
    CLASICA = "Clasica"
    TRAP = "Trap"

class TipoTapa(Enum):
    DURA = "DURA"
    BLANDA = "BLANDA"

class Producto:
    def __init__(self, id, titulo, autor, precio, stock):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock
    def mostrarProducto(self):
        pass

class Libro(Producto):
    def __init__(
            self,
            id,
            titulo,
            autor,
            precio,
            stock,
            editorial,
            tapa,
            generoLiterario
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.editorial = editorial
        self.tapa = tapa
        self.generoLiterario = generoLiterario
    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Editorial: {self.editorial}')
        print(f'Tapa: {self.tapa}') # enums
        print(f'Genero: {self.generoLiterario}') # enums

class Musica(Producto):
    def __init__(
            self,
            id,
            titulo,
            autor,
            precio,
            stock,
            duracionMinutos,
            formato, # enum
            sello
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.duracionMinutos = duracionMinutos
        self.formato = formato
        self.sello = sello
    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Duracion minutos: {self.duracionMinutos}')
        print(f'Formato: {self.formato}') # enums
        print(f'Sello: {self.sello}') # enums

class Pelicula(Producto):
    def __init__(
            self,
            id,
            titulo,
            autor,
            precio,
            stock,
            calificacion,
            estudio,
            fuePremiada
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.calificacion = calificacion
        self.estudio = estudio
        self.fuePremiada = fuePremiada
    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Calificacion: {self.calificacion}')
        print(f'Estudio: {self.estudio}') # enums
        print(f'Fue premiada: {self.fuePremiada}') # enums

libro1 = Libro("1", "Quijote", "Miguel de Cervantes", 15000, 10, "Anagrama", TipoTapa.DURA.value , GeneroLiterario.NOVELA.value)
libro2 = Libro("2", "1984", "Aldous Huxley", 20000, 45, "De Bolsillo", TipoTapa.BLANDA.value, GeneroLiterario.NOVELA.value )
libro3 = Libro("3", "Guia Turismo Bariloche", "Nat geo", 8000, 34, "Nat Geo", TipoTapa.BLANDA.value, GeneroLiterario.ENSAYO.value)

musica1 = Musica("1", "Fix you", "Coldplay", 3000, 15,  60, FormatoDiscos.VINILO.value, "Sony" )
musica2 = Musica("2", "The Scientist", "Coldplay", 2700,15,  108, FormatoDiscos.CD.value, "Warner")
musica3 = Musica("3", "In my place", "Coldplay", 3100,15,  120, FormatoDiscos.VINILO.value, "Tito Records")

pelicula1 = Pelicula("1","Spiderman", "Sam Raimi", 15000,15, CalificacionesCine.MAS13.value , "Disney", False)
pelicula2 = Pelicula("2","El exorcista", "John Borman", 14500,15, CalificacionesCine.MAS18.value , "A24", True)
pelicula3 = Pelicula("3","Matrix", "Hermanas Wachowski", 16500,15, CalificacionesCine.ATP.value, "Dreamworks", False)

print("LIBROS ---")
libro1.mostrarProducto()
print("---")
libro2.mostrarProducto()
print("---")
libro3.mostrarProducto()
print("DISCOS ---")
musica1.mostrarProducto()
print("---")
musica2.mostrarProducto()
print("---")
musica3.mostrarProducto()
print("PELICULAS ---")
pelicula1.mostrarProducto()
print("---")
pelicula2.mostrarProducto()
print("---")
pelicula3.mostrarProducto()
print("---")




#enumeración - 

# key - entidad financiera - 2 opciones validas (visa, master)

















""" 

class Auto:
    def andar(self):
        print("Ando en 4 ruedas")

class Moto:
    def andar(self):
        print("Ando en 2 ruedas")

class Camion:
    def andar(self):
        print("Ando en 18 ruedas")

def andarVehiculo(vehiculo):
    vehiculo.andar()

miVehiculo = Camion()

andarVehiculo(miVehiculo)
 """