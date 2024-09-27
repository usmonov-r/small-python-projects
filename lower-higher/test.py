

import random 
from art import vs, logo
from game_data import data

def get_random_account():
    """Getting  new random account everytime"""
    random_account = random.choice(data)
    print(f"GET RANDOM ACCOUNT {random_account}")
    return random_account


def format_data(account):
    """Formatting account's details 
        name-description-followers
    """
    print(f"ACCOUNT PARAMETER {account}")
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"

def check_answer(guess, follower_a, follower_b):
    """Comparing followers """


    #Return True if user's guess  is right  of return False if wrong
    if follower_a> follower_b:
        return guess == "a"
    else:
        return guess == "b"
    

def game():
    score = 0
    game_over = True
    print(logo)
    account_a = get_random_account()
    account_b = get_random_account()
    while  game_over:
        account_a= account_b
        account_b = get_random_account()

        while  account_a == account_b:
            account_b = get_random_account()
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")
        guess = input("Who has a more followers? A or B :").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_corret = check_answer(guess,a_follower_count,b_follower_count)

        if is_corret:
            score+=1
            print(f"You're right, Current Score: {score}")
        else:
            print(f"You're wrong, Final Score: {score}")
            game_over=False
    
game()