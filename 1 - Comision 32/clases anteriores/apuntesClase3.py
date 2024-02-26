# FUNCIONES DEL USUARIO 
# DECLARAR
# DEFINIR
# INVOCAR/ LLAMAR

def sumarIva(nombre = "Admin", precioSinIva = 1000, porcIva = 1.21): # Tomé como entrada el precio sin iva
    precioConIva = precioSinIva * porcIva # multiplique por 1.21 y lo plasmé en una variable
    mensaje = f'Hola {nombre}, precio final {precioConIva}'
    return mensaje # retorno esa variable

print(sumarIva())
print(sumarIva("Pepe", 1650, 1.21))
print(sumarIva("Tito", 4700, 1.18))
print(sumarIva("Laura", 9300, 1.10))

# ALGORITMO.
    # ENTRADA - el precio sin impuestos
    # PROCESAMIENTO - multiplicar por 1.21
    # RETORNO - el precio con IVA

# LISTAS ----------

#dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
# dias = [4, 5, 2, 76, 5, 2, 34, 473, 234, 1,3, 24, 64, 35, 621, 5]

#Insertar Elementos
""" dias.insert(3, False)
dias.append("Domingo") """

# Remover elementos
""" dias.pop(5)
dias.remove("Martes") """

#Organizar elementos de la lista
""" dias.sort()
dias.reverse() """

# iterar sobre la lista y hacer prints de cada uno de sus elementos
""" for dia in dias:
    print(f'#{dias.index(dia)} - {dia}') """

# TUPLAS --------------------
""" 
miTupla = (
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo"
) """

#Métodos de las tuplas

""" count = miTupla.count("Sabado")
print(count)

index = miTupla.index("Sabado")
print(index)
"""
# DICCIONARIOS -----------

""" persona1 = {
    "nombre": "Juan", 
    "apellido": "Perez", 
    "edad": 34
}

persona2 = {
    "nombre": "Carlos", 
    "apellido": "Gomez", 
    "edad": 40,
    "altura": 160
} """

""" print(persona2["nombre"]) """
# metodos

# get 
""" print(persona1.get("nombre")) """

# index + values = items
""" print(persona2.keys())
print(persona2.values())
print(persona2.items()) """

# remover un elemento con su index

""" persona2.pop("apellido")
print(persona2.items()) """

# elimina todos los elementos de un diccionario

""" persona1.clear()
print(persona1.items()) """
