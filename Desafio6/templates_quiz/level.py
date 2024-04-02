def choose_level(n_pregunta, p_level):
    if p_level == 2:
        if n_pregunta <= 2:
            return "basicas"
        elif n_pregunta <= 4:
            return "intermedias"
        else:
            return "avanzadas"
    elif p_level == 3:
        if n_pregunta <= 3:
            return "basicas"
        elif n_pregunta <= 6:
            return "intermedias"
        else:
            return "avanzadas"
    
    return choose_level

if __name__ == '__main__':
    
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias