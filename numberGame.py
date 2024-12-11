import os
import random
import time
import json

class NumberGuessingGame:
    def __init__(self):
        
        
        self.diff_level = {1: 10, 2: 5, 3: 3}
        self.guess_counter = 0
        self.reset_game()
    
    def reset_game(self):
        self.random_generator = random.randint(1, 100)
        self.guess_counter = 0
        self.sel_diff = 0
    
    def start_menu(self):
        print(f"""
        Welcome to the Number Guessing Game!:
        1. Start a new game
        2. View high scores """)
        menu_ans = int(input("Choose an option: "))
        if menu_ans == 1:
            self.play_game()
        elif menu_ans == 2:
            with open('scores.json', 'r') as file:
                self.data = json.load(file)
                view = self.data

                print("Easy Difficulty:")
                for i, score in enumerate(view["easy_difficulty"], start=1):
                    print(f"{i}st Place: {score['First_Place']} - {score['guess_counter']} attempts")
                
                # print("\nMedium Difficulty")
                # for i, score in enumerate(view["medium_difficulty"], start=1):
                #     print(f"{i}st Place: {score['First_Place']} - {score['guess_counter']} attempts")
                
                # print("\nhard_difficulty")
                # for i, score in enumerate(view["hard_difficulty"], start=1):
                #     print(f"{i}st Place: {score['First_Place']} - {score['guess_counter']} attempts")

      

            
              



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

    def high_score(self):
        with open('scores.json', 'r') as file:
            self.data = json.load(file)
       

        difficult_map = {
            1: "easy_difficulty",
            2: "medium_difficulty",
            3: "hard_difficulty"
        }
        current_difficulty = difficult_map[self.sel_diff]
        high_scores = self.data[current_difficulty]

        self.current_score = self.diff_level[self.sel_diff] - self.guess_counter + 1
        if self.current_score <= int(high_scores[0]["guess_counter"]):
            high_scores[2] = high_scores[1]
            high_scores[1] = high_scores[0]
            high_scores[0] = {"First_Place": self.user_name, "guess_counter": str(self.current_score)}
        elif self.current_score <= int(high_scores[1]["guess_counter"]):
            high_scores[2] = high_scores[1]
            high_scores[1] = {"Second_Place": self.user_name, "guess_counter": str(self.current_score)}
        elif self.current_score < int(high_scores[2]["guess_counter"]):
            high_scores[2] = {"Third_Place": self.user_name, "guess_counter": str(self.current_score)}

        
        with open('scores.json', 'w') as file:
            json.dump(self.data, file, indent=4)
            





    def play_game(self):
        self.user_name = input("Enter name to begin game: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            self.welcome_message()
            self.difficulty_level()
            start_time = time.time()
            while self.guess_counter > 0:
                
                guess_number = int(input("Enter your guess: "))
                
                
                if guess_number == self.random_generator:
                    end_time = time.time()
                    time_taken = end_time - start_time
                    attempts = self.diff_level[self.sel_diff] - self.guess_counter + 1
                    print(f"""Congratulations! The number was {self.random_generator} and you guessed it correctly.\n
            You guessed the correct number in {self.diff_level[self.sel_diff] - self.guess_counter + 1 } attempts.""")
                    print(f"It took you {time_taken:.2f} seconds to guess the number.")
                    self.high_score()
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
    playgame.start_menu()

