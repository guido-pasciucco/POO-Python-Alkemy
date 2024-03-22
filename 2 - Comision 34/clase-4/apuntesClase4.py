# librería
"""
Vehiculos
    marca
    modelo
    anio
    color
    precio
    Autos
        cantPuertas
        tipoCombustible
    Moto
        ponerCasco
        sacarCasco
    Barco
        Anclar
    Avion
        Despegar

Libreria
    agregarAlCarrito
    productos/catalogo
    discos
        id
        titulo
        artista
        generoMusical
        formato (CD, Vinilos, cassette)
        precio
        discográfica
    peliculas
        id
        titulo
        autor
        generoCine
        formato (DVD)
        precio
    libros
        id
        autor
        generoLiterario
        anio
        cantPaginas
        ISBN
        editorial (una)
        precio

editorial
    id
    nombre
    cuil
    colección de libros 

autor
    id
    nombre
    apellido
    colección de libros que publicó

usuario/cliente 
    id
    carrito de compras (libros que compró)



"""








# OBJETO - clase (el "molde" de los objetos)+
# INSTANCIAS. - EJEMPLAR DE UN OBJETO BASADO EN UNA CLASE

class Auto:
    # PROPIEDADES / Atributos
    def __init__(self, marca, modelo, color, anio, estado, motorPrendido):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.estado = estado
        self.motorPrendido = motorPrendido
    # MÉTODOS - comportamientos, acciones
    # Getters
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getAnio(self):
        return self.anio
    def getEstado(self):
        return self.estado
    def getMotorPrendido(self):
        return self.motorPrendido
    
    def mostrarAuto(self):
        print("Marca: " + self.getMarca())
        print(f'Modelo: {self.getModelo()}')
        print(f'Color: {self.getColor()}')
        print(f'Anio: {self.getAnio()}')
        print(f'Estado: {self.getEstado()}')
        print(f'Estado Motor: {self.getMotorPrendido()}')

    def repararAuto(self):
        if(self.estado == "Daniado"):
            print("Ya lo estoy arreglando")
            self.estado = "Funcionando"
            print("Ya funciona")
        else:
            print("No hace falta arregarlo")
    
    def modificarEstadoMotor(self):
        if(self.motorPrendido):
            print("Esta prendido, lo apago")
            self.motorPrendido = False
            print("Lo apague")
        else:
            print("Esta apagado, lo prendo")
            self.motorPrendido = True
            print("ya este prendido")

auto1 = Auto("Toyota", "Prius", "Rojo", "2020", "Funcionando", False)
auto2 = Auto("Peugeot", "208", "Azul", "2022", "Daniado", True)

auto1.modificarEstadoMotor()
auto2.modificarEstadoMotor()


