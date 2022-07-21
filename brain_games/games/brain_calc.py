import operator

from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def get_question_and_answer():
    """Generate question."""
    number1, number2 = randint(1, 100), randint(1, 100)
    operation = choice(list(operations.keys()))
    question = f'Question: {number1} {operation} {number2}'
    answer = str(operations[operation](number1, number2))
    return (question, answer)
