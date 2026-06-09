import random
from art import logo
print(logo)

EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

#function to check users guess against actual answer
def check_answer(user_guess,actual_answer,turns):
    """ checks answer against guess, returns the number of turns remaining"""
    if user_guess> actual_answer:
        print("Too high")
        return turns-1
    elif user_guess<actual_answer:
        print("Too low")
        return turns-1
    else:
        print(f"You got it! the answer was{actual_answer}")

#function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


#choosing a random number between 1 and 100
def game():
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer =  randint(1,100)
    print(f"psst, the correct answer is {answer}")

    turns=set_difficulty()

#let the user guess a num
    guess=0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("you've run out of guesses,you lose.")
            return
        elif guess!=answer:
            print("guess again")

game()

