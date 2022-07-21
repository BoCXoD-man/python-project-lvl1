from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Generate question."""
    len_progression = randint(5, 10)
    step_progression = randint(1, 10)
    list_progression = [randint(0, 90)]
    question_progression = randint(0, len_progression - 1)
    string_progression = ''
    # Create progression
    for i in range(1, len_progression):
        list_progression.append(list_progression[i - 1] + step_progression)
    # Correct answer:
    ans_pr = list_progression[question_progression]
    list_progression[question_progression] = '..'
    # Create final Question
    for i in list_progression:
        string_progression += f'{i} '
    question = f'Question: {string_progression}'
    answer = correct_answer(ans_pr)
    return (question, answer)


def correct_answer(ans_pr):
    """Return True answer."""
    return str(ans_pr)
