# Definición del diccionario 'ventas' que contiene las ventas mensuales
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

# Solicitud al usuario para ingresar el umbral y conversión a entero
umbral = int(input("Ingrese el Umbral: "))

# Creacion de un nuevo diccionario 'informe' mediante comprehensions, que contiene solo los meses y valores que superan el umbral ingresado por el usuario
informe = {mes: valor for mes, valor in ventas.items() if valor > umbral}

# Impresion de los meses que superan el umbral
print("Los meses que superan el umbral de", umbral, "son :" )
for mes, valor in informe.items():
    print(mes, ":", valor)