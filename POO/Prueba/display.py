from anuncio import Anuncio

class Display(Anuncio):
    def __init__(self, ancho, alto, sub_tipo, url_archivo=None, url_click=None):
        super().__init__("Display", ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio(self):
        print("Comprimiendo anuncio Display...")

    def redimensionar_anuncio(self):
        print("Redimensionando anuncio Display...")