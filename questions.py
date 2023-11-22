import time

# Variables

mx = 0
ch = 0
jp = 0
fr = 0
sp = 0
it = 0

# Answer validation

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

        if ans1 == "a":
          fr += 2
          it +=1

        elif ans1 == "b":
          jp += 2
          fr += 1
          sp += 2
          it += 2

        elif ans1 == "c":
          mx += 2
          ch += 2

        break

    else:
        continue

while True:
    ans2 = str(input("2. At what temperature do you prefer to eat your food?\na) Cold\nb) Hot\n")).lower()

    if ans2 in ansCheck2:

      if ans2 == "a":
        jp += 2
        sp += 2

      elif ans2 == "b":
        mx += 2
        ch += 2
        fr += 2
        it += 2

      break  

    else:
        continue

while True:
    ans3 = str(input("3. Which of these cultures are you most interested in?\na) Mexican \nb) Chinese \nc) Japanese \nd) French \ne) Spanish \nf) Italian \n")).lower()

    if ans3 in ansCheck6:

        match ans3:
          case "a":
            mx += 1

          case "b":
            ch += 1

          case "c":
            jp += 1

          case "d":
            fr += 1

          case "e":
            sp += 1

          case "f":
            it += 1

        break

    else:
        continue

while True:
    ans4 = str(input("4. What is the time you want to spend cooking? \na) Instantly \nb) Less than an hour \nc) Many hours \n")).lower()

    if ans4 in ansCheck3:

        match ans4:
          case "a":
            mx += 1
            ch += 1
            it += 1

          case "b":
            it += 1
            jp += 1


          case "c":
            sp += 1
            fr += 1

        break

    else:
        continue

while True:
    ans5 = str(input("5. How much experience do you have cooking? \na) I'm a beginner \nb) I have some practice \nc) I cook a lot \n")).lower()

    if ans5 in ansCheck3:

       match ans5:
          case "a":
            mx += 1
            ch += 1
            jp += 1
            it += 1

          case "b":
            mx += 1
            jp += 1
            sp += 1


          case "c":
            sp += 1
            fr += 1

    break

while True:
    ans6 = str(input("6. What protein do you prefer? \na) Chicken \nb) Fish \nc) Beef \nd) Pork \n")).lower()

    if ans6 in ansCheck4:

       match ans4:

          case "a":
            mx += 1
            fr += 1
            ch += 1

          case "b":
            jp += 1

          case "c":
            sp += 1
            fr += 1
            it += 1
            mx += 1

          case "c":
            ch += 1
            sp += 1
       break  

    else:
        continue

while True:
    ans7 = str(input("7. What prize are you looking for? \na) Cheap \nb) Moderate \nc) Expensive \n")).lower()

    if ans7 in ansCheck3:

      if ans7 == "a":
        sp += 2
        it += 1

      elif ans7 == "b":
        ch += 2
        mx += 1

      elif ans7 == "c":
        fr += 2
        jp += 2

      break

    else:
        continue

while True:
    ans8 = str(input("8. Do you like spicy food? \na) Yes \nb) No\n")).lower()

    if ans8 in ansCheck2:

      if ans8 == "a":
        jp += 2
        mx += 2
        ch += 2

      elif ans8 == "b":
        sp += 2
        fr += 2
        it += 2

      break

    else:
        continue

while True:
    ans9 = str(input("9. What size do you want? \na) Small \nb) Medium \nc) Large \n")).lower()

    if ans9 in ansCheck3:

      if ans9 == "a":
        jp += 2
        sp += 2
        it += 1

      elif ans9 == "b":
        fr += 2
        mx += 1

      elif ans9 == "c":
        ch += 2

      break

    else:
        continue

res = [mx, ch, jp, fr, sp, it]

print("Results in...")

for i in range (3, 0, -1):
   print(i, "second(s)...")
   time.sleep(1)

if max(res) == mx:
   print("You should try Mexican food!")

elif max(res) == ch:
   print("You should try Chinese food!")

elif max(res) == jp:
   print("You should try Japanese food!")

elif max(res) == fr:
   print("You should try French food!")

elif max(res) == sp:
   print("You should try Spanish food!")

elif max(res) == it:
   print("You should try Italian food!")