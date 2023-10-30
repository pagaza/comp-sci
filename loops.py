# Exercise 1

num = int(input("Enter a number between 1 and 100: "))

while num >= 1 and num <= 100:
    num = int(input("Enter a number between 1 and 100: "))

print("Out of range.")

# Exercise 2

password = "A01384910"

i = 0

while i < 3:
    pcheck = str(input("Enter your password: "))

    if pcheck != password:
        print("Incorrect.")
        i += 1
        print("Attempts left: ", 3 - i)

    elif pcheck == password:
        print("Access granted.")
        break

# Exercise 3

month = int(input("Enter a month in numerical form (1-12): "))

while month >= 1 and month <= 12:
    month = int(input("Enter a month in numerical form (1-12): "))

print("Out of range.")

# Exercise 4

num = int(input("Enter a number (positive or negative): "))

while num >= 0:
    num = int(input("Enter a number (positive or negative): "))

print("Negative number.")

# Exercise 5

list = ['A', 'B', 'C', 'D', 'F']

grade = str(input("Enter your grade (A, B, C, D or F): ")).upper()

for grade in list:
    grade = str(input("Enter your grade (A, B, C, D or F): "))

print("Incorrect grade.")