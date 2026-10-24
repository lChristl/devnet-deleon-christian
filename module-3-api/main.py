import requests
import random

name = input("pokemon name: ")
x = (f'https://pokeapi.co/api/v2/pokemon/{name}')

response = requests.get(x)

result = response.json()
print(result['name'])
print(result['weight'])
print(result['height'])

# #bulbasaur charmander squirtle pikachu charizard
