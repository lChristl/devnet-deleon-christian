"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: [De Leon, Christian F.]
"""
pets =  []

def display_menu():
    # print the menu, return the user's choice
    print("1. Add a pet")
    print("2. View all pets")
    print("3. Count available vs adopted")
    print("4. Find a pet by name")
    print("5. Exit")
    option = input("Choose an option: ")
    if option == 1:
        print("")
    elif option == 2:
        print("")
    elif option == 3:
        print("")
    elif option == 4:
        print("")
    elif option == 5:
        print("")
    pass

def add_pet(pet_list):
    # ask for name, animal type, status — build the string, add to the list
    p_name = input("What is your pet's name?: ")
    p_type = input("What animal type is your pet?: ")
    p_status = input("Is the pet Available or Adopted?")
    pass

def view_pets(pet_list):
    # loop through and print every pet — handle empty list
    for x in pets:
        print(x)
    pass

def count_available_adopted(pet_list):
    # loop through, count Available vs Adopted, return both

    pass

def find_pet(pet_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_pet(pet_list):
    # your code here
    pass

def main():
    running = True
    while running:
        print("[1] Display Menu")
        print("[2] Exit")
        choice = int(input("Insert number [1] or [2]: "))
        if choice == 1:
            display_menu()
        elif choice == 2:
            print("Exiting program")
            break
        else:
            break
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit
main()