""" Module Welcome User"""

import prompt


def welcome_user():
    """ Print Welcome User"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
