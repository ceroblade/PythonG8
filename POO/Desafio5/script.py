import json
from usuario import Usuario

def crear_usuario_desde_json(json_str):
    try:
        usuario_data = json.loads(json_str)
        usuario = Usuario(**usuario_data)
        return usuario
    except Exception as e:
        with open("error.log", "a") as archivo_errores:
            archivo_errores.write(f"Error al crear usuario: {str(e)}\n")
        return None

with open("usuarios.txt", "r") as archivo_usuarios:
    usuarios_data = archivo_usuarios.readlines()

usuarios = []

for usuario_str in usuarios_data:
    usuario = crear_usuario_desde_json(usuario_str)
    if usuario:
        usuarios.append(usuario)

if usuarios:
    print("Usuarios creados con éxito:")
    for usuario in usuarios:
        print(usuario)
else:
    print("No se crearon usuarios debido a errores. Revisa el archivo error.log para más detalles.")