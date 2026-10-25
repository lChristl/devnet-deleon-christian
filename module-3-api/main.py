import requests
import random

pokemon_list = ["pikachu","bulbasaur","squirtle","charizard","charmander"]
randomnumber = random.randint(0,4)
randpok = (randomnumber)

poklist = (pokemon_list[randomnumber]) # grabs a random pokemon in the list
x = (f'https://pokeapi.co/api/v2/pokemon/{poklist}')

response = requests.get(x)

def show_info():    
    result = response.json()
    # print(result['name'])
    print(result['weight'])
    print(result['height'])

print("Would you like to play Who's that Pokemon?")
print("[1] Yes")
print("[2] No")
choice = input("Your choice: ")

if choice == 1:
    print("Who's that pokemon?")
    show_info()

elif choice == 2:
    exit