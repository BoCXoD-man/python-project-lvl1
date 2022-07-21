from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    """Generate question."""
    number1, number2 = randint(1, 100), randint(1, 100)
    question = f'Question: {number1} {number2}'
    answer = str(gcd(number1, number2))
    return (question, answer)
