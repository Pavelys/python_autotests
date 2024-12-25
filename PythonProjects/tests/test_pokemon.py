import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '434269f9062ca79f16568220f3f93b89'
HEADER = {'Content-Type' : 'application/json',
         'trainer_token' : TOKEN }
TRAINER_ID = 13160

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Павел63'
