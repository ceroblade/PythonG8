import random

opciones = ["piedra", "papel", "tijera"]

jugador = input("Elige piedra, papel o tijera: ").lower()

if jugador not in opciones:
    print("Opción no válida. Por favor, elige piedra, papel o tijera.")
else:
    computadora = random.choice(opciones)

    if jugador == computadora:
        print("Empate")
    elif jugador == "piedra":
        if computadora == "tijera":
            print("Ganaste. La computadora eligió tijera.")
        else:
            print("Perdiste. La computadora eligió papel.")
    elif jugador == "papel":
        if computadora == "piedra":
            print("Ganaste. La computadora eligió piedra.")
        else:
            print("Perdiste. La computadora eligió tijera.")
    else:  # jugador == "tijera"
        if computadora == "papel":
            print("Ganaste. La computadora eligió papel.")
        else:
            print("Perdiste. La computadora eligió piedra.")