from random import randint
random_number_to_guess = randint(1, 20)

print("Welcome to Guessing Game")
print("You have 3 chances to guess the number")
print("Let's Start")

num = int(input("Enter a number: "))

chances = 3

if(num == random_number_to_guess)
    print("Woww!!You guessed it correct")
elif(num != random_number_to_guess)
    print("Oops! Wrong")
    print("Try again")
    chances -= 1
