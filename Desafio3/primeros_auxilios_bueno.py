respuesta = input("¿La persona responde a estimulos? (si/no): ")
if respuesta == "si":
        print("Trasladando al hospital")
else:
    print("Abrir via aerea")
    respira = input("¿La persona respira? (si/no): ")
    if respira == "si":
        print("Permitir ventilacion")
    else:
        print("administrar ventilacion")
        llego_ambulancia ="no"    
        while llego_ambulancia == "no":
                signos_vida = input("Tiene signos vitales? (si/no): ")
                if signos_vida == "si":
                    print("Evaluar espera de ambulancia")
                else:
                    print("Administrar RCP")
                llego_ambulancia=input("llego ambulancia? (si/no): ")
