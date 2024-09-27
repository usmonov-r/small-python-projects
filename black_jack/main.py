
from art import logo
import random

is_restart = True
while is_restart:
    print(logo)
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #all playing cards
        card  = random.choice(cards)
        return card

    user_cards = []
    computer_cards = []
    #from starting give 2 cards to them randomly
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(score): 
            """Calculate total card's sum"""
            if sum(score) == 21 and len(score) == 2:
                return 0 # if it returns 0 then socre was be '11+10'
            if 11 in score and sum(score) > 21:
                score.remove(11)
                score.append(1)
            return sum(score)

    def compare(user_score, comp_score):
        if user_score == comp_score:
            return "Draw"
        elif comp_score == 0:
            return "Lose, Opponent has a Black-Jack"
        elif user_score == 0:
            return "You Won with  a Black-Jack"
        elif user_score >21:
            return "You went over, Lose"
        elif comp_score >21:
            return "Opponent went over, You Win"
        elif user_score > comp_score:
            return "You win"
        else:
            return 'You Lose'

    game_over = False

    while not  game_over:
        user_score = calculate_score(user_cards)
        computer_score =calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computers first card: {user_cards[0]}")

        if user_score == 0 or  computer_score == 0 or user_score> 21:
            compare(user_score, computer_score)
            game_over = True 
        else:
            another_card = input("Type 'y' for another card , type 'n' to pass: ").lower()
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                game_over=True

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    reset_game = input("Do you want to restart game? 'yes/no': ").lower()
    if reset_game == "no" or reset_game == "n":
        print("GOODBYE")
        is_restart =False

