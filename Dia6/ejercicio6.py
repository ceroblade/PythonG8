""" 
Determinar si un numero ingresado por el usuario
es par o impar
utilizaremos el modulo
"""
#paso 1: solicitud de ingreso de datos
numero = input("Ingresa numero a evaluar\n")
#paso 2: transformar string a numeros
numero = int(numero)
#paso 3: evaluar con las condicionales
if numero == 0:
    print("El numero ingresado es cero")
elif numero%2 == 0: 
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")
    
    
# 0/2 = 0
0
# -35/2 = -17
1