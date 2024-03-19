while True:
    respuesta = input("¿Responde a estímulos? (sí/no): ")
    
    if respuesta.lower() == "sí":
        necesidad_traslado = input("¿Se valora la necesidad de trasladar al hospital? (sí/no): ")
        if necesidad_traslado.lower() == "sí":
            print("Trasladar al hospital.")
            break
        else:
            print("Abrir vía aérea.")
    else:
        respira = input("¿Respira? (sí/no): ")
        if respira.lower() == "sí":
            print("Permitir ventilación.")
        else:
            administrar_ventilacion = input("¿Se administra ventilación? (sí/no): ")
            if administrar_ventilacion.lower() == "sí":
                print("Llamar ambulancia.")
                break
            else:
                print("Realizar RCP.")
    
    llego_ambulancia = input("¿Llegó la ambulancia? (sí/no): ")
    if llego_ambulancia.lower() == "sí":
        print("Salir del programa.")
        break