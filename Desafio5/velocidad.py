def calcular_promedio(velocidades):
    if not velocidades:
        return 0
    suma_velocidades = sum(velocidades)
    total_correas = len(velocidades)
    return suma_velocidades / total_correas

def correas_sobre_promedio(velocidades):
    promedio = calcular_promedio(velocidades)
    correas_sobre_promedio = []
    for i in range(len(velocidades)):
        if velocidades[i] > promedio:
            correas_sobre_promedio.append(i)
    return correas_sobre_promedio

velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

correas_sobre_promedio = correas_sobre_promedio(velocidad)

print(correas_sobre_promedio)
