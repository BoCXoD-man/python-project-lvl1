"""Game engine functions."""

import prompt

NUMBER_OF_ROUNDS = 3


def engine(game):
    """Start game."""
    print('Welcome to the Brain Games!')
    if game:
        print(game.DESCRIPTION)
    user_name = prompt.string('May I have your name? ')
    greeting = f'Hello, {user_name}!'
    print(greeting)
    if game:
        for _ in range(NUMBER_OF_ROUNDS):
            question, correct_answer = game.get_question_and_answer()
            print(question)
            users_answer = prompt.string('Your answer: ')
            if users_answer == correct_answer:
                print('Correct!')
                continue
            show_game_over(users_answer, correct_answer, user_name)
            break
        else:
            print(f'Congratulations, {user_name}!')


def show_game_over(users_answer, correct_answer, user_name):
    """Show that the user's answer is incorrect and offers to play again."""
    print(f"'{0}' is wrong answer ;(. Correct answer was '{1}'".format(
        users_answer,
        correct_answer,
        ))
    print(f"Let's try again, {user_name}!")
