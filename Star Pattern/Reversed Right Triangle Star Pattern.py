# Reversed Right Triangle Star Pattern

num = int(input("Enter number: "))

for i in range(1,num+1):
    print(" " * (num-i) + "*" * i)
