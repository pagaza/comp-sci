money = float(input("How much money did you spend?\n"))

if money < 250:
    (print("You don't get any rewards."))

elif money >= 250 and money <= 350:
    (print("You get free popcorn!"))

elif money >= 351 and money <= 500:
    (print("You get a free entrance!"))

elif money > 500:
    (print("You get a $1000 gift card!"))