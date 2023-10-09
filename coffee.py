while (True):
    size = str(input("What size would you like for your coffee? Short, Alto, Grande, or Venti?\n")).lower()

    if size == "short":
        print("The price for a short coffee is $24.")
        break

    elif size == "alto": 
        print("The price for an alto coffee is $36.")
        break

    elif size == "grande":
        print("The price for a grande coffee is $45.")
        break

    elif size == "venti":
        print("The price for a venti coffee is $56.")
        break

    else:
        print("That size doesn't exist. Please enter the size.")
