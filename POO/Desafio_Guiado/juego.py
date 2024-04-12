from random import randint
from personaje import Personaje

class Juego:
    def __init__(self):
        print("Bienvenido a Gran Fantasia")
        nombre_personaje = input("Por favor indica el nombre de tu personaje: ")
        self.personaje = Personaje(nombre_personaje)
        print(self.personaje.get_estado())

    def enfrentar_orco(self):
        print("¡Oh no!, ¡Ha aparecido un Orco!")
        probabilidad_ganar = self.calcular_probabilidad_ganar()
        print(f"Con tu nivel actual, tienes {probabilidad_ganar}% de probabilidades de ganarle al Orco.")
        opcion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")

        if opcion == "1":
            if randint(0, 1) == 0:
                print("¡Le has ganado al orco, felicidades!")
                self.personaje.exp += 50
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                self.personaje.exp -= 30
        else:
            print("¡Has huido! El orco ha quedado atrás.")

        print(f"¡Recibirás {self.personaje.exp} puntos de experiencia!")
        print(self.personaje.get_estado())

    def calcular_probabilidad_ganar(self):
        return 50

if __name__ == "__main__":
    juego = Juego()
    juego.enfrentar_orco()
