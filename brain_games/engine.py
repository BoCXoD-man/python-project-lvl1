#!/usr/bin/env python
"""Game engine functions."""

import prompt

NUMBER_OF_ROUNDS = 3


def engine(game=None):
    """Start game."""
    print('Welcome to the Brain Games!')
    if game:
        print(game.DESCRIPTION)
    print()
    user_name = prompt.string('May I have your name? ')
    greeting = f'Hello, {user_name}!'
    print(greeting)
    if game:
        print()
        correct_answers = 0
        while correct_answers < NUMBER_OF_ROUNDS:
            question, correct_answer = game.get_question_and_answer()
            print(question)
            result, msg = check_answer(prompt.string('Your answer: '), correct_answer)
            print(msg)
            if not result:
                print(f"Let's try again, {user_name}!")
                return
            correct_answers += 1
        print(f'Congratulations, {user_name}!')


def check_answer(user_answer, correct_answer):
    """Check users answer."""
    if user_answer == correct_answer:
        msg = 'Correct!'
        return (True, msg)
    msg = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    return (False, msg.format(wrong=user_answer, correct=correct_answer))
