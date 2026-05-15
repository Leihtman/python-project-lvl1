import random

from brain_games.cli import (
    congratulate_player_win,
    print_correct,
    print_question,
    request_user_answer,
    welcome_and_give_name,
    wrong_answer_feedback,
)
from brain_games.integer_helper import (
    make_arithmetic_progression,
    give_list_with_hided_number,
)

NUMBERS_COUNT = 10
MIN_STEP = 2
MAX_STEP = 5
MAX_FIRST_NUMBER = 100


def main():
    player_name = welcome_and_give_name()
    print("What number is missing in the progression?")
    correct_attempts_to_win = 3

    while correct_attempts_to_win > 0:
        position_to_hide = random.randint(0, NUMBERS_COUNT - 1)
        first_number = random.randint(0, MAX_FIRST_NUMBER)
        step = random.randint(MIN_STEP, MAX_STEP)

        numbers_list = make_arithmetic_progression(first_number, step, NUMBERS_COUNT)
        list_with_hided_number = give_list_with_hided_number(
            numbers_list, position_to_hide, mask_value=".."
        )
        correct_answer = numbers_list[position_to_hide]

        expression = f"{list_with_hided_number}"
        print_question(expression)

        player_answer = request_user_answer()

        if player_answer == str(correct_answer):
            correct_attempts_to_win -= 1
            print_correct()
        else:
            wrong_answer_feedback(player_answer, correct_answer, player_name)
            return

    congratulate_player_win(player_name)
