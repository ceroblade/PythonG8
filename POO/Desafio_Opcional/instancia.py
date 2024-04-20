from te import Te

# Se crean dos instancias
instancia_1 = Te()
instancia_2 = Te()

# Se guardan los tipos de la variable
instancia1 = type(instancia_1)
instancia2 = type(instancia_2)

print('La instancia 1 es de tipo', instancia1)
print('La instancia 2 es de tipo', instancia2)

if instancia1 == instancia2:
    print('Ambos objetos son del mismo tipo')
else:
    print('Los objetos no son del mismo tipo')
    