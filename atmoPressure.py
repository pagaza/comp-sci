while (True):   

    press = str(input("Is the atmospheric pressure normal?\n")).lower()

    if press == "no":
        print("The test can't be performed.")
        break

    elif press == "yes":
        temp = float(input("Please enter the water's temperature: "))

        if temp <= 0:
            print("The state is solid.")
            break

        elif temp < 100:
            print("The state is liquid.")
            break

        elif temp >= 100:
            print("The state is gas.")
            break
        
        break
    
    else:
        print("Please answer yes or no.")