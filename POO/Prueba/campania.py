from datetime import date
from display import Display
from social import Social
from video import Video
from error import LargoExcedidoError, SubTipoInvalidoError

class Campania:
    def __init__(self, nombre, fecha_inicio, fecha_termino):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.anuncios = []

    def crear_anuncio(self):

        pass

nombre_campania = input("Ingrese el nombre de la campaña: ")
fecha_inicio = input("Ingrese la fecha de inicio: ")
fecha_termino = input("Ingrese la fecha de término: ")

campania = Campania(nombre_campania, fecha_inicio, fecha_termino)
print(campania)

crear_anuncio = ""
while crear_anuncio != "no":
    anuncio = campania.crear_anuncio()
    crear_anuncio = input("¿Desea crear otro anuncio? si/no ")

print("Los anuncios creados son:")
for anuncio in campania.anuncios:
    print(anuncio.formato)