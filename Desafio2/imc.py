peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Su IMC es {imc:.2f}, lo que corresponde a la clasificación de Bajo Peso según la OMS.")
elif imc < 25:
    print(f"Su IMC es {imc:.2f}, lo que corresponde a la clasificación de Adecuado según la OMS.")
elif imc < 30:
    print(f"Su IMC es {imc:.2f}, lo que corresponde a la clasificación de Sobrepeso según la OMS.")
elif imc < 35:
    print(f"Su IMC es {imc:.2f}, lo que corresponde a la clasificación de Obesidad Grado I según la OMS.")
elif imc < 40:
    print(f"Su IMC es {imc:.2f}, lo que corresponde a la clasificación de Obesidad Grado II según la OMS.")
else:
    print(f"Su IMC es {imc:.2f}, lo que corresponde a la clasificación de Obesidad Grado III según la OMS.")