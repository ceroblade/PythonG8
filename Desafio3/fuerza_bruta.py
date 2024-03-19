# Importación del módulo ascii_lowercase del módulo string
from string import ascii_lowercase

# Solicitud de la contraseña al usuario y conversión a minúsculas
password = input("Ingrese la contraseña: ").lower()

# Inicialización del contador de intentos
intentos = 0

# Bucle externo para iterar sobre cada letra de la contraseña
for letra in password:
    # Bucle interno para iterar sobre cada letra del alfabeto
    for guess in ascii_lowercase:
        # Incremento del contador de intentos en 1 en cada iteración
        intentos += 1
        # Comparación de la letra de la contraseña con la letra del alfabeto actual
        if letra == guess:
            # Si las letras coinciden, se interrumpe el bucle interno
            break

# Mensaje de salida indicando el número total de intentos realizados
print("Se adivinó la palabra en", intentos, "intentos.")