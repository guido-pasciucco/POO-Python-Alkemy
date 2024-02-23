class Bicicleta:
    def __init__(
            self, marca, modelo,
            color, rodado, cambios,
            precio, velocidad
        ):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.rodado =rodado
        self.cambios = cambios
        self.precio = precio
        self.velocidad = velocidad
    def mostrarBici(self):
        print("........................")
        print(f'marca: {self.marca}')
        print(f'modelo: {self.modelo}')
        print(f'color: {self.color}')
        print(f'rodado: {self.rodado}')
        print(f'cambios: {self.cambios}')
        print(f'precio: {self.precio}')
        print(f'velocidad: {self.velocidad} Km/h')
        print("........................")
    def actualizarPrecio(self, porcentaje):
        print(f'Precio anterior: {self.precio}')
        self.precio += self.precio * (porcentaje / 100)
        print(f'Precio actual: {self.precio}')
    def frenar(self):
        while(self.velocidad > 0):
            self.velocidad -= 1
            print(f'{self.velocidad} Km/h')
        print(f'ya frenaste')


miBici = Bicicleta("Venzo", "XR", "Rojo", 29, 18, 300000, 15)
miBici.mostrarBici()
miBici.actualizarPrecio(21)
miBici.mostrarBici()
miBici.frenar()
miBici.mostrarBici()