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
random_generator = random.randint(1,100)

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


diff_level = {1: 10, 2: 5, 3: 3}
guess_counter = diff_level.get(sel_diff, 0)

while guess_counter > 0:
    guess_number = int(input("Enter your guess: "))
    if guess_number == random_generator:
        print(f"""Congratulations the number was {random_generator} and you guessed {guess_number}.\n
                You guessed the correct number in {guess_counter} attempts""")
        break
    elif guess_number != random_generator:
        guess_counter -= 1
        print(f"Try again you have {guess_counter} tries left!")
else:
    print(f"You ran out of attempts!\nThe correct answer was {random_generator}")