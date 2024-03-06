# Módulo circulo.py

import math

def calcular_area(radio):
    return math.pi * radio**2

def calcular_perimetro(radio):
    return 2 * math.pi * radio

# Programa principal

import circulo

radio = float(input("Ingrese el radio del círculo: "))

area = circulo.calcular_area(radio)
perimetro = circulo.calcular_perimetro(radio)

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")


# Sin modularizar 

import math

def calcular_circulo(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro

radio = float(input("Ingrese el radio del círculo: "))
area, perimetro = calcular_circulo(radio)

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")


















""" class Usuario:
    def __init__(self): 
        self.nombre = "Tito" # Público
        self.__contrasenia = "abcd" # Privado - 2 guiones bajos 

    # Getter
    def get_contrasenia(self):
        return self.__contrasenia

user1 = Usuario()

print(user1.nombre)
print(user1.get_contrasenia()) # Vemos en consola contraseña vieja
"""







""" class Auto():
    def contarRuedas(self):
        return "Tengo 4 Ruedas"

class Moto():
    def contarRuedas(self):
        return "Tengo 2 Ruedas"

class Camion():
    def contarRuedas(self):
        return "Tengo 18 Ruedas"

auto = Auto()
moto = Moto()
camion = Camion() """

# EJEMPLO 1
# mismo método - diferentes resultados para diferentes objetos

""" print(auto.contarRuedas()) # 4 ruedas
print(moto.contarRuedas()) # 2 ruedas
print(camion.contarRuedas()) # 18 ruedas
"""
# EJEMPLO 2
# mismo método - diferentes resultados para diferentes parámetros
""" 
def contarRuedasVehiculo(e):
    print(e.contarRuedas())

contarRuedasVehiculo(auto) # 4 ruedas
contarRuedasVehiculo(moto) # 2 ruedas
contarRuedasVehiculo(camion) # 18 ruedas """


















# lo que estoy haciendo es llamar a la línea "print(n1 + n2)"
# que al ser una suma en un print, me devuelve el resultado de la suma
# pero mi función NO es esa suma, no es ese dato
# no se almacena en ningún lugar
""" 
def suma_con_return(n1, n2):
    return n1 + n2

print(suma_con_return(10, 5))
 """
# cuando hay retorno, toda la función, se convierte en el resultado
# todo lo que componía a la función, ahora se convirtió en su resultado, por eso hacemos print
# directamente de la función ejecutada y nos devuelve el valor
# sin retorno, lo que nos da la ejecución de la función son las líneas de código que tiene dentro
# con retorno, lo que nos da la ejecución de la función es el dato en sí.














# range(stop)
# Crea un iterador desde 0 hasta el valor del stop añadiendo 1 en cada iteración
# No llega a su valor del stop, se detiene 1 antes (9 en este caso)

""" for e in range(10):
    print(e) """

# range(start, stop)
# Crea un iterador desde el valor de start hasta el valor del stop añadiendo 1 en cada iteración
# Comienza en su valor de start (5) pero se detiene 1 antes de su valor del stop (9)
"""     
for e in range(5, 10):
    print(e) """

# range(start, stop, step)
# Crea un iterador desde el valor de start hasta el valor del stop
# Con el parámetro step definimos la cantidad que aumenta o disminuye en cada iteración
# En este caso está contando de a 2
# Comienza en su valor de start (5) pero se detiene 2 antes de su valor del stop (18)
    
""" for e in range(4, 20, 2):
    print(e) """





# Ejemplo - Lista

""" compras_almacen = ["Café", "Pan", "Verduras", "Fideos", "Aceite"]
"""
# Si se vuelve demasiado larga también se puede escribir así

""" compras_almacen = [
    "Café",
    "Pan",
    "Verduras",
    "Fideos",
    "Aceite"
] """

""" print(compras_almacen) # mostramos toda la lista
print(compras_almacen[0]) # mostramos solo el elemento en la posición 3 de la lista
 """
# ----------------------------------------------------------------

# Ejemplo - Tupla

""" dias_semana_1 = ("Lunes", "Martes", "Miercoles","Jueves","Viernes", "Sabado", "Domingo")
"""
# Si se vuelve demasiado larga también se puede escribir así

""" dias_semana_2 = (
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo"
) """
""" 
print(dias_semana_1) # mostramos toda la lista
print(dias_semana_1[3]) # mostramos solo el elemento en la posición 3 de la tupla
"""
# ---

# Ejemplo - Diccionario
""" 
jugador1 = {"nombre": "Leo", "apellido": "Messi", "edad": "36", "pais_nacimiento": "Argentina"}
 """
# Si se vuelve demasiado largo también se puede escribir así
""" 
jugador2 = {
    "nombre": "Leo",
    "apellido": "Messi",
    "edad": "36",
    "pais_nacimiento": "Argentina"
} """











# Ejemplo con Boolean
""" 
cumple_anios = False

if (cumple_anios): # Abreviación "=True" implícito
    print("Feliz Cumple!")
else:
    print("¿Cuando es tu cumple?")
 """
# Ejemplo con String

""" nombre = "Carlos"

if (nombre == "Carlos"):
    print(f'Hola {nombre}!')
else:
    print(f'¿Donde está {nombre}?')
 """
# Ejemplo con dato numérico

""" nota_final = 8

if (nota_final >= 7):
    print("Promocionaste!")
elif (nota_final > 4 and nota_final < 7):
    print("Aprobaste, pero vas a final")
else:
    print("Desaprobaste") """