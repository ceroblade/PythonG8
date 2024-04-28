from abc import ABC, abstractmethod

class Anuncio(ABC):
    def __init__(self, formato, ancho, alto, url_archivo=None, url_click=None, sub_tipo=None):
        self.__ancho = max(1, ancho) if ancho else 1
        self.__alto = max(1, alto) if alto else 1
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.formato = formato
        self.sub_tipo = sub_tipo

    # Propiedades y setters para ancho, alto, url_archivo, url_click

    @staticmethod
    def mostrar_formatos(formato, SUB_TIPOS):
        print(f"Los subtipos del formato: {formato} son:")
        for sub_tipo in SUB_TIPOS:
            print(f"- {sub_tipo}")

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass