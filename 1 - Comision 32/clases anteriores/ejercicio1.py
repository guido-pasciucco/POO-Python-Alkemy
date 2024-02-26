class Bicicleta:
    def __init__(self, marca, rodado, precio, velocidad):
        self.marca = marca
        self.rodado = rodado
        self.precio = precio
        self.velocidad = velocidad
    
    def frenar(self):
        if(self.velocidad < 0):
            print("ERROR, velocidad en num negativo")
        else:
            while(self.velocidad > 0):
                self.velocidad -= 1
                print(f'bajando velocidad : {self.velocidad}')
            print("Ya frenaste")
            # 7 6 5 4 3 2 1 0 (frenó)
    def acelerar(self, velocidadEsperada):
        if(self.velocidad < 0):
            print("ERROR, velocidad en num negativo")
        else:
            while(self.velocidad < velocidadEsperada):
                self.velocidad += 1
                print(f'aumentando velocidad : {self.velocidad}')
            print("llegamos a la velocidad deseada")

    def mostrarBici(self):
        print("Marca: " + self.marca)
        print("Rodado: " + self.rodado)
        print(f'Precio: {self.precio}')
        print(f'Velocidad: {self.velocidad}')
    
miBici = Bicicleta("Venzo", "29", 150000, -25)

miBici.mostrarBici()
miBici.frenar()
miBici.mostrarBici()
miBici.acelerar(9)
miBici.mostrarBici()