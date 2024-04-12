from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, producto):
        for p in self.__productos:
            if p.nombre == producto.nombre:
                p.stock += producto.stock
                return
        self.__productos.append(producto)

    def listar_productos(self):
        return

    def realizar_venta(self, nombre_producto, cantidad):
        pass

class Restaurante(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def listar_productos(self):
        lista = ""
        for producto in self._Tienda__productos:
            lista += f"{producto.nombre}: ${producto.precio}\n"
        return lista

class Supermercado(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def listar_productos(self):
        lista = ""
        for producto in self._Tienda__productos:
            mensaje = "Pocos productos disponibles" if producto.stock < 10 else ""
            lista += f"{producto.nombre}: ${producto.precio} ({mensaje}{producto.stock})\n"
        return lista

class Farmacia(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def listar_productos(self):
        lista = ""
        for producto in self._Tienda__productos:
            mensaje = "Envio gratis al solicitar este producto" if producto.precio > 15000 else ""
            lista += f"{producto.nombre}: ${producto.precio} {mensaje}\n"
        return lista