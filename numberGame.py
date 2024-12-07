import os
import random

#Welcome Message to start the Number Guessing Game
user_name = input("Enter name: ")
os.system('cls' if os.name == 'nt' else 'clear')

welcome_message = f"""Hello {user_name}, Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number."""
print(welcome_message)

#Setting the variable to randomly select a number between 1 and 100.
random_generator = random.randrange(1,100)

#Setting match case for difficulty level

cli_level = f"""
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)"""
print(cli_level)
print()

sel_diff = int(input("Enter your choice: "))
match sel_diff:
    case 1:
        print("Good! Easy is the safest way")
    case 2:
        print("Great! You have selected the Medium difficulty level.\n"
"Let's start the game!")
    case 3:
        print("You are bold! You have selected the Hardest difficulty level.\n"
"Let's start the game!")



guess_counter = 0
if sel_diff == 1:
    guess_counter += 10



guess_number = int(input("Enter your guess: "))
while guess_number != random_generator:
    # if guess_counter != 0:
    #     guess_counter -= 1
    #     print("Try again")
    if guess_counter == 0:
        print("Sorry you ran out of turns") 

    else:
        print(f"""Congratulations the number was {random_generator} and you guessed {guess_number}.\n
            You guessed the correct number in {guess_counter} attempts""")
