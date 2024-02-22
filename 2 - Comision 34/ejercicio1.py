class Bicicleta:
    def __init__(self, marca, cambios, rodado, color, precio, stock, velocidad):
        self.marca = marca
        self.cambios = cambios
        self.rodado = rodado
        self.color = color
        self.precio = precio
        self.stock = stock
        self.velocidad = velocidad
        
    def subirVelocidad(self, velObjetivo):
        print(f'Velocidad inicial: {self.velocidad}')
        while(self.velocidad <= velObjetivo):
            self.velocidad += 1
            print(f'Subiendo velocidad: {self.velocidad}')
        print("Listo, velocidad alcanzada")
    def bajarVelocidad(self):
        print(f'Velocidad inicial: {self.velocidad}')
        while(self.velocidad > 0):
            self.velocidad -= 1
            print(f'Bajando velocidad: {self.velocidad}')
        print("Paraste completamente")


bici = Bicicleta("Venzo", 18, 29, "Rojo", 250000, 5, 20)
bici.bajarVelocidad()
bici.subirVelocidad(9)
