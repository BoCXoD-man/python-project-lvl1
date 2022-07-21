"""Brain even game functions."""

from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_answer():
    """Generate question."""
    number = randint(1, 100)
    question = f'Question: {number}'
    answer = correct_answer(number)
    return (question, answer)


def correct_answer(number):
    """Return True answer."""
    return 'no' if number % 2 else 'yes'
