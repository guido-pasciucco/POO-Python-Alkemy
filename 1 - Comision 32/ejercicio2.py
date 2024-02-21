# animal
# perro (animal)
# aguila (animal)

class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo #ENUMS - Enumeraciones
    def moverse(self):
        pass

class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza
    def moverse(self):
        return "Estoy corriendo"

class Aguila(Animal):
    def __init__(self, cantidad_patas, tipo, tipoAlas, tipoPico):
        super().__init__(cantidad_patas, tipo)
        self.tipoAlas = tipoAlas
        self.tipoPico = tipoPico
    def moverse(self):
        return "Estoy volando"

aguila1 = Aguila("2", "Vertebrado", "Grandes", "Puntiagudo")
perro1 = Perro ("4", "Vertebrado", "Firulais", "Golden")
print(aguila1.moverse())
print(perro1.moverse())