# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 14 - Beginner - Project - Number Guessing Game

import random
from random import choice

from game_data import data
from art import logo
from art import vs

# Logo
# Compare A: NASA, a Space agency, from United States.
# VS
# Against B: NBA, a Club Basketball Competition, from United States.
# Who has more followers? Type 'A' or 'B':
# Sorry, that's wrong. Final score: 0.
# You're right! Current score 1

# Randomly pick A and B from game_data.py, make sure they're not same, save
def pick_data():
    return random.choice(data)

choice = {}
keep_playing = True

def play_game(choice_list):
    score = 0
    game_over = False

    while not game_over:
        # Display A and B
        print(f"Compare A: {choice_list['a']['name']}, {choice_list['a']['description']}, from {choice_list['a']['country']}.")
        print(vs)
        print(f"Against B: {choice_list['b']['name']}, {choice_list['b']['description']}, from {choice_list['b']['country']}.")

        # Ask payer which has more followers
        def a_or_b():
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            return guess
        player_guess = a_or_b()

        # Check to make sure a or b was entered, if not enter again
        while player_guess != "a" and player_guess != "b":
            print("Input not recognized.")
            player_guess = a_or_b()

        # Compare which has more followers
        if choice_list["a"]["follower_count"] > choice_list["b"]["follower_count"]:
            correct_answer = "a"
        elif choice_list["a"]["follower_count"] < choice_list["b"]["follower_count"]:
            correct_answer = "b"
        else:
            print("Oops 'A' and 'B' seem to have the same number of followers!")
            correct_answer = player_guess

        # Check if player is right or wrong
        # If right, increase score by one
        # If wrong, end of game
        # Let player know if he/she is right or wrong
        if player_guess == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            return

        print("\n") # add a space

        # If right, take the previous correct answer, if it's B, save it as A
        if correct_answer == "b":
            choice_list["a"] = choice_list["b"]

        choice["b"] = pick_data()

        # make sure B is not the same as A
        while choice["a"] == choice["b"]:
            choice["b"] = pick_data()

while keep_playing:
    print(logo)
    choice["a"] = pick_data()
    choice["b"] = pick_data()
    # make sure B is not the same as A
    while choice["a"] == choice["b"]:
        choice["b"] = pick_data()

    # print(f"choice = {choice}") # checking
    play_game(choice)
    another_game = input("Would you like to play again? Type 'y' or 'n': ").lower()
    if another_game != "y" and another_game != "n":
        while another_game != "y" and another_game != "n":
            another_game = input("Please make sure to type 'y' or 'n': ")
    if another_game == "n":
        print("Thanks for playing!")
        keep_playing = False
    elif another_game == "y":
        print("\n" * 30)
