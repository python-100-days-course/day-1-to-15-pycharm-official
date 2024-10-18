# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 12 - Project - Number Guessing Game

import random

logo = """
    ______                    
  / ____/_  _____  __________
 / / __/ / / / _ \/ ___/ ___/
/ /_/ / /_/ /  __(__  |__  ) 
\____/\__,_/\___/____/____/  
  ________            _   __                __             
 /_  __/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
  / / / __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
 / / / / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
/_/ /_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                           
"""

select_difficulty = True
play_game = True
difficulty = ""
attempts_left = 0
guess_number = 0

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

while select_difficulty:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts_left = 10
        select_difficulty = False
    elif difficulty == "hard":
        attempts_left = 5
        select_difficulty = False
    else:
        print("Please make sure to enter 'easy' or 'hard'.")
        continue

def print_attempts_left(attempts):
    print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")

print(f"You have {attempts_left} attempts remaining to guess the number.")
random_number = random.randint(1, 100)
# print(f"Pssst, the correct answer is {random_number}") # checking

while play_game:
    guess_number = int(input("Make a guess: "))
    if guess_number < random_number:
        print("Too low.")
        attempts_left -= 1
    elif guess_number > random_number:
        print("Too high.")
        attempts_left -= 1
    elif guess_number == random_number:
        print("Congrats! You got it!")
        play_game = False
    if attempts_left == 0:
        print(f"You've lost! The correct number was {guess_number}.")
        play_game = False
    elif attempts_left != 0 and guess_number != random_number:
        print_attempts_left(attempts_left)