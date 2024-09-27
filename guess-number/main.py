import random 
from art import logo

numbers = random.randint(1,100)
# for n in range(1,100):
#     numbers.append(n)

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
computer_random = numbers
# print(f"Pss the random number is {computer_random}")


def check_number(user, comp):
    """Return right Answers if User's guess is right, IF NOT ....   """
    global user_attempts
    global is_answer
    if user == comp:
        is_answer = True
        user_attempts = 0
        return f"You got it, answer was {comp}"

    elif user > comp:
        user_attempts -= 1
        return f"Too hight\n{user_attempts} Attempt left"
    elif user < comp:
        user_attempts -= 1
        return f"Too low\n{user_attempts} Attempts left"


def guess_number(user_att):
    is_answer = False
    while user_att > 0:
        user_guess = int(input("Make a guess: "))
        print(check_number(user_guess, computer_random))
    user_att = 0
    if user_att == 0 and is_answer is False:
        print(f"You don't have any attempts\nRight answer was {computer_random} ")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    print("You have 10 attempts reining to guess number")
    user_attempts = 10
    guess_number(user_attempts)
else:
    print("You have 5 attempts reining to guess number")
    user_attempts = 5
    guess_number(user_attempts)

