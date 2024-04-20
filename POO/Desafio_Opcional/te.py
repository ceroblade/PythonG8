class Te():
    precio_1 = 3000
    precio_2 = 5000
    
    @staticmethod
    def tiempo_recomendacion(tipo_te):
        if tipo_te == 1:
            return 3, 'Recomendado al desayuno'
        elif tipo_te == 2:  
            return 5, 'Recomendado al mediodia'
        else:
            return 6, 'Recomendado al atardecer'
    
    @staticmethod
    def precio_te(gramos):
        if gramos == 300:
            return Te.precio_1
        else:
            return Te.precio_2