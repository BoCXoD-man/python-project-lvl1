#!/usr/bin/env python
"""Game engine functions."""

import prompt

from random import randint

NUMBER_OF_ROUNDS = 3


def generate_number(n1=1, n2=100):
    """Generate random Number"""
    return randint(n1, n2)


def start(game=None):
    """Start game."""
    print('Welcome to the Brain Games!')
    if game:
        print(game.DESCRIPTION)
    print()
    user_name = welcome_user()
    if game:
        print()
        engine(user_name, game.make_question)


def check_answer(user_answer, correct_answer):
    """Check users answer."""
    if user_answer == correct_answer:
        msg = 'Correct!'
        return (True, msg)
    msg = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    return (False, msg.format(wrong=user_answer, correct=correct_answer))


def welcome_user():
    """Ask username and print greeting."""
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'
    print(greeting)
    return user_name


def engine(user_name, game_make_question):
    """Engine of all games."""
    correct_answers = 0
    while correct_answers < NUMBER_OF_ROUNDS:
        question, correct_answer = game_make_question()
        print(question)
        result, msg = check_answer(get_user_answer(), correct_answer)
        print(msg)
        if not result:
            print(f"Let's try again, {user_name}!")
            return
        correct_answers += 1
    print(f'Congratulations, {user_name}!')



def get_user_name():
    """Get username."""
    return prompt.string('May I have your name? ')


def get_user_answer():
    """Get user answer."""
    return prompt.string('Your answer: ')