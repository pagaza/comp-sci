# Here we will create the variables representing the countries of each possible result. Depending on the answer, the value
# of some of the variables will increase. The variable with the highest value will be chosen as the final result

ansCheck2 = ["a", "b"]
ansCheck3 = ["a", "b", "c"]
ansCheck4 = ["a", "b", "c", "d"]
ansCheck6 = ["a", "b", "c", "d", "e", "f"]

while True: 
    start = str(input("Would you like to begin the questionnaire? (y/n):\n")).lower()

    if start == "yes" or start == "y":
        break

    else:
        continue

print("The questions will allow you to select your answer by typing the letter corresponding to the answer.\nPlease type the letter as your answer (it can be on uppercase or lowercase). ")

while True: 
    ans1 = str(input("1. What flavor do you prefer?\na) Sweet\nb) Savoury\nc) Sour\n")).lower()

    if ans1 in ansCheck3:
        break
        # Add modifier

    else:
        continue

while True: 
    ans2 = str(input("2. At what temperature do you prefer to eat your food?\na) Cold\nb) Hot\nc) Warm")).lower()

    if ans2 in ansCheck3:
        break
        # Add modifier

    else: 
        continue

while True: 
    ans3 = str(input("3. Which of these cultures are you most interested in?\na) Mexican \nb) Chinese \nc) Japanese \nd) French \ne) Spanish \nf) Italian \n")).lower()

    if ans3 in ansCheck6:
        # Add modifier
        break

    else: 
        continue

while True: 
    ans4 = str(input("4. What is the time you want to spend cooking? \na) Instantly \nb) Less than an hour \nc) Many hours \n")).lower()

    if ans4 in ansCheck3:
        # Add modifier
        break

    else: 
        continue

while True: 
    ans5 = str(input("5. How much experience do you have cooking? \na) I'm a beginner \nb) I have some practice \nc) I cook a lot \n")).lower()

    if ans5 in ansCheck3:
        # Add modifier
        break

    else:
        continue

while True: 
    ans6 = str(input("6. What protein do you prefer? \na) Chicker \nb) Fish \nc) Beef \nd) Pork \n")).lower()

    if ans6 in ansCheck4:
        # Add modifier
        break

    else:
        continue

while True: 
    ans7 = str(input("7. What prize are you looking for? \na) Cheap \nb) Moderate \nc) Expensive \n")).lower()

    if ans7 in ansCheck3:
        # Add modifier
        break

    else: 
        continue

while True: 
    ans8 = str(input("8. Do you like spicy food? \na) Yes \nb) No\n")).lower()

    if ans8 in ansCheck2:
        # Add modifier
        break

    else:
        continue

while True:
    ans9 = str(input("9. What size do you want? \na) Small \nb) Medium \nc) Large \n")).lower()

    if ans9 in ansCheck3:
        # Add modifier
        break

    else:
        continue

