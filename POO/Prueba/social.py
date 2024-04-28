from anuncio import Anuncio

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho, alto, sub_tipo, url_archivo=None, url_clic=None):
        super().__init__(Social.FORMATO, ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS SOCIAL NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIÓN DE ANUNCIOS SOCIAL NO IMPLEMENTADA AÚN")