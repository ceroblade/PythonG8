class DetalleVentaItem():
    def __init__(self, producto: str, cantidad: int):
        self.__producto = producto
        self.__cantidad = cantidad

    ##getters
    @property
    def producto(self):
        return self.__producto
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    ##setters
    @producto.setter
    def producto(self,producto: str):
        self.__producto = producto
    
    @cantidad.setter
    def cantidad(self, cantidad: int):
        self.__cantidad = cantidad

    def __str__(self):
        
        return f"{self.producto} - {self.cantidad}"
        
class DetalleVenta():
    def __init__(self):
        self.__items = []

    def agregar_item(self, item: DetalleVentaItem):
        self.__items.append(item)

    def __str__(self):
        retorno = (":::::::: DETALLE DE ESTA VENTA :::::::::\n PRODUCTO\tCANTIDAD\n")
    

        items = [
            f"{i.producto}\t\t{i.cantidad}\n" for i in self.__items
        ]
        return f"{retorno}{''.join(items)}"

class Venta():
    def __init__(self):
        self.__detalle = DetalleVenta()
    
    def modificar_detalle(self, producto: str, cantidad: int):
        detalle_venta_item = DetalleVentaItem(producto, cantidad)#objeto
        self.__detalle.agregar_item(detalle_venta_item)

    @property
    def detalle(self):
        return self.__detalle