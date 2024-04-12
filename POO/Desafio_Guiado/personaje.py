class Personaje:
    def __init__(self, nombre, nivel=1, exp=0):
        self.nombre = nombre
        self.nivel = nivel
        self.exp = exp

    def get_estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.exp}"

    def set_estado(self, nivel, exp):
        self.nivel = nivel
        self.exp = exp

    def __lt__(self, otro):
        return self.nivel < otro.nivel

    def __gt__(self, otro):
        return self.nivel > otro.nivel

    def __eq__(self, otro):
        return self.nivel == otro.nivel

    def calcular_probabilidad_ganar(self, otro_personaje):
        
        pass

    def enfrentamiento_con_orco(self, probabilidad):
        
        pass
