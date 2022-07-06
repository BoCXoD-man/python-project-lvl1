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


def generate_number():
    """Generate random Number"""
    return randint(1, 101)
