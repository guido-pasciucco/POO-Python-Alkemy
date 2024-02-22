class Producto:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
    def mostrarProducto(self):
        pass

class Libro(Producto):
    def __init__(self, titulo, autor, precio, cant_paginas, tipo_tapa):
        super().__init__(titulo, autor, precio)
        self.cant_paginas = cant_paginas
        self.tipo_tapa = tipo_tapa
    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Cant_paginas: {self.cant_paginas}')
        print(f'Tipo_tapa: {self.tipo_tapa}')
    
class Musica(Producto):
    def __init__(self, titulo, autor, precio, genero, duracion):
        super().__init__(titulo, autor, precio)
        self.genero = genero
        self.duracion = duracion
    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Genero: {self.genero}')
        print(f'Duracion: {self.duracion}')

class Pelicula(Producto):
    def __init__(self, titulo, autor, precio, genero, clasificacion):
        super().__init__(titulo, autor, precio)
        self.genero = genero
        self.clasificacion = clasificacion
    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Genero: {self.genero}')
        print(f'Clasificacion: {self.clasificacion}')

libro1 = Libro("IT", "Sthepen King", 20000, 323, "dura")
libro2 = Libro("Harry Potter", "J.K Rowling", 22000, 413, "blanda")
libro3 = Libro("Cancion de Hielo y Fuego", "George RR Martin", 21000, 455, "dura")

musica1 = Musica("Fix you", "Coldplay", 3000, "Pop-rock", "172s")
musica2 = Musica("The Scientist", "Coldplay", 2700, "Pop-rock", "165s")
musica3 = Musica("In my place", "Coldplay", 3100, "Pop-rock", "189s")

pelicula1 = Pelicula("Spiderman", "Sam Raimi", 15000, "accion", "G")
pelicula2 = Pelicula("El exorcista", "John Borman", 14500, "terror", "R")
pelicula3 = Pelicula("Matrix", "Hermanas Wachowski", 16500, "accion", "PG")

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
