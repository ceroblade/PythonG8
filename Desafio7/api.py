import requests

def get_informacion():
    url = 'https://aves.ninjas.cl/api/birds'
    response = requests.get(url)
    datos = response.json()
    return datos