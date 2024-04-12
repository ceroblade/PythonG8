from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def crear_producto():
    nombre = input("Ingresar el nombre del producto: ")
    precio = float(input("Ingresar el precio del producto: "))
    stock = int(input("Ingresar el stock del producto: "))
    return Producto(nombre, precio, stock)

def crear_tienda():
    nombre = input("Ingresar el nombre de la tienda: ")
    costo_delivery = float(input("Ingresar el costo de delivery: "))
    tipo_tienda = input("Ingresar el tipo de tienda - Restaurante - Supermercado - Farmacia : ")
    if tipo_tienda.lower() == "restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo_tienda.lower() == "supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo_tienda.lower() == "farmacia":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no valido / Intente nuevamente...")
        return crear_tienda()

def main():
    tienda = crear_tienda()
    continuar = True
    while continuar:
        print("\n¿Que accion desea realizar?")
        print("1. Ingresar un producto")
        print("2. Listar productos existentes")
        print("3. Realizar una venta")
        print("4. Salir del programa")
        opcion = input("Ingresar el número de la opcion: ")
        if opcion == "1":
            producto = crear_producto()
            tienda.ingresar_producto(producto)
            print("Producto ingresado correctamente.")
        elif opcion == "2":
            print("Productos existentes:")
            print(tienda.listar_productos())
        elif opcion == "3":
            # Lógica para realizar una venta
            pass
        elif opcion == "4":
            continuar = False
            print("¡Hasta luego!")
        else:
            print("Opcion no volida. Intente nuevamente.")

if __name__ == "__main__":
    main()
