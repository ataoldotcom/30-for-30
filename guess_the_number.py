#computer guess the number game

#rng (random number generator)
import random

print("What is your name?")
name = input()

print(f"hello {name}, I am thinking of a number between 1 and 10")
mystery_number = random.randint(1,10)

#print(mystery_number)


def computer_guess(x):
    low = 1
    high = x