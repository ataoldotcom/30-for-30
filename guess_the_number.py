#computer guess the number game

#rng (random number generator)
import random

start = "What is your name?"
loop_game = "That's not it.\nWould you like to guess again: \'Yes\' or \'No\'?"
print(start)
name = input()

print(f"Hello {name}, I am thinking of a number between 1 and 10")
mystery_number = random.randint(1,10)

#print(mystery_number)


while True:
    latest_guess = int(input("Alright {name}, take your guess!"))

    if latest_guess == mystery_number:
        print("Winner! Winner! chicken dinner!")
        break
    # below code needs to be finished. exception thrown  when user puts in a non numeric value
    elif latest_guess =
        # need to add a line break between "{name}." and "So".
        print("Numbers only {name}.\nSo close!! That is a shape 💕") 
    else: 
        print(loop_game)
        cont_loop = input().lower
        if cont_loop.lower() == "yes":
            print("No problemo. Thanks for playing")
            break





###turn to Loop
##print("Please guess the number")
##user_latest_guess = int(input())

##print(user_latest_guess)
