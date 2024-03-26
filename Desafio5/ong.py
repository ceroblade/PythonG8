def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def productoria(lista):
    result = 1
    for num in lista:
        result *= num
    return result

def preguntar_operacion():
    while True:
        operacion = input("¿Qué operación desea realizar? (factorial / productoria): ").lower()
        if operacion == 'factorial' or operacion == 'productoria':
            return operacion
        else:
            print("Por favor, ingrese 'factorial' o 'productoria'.")

def calcular(operacion, valor):
    try:
        if operacion == 'factorial':
            valor = int(valor)
            print(f"El factorial de {valor} es {factorial(valor)}")
        elif operacion == 'productoria':
            lista = [int(x) for x in valor.split(',')]
            print(f"La productoria de {lista} es {productoria(lista)}")
    except ValueError:
        print("El valor debe ser un número entero para el factorial y una lista de números para la productoria.")

operacion = preguntar_operacion()

valor = input("Ingrese el valor para Factorial o la lista de valores separados por comas para productoria: ")

calcular(operacion, valor)