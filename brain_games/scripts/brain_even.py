import random
from enum import Enum

import prompt


class UserValidAnswers(Enum):
    YES = "yes"
    NO = "no"


def is_even(number: int):
    return number % 2 == 0


def calculate_result(number: int):
    return UserValidAnswers.YES.value if is_even(number) else UserValidAnswers.NO.value


def main():
    player_name = prompt.string('May I have your name? ')
    print(f"Hello, {player_name}!")
    print(f"Answer \"{UserValidAnswers.YES.value}\" if the number is even, otherwise answer \"{UserValidAnswers.NO.value}\".")
    correct_attempts_to_win = 3

    while correct_attempts_to_win > 0:
        random_number = random.randint(1, 100)

        print(f"Question: {random_number}")
        player_answer = prompt.string('Your answer: ')
        correct_answer = calculate_result(random_number)

        if player_answer == correct_answer:
            correct_attempts_to_win -= 1
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            return

    print(f"Congratulations, {player_name}!")


