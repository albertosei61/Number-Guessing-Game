import os
import random
import time

class NumberGuessingGame:
    def __init__(self):
        self.user_name = input("Enter name: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        
        self.diff_level = {1: 10, 2: 5, 3: 3}
        self.guess_counter = 0
        self.reset_game()
    
    def reset_game(self):
        self.random_generator = random.randint(1, 100)
        self.guess_counter = 0
        self.sel_diff = 0



    def welcome_message(self):
        # Welcome Message to start the Number Guessing Game
        print(f"""Hello {self.user_name}, Welcome to the Number Guessing Game!
        I'm thinking of a number between 1 and 100.""")
        


    def difficulty_level(self):
        # Setting match case for difficulty level
        print(f"""
        Please select the difficulty level:
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)""")
    

        self.sel_diff = int(input("Enter your choice: "))
        self.guess_counter = self.diff_level.get(self.sel_diff, 0)
        match self.sel_diff:
            case 1:
                print("Good! Easy is the safest way")
            case 2:
                print("Great! You have selected the Medium difficulty level.\nLet's start the game!")
            case 3:
                print("You are bold! You have selected the Hardest difficulty level.\nLet's start the game!")


    def play_game(self):
        while True:
            self.welcome_message()
            self.difficulty_level()
            start_time = time.time()
            while self.guess_counter > 0:
                
                guess_number = int(input("Enter your guess: "))
                
                if guess_number == self.random_generator:
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print(f"""Congratulations! The number was {self.random_generator} and you guessed it correctly.\n
            You guessed the correct number in {self.diff_level[self.sel_diff] - self.guess_counter + 1 } attempts.""")
                    print(f"It took you {time_taken:.2f} seconds to guess the number.")
                    break
                elif guess_number < self.random_generator:
                    print(f"Incorrect! The number is greater than {guess_number}.")
                else:
                    print(f"Incorrect! The number is less than {guess_number}.")
                
                self.guess_counter -= 1
                print(f"You have {self.guess_counter} tries left!")
            else:
                print(f"You ran out of tries. The number was {self.random_generator}.")
            play_again = input("Do you want to play again yes/no?").lower()
            if play_again != "yes":
                print("Thank you for playing, Goodbye")
                break
            self.reset_game()


if __name__ == "__main__": 
    playgame = NumberGuessingGame()
    playgame.play_game()

