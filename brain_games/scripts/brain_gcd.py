import random

from brain_games.cli import (
    congratulate_player_win,
    print_correct,
    print_question,
    request_user_answer,
    welcome_and_give_name,
    wrong_answer_feedback,
)
from brain_games.integer_helper import find_greatest_common_divisor

MIN_NUMBER = 0
MAX_NUMBER = 100


def main():
    player_name = welcome_and_give_name()
    print("Find the greatest common divisor of given numbers.")
    correct_attempts_to_win = 3

    while correct_attempts_to_win > 0:
        number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        expression = f"{number_1} {number_2}"

        print_question(expression)

        player_answer = request_user_answer()
        correct_answer = find_greatest_common_divisor(number_1, number_2)

        if player_answer == str(correct_answer):
            correct_attempts_to_win -= 1
            print_correct()
        else:
            wrong_answer_feedback(player_answer, correct_answer, player_name)
            return

    congratulate_player_win(player_name)
