# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 11 - Beginner - The Blackjack Capstone Project
# Difficulty - Hard 🤔: Use only Hints 1, 2, 3 to complete the project.

# Possible bugs/improvements:
# 1. If user has more than 11 (Ace), both will be replaced with 1 in case score is over 21?
# 2. Blackjack is a score of 21 with only 2 cards, curretly more than two cards can be "Blackjack", fixed
# 3. Code can probably be made simpler

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

keep_playing = True
cards_in_deck = len(cards)
# print(f"cards_in_deck = {cards_in_deck}") # 13

def draw_cards(number_of_cards):
    if number_of_cards == 0:
        return # terminate if no cards need to be drawn
    cards_drawn = []
    for card in range(1, number_of_cards + 1):
        random_card = random.choice(cards)
        # print(f"random_card = {random_card}") # check
        cards_drawn.append(random_card)
    return cards_drawn

# Note: sum() function could have been used instead
def compute_score(cards_list):
    score = 0
    for card in cards_list:
        score += card
    return score

def final_hand_print():
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")


while keep_playing:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == "n":
        break
    elif play_game != "n" and play_game != "y":
        print("Please make sure to enter 'y' or 'n'")
        continue
    user_cards = []
    comp_cards = []
    user_draw_cards = 2  # initially two cards are drawn
    comp_draw_cards = 2  # initially two cards are drawn
    print("\n" * 30)
    print(logo)
    while keep_playing:
        if user_draw_cards != 0:
            user_cards += draw_cards(user_draw_cards)
        # user_cards = [11, 7, 9, 10] # checking
        # print(f"user_cards = {user_cards}") # checking
        if comp_draw_cards != 0:
            comp_cards += draw_cards(comp_draw_cards)
        # print(f"comp_cards = {comp_cards}") # checking
        user_score = compute_score(user_cards)
        # print(f"user_score = {user_score}") # checking
        comp_score = compute_score(comp_cards)
        # print(f"comp_score = {comp_score}") # checking
        if comp_score == 21 and len(comp_cards) == 2:
            final_hand_print()
            print("Opponent got Blackjack! You lose 😭")
            user_cards = []
            comp_cards = []
            break
        elif user_score == 21 and len(user_cards) == 2:
            final_hand_print()
            print("Blackjack! You win 🥳")
            user_cards = []
            comp_cards = []
            break
        elif comp_score > 21:
            if 11 in comp_cards:
                comp_cards_temp = []
                for card in comp_cards:
                    if card == 11:
                        comp_cards_temp.append(1)
                    else:
                        comp_cards_temp.append(card)
                comp_cards_temp_score = compute_score(comp_cards_temp)
                # print(f"comp_cards_temp = {comp_cards_temp}")
                # print(f"comp_cards_temp_score = {comp_cards_temp_score}")
                if comp_cards_temp_score < 21:
                    comp_cards = comp_cards_temp
                    comp_score = comp_cards_temp_score
                    # print(f"user_cards = {user_cards}")
                # else:
                #     final_hand_print()
                #     print("You lose 😤")
                #     user_cards = []
                #     comp_cards = []
                #     break
            # else:
            #     final_hand_print()
            #     print("You lose 😤")
            #     user_cards = []
            #     comp_cards = []
            #     break
        elif user_score > 21:
            if 11 in user_cards:
                user_cards_temp = []
                for card in user_cards:
                    if card == 11:
                        user_cards_temp.append(1)
                    else:
                        user_cards_temp.append(card)
                user_cards_temp_score = compute_score(user_cards_temp)
                # print(f"user_cards_temp = {user_cards_temp}") # checking
                # print(f"user_cards_temp_score = {user_cards_temp_score}") # checking
                if user_cards_temp_score < 21:
                    user_cards = user_cards_temp
                    user_score = user_cards_temp_score
                    # print(f"user_cards = {user_cards}")
                else:
                    final_hand_print()
                    print("Went over, you lose 😤")
                    user_cards = []
                    comp_cards = []
                    break
            else:
                final_hand_print()
                print("Went over, you lose 😤")
                user_cards = []
                comp_cards = []
                break
        if user_draw_cards != 0:
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {comp_cards[0]}")
            user_draw_more = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_draw_more == "y":
            user_draw_cards = 1
            comp_draw_cards = 0
        elif user_draw_more == "n" and comp_score <= 16:
            user_draw_cards = 0
            comp_draw_cards = 1
        elif user_draw_more == "n" and comp_score > 16:
            if comp_score > 21:
                final_hand_print()
                print("Opponet went over, you win 🥳")
                user_cards = []
                comp_cards = []
                break
            if user_score > comp_score:
                final_hand_print()
                print("You win 🥳")
                user_cards = []
                comp_cards = []
                break
            elif user_score < comp_score:
                final_hand_print()
                print("You lose ☹️")
                user_cards = []
                comp_cards = []
                break
            elif user_score == comp_score:
                final_hand_print()
                print("It's a draw 😎")
                user_cards = []
                comp_cards = []
                break
            else:
                print("Oops! Something went wrong 😬")
                final_hand_print()
                user_cards = []
                comp_cards = []
                break