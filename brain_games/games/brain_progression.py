from random import randint, choice

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Generate question."""
    progression_length = randint(5, 11)
    start, step = randint(1, 20), randint(1, 10)
    progression = list(range(start, progression_length * step + start, step))

    answer = choice(progression)
    question = 'Question:' + ' '.join(
        '..' if number == answer else str(number) for number in progression
    )
    return question, str(answer)
