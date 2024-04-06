class Pizza:
    ingredientes = {
        "proteicos": ["pollo", "vacuno", "vegetal"],
        "vegetales": ["tomate", "champiñon", "aceitunas"],
        "masas": ["tradicional", "delgada"],
    }
    precio = 10000
    tamanio = "familiar"
    
    @staticmethod
    def validar_elemento(elemento, posibles_valores):
        return elemento in posibles_valores

    def realizar_pedido(self):
        self.ingrediente_proteico = input("Ingresar ingrediente proteico:  (pollo / vacuno / vegetal): ")
        self.ingrediente_vegetal_1 = input("Ingresar primer ingrediente vegetal:  (tomate / champiñon / aceitunas): ")
        self.ingrediente_vegetal_2 = input("Ingresar  segundo ingrediente vegetal:  (tomate / champiñon / aceitunas): ")
        self.tipo_masa = input("Ingresar tipo de masa (tradicional / delgada): ")

        if (self.validar_elemento(self.ingrediente_proteico, self.ingredientes["proteicos"]) and
            self.validar_elemento(self.ingrediente_vegetal_1, self.ingredientes["vegetales"]) and
            self.validar_elemento(self.ingrediente_vegetal_2, self.ingredientes["vegetales"]) and
            self.validar_elemento(self.tipo_masa, self.ingredientes["masas"])):
            self.pizza_valida = True
        else:
            self.pizza_valida = False
            print("Pizza no Valida")