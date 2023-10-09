import random
import sys

while (True):
  start = str(input("Start the game? \n"))

  if start.lower() == "yes":
    break

while(True):
  stats = str(input("It is time to set your stats. How will you do so? \n Manually | Automatically \n"))

  if stats.lower() == "manually":
    health = int(input("Use a D20 dice to get your health. Enter your health here: "))
    print("Your stats are: \nHealth: ", health)
    break

  elif stats.lower() == "automatically":
    health = random.randint(1, 20)
    print("Your stats are: \nHealth: ", health)
    break

  else:
    print("Please select manually or automatically.")

print("You find yourself in a tavern, looking for odd jobs to make money. As a thief, you sure made some cash,\n but you were in need of some extra. You notice two different creatures who look promising.\n One is sitting at the bar and the other is sat at a corner table.")

tavernChoice = str(input("Who will you approach? (Type 'Bar' or 'Table')\n"))

if tavernChoice.lower() == "bar":
  print("You carefully approach a strange-looking fairy at the bar. As you enter their field of vision their eyes widen, and so do yours.\n You recognize them from the giant family portrait in the last house you robbed. They quickly report you to the \nauthorities and you get sent to the gallows.")
  print("BAD ENDING: HANGING")
  print("Health: 0")
  sys.exit()

elif tavernChoice.lower() == "table":
  print("You strut to the odd fella at the corner table, who, after you explain your need for a job,\n agrees to pay you if you return to him a precious necklace that is lost in some ruined temple.\n You accept and he leaves, but you realize you have no idea where this temple is.\n You could buy a map to the temple or ask some random passerby for directions.")
  directions = str(input("Which one will be the one you choose? (Type 'Buy a map' or 'Ask someone')\n"))

  if directions.lower() == "buy a map":
    print("You decide to buy a map. It will be useful even after the mission is done and you can just barely afford it.\n After walking for a short time you arrive at the ruins, and you notice the door is caved in, with a bunch of rocks covering the entrance.\n With your strength you could maybe lift the rocks up. However, this will cost you time and a little health.\n You could also walk around to see if you can find another way in.")
    enter = str(input("How will you get in? (Type 'Lift the rocks' or 'Find another way')\n"))

    if enter.lower() == "find another way":
      print("You choose to walk around and search for an alternative way in. However, while you are trying to get to a window to get\n inside you fall backward into some rocks.")
      fall = random.randint(1, 20)

      if fall < 10:
        print("Unfortunately for you, your constitution could do some work and you pass out on the ground.\n BAD ENDING: FALL")
        sys.exit()

      elif fall >= 10:
        health = health//2
        print("Fortunately for you, the rocks were not very sharp. After laying on the ground for some time you stand,\n getting away with some bruises and what you are pretty sure is a sprained wrist.\n However, you get to the window after trying again and get inside.")
        print("When you get inside the temple you look around for places where the necklace might be.\n You decide that the two more probable places it might be are the wardrobe at a corner and the main altar at the front.")
        path = str(input("Which one do you walk up to? (Type 'Wardrobe' or 'Altar')\n"))

        if path.lower() == "altar":
          print("You choose to walk up to the main altar, noticing glittering objects. However, none of them seem to be the necklace you were asked to retrieve,\n but some mixture of golden coins, bracelets, and golden plates. You are a thief and you consider taking some for yourself.\n After all, it's not like someone will notice in this ruined temple.")
          altarChoice = str(input("Do you take the offerings? (Type 'Yes' or 'No')\n"))

          if altarChoice.lower() == "yes":
            print("You extend a hand towards the treasure, and when your fingers touch the gold your vision turns white in a flash as a loud boom ruptures your ears.\n You have summoned the fury of the goddess of the temple in daring to take her offerings.\n You fall to the ground, your body disintegrating.\n BAD ENDING: WRATH")
            print("Health: 0")
            sys.exit()

          elif altarChoice.lower() == "no":
            print("You respect whichever deity this temple was dedicated to, and so you do not touch their treasure.\n Not noticing the necklace there you head for the other place: The wardrobe.\n You open the doors to the wardrobe and notice it actually leads down a steep staircase into a hallway.\n You light up your torch and gaze into the darkness.\n You could run, trying to dodge whatever came your way, or walk and risk a hidden arrow hitting you.")
            runOrEscape = str(input("What will you do? (Type 'Run' or 'Walk') \n"))

            if runOrEscape.lower() == "run":
              print("You decide to run. It'll be quicker, you are pretty sure you have fast reflexes and the hallway seems safe so far.\n You run, stumbling with rubble at times. And then you finally trip and fall into an open hole in the ground.\n Well, they did say the temple was in ruins, huh?\n BAD ENDING: TRIP")
              print("Health: 0")
              sys.exit()

            elif runOrEscape.lower() == "walk":
              print("Choosing to be cautious, you take hesitant steps across the hallway, one hand on the wall leading you forward.\n After a while, you notice that the wall has a slight depth to it. You press a brick and like magic, the wall moves.\n You peek in, gazing around a carpeted room. There is a body lying on the ground, and when you approach it you notice that,\n whoever they are, they are dead, although their body is still warm. Maybe if you were faster you could've saved them.\n But not all is sad, as you do find the necklace in a drawer. You return to the town and get paid for a job well done.\n NEUTRAL ENDING: ANOTHER JOB")
              print("Health: ", health)
              sys.exit()

        elif path.lower() == "wardrobe":
          print("You respect whichever deity this temple was dedicated to, and so you do not touch their treasure.\n Not noticing the necklace there you head for the other place: The wardrobe.\n You open the doors to the wardrobe and notice it actually leads down a steep staircase into a hallway.\n You light up your torch and gaze into the darkness.\n You could run, trying to dodge whatever came your way, or walk and risk a hidden arrow hitting you.")
          runOrEscape = str(input("What will you do? (Type 'Run' or 'Walk') \n"))

          if runOrEscape.lower() == "run":
            print("You decide to run. It'll be quicker, you are pretty sure you have fast reflexes and the hallway seems safe so far.\n You run, stumbling with rubble at times. And then you finally trip and fall into an open hole in the ground.\n Well, they did say the temple was in ruins, huh?\n BAD ENDING: TRIP")
            print("Health: 0")
            sys.exit()

          elif runOrEscape.lower() == "walk":
            print("Choosing to be cautious, you take hesitant steps across the hallway, one hand on the wall leading you forward.\n After a while, you notice that the wall has a slight depth to it. You press a brick and like magic, the wall moves.\n You peek in, gazing around a carpeted room. There is a body lying on the ground, and when you approach it you notice that,\n whoever they are, they are dead, although their body is still warm. Maybe if you were faster you could've saved them.\n But not all is sad, as you do find the necklace in a drawer. You return to the town and get paid for a job well done.\n NEUTRAL ENDING: ANOTHER JOB")
            print("Health: ", health)
            sys.exit()

    elif enter.lower() == "lift the rocks":
      health == health//3
      print("You choose to try to move the rocks at the entrance. It takes you half a day and about a third of your health but you make it.\n When you get inside the temple you look around for places where the necklace might be.\n You decide that the two more probable places it might be are the wardrobe at a corner and the main altar at the front.")
      path = str(input("Which one do you walk up to? (Type 'Wardrobe' or 'Altar')\n"))

      if path.lower() == "altar":
        print("You choose to walk up to the main altar, noticing glittering objects. However, none of them seem to be the necklace you were asked to retrieve,\n but some mixture of golden coins, bracelets, and golden plates. You are a thief and you consider taking some for yourself.\n After all, it's not like someone will notice in this ruined temple.")
        altarChoice = str(input("Do you take the offerings? (Type 'Yes' or 'No')\n"))

        if altarChoice.lower() == "yes":
          print("You extend a hand towards the treasure, and when your fingers touch the gold your vision turns white in a flash as a loud boom ruptures your ears.\n You have summoned the fury of the goddess of the temple in daring to take her offerings.\n You fall to the ground, your body disintegrating.\n BAD ENDING: WRATH")
          print("Health: 0")
          sys.exit()

        elif altarChoice.lower() == "no":

          print("You respect whichever deity this temple was dedicated to, and so you do not touch their treasure.\n Not noticing the necklace there you head for the other place: The wardrobe.\n You open the doors to the wardrobe and notice it actually leads down a steep staircase into a hallway.\n You light up your torch and gaze into the darkness.\n You could run, trying to dodge whatever came your way, or walk and risk a hidden arrow hitting you.")
          runOrEscape = str(input("What will you do? (Type 'Run' or 'Walk') \n"))

          if runOrEscape.lower() == "run":
            print("You decide to run. It'll be quicker, you are pretty sure you have fast reflexes and the hallway seems safe so far.\n You run, stumbling with rubble at times. And then you finally trip and fall into an open hole in the ground.\n Well, they did say the temple was in ruins, huh?\n BAD ENDING: TRIP")
            print("Health: 0")
            sys.exit()

          elif runOrEscape.lower() == "walk":
            print("Choosing to be cautious, you take hesitant steps across the hallway, one hand on the wall leading you forward.\n After a while, you notice that the wall has a slight depth to it. You press a brick and like magic, the wall moves.\n You peek in, gazing around a carpeted room. There is a body lying on the ground, and when you approach it you notice that,\n whoever they are, they are dead, although their body is still warm. Maybe if you were faster you could've saved them.\n But not all is sad, as you do find the necklace in a drawer. You return to the town and get paid for a job well done.\n NEUTRAL ENDING: ANOTHER JOB")
            print("Health: ", health)
            sys.exit()

      elif path.lower() == "wardrobe":
        print("You head for the wardrobe. You open the doors to the wardrobe and notice it actually leads down a steep staircase into a hallway.\n You light up your torch and gaze into the darkness.\n You could run, trying to dodge whatever came your way, or walk and risk a hidden arrow hitting you.")
        runOrEscape = str(input("What will you do? (Type 'Run' or 'Walk') \n"))

        if runOrEscape.lower() == "run":
          print("You decide to run. It'll be quicker, you are pretty sure you have fast reflexes and the hallway seems safe so far.\n You run, stumbling with rubble at times. And then you finally trip and fall into an open hole in the ground.\n Well, they did say the temple was in ruins, huh?\n BAD ENDING: TRIP")
          print("Health: 0")
          sys.exit()

        elif runOrEscape.lower() == "walk":
          print("Choosing to be cautious, you take hesitant steps across the hallway, one hand on the wall leading you forward.\n After a while, you notice that the wall has a slight depth to it. You press a brick and like magic, the wall moves.\n You peek in, gazing around a carpeted room. There is a body lying on the ground, and when you approach it you notice that,\n whoever they are, they are dead, although their body is still warm. Maybe if you were faster you could've saved them.\n But not all is sad, as you do find the necklace in a drawer. You return to the town and get paid for a job well done.\n NEUTRAL ENDING: ANOTHER JOB")
          print("Health: ", health)
          sys.exit()

  elif directions.lower() == "ask someone":
    print("You decide to not waste money on a map and ask a random passerby for directions to the ruined temple.\n Fortunately, it seems they used to work there and they tell you of a hidden passage in case you might need it.\n And you are grateful for it when you arrive and see that the door is caved in.\n You waste no time entering the temple through a narrow hidden hallway.\n Now, you can choose to do this quickly and run, or be cautious and choose to walk.")
    runOrEscape = str(input("What will you do? (Type 'Run' or 'Walk') \n"))

    if runOrEscape.lower() == "run":
      print("You decide to run. It'll be quicker, you are pretty sure you have fast reflexes and the hallway seems safe so far.\n You run, stumbling with rubble at times. And then you finally trip and fall into an open hole in the ground.\n Well, they did say the temple was in ruins, huh?\n BAD ENDING: TRIP")
      print("Health: 0")
      sys.exit()

    elif runOrEscape.lower() == "walk":
      print("Choosing to be cautious, you take hesitant steps across the hallway, one hand on the wall leading you forward.\n After a while, you notice that the wall has a slight depth to it. You press a brick and like magic, the wall moves.\n Before you can peek in you hear a scuffle. When you do look you notice two people fighting, one attacking with a dagger.\n You can choose to stay frozen and watch or go in and try to help the attacked.")
      action = str(input("What will you do? (Type 'Stay' or 'Help') \n"))

      if action.lower() == "stay":
        print("You stay frozen, not expecting to see such brutal sights at the ruins.\n In a flash, the dagger comes down and slits the throat of the victim, who slumps onto the floor.\n Horrified, you take a step back, losing your footing and landing on the ground with a thud.\n The armed figure hears and turns to you, brandishing the dagger. It slits your throat too and you bleed out on the ground.\n BAD ENDING: COWARD")
        print("Health: 0")
        sys.exit()

      elif action.lower() == "help":
        print("A burst of adrenaline courses through your body and you find the courage to tackle the armed figure. They slash at you.")
        agiRoll = random.randint(1, 20)

        if agiRoll <= 10:
          print("They cut your throat open and as you lay bleeding on the floor you watch as the other victim falls the the floor, bleeding in unison.\n BAD ENDING: VICTIM")
          print("Health: 0")
          sys.exit()

        elif agiRoll > 10:
          print("They miss their slash and you kick the dagger out of the attacker's hand. You then take it, and without thinking about it, slit their throat.\n You are standing, breathing heavily, when a hesitant hand touches your shoulder. You whirl around to find the one who was getting attacked.\n They express their gratitude and introduce themselves as a noble from a foreign country.\n They tell you prophecy foretold that the one who saves them from an attacker at this temple is fated to be with them.\n They offer you their hand, and as they do so you notice the necklace you were looking for in a drawer.\n You could take their hand, or reject them in favor of your outlaw life.")
          hand = str(input("What will you choose? (Type 'Take their hand' or 'Reject them')\n"))

          if hand.lower() == "take their hand":
            print("A life of wealth and riches awaits for you, as you accept their hand. Overjoyed, they lead you to their abandoned carriage, taking you to their lands.\n You dine and dance and dine again with your new partner, forgetting your unlawful life before, while the necklace sits abandoned at the ruined temple.\n GOOD ENDING: NOBILITY")
            print("Health: ", health)
            sys.exit()

          elif hand.lower() == "reject them":
            print("You choose to ignore their hand, convinced a life with them is not what you want.\n Dejected, they accept your decision and you leave with the necklace.\n You return to the town and get paid for a job well done.\n NEUTRAL ENDING: MISSED OPPORTUNITIES")
            print("Health: ", health)
            sys.exit()