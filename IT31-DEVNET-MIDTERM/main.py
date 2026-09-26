"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: [De Leon, Christian F.]
"""
#BSIT3C
pet_list =  []

def display_menu():
    # print the menu, return the user's choice
    try:
        print("1. Add a pet")
        print("2. View all pets")
        print("3. Count available vs adopted")
        print("4. Find a pet by name")
        print("5. Remove a pet")
        print("6. Exit")
        option = int(input("Choose an option: "))
        if option == 1:
            add_pet(pet_list)
        elif option == 2:
            view_pets(pet_list)
        elif option == 3:
            count_available_adopted(pet_list)
        elif option == 4:
            find_pet(pet_list)
        elif option == 5:
            remove_pet(pet_list)
        elif option == 6:
            print("Exiting...")
    except:
        print("Insert number values only from [1] - [6]")

def add_pet(pet_list):
    # ask for name, animal type, status — build the string, add to the list
    p_name = input("What is your pet's name?: ")
    pet_list.append(p_name)
    p_type = input("What animal type is your pet?: ")
    pet_list.append(p_type)
    p_status = input("Is the pet Available or Adopted?: ")
    pet_list.append(p_status)
    pass

def view_pets(pet_list):
    # loop through and print every pet — handle empty list
    for x in pet_list:
        print(x)
    pass

def count_available_adopted(pet_list):
    # loop through, count Available vs Adopted, return both
    print(f"Available pets: {pet_list.count("Available")}")
    print(f"Adopted pets: {pet_list.count("Adopted")}")
    pass

def find_pet(pet_list):
    # ask for a name, search the list, print result or "not found"
    try:
        find = input("What is the pet's name?: ")
        x = pet_list.index(find)
        print(x)
    except:
        print("Not found")
    pass

# BONUS (optional)
def remove_pet(pet_list):
    # your code here
    rm = input("Remove pet")
    pet_list.remove(rm)
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
            running = False
            print("Ending program...")
        else:
            break
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit
main()