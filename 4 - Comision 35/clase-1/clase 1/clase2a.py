# TIPOS DE DATOS
""" nombre = "Juan"
apellido = "Perez"
nombreCompleto = f'{nombre} {apellido}'
oldNombreCompleto = nombre + " " + apellido
mensaje = f'Hola! mi nombre es {nombreCompleto} y tengo {edad} anios'
print(mensaje) """

# NUMERICOS
# int - Numero entero (sin coma)
# numInt = 46
# float - Numero con decimal (con punto)
# numFloat = 32.6

# TEXTO - String - CADENA DE CARACTERES
# saludo = "Buen día !"

# BOOLEAN - GRADO 0 INFORMÁTICA - 0 Y 1 - True o False
# convencion escribir nombres variables - como si fueran una pregunta
# esEstudiante = True

# OPERADORES ----------------

# Aritméticos

num1 = 28
num2 = 66

print(num1 + num2) #suma
print(num1 - num2) #resta
print(num1 * num2) #multiplicacion
print(num1 / num2) #división
print(num1 // num2) #division + trunca del resultado (int)
print(num1 % 2) #modulo + chequear si un numero es o no par
print(num1 ** 2) #exponente

# ASIGNACIÓN

# ASIGNACIÓN (=) =/= COMPARACIÓN (==)

numero = 20 # "la variable que se llama número ES 20."

resultado = 18
print(numero != resultado) # "¿la variable que se llama número ES IGUAL A 20?" SI / NO (V/F) BOOL

# TODOS DEVUELVEN BOOLEANOS (TRUE O FALSE)
# (=) asignación 
# (==) igual que
# (!=) distinto que
# SOLO SE PUEDEN USAR CON TIPO DE DATO NUMÉRICO (INT O FLOAT)
# (<) menor
# (<=) menor o igual
# (>) mayor
# (>=) mayor o igual

n1 = 20
n2 = 20
print(n1 <= n2)
print(n1 <= n2)
print(n1 > n2)
print(n1 >= n2)

# operacion matemática + asignan nuevo valor

numero1 = 20
print(numero1)
numero1 = 21 # AHORA QUIERO QUE LA VARIABLE VALGA 21
print(numero1)

saludo = "Hola"
print(saludo)
saludo += " mundo"
print(saludo)

# operadores LOGICOS - AND Y OR

# nuclear diferentes condiciones bajo un mismo resultado (bool) true o false

#  matinee - 2 condiciones a cumplir
# 1. edad mayor o igual a 13 años
# 2. edad menor o igual a 17 años

# AND - conjunción
# V + V = V
# V + F = F
# F + V = F
# F + F = F

# OR - disyunción
# V + V = V
# V + F = V
# F + V = V
# F + F = F

""" edad = 21
print((edad >= 13) and (edad <= 17)) """
#           v      and      v         = V

# BOLICHE + MATINEE
# mayor o igual a 18 años, podes pasar al boliche
# sos menor de 18, pero tenes entre 13 y 17 , podes ir a la matinee, 
# si sos menor a 12, chau


edad = 15
cumpleAnios = True

print("inicio")
# todos los numeros
if(edad >= 18):
    # 18 a infinito
    print(f'tenes {edad} anios, podes pasar al boliche!')
    if(cumpleAnios):
        print("Feliz cumple! te ganaste un trago")
    else:
        print("no te podemos regalar nada porque no es tu cumple")
elif((edad >= 13) and (edad <= 17)):
    # 13 a 17
    print(f'tenes {edad} anios, NO podes ir al boliche, pero SI a la matinee')
    if(cumpleAnios):
        print("Feliz cumple! te ganaste una gaseosa")
    else:
        print("no te podemos regalar nada porque no es tu cumple")
else:
    # 12 a menos infinito
    print(f'tenes {edad} anios, NO podes pasar a nada!!')
print("fin")
