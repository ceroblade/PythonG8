from abc import ABC, abstractmethod

class Material(ABC):
    @abstractmethod
    def romper(self):
        pass

class MaterialPlastico(Material):
    nombre = "Plástico"
    duracion = "Corta"

    def __init__(self, textura: str):
        self.textura = textura

    def romper(self):
        pass

class Pelota():
    def __init__(self, tamanio: int, color: str, textura: str):
        self.tamanio = tamanio
        self.color = color
        self.textura = textura
        # La pelota está compuesta por un componente material
        self.__material = MaterialPlastico(self.textura)

p = Pelota(16, "Amarillo", "Lisa")
# Salida: Plástico
print(p.__material.nombre)
print(p.__material.textura)