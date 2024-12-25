import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '434269f9062ca79f16568220f3f93b89'
HEADER = {'Content-Type' : 'application/json',
         'trainer_token' : TOKEN }
body_Creationp = {
    "name": "Бульбазавр",
    "photo_id": 1
}

name_change = {
    "pokemon_id": "170812",
    "name": "PavelAP",
    "photo_id": 2
}
caught = {
    "pokemon_id": "170812"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_Creationp)
print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = name_change)
print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = caught)
print(response.text)