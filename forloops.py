# Exercise 1

for x in range(20,1,-5):
    print(x)

# Exercise 2

num = int(input("Enter a number between 5 and 12:"))

while True: 

    if num >= 5 and num <= 12:
        for x in range(1,11):
            print(num * x)

        break

    else:
        num = int(input("Enter a number between 5 and 12:"))