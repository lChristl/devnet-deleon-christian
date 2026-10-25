import requests
import random

pokemon_list = ["pikachu","bulbasaur","squirtle","charizard","charmander"]
randomnumber = random.randint(0,4)
randpok = (randomnumber)

poklist = (pokemon_list[randomnumber]) # grabs a random pokemon in the list
x = (f'https://pokeapi.co/api/v2/pokemon/{poklist}')

response = requests.get(x)

result = response.json()
print(result['name'])
print(result['weight'])
print(result['height'])

