# las separacion de los decimales es con punto (.)
# la division entre integers sera como resultado un float

print(4/2) #resultados enteros siempre sera con decimales
print(5/2)
print(5/3.5)
print(2.4*4)

nombre = "Alexis"
año = "2024"
print(3*nombre)
print(2*año) # se puede multiplicar un string

# no se puede dividir un string
mes = 3
dia = 7

print(f"Hola {nombre}, El año es {año} del mes {mes} y el dia {dia}") #interpolacion de cadenas

#string.format
#print("",format())

print("Hola {}, el año es {} del mes {} y el dia {}".format(nombre,año,mes,dia))

#Metodo Count -> busca cuantras veces se encuentra un caracter en un string

print("Saitama".count("a"))
print(nombre.count("i"))

#Metodo upper y lower cualquiera de las 2 formas funciona
print("Alexis".upper())
print(nombre.lower())

#Metodo title primera letra mayuscula
print(nombre.title())
print("aLEXIS".title())

nombre = input("Ingrese Su Nombre: ")

# len() -> contar los caracteres de una string
print(len(" israel palma 2024"))#18

#join -> unir string separados en un solo string
print(", ".join(["mijail","palma","loren"]))

#imprimir en mas de una linea (\n)
print("escribir\ncualquier\ncosas")
"""
escribir
cualquier
cosas
"""

mi_direccion = ""
miDireccion = ""
cantidad_alumnos= 30
peso = 85.5
verdadero= True

#Tipo de datos type(nombre_variable)
print(type(nombre))#<class 'str'>
print(type(año))#<class 'str'>
print(type(mes))#<class 'int'>
print(type(peso))#<class 'float'>
print(type(verdadero))#<class 'bool'>

type(verdadero) # no imprime el tipo de dato

#Manipulacion Variables

numero = 2
numero = numero + 3 #numero = 2 + 3
print(numero)#5

nombre = nombre + "Palma" # nombre = "Mijail"+"Palma"
print(nombre)#MijailPalma

#precision de datos 
print(5/9)#0.5555555555555556
print(f"resultado de la division {5/9:.2f}")
print("el resultado de la division",round(5/9,3))


nombre = input("Ingrese su Nombre:  ")
print("Tu nombre es",nombre)
print(f"Tu nombre es {nombre}")

edad = input("Ingrese su Edad:  ")
print("Tu tienes",edad,"años")
print(type(edad))