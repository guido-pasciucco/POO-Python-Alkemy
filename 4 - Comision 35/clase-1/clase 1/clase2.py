edad = 54
esSuCumpleanios = True
print("comienzo")

if(edad >= 18):
    print(f'tenes {edad} anios, podes pasar al BOLICHE')
    if(esSuCumpleanios):
        print("Feliz cumple! Te ganaste un trago")
elif(edad >= 14 and edad <= 17):
    print(f'tenes {edad} anios, podes pasar a la MATINEE')
    if(esSuCumpleanios):
        print("Feliz cumple! Te ganaste una gaseosa")
else:
    print(f'tenes {edad} anios, no podes pasar a nada')

print("fin")

# debilmente tipado 
# no hace falta la declaración de los tipos de datos en las variables

# matinee - 14 a 17 años
# boliche + 18 años

#1. la edad tiene que ser mayor o igual a 14
#2. la edad tiene que ser menor o igual a 17

# operador lógico AND ("y")

# V + V = V
# V + F = F
# F + V = F
# F + F = F

#            v             f             f
#print((edad >= 14 ) and (edad <= 17)) 

# operador lógico OR ("o")

# V + V = V
# V + F = V
# F + V = V
# F + F = F
#             v             f             v 
# print((edad >= 14 ) or (edad <= 17)) 

# Dprint(edad not in range(14, 17))


# TIPOS DE DATOS PRIMITIVOS
# Numéricos
# int (entero)
# numeroEntero = 35
# float (con decimales)
# numeroConDecimales = 20.5
# STRINGS (CADENAS DE CARACTERES / TEXTO)
# saludo = "Bienvenidos al curso de Python"
# BOOLEAN (V/F)
""" esEstudiante = True """

# la variable num1 ES 14
""" num1 = 14
num2 = 35 """

# Operadores aritméticos

""" suma = num1 + num2
print(suma)

resta = num1 - num2
print(resta)

mult = num1 * num2
print(mult)

div = num1 / num2
print(div)

divInt = num1 // num2
print(divInt)

exp = num1 ** 3
print(exp)
 """
# = ASIGNANDO - "Esto ES esto otro"

