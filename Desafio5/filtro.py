import sys

def filtrar_productos(precios, umbral, modo='mayor'):
    productos_filtrados = []
    
    if modo == 'mayor':
        for producto, precio in precios.items():
            if precio > umbral:
                productos_filtrados.append(producto)
    elif modo == 'menor':
        for producto, precio in precios.items():
            if precio < umbral:
                productos_filtrados.append(producto)
    else:
        return "Lo sentimos, no es una operación válida"
    
    return productos_filtrados

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

if len(sys.argv) < 3:
    print("Debe proporcionar un umbral y un modo ('mayor' o 'menor').")
    sys.exit(1)

umbral = int(sys.argv[1])
modo = sys.argv[2]

if modo == 'mayor':
    productos = filtrar_productos(precios, umbral)
    if type(productos) == list:
        print("Los productos mayores al umbral son:", ", ".join(productos))
    else:
        print(productos)
elif modo == 'menor':
    productos = filtrar_productos(precios, umbral, modo='menor')
    if type(productos) == list:
        print("Los productos menores al umbral son:", ", ".join(productos))
    else:
        print(productos)
else:
    print("Lo sentimos, no es una operación válida")