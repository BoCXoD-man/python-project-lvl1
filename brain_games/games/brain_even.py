"""Brain even game functions."""

import prompt
from brain_games.engine import generate_number, welcome


def generation_question():
    """Question"""
    qwest = generate_number()
    print(f'Question: {qwest}')
    return 'yes' if qwest % 2 == 0 else 'no'


def answer():
    """Answer"""
    ent = prompt.string('Your answer: ')
    return ent


def brain_even():
    """Brain_even game"""
    name = welcome()
    count = 0
    while True:
        question = generation_question()
        ent = answer()
        if question == ent:
            print('Correct!')
            count += 1
        else:
            print(f"'{ent}' is wrong answer ;(. Correct answer was '{question}"
                  f"'.\nLet's try again, {name}")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
            break
