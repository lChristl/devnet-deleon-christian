import requests
import random

pokemon_list = ["pikachu","bulbasaur","squirtle","charizard","charmander"]
randomnumber = random.randint(0,4)
randpok = (randomnumber)

poklist = (pokemon_list[randomnumber]) # grabs a random pokemon in the list
x = (f"https://pokeapi.co/api/v2/pokemon/{poklist}")


def show_info():    
    response = requests.get(x)
    if response.status_code == 200:
        result = response.json()
        print(f"Weight: {result['weight']}")
        print(f"Height: {result['height']}")
        ability_name = result["abilities"][0]["ability"]["name"]
        print(f"Ability: {ability_name}")
    else:
        print("No pokemon found")

print("Would you like to play Who's that Pokemon?")
print("[1] Yes")
print("[2] No")
choice = input("Your choice: ")
print(f"="*20)

if choice == "1":
    print("Who's that pokemon?")
    show_info()
    print(f"="*20)

    
    for i, pokemon in enumerate(pokemon_list, start=1):
        print(f"[{i}] {pokemon}")

    try:
        guess = int(input("Your guess, pick from [1] to [5]: "))
        guessed_pokemon = pokemon_list[guess - 1]

        if guessed_pokemon == poklist:
            print(f"You guessed correctly! it was {poklist.capitalize()}")   
        else:
            print(f"You guessed wrong! it was actually {poklist.capitalize()}")

    except(ValueError, IndexError):
        print("Invalid Input! Enter only a number from 1 to 5")       
elif choice == "2":
    exit