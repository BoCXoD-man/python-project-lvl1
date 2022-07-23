from random import randint, choice

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def get_question_and_answer():
    """Generate question."""
    start, step = randint(1, 20), randint(1, 10)
    progression = list(range(start, PROGRESSION_LENGTH * step + start, step))

    answer = choice(progression)
    question = 'Question:' + ' '.join(
        '..' if number == answer else str(number) for number in progression
    )
    return question, str(answer)
