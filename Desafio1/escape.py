import math

# Solicitar al usuario que ingrese el radio en kilómetros
# una sola linea radio_km = float(input("Ingrese el radio en kilómetros: ")) * 1000

radio_km = float(input("Ingrese el radio en kilómetros: "))
# Convertir el radio a metros
radio_m = radio_km * 1000

# Solicitar al usuario que ingrese la constante g
constante_g = float(input("Ingrese la constante g en m/s^2: "))

# Calcular la velocidad de escape
velocidad_escape = math.sqrt(2 * constante_g * radio_m)

# Mostrar el resultado
print("La velocidad de escape es {:.1f} [m/s]".format(velocidad_escape))