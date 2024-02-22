class Bicicleta:
    def __init__(
            self,
            rodado,
            precio,
            color,
            marca,
            modelo,
            velocidad):
        self.rodado =rodado
        self.precio = precio
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
    def acelerar(self, velObjetivo):
        if(self.velocidad < 0):
            print("ERROR - VELOCIDAD NEGATIVA")
        else:
            while(self.velocidad < velObjetivo):
                self.velocidad += 1
                print(f'Velocidad: {self.velocidad}')
    def frenar(self):
        if(self.velocidad < 0):
            print("ERROR - VELOCIDAD NEGATIVA")
        else:
            while(self.velocidad > 0):
                self.velocidad -= 1
                print(f'Velocidad: {self.velocidad}')
    def getVelocidad(self):
        if(self.velocidad < 0):
            print("ERROR - VELOCIDAD NEGATIVA")
        else:
            print(self.velocidad) 


miBici = Bicicleta("29", 250000, "Rojo", "Venzo", "2000", -18)
miBici.getVelocidad()
miBici.frenar()
miBici.getVelocidad()
miBici.acelerar(7)
miBici.getVelocidad()
# 1 O + - ESTA EN MOVIMIENTO
# 0 - ESTA QUIETA LA BICI
# -1 O - ERROR