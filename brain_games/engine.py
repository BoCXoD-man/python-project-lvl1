#!/usr/bin/env python
"""Game engine functions."""

import prompt
from random import randint


def welcome():
    """Print Welcome User"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


# First game
def generation_question():
    qwest = randint(0, 101)
    print(f'Question: {qwest}')
    return 'yes' if qwest % 2 == 0 else 'no'


def answer():
    ent = prompt.string('Your answer: ')
    return ent
