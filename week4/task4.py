#
import random
#Computer picks a random number between 1 and 10
number = random.randint(1, 10)

while True:
        # Ask the user for their guess
        guess = int(input("Enter your guess "))

        # Check if the guess is too low, too high, or correct
        if guess < number:
            print("Too low hahaha Try again.")
        elif guess > number:
            print("Too high Try again.")
        else:
            print("Correct! You guessed the number.")
