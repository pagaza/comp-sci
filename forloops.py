# Exercise 1

n = int(input("Please enter a number: "))
s = int(input("Please enter steps: "))

for i in range (1, n + 1, s):
    print(i)

# Exercise 2

n = int(input("Please enter a number: "))

for j in range (n, -1, -1):
    print(j)

print("Done.")

# Exercise 3

n = int(input("Please enter a number: "))
op = str(input("Please choose a type of operation (add, substract, multiply): "))

if op.lower() == "add":

    for i in range (1, n +1):

        if i%2 == 0:
            print(i, "Even")

        else:
            print(i, "Odd")

elif op.lower() == "substract":
    for j in range (n, 0, -1):
        
        if j%2 == 0:
            print(j, "Even")

        else:
            print(j, "Odd")

elif op.lower() == "multiply":

    for k in range(n, 1, -1):

        k -= 1
        n = n*k

    print(n)