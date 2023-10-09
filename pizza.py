veg = ['Pepper', 'Olives']
nonveg = ["Pepperoni", "Sausage", "Ham"]
mainIng = ["Tomato sauce", "Cheese"]

while (True):
    prompt1 = str(input("Would you like a vegetarian pizza?")).lower()

    if prompt1 == "yes":
        vegChoice = str(input("Would you like pepper or olives? \n"))

        if vegChoice in veg: 
            mainIng.append(vegChoice)
            print("You ordered a vegetarian pizza with: ", mainIng)
            break

        elif vegChoice not in veg: 
            print("That ingredient is not available.")
            break

    elif prompt1 == "no":
        nonvegChoice = str(input("Would you like pepperoni, sausage, or ham?"))

        if nonvegChoice in nonveg:
            mainIng.append(nonvegChoice)
            print("You ordered a non-vegetarian pizza with: ", mainIng)
            break

        elif nonvegChoice not in nonveg:
            print("That ingredient isn't available.")

    else:
        print("Please answer yes or no.")