# Exercise 1

waterON = True

while waterON == True:
    print("You are pressing the button. The water is flowing.")
    ans = str(input("Are you still pressing the button? (y/n)\n")).lower()

    if ans == "yes" or ans == "y":
        continue

    elif ans == "no" or ans == "n":
        "The water has stopped flowing."
        break

# Exercise 2

curFloor = 1

while True: 
    buttonPress = str(input("Will you press the elevator button? (y/n)")).lower()

    if buttonPress == "yes" or buttonPress == "y":
        floor = int(input("Input floor number: "))

        while curFloor < floor: 
            print("The current floor is floor ", curFloor)
            curFloor += 1

        print("You have reached floor ", floor)

    else:
        break

# Exercise 3

print("Please insert your money to buy some cookies :). They are 15$")

money = int(input("Insert money here: "))
ck = 0

while (money >= 15):
  ck = ck + 1
  money = money - 15
print("You have bought", ck, "cookies")