#Importacion siempre en primera linea
import os
import math

#operadores
print(2 ** 4) #Exponenciación/Potencia. Ej: 2 elevado a 4 es 16
print(5 // 2) #División Entera. Ej: 5 dividido 2 es 2.
print(5 / 2) #División con decimales. Ej: 5 dividido 2 es 2.5
print(5 % 2) #Módulo. Ej: 5 Módulo 2 es 1. 1 es el resto de 5 // 2

x = 10
y = 5
z = 2
resultado=((x - y) * z + y)
print(resultado)

print(os.getcwd()) #Ruta en C:
print(math.sqrt(9)) #Raiz cuadrada

from math import ceil # importa sólo la función ceil
print(ceil(3.14)) # ceil aproxima al entero superior


