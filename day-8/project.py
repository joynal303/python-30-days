"""#Pet Information Management System
import json
while True:
    print("Welcome to Pet Management System")
    
    print("1. Add New Pet")
    print("2. View All Pets")
    print("3. Exit!")
    print("4. Search Pet")
    print("5. Delete Pet")

    choice = input("Choose an option: ")

    if choice=="1":
        name=input("Enter your pet name:")
        age=int(input("Enter your pet age:"))
        color=input("Enter your pet color:")
        food=input("Enter your pet food:")
        new_pet = {
            "Pet Name": name,
            "Age": age,
            "Color": color,
            "Food": food
        }

        try:
            with open("pet.json", "r") as my_pet:
                pets = json.load(my_pet)

        except FileNotFoundError:
            pets = []

        except json.JSONDecodeError:
            print("Error: Invalid JSON file!")
            exit()

        pets.append(new_pet)
        with open("pet.json", "w") as my_pet:
            json.dump(pets, my_pet, indent=4)

    elif choice=="2":

        try:
            with open("pet.json", "r") as my_pet:
                pets = json.load(my_pet)
        except FileNotFoundError:
            pets = []

        except json.JSONDecodeError:
            print("Error: Invalid JSON file!")
            exit()

        if pets:
            for pet in pets:
                print("Pet Name:", pet["Pet Name"])
                print("Age:", pet["Age"])
                print("Color:", pet["Color"])
                print("Food:", pet["Food"])
                print("-------------------")
        else:
            print("No pet information found!")

    elif choice == "3":
        print("Thank you!")
        break

    elif choice == "4":
        search_name = input("Search Pet Name: ")

        with open("pet.json", "r") as my_pet:
            pets = json.load(my_pet)

        found = False

        for pet in pets:
            if pet["Pet Name"].lower() == search_name.lower():
                print("Pet Name:", pet["Pet Name"])
                print("Age:", pet["Age"])
                print("Color:", pet["Color"])
                print("Food:", pet["Food"])
                print("-------------------")

                found = True

        if found == False:
            print("Pet Not Found!")

    elif choice == "5":
        delete_name = input("Enter Pet Name to Delete: ")

        with open("pet.json", "r") as my_pet:
            pets = json.load(my_pet)

        updated_pets = []
        found = False

        for pet in pets:
            if pet["Pet Name"].lower() != delete_name.lower():
                updated_pets.append(pet)
            else:
                found = True

        if found:
            with open("pet.json", "w") as my_pet:
                json.dump(updated_pets, my_pet, indent=4)

            print("Pet Deleted Successfully!")
        else:
            print("Pet Not Found!")

    else:
        print("Invalid Choice!")"""




import json

while True:
    print("\nWelcome to Pet Management System")

    print("1. Add New Pet")
    print("2. View All Pets")
    print("3. Exit")
    print("4. Search Pet")
    print("5. Delete Pet")
    print("6. Pet Update!")

    choice = input("Choose an option: ")

    # 1. Add New Pet
    if choice == "1":

        name = input("Enter your pet name: ")

        try:
            age = int(input("Enter your pet age: "))
        except ValueError:
            print("Invalid Age! Please enter a number.")
            continue

        color = input("Enter your pet color: ")
        food = input("Enter your pet food: ")

        new_pet = {
            "Pet Name": name,
            "Age": age,
            "Color": color,
            "Food": food
        }

        try:
            with open("pet.json", "r") as my_pet:
                pets = json.load(my_pet)

        except FileNotFoundError:
            pets = []

        except json.JSONDecodeError:
            print("Error: Invalid JSON file!")
            continue

        pets.append(new_pet)

        with open("pet.json", "w") as my_pet:
            json.dump(pets, my_pet, indent=4)

        print("Pet Added Successfully!")

    # 2. View All Pets
    elif choice == "2":

        try:
            with open("pet.json", "r") as my_pet:
                pets = json.load(my_pet)

        except FileNotFoundError:
            pets = []

        except json.JSONDecodeError:
            print("Error: Invalid JSON file!")
            continue

        if pets:
            for pet in pets:
                print("Pet Name:", pet["Pet Name"])
                print("Age:", pet["Age"])
                print("Color:", pet["Color"])
                print("Food:", pet["Food"])
                print("-------------------")
        else:
            print("No pet information found!")

    # 3. Exit
    elif choice == "3":
        print("Thank you!")
        break

    # 4. Search Pet
    elif choice == "4":

        search_name = input("Search Pet Name: ")

        try:
            with open("pet.json", "r") as my_pet:
                pets = json.load(my_pet)

        except FileNotFoundError:
            pets = []

        except json.JSONDecodeError:
            print("Error: Invalid JSON file!")
            continue

        found = False

        for pet in pets:
            if pet["Pet Name"].lower() == search_name.lower():

                print("Pet Name:", pet["Pet Name"])
                print("Age:", pet["Age"])
                print("Color:", pet["Color"])
                print("Food:", pet["Food"])
                print("-------------------")

                found = True

        if not found:
            print("Pet Not Found!")

    # 5. Delete Pet
    elif choice == "5":

        delete_name = input("Enter Pet Name to Delete: ")

        try:
            with open("pet.json", "r") as my_pet:
                pets = json.load(my_pet)

        except FileNotFoundError:
            pets = []

        except json.JSONDecodeError:
            print("Error: Invalid JSON file!")
            continue

        updated_pets = []
        found = False

        for pet in pets:
            if pet["Pet Name"].lower() != delete_name.lower():
                updated_pets.append(pet)
            else:
                found = True

        if found:
            with open("pet.json", "w") as my_pet:
                json.dump(updated_pets, my_pet, indent=4)

            print("Pet Deleted Successfully!")

        else:
            print("Pet Not Found!")

    
    elif choice == "6":

        update_name = input("Enter Pet Name to Update: ")

        try:
            with open("pet.json", "r") as my_pet:
                pets = json.load(my_pet)

        except FileNotFoundError:
            pets = []

        except json.JSONDecodeError:
            print("Error: Invalid JSON file!")
            continue

        found = False
        update_success = False

        for pet in pets:

            if pet["Pet Name"].lower() == update_name.lower():

                found = True

                print("\nCurrent Pet Information:")
                print("Pet Name:", pet["Pet Name"])
                print("Age:", pet["Age"])
                print("Color:", pet["Color"])
                print("Food:", pet["Food"])

                print("\nEnter New Information:")

                new_name = input("New Pet Name: ")

                try:
                    new_age = int(input("New Pet Age: "))

                    if new_age < 0:
                        print("Age cannot be negative!")
                        break

                except ValueError:
                    print("Invalid Age! Update Cancelled.")
                    break

                new_color = input("New Pet Color: ")
                new_food = input("New Pet Food: ")

                pet["Pet Name"] = new_name
                pet["Age"] = new_age
                pet["Color"] = new_color
                pet["Food"] = new_food

                update_success = True

        if update_success:
            with open("pet.json", "w") as my_pet:
                json.dump(pets, my_pet, indent=4)

            print("Pet Information Updated Successfully!")

        elif not found:
            print("Pet Not Found!")


    # Invalid Choice
    else:
        print("Invalid Choice!")


