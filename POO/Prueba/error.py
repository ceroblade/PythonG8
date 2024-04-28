class SubTipoInvalidoError(Exception):
    def __init__(self, mensaje, sub_tipo):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.sub_tipo = sub_tipo

    def __str__(self):
        print(f"El subtipo {self.sub_tipo} no es válido.")

class LargoExcedidoError(Exception):
    def __init__(self, mensaje, sub_tipo):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.sub_tipo = sub_tipo

    def __str__(self):
        print(f"El largo del nombre no debe exceder los 250 caracteres")