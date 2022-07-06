import operator
from random import choice

from brain_games.engine import generate_number

DESCRIPTION = 'What is the result of the expression?'

operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def generate_operation():
    """Generate random choice operations from the dictionary"""
    return choice(list(operation.keys()))


def make_question():
    """Generate question."""
    num1, num2 = generate_number(), generate_number()
    oper = generate_operation()  # oper - operation
    question = f'Question: {num1} {oper} {num2}'
    answer = correct_answer(num1, num2, oper)
    return (question, answer)


def correct_answer(num1, num2, oper):
    """Return True answer."""
    return str(operation[oper](num1, num2))
