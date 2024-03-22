import sys

tasas = [float(arg) for arg in sys.argv[1:4]]
valor_en_pesos = float(sys.argv[4])

sol_peruano = round(valor_en_pesos * tasas[0])
peso_argentino = round(valor_en_pesos * tasas[1])
dolar_americano = round(valor_en_pesos * tasas[2])

print("Valor en Sol Peruano:", sol_peruano)
print("Valor en Peso Argentino:", peso_argentino)
print("Valor en Dolar Americano:", dolar_americano)