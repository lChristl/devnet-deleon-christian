import requests
import random

pokemon_list = ["pikachu","bulbasaur","squirtle","charizard","charmander"]
x = random.randint(1,5)
randpok = (x)
x = (f'https://pokeapi.co/api/v2/pokemon/{randpok}')

response = requests.get(x)

result = response.json()
print(result['name'])
print(result['weight'])
print(result['height'])


# #bulbasaur charmander squirtle pikachu charizard
