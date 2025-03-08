#computer guess the number game

#rng (random number generator)
import random

start = "What is your name?"
print(start)
name = input()

print(f"Hello {name}, I am thinking of a number between 1 and 10")
mystery_number = random.randint(1,10)

#print(mystery_number)

while True:

###turn to Loop
print("Please guess the number")
user_latest_guess = int(input())

print(user_latest_guess)
