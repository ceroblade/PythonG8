# Solicitar ingreso precio de suscripcion
precio_suscripcion = float(input("Ingrese el precio de suscripcion: "))
# Solicitar ingreso de numero de usuarios
numero_usuario = int(input("Ingrese numero de usuarios: "))
# Solicitar que se ingrese los gastos totales
gastos_totales = float(input("Ingrese gastos totales: "))

# Calcular el precio total con el aumento del 50% por usuario
precio_total = precio_suscripcion * 1.5

# Calcular las utilidades
utilidades = precio_total * numero_usuario - gastos_totales

utilidad_anterior = float(input("Ingrese utilidades del año anterior: "))

utilidades_totales = utilidades - utilidad_anterior

# Mostrar el resultado de las utilidades
print("Las utilidades son ${:.2f}".format(utilidades_totales))