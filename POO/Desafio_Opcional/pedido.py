from te import Te

print('Ingresar numero segun tipo de te')
print('1 - Te Negro')
print('2 - Te Verde')
print('3 - Infusion')
tipo_te = int(input())

print('Ingresar el formato que desea en numeros')
print('300 gramos')
print('500 gramos')
formato = int(input())

precio = Te.precio_te(formato)

tiempo, recomendacion = Te.tiempo_recomendacion(tipo_te)

print('Detalle de su pedido')
print('********************')
print('tipo de te:')
if tipo_te == 1:
    print('Te Negro')
elif tipo_te == 2:
    print('Te Verde')
elif tipo_te == 3:
    print('Infusion de Hierbas')
print('Formato:', formato, 'gramos')
print('Precio: $', precio)
print('Recomendaciones:', recomendacion,'. El tiempo de preparacion son:', tiempo, 'minutos')