# Solicitar ingreso precio de suscripcion
precio_suscripcion = int(input("Ingrese el precio de suscripcion: "))
# Solicitar ingreso de numero de usuarios
numero_usuario = int(input("Ingrese numero de usuarios: "))
# Solicitar que se ingrese los gastos totales
gastos_totales = int(input("Ingrese gastos totales: "))

# Calcular las utilidades
utilidades1 = precio_suscripcion * numero_usuario - gastos_totales

# Mostrar el resultado de las utilidades
print("Las utilidades son $",utilidades1,"pesos")