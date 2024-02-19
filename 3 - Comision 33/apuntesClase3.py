# funciones


# ALGORITMO.
# 1. ENTRADA DE DATOS
# 2. PROCESAMIENTO DE DATOS
# 3. RETORNO DE LOS DATOS

def sumar_iva(
        nombre = "Admin",
        precio = 100 ,
        porcentajeIva = 1.10
    ): # 1. ENTRADA DE DATOS
    # 2. PROCESAMIENTO DE DATOS
    precioConIva = precio * porcentajeIva
    saludo =  f'hola {nombre} precio final: {precioConIva}'
    return saludo # 3. RETORNO DE LOS DATOS

# atributos / parámetros
# "variables"  dentro del contexto de una funcion

# llamar en distintos lugares a x funcionalidad 
print(sumar_iva("Marcos", 3400, 1.21)) # 1. ENTRADA DE DATOS
print(sumar_iva("Claudia", 1900, 1.18))
print(sumar_iva("Pepe", 6450, 1.10))
print(sumar_iva("Tito", 1030, 1.15))
print(sumar_iva("Jose", 854, 1.2))
print(sumar_iva())




















# Colecciones de datos

# 1. LISTAS --------
nombres = ["Juan", "Carlos", "Pedro", "Luis"]

for e in nombres :
    print(e)

# objetos/diccionarios - representar ENTIDADES (personas, objetos)

print(" ----------------- ")
persona1 = {
    "nombre" : "Juan",
    "apellido" : "Perez",
    "edad" : 30,
    "altura" : 1.80
}

# get - devuelve un elem a través de su key, si no lo encuentra -> default

# print(persona1.get("edad"))

# keys + values = items
""" print(persona1.keys())
print(persona1.values())
print(persona1)
print(persona1.items()) """


# print(persona1)
#persona1.pop("edad")  pop - eliminar un eleme del dict a través de su key
# print(persona1)
# persona1.clear()  clear - elimina todo lo que tiene el dict
# print(persona1)

# recorrer dictionario con un FOR IN

for dato in persona1.items():
    for e in dato :
        print(e)

""" apellidos = ["Perez", "Gomez", "Gonzalez"]


# elementos    1        2       3         4
# posición     0        1       2         3

# print(nombres)
nombres = "Hola"
print(nombres)

# Métodos para las listas - FUNCIONES específicas para las listas

# append - agregar un elemento al final de la lista

# print(nombres)

# insert - agregar un elemento en un indice determinado
nombres.insert(10, "Martina")
# print(nombres)

# extend - añadir una lista a otra lista preexistente
nombres.extend(apellidos)
# print(nombres)

# pop - elimina un elemento al final de la lista, o en un index especifico
nombres.pop()
# print(nombres)

# remove - elimina un elemento si consigue el elem específico

nombres.remove("Pedro") """
# print(nombres)
""" 
numeros = [34, 65, 12, 76, 15, 74, 265, 1, 4, 56, 123]
print(numeros)
numeros.reverse() # hace el orden inverso
print(numeros)
numeros.sort() # ordena de menor a mayor
print(numeros)
numeros.reverse() # hace el orden inverso
print(numeros)  """

# TUPLAS - INMUTABLES
""" 
diasSemana = (
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo"
)

# count - cuenta la cant de veces que aparece x elemento en una tupla
print(diasSemana.count(diasSemana[2]))

# index - devuelve la posicion del elemento de la tupla
print(diasSemana.index("Viernes")) """

# Bucle FOR

# coleccion de datos -> elementos

# for ... in 
# "por cada ELEMENTO en la lista NOMBRES --- HACE X COSA"

