num_rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(num_rows):
        print(' ' * (num_rows - i - 1) + '*' * (2 * i + 1))



