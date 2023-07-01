num_rows = int(input("Enter the number of rows for the inverted pyramid: "))
for i in range(num_rows, 0, -1):
    print(' ' * (num_rows - i) + '*' * (2 * i - 1))


