#rng (random number generator)
    #need to add a count feature after every X amount of guesses
    #add feature number reveal on guess_count = random.randint()
    #add a user database and leaderboard of high scores
    #add a time element



import random

start = "What is your name?"
loop_game = "would you like to go again: \"Yes\" or \"No\"?"
print(start)
name = input()

while True:

    print(f"Hello {name}, I am thinking of a number between 1 and 10")
    mystery_number = random.randint(1,10)

    #print(mystery_number)


    while True:
        #turned into exception handling
        try:
            latest_guess = int(input(f"Alright, take your guess! \n"))
        except ValueError:
            print(f"\"So close!! That is a shape 💕.\" Numbers only I'm afraid {name}.") 
            continue
        if latest_guess == mystery_number:
            print("Winner! Winner! chicken dinner!\nYou can end on a winning streak.")
            print("Unless", end="...")
            break
        # added hints
        if latest_guess > mystery_number:
            print(f"Sorry, {name} your're too high.")

        else:
            print(f"Sorry, {name} you're too low.")
    
    # moved the loop_game prompt to its own loop for effeciency
    print(loop_game)
    cont_loop = input().lower().strip()[:2]
    if cont_loop == "no":
        print("No problemo. Thanks for playing.")
        break
    else:
        continue