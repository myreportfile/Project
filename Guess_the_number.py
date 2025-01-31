from random import randint
from art import logo
easy_level=10
hard_level=5

def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")

def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return easy_level
    else:
        return hard_level


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns=check_answer(guess, answer,turns)
        if guess ==0:
            print("You've run out of guesses, you lose .")
            return
        elif guess != answer:
            print("Guess again.")

game()















