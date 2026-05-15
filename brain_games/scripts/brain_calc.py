import random

from brain_games.cli import (
    congratulate_player_win,
    print_correct,
    print_question,
    request_user_answer,
    welcome_and_give_name,
    wrong_answer_feedback,
)
from brain_games.integer_helper import calc

MIN_NUMBER = 1
MAX_NUMBER = 25
OPERATORS = ["+", "-", "*"]


def main():
    player_name = welcome_and_give_name()
    print("What is the result of the expression?")
    correct_attempts_to_win = 3

    while correct_attempts_to_win > 0:
        operand_1 = random.randint(1, 100)
        operand_2 = random.randint(1, 100)
        operator = OPERATORS[random.randint(0, 2)]
        expression = f"{operand_1} {operator} {operand_2}"

        print_question(expression)

        player_answer = request_user_answer()
        correct_answer = calc(operator, operand_1, operand_2)

        if player_answer == str(correct_answer):
            correct_attempts_to_win -= 1
            print_correct()
        else:
            wrong_answer_feedback(player_answer, correct_answer, player_name)
            return

    congratulate_player_win(player_name)
