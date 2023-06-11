#Square Star Pattern

num = int(input("Enter the number: "))

for rows in range(num):
    for cols in range(num):
        print("*", end=' ')
    print()
