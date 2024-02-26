""" EJERCICIO

CREAR UNA CLASE PRODUCTO QUE TENGA 3 HIJOS

ESTA CLASE PRODUCTO VA A TENER
- 3 ATRIBUTOS
- METODO MOSTRAR PRODUCTO QUE DEPENDIENDO EL PRODUCTO
VA A MOSTRAR DIFERENTES CARACTERÍSTICAS

LIBRO, PELICULA, DISCO - CADA UNA VA A TENER 2 ATRIBUTOS

3 instancias por clase hijo (3 libros, 3 discos y 3 peliculas)

"""



















"""
Clase 5 - POO en Python II

Objetivos:
    Conocer los principios fundamentales
    de la Programación Orientada a Objetos (POO),
    como encapsulamiento, herencia, polimorfismo y abstracción

    
"""

#Ejemplo POLIMORFISMO

# LIBRERÍA
# LIBROS
# MUSICA (CD, VINILOS)
# PELICULAS

# publicas - pueden ser leidos sin un getter - métodos
# _privadas - solo puedan ser leidos con un getter - atributos

class Producto:
    def __init__(self, _id, _titulo, _autor, _precio):
        self._id = _id
        self._titulo = _titulo
        self._autor = _autor
        self._precio = _precio

class Libro(Producto):
    def __init__(self, _id, _titulo,_autor,_precio, _editorial, _generoLiterario):
        super().__init__(self, _id, _titulo,_autor,_precio)
        self._editorial = _editorial
        self._generoLiterario = _generoLiterario

class Pelicula(Producto):
    def __init__(self, _id, _titulo,_autor,_precio, _duracion, _generoCine):
        super().__init__(self, _id, _titulo,_autor,_precio)
        self._duracion = _duracion
        self._generoCine = _generoCine

class Musica(Producto):
    def __init__(self, _id, _titulo,_autor,_precio, _duracion, _generoMusica):
        super().__init__(self, _id, _titulo,_autor,_precio)
        self._duracion = _duracion
        self._generoMusica = _generoMusica








""" class Auto():
    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo con 18 ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento() """








""" from enum import Enum

class EntidadFinanciera(Enum):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD" """


"""
EJERCICIO

Enunciado
Se desea implementar la lógica de un dispositivo POSNET
que procesa pagos con tarjetas de crédito.
Las tarjetas de crédito guardan el nombre de la entidad financiera a la que pertenecen (únicamente
Visa o Mastercard), el nombre de la entidad bancaria, el número de tarjeta, el saldo disponible y
los datos del titular (DNI, nombre, apellido, teléfono y mail). Cada vez que se cree una nueva tarjeta,
deberán indicarse todos estos datos.
A la hora de abonar, el POSNET recibiría la tarjeta con la que desea hacerse el pago, junto con el
monto que se desea abonar y la cantidad de cuotas (de 1 a 6).
Si el pago es en 1 cuota, no se genera ningún recargo, de lo contrario, el monto se incrementará en
un 3% por cada cuota superior a 1. (Ejemplo: Pagar en 4 cuotas representará un 9% de incremento).
El POSNET debe chequear que la tarjeta tenga saldo suficiente para poder efectuar el pago junto
con el recargo, si hubiese. En caso de éxito, debe generar y retornar (no mostrar) un ticket donde
consten los siguientes datos:
▪ Nombre y apellido del cliente.
▪ Monto total a pagar.
▪ Monto de cada cuota.
Si la operación no tuvo éxito, se retornará null.
Puntos a desarrollar
1)Desarrollar el diagrama de clases UML que modele lo enunciado y donde consten las clases con
sus atributos, métodos y relaciones (los constructores pueden omitirse).
2)Crear un proyecto en Java que resuelva:
A) Desarrollar, en la clase Posnet, el método efectuarPago(), cuyos parámetros, lógica y
valor de retorno deben deducirse según lo enunciado. Desarrollar también los métodos
derivados que puedan surgir de él para conseguir el objetivo.
B) Desarrollar el método main del proyecto y generar las instancias necesarias para poder
efectuar un pago de $10000 en 5 cuotas, usando una tarjeta de crédito con saldo
disponible de $15000 (el resto de los datos, pueden inventarse a gusto).

"""