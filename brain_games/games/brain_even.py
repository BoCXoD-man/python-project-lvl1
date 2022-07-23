"""Brain even game functions."""

from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_answer():
    """Generate question."""
    number = randint(1, 100)
    question = f'Question: {number}'
    answer = 'yes' if is_even(number) else 'no'
    return (question, answer)


def is_even(number):
    """Return True answer."""
    return True if number % 2 == 0 else False
