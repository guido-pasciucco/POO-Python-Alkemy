
# boliche 18 o más años
# matinee entre 13 y 17 años

# 12 o menos - nada
# 13, 14, 15, 16, 17 - matinee
# 18 o más - boliche

edad = 19
esSuCumpleanios = True

print("inicio")
if (edad >= 18):
    print(f'Tenes {edad} anios, podes entrar al BOLICHE')
    if(esSuCumpleanios):
        print(f'Feliz cumple! te ganaste un trago')
elif ((edad >= 13 ) and (edad <= 17)):
    print(f'Tenes {edad} anios, Boliche no, pero podes entrar a la MATINEE')
    if(esSuCumpleanios):
        print(f'Feliz cumple! te ganaste una gaseosa')
else:
    print(f'Tenes {edad} anios, NO podes entrar a nada')
print("fin")






# 1. edad tiene que ser mayor o igual a 13
# 2. edad tiene que ser menor o igual a 17

#          V       and         F        = FALSE (cORRECTO)
#          V       or         F        = TRUE (INCORRECTO)
#print((edad >= 13) or (edad <= 17))

# AND - Conjunción
# V + V = V
# V + F = F
# F + V = F
# F + F = F

# OR - Disyunción
# V + V = V
# V + F = V
# F + V = V
# F + F = V



#Tipos de datos

# numérico - int (numero entero, sin comas)
# numEntero = 25

# numérico - float (numero con comas, con decimales)
# numFloat = 29.4

# boolean (verdadero/falso, 1 y 0)
# esCliente = True

# Texto - String (Cadena de caracteres)
# saludo = "Hola mundo!"

# OPERADORES
# Aritméticos

""" num1 = 10
num2 = 7


suma = num1 + num2
print(suma)

resta = num1 - num2
print(resta)

mult = num1 * num2
print(mult)

div = num1 / num2
print(div)

div = num1 // num2
print(div)

raizCuadrada = num1 ** num2
print(raizCuadrada) """

# ASIGNACIÓN - "ESTA VARIABLE ES!!!!! ESTE DATO"
# variable = "Hola"
#" Esta variable ES el string "Hola"
#print(variable)

# == COMPARACIÓN - "¿ESTA VARIABLE ES IGUAL A -ESTE DATO?" - devolvernos un boolean
#print(variable == "CHAU")  false

# != distinto que - lo opuesto a "igual que"
# print(variable != "CHAU") true - es verdad que es distinto de chau


""" print(edad == 18) # igual que
print(edad != 18) # distinto de 
print(edad > 18) # mayor que (19, 20, 21, ...)
print(edad >= 18) # mayor o igual que (18, 19, 20, ...)
print(edad < 18) # mayor que (19, 20, 21, ...)
print(edad <= 18) # mayor o igual que (18, 19, 20, ...)
 """

