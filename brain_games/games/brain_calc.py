import operator
from random import choice

from brain_games.engine import generate_number

DESCRIPTION = 'What is the result of the expression?'

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def make_question():
    """Generate question."""
    num1, num2 = generate_number(), generate_number()
    operation = choice(list(operations.keys()))  # oper - operation
    question = f'Question: {num1} {operation} {num2}'
    answer = correct_answer(num1, num2, operation)
    return (question, answer)


def correct_answer(num1, num2, oper):
    """Return True answer."""
    return str(operation[oper](num1, num2))
