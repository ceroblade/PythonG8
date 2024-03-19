while True:
    respuesta = input("¿La persona responde a estimulos? (si/no): ")
    
    if respuesta.lower() == "si":
        necesidad_traslado = input("¿Se necesita trasladar al hospital? (si/no): ")
        if necesidad_traslado.lower() == "si":
            print("Trasladando al hospital")
            break
        else:
            print("Abrir via aerea")
    else:
        respira = input("¿La personaa respira? (si/no): ")
        if respira.lower() == "si":
            print("Permitir ventilacion")
        else:
            administrar_ventilacion = input("¿Se debe administra ventilacion? (si/no): ")
            if administrar_ventilacion.lower() == "si":
                print("Llamar ambulancia")
                break
            else:
                print("Realizar RCP")
    
    llego_ambulancia = input("¿Llego la ambulancia? (si/no): ")
    if llego_ambulancia.lower() == "si":
        print("Salir del programa")
        break