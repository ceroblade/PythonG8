from pizza import Pizza
print("Tamaño y Precio de la Pizza:")
print(Pizza.tamanio, Pizza.precio)

print("¿La salsa de tomate está presente en la lista?")
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

mi_pizza = Pizza()
mi_pizza.realizar_pedido()

print("\nIngredientes y tipo de masa:")
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Primer ingrediente vegetal:", mi_pizza.ingrediente_vegetal_1)
print("Segundo ingrediente vegetal:", mi_pizza.ingrediente_vegetal_2)
print("Tipo de masa:", mi_pizza.tipo_masa)
print("¿La Pizza es Valida?", mi_pizza.pizza_valida)