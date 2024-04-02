import requests

response_get = requests.get("https://reqres.in/api/users")
users_data = response_get.json()
print("Datos de Usuario:")
print(users_data)

new_user = {
    "name": "Ignacio",
    "job": "Profesor"
}

response_post = requests.post("https://reqres.in/api/users", json=new_user)
created_user = response_post.json()
print("\nUsuario Creado:")
print(created_user)
user_id_to_update = 2  
updated_user_info = {
    "residence": "zion"
}

response_put = requests.put(f"https://reqres.in/api/users/{user_id_to_update}", json=updated_user_info)
updated_user = response_put.json()
print("\nUsuario Añadido:")
print(updated_user)
user_id_to_delete = 6
response = requests.delete(f"https://reqres.in/api/users/{user_id_to_delete}")
print("\nCodigo Respuesta Eliminacion:", response.status_code)