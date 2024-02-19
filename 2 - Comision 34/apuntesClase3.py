# Colecciones de datos / tipos complejos

# [] Listas ----------------------------------------------------------------
""" 
diasSemana = [   #pos  #elementos
    "Lunes",     #0     1
    "Martes",    #1     2
    "Miercoles", #2 
    "Jueves",    #3
    "Viernes",   #4
    "Sabado",    #5
    "Domingo"    #6     7
    ]

meses = [
    "Enero",
    "Febrero",
    "Marzo"
]

# print(diasSemana)
# acceder individualmente a un elemento
# diasSemana[2]

# modificar individualmente un elemento
# diasSemana[2] = "Cualquier Cosa"


# agregar elemento al final de la lista
diasSemana.append("Feriado")

# añade una lista a otra preexistente
diasSemana.extend(meses)

# agregar elemento en un index específico
diasSemana.insert(0, "Feriadooo")

# eliminar un elemento el último o el aclarado en index
diasSemana.pop(5) """

""" # elimina elemento si consigue elem específico
diasSemana.remove("Sabado")

# por cada día de la semana...
for dia in diasSemana:
    #hace un print de ese día
    print(dia) """

""" 
listaNums = [4, 2, 65, 43,  6, 5,85, 254, 9,34,1234]
 """
"""
listaNums.sort()
listaNums.reverse()
"""

""" for numero in listaNums:
    #hace un print de ese día
    print(numero) """

# TUPLAS ----------------------------------------------------------------
""" 
preposiciones = (  
    "A",     
    "ANTE",    
    "BAJO",
    "CON",    
    "CONTRA", 
)

print(preposiciones.count("BAJO"))
print(preposiciones.index("BAJO")) """

# objetos - entidades con características

# key - value
""" 
persona = {
    #        ITEM
    # KEYS           VALUES
    "nombre"       : "Juan",
    "apellido"     : "Gomez",
    "edad"         : 23,
    "altura"       : 1.80,
    "promedioNotas": [9,6,8],
    "esEstudiante" : False
}

print(persona["nombre"]) """

# GET
""" resultado = persona.get("nombre")
print(resultado) """

# keys + values = items
""" print(persona.keys())
print(persona.values())
print(persona.items()) """

# persona.pop("promedioNotas")
""" print(persona.items())
persona.clear()
print(persona.items()) """






















# FUNCIONES

# declaré y definí mi función
def sumar_iva(precioInicial):
    precioConIva = precioInicial * 1.21
    return precioConIva       

# ALGORITMO
# 1. entrada de datos
# 2. procesamiento de datos - cuerpo de la función
# 3. el retorno de datos

# ejecutarla 
print(sumar_iva(4500))
print(sumar_iva(12600))
print(sumar_iva(3900))

def saludar(nombre, apellido, curso):
    saludo = f'Hola {nombre} {apellido}! '
    bienvenida= f'Bienvenido al curso de {curso}'
    return saludo + bienvenida

print(saludar("Pepe", "Martinez", "Python"))
print(saludar("Tito", "Rodriguez", "Java"))