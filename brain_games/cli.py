"""CLI functions."""

import prompt


def welcome_user():
    """Welcome to the game."""
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May i have your name?')
    print('Hello, {0}!'.format(name_user))
    return name_user
