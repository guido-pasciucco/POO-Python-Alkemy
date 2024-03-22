
# PARÁMETROS 
# variable dentro de la función 


# ALGORITMOS.
# 1. ENTRADA DE DATOS
# 2. PROCESAMIENTO DE DATOS
# 3. RETORNO DE DATOS 

def sumar_iva(nombre, precio, porcIva):
    resultado = precio * porcIva
    saludo = f'Hola {nombre} precio total {resultado}' 
    return saludo


print(sumar_iva("Juan",100, 1.10)) # invocar / llamar a la función # 1. ENTRADA DE DATOS)
print(sumar_iva("Luis",2960, 1.18))
print(sumar_iva("Pepe",1650, 1.21))
print(sumar_iva("Carlos",850, 1.25))
print(sumar_iva("Carla", 496, 1.20))









# Colecciones de Datos

# LISTA - Array / ArrayList
nombres = ["Tito", "Juan", "Pepe", "Martina", "Luis", "John", "Mary", "Louis"]

#"POR CADA ELEMENTO "nombre" EN LA LISTA "nombres"...

for e in nombres:
    # "hacé lo siguiente..."
    print(e)


""" 
names = ["John", "Mary", "Louis"]

# posiciones   0       1       2         3
# elementos    1       2       3         4

print(nombres)

# append - agregar un elem al final de la lista
nuevoDato = "Lucia"
nombres.append(nuevoDato)
print(nombres)

# insert - agregar un elem en el indice indicado
nombres.insert(2, "Carla")
print(nombres)

# pop - elimina un elem al final de la lista o en el indice indicado
nombres.pop(4)
print(nombres)

# remove - elimina un elem si consigue el elem específico
nombres.remove("Tito")
print(nombres)

# extend - añadir una lista a otra lista preexistente

nombres.extend(names)
print(nombres) """

numeros = [16, 43, 25, 76, 44, 87, 555, 897,4325,23,4,2,7,6]

#print(numeros)
# sort - ordenar la lista de menor a mayor
""" numeros.sort()
print(numeros) """

""" # reverse - invertir el orden de la lista (sea cual sea)
numeros.reverse()
print(numeros)
"""
print("------------------")
diasSemana = (
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo"
) 

for e in diasSemana :
    print(e)


# count - devuelve la cant de veces que un elemento aparece en la tupla
# print(diasSemana.count("Lunes"))

# index - devuelve el indice (la posicion) del elemento en cuestión
# print(diasSemana.index("Viernes"))
print("------------------")
persona1 = {
    "nombre": "Pepe",
    "apellido":"Gomez",
    "edad": 30,
    "altura": 1.75
}

""" for dato in persona1.items():
    for e in dato :
        print(e) """
# edad : 30 
for p in persona1:
	print(f'{p}: {persona1[p]}')

""" 










# entidad (sus características) 
#    key        value
persona1 = {
    "nombre": "Pepe",
    "apellido":"Gomez",
    "edad": 30,
    "altura": 1.75
}

# key + value = items
print(persona1)
print(persona1.keys())
print(persona1.values())
print(persona1.items())


# get - devuelve un element con su key / si no lo encuentra -> default
resultado = persona1.get("apellido")
print(resultado)

# Eliminar elementos de mi diccionario

# pop - 
print(persona1)
persona1.clear()
print(persona1)



 """

