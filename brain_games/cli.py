import prompt


def welcome_user() -> None:
    welcome_and_give_name()


def welcome_and_give_name() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def print_question(question) -> None:
    print(f"Question: {question}")


def request_user_answer() -> str:
    return prompt.string("Your answer: ")


def print_correct() -> None:
    print("Correct!")


def wrong_answer_feedback(player_answer, correct_answer, player_name) -> None:
    print(
        f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    )
    print(f"Let's try again, {player_name}!")


def congratulate_player_win(player_name) -> None:
    print(f"Congratulations, {player_name}!")
