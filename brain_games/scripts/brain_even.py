import random

from brain_games.cli import (
    congratulate_player_win,
    print_correct,
    print_question,
    request_user_answer,
    welcome_and_give_name,
    wrong_answer_feedback,
)
from brain_games.integer_helper import is_even

YES_ANSWER = "yes"
NO_ANSWER = "no"
MIN_NUMBER = 1
MAX_NUMBER = 100


def main():
    player_name = welcome_and_give_name()
    print(
        f'Answer "{YES_ANSWER}" if the number is even, otherwise answer "{NO_ANSWER}".'
    )
    correct_attempts_to_win = 3

    while correct_attempts_to_win > 0:
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)

        print_question(f"{random_number}")
        player_answer = request_user_answer()
        correct_answer = YES_ANSWER if is_even(random_number) else NO_ANSWER

        if player_answer == correct_answer:
            correct_attempts_to_win -= 1
            print_correct()
        else:
            wrong_answer_feedback(player_answer, correct_answer, player_name)
            return

    congratulate_player_win(player_name)
