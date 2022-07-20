import operator
from random import choice

from brain_games.engine import generate_number

DESCRIPTION = 'What is the result of the expression?'

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def get_question_and_answer():
    """Generate question."""
    num1, num2 = generate_number(), generate_number()
    operation = choice(list(operations.keys()))  # oper - operation
    question = f'Question: {num1} {operation} {num2}'
    answer = str(operations[operation](num1, num2))
    return (question, answer)
