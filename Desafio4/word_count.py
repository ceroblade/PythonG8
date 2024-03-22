with open("lorem_ipsum.txt", "r", encoding="utf-8") as file:
    texto = file.read()

caracteres_distintos = len(set(texto))

palabras = texto.split()
palabras_distintas = len(set(palabras))

print("Cantidad de caracteres distintos:", caracteres_distintos)
print("Cantidad de palabras distintas:", palabras_distintas)