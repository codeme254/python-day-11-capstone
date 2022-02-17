# THE BLACKJACK PROJECT
# The gaol is to get as close to 21 as possible
# The goal is to add up your cards to the largest number without going over 21, if they go over 21, it is a burst and you loose immediately
# All cards from 2 to 10 count as a face value, so a 2 is a 2, a 9 is a 9 etc, however, jack, queen and king count as 10, Ace can count as 1 towards your total or 11.
# if the dealer ends up with a hand that is smaller tha 17, i.e 16 and under, then they must take another card

from random import choice, random
import os


cards = [11, 2, 3, 4, 5, 6, 7,8, 9, 10, 10, 10, 10]
def deal_card():
    return choice(cards)

#TODO: function calculate_score that takes a list of cards as input and returns the score
def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0 #blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    return sum(cards)
#TODO: Comparing two scores
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack"
    elif user_score == 0:
        return "Won with a blackjack"
    elif user_score > 21:
        return "You went over. You loose"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    #TODO: dealing the computer and the user two cards each
    print("=======================================")
    print("     PLAYING A NEW BLACKJACK GAME")
    print("=======================================")
    user_cards = []
    computer_cards = []
    is_game_over = False

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    print(user_cards, computer_cards)


    print(calculate_score(computer_cards), calculate_score(user_cards))
    while not is_game_over:
        #TODO: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        computer_score = calculate_score(computer_cards) 
        user_score = calculate_score(user_cards)
        print(f"Your cards {user_cards}, current score {user_score}")
        print(f"Computer's first card {computer_cards[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
            print("Game ended")
        else:
            deal_another = input("Type 'y' to draw another card or 'n' if you don't want:: ").lower()
            if deal_another == 'y':
                user_cards.append(deal_card())
                calculate_score(user_cards)
            else:
                is_game_over = True
                print("End game")
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    print(compare(user_score= user_score, computer_score=computer_score))
    print(f"Your final hand was {user_score} and for the computer {computer_score}")

# play_game()
play_another  = input("Do you want to play another, type 'y' for yes or 'n' for no: ")
while play_another == 'y':
    # os.system('cls')
    play_game()