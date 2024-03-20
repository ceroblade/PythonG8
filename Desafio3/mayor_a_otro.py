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

informe = {} #declarando un diccionario vacio


print("Los meses que superan el umbral de", umbral, "son :" )
for mes, valor in ventas.items():
    if valor > umbral :
        informe[mes] = valor
print(f"Los meses y valores son: {informe}")
    
#Ejemplo Añadiendo clave valor a un diccionario
#ventas["lunes"] = 2000
#print(ventas)