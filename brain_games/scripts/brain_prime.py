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
    is_prime,
)

MIN_NUMBER = 1
MAX_NUMBER = 600
YES_ANSWER = "yes"
NO_ANSWER = "no"


def main():
    player_name = welcome_and_give_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_attempts_to_win = 3

    while correct_attempts_to_win > 0:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)

        correct_answer = YES_ANSWER if is_prime(number) else NO_ANSWER
        print_question(number)

        player_answer = request_user_answer()

        if player_answer == str(correct_answer):
            correct_attempts_to_win -= 1
            print_correct()
        else:
            wrong_answer_feedback(player_answer, correct_answer, player_name)
            return

    congratulate_player_win(player_name)
