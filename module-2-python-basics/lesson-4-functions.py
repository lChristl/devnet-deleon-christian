"""
Module 2 — Lesson 4: Functions
Student: [De Leon, Christian F.]
Date: [9/27/2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
A function is something related to a recipe.
As the program you would follow these sets of instruction inside a function,
or rather as the cook you would follow the steps to create this recipe every time.

============================================
KEY VOCABULARY
============================================
- def: Used to create a function.
- function: A block of code that you can call for a specific task.
- parameter: A variable that is inside a function.
- argument: The value passed into a function.
- return: Gets the result after running the function


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
characters = ["Denia", "Aemeath", "Hsin"]
games = ["Wuthering Waves", "Zenless Zone Zero", "Honkai Star Rail"]
print(f"="*20)
print("1. Favorite Characters")
print("2. Favorite Games")
print("3. Exit")
print(f"="*20)
def fav_char(characters):
    print(characters) 
def fav_game(games):
    print(games) 
option = int(input("Input number 1 to 3: "))

if option == 1:
    fav_char(characters)
elif option == 2:
    fav_game(games)
elif option == 3:
    print("Exiting Program")
    exit()
else:
    print("Insert number 1 to 3 only")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
inputting the wrong parameter or forgetting to input for functions.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
Functions can be related to recipes
and you do this recipes as defined
in order to create a result from that recipe.

"""
