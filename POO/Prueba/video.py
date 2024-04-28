from anuncio import Anuncio

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, ancho, alto, duracion, sub_tipo, url_archivo=None, url_clic=None):
        super().__init__(Video.FORMATO, ancho, alto, url_archivo, url_clic, sub_tipo)
        self.__duracion = max(5, duracion)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")