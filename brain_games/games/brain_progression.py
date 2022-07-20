from brain_games.engine import generate_number

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Generate question."""
    len_pr = generate_number(5, 10)  # Len progression
    step_pr = generate_number(1, 10)  # Step progression
    lst_pr = [generate_number(0, 90)]  # List progression
    que_pr = generate_number(0, len_pr - 1)  # Question progression
    str_pr = ''  # String progression
    # Create progression
    for i in range(1, len_pr):
        lst_pr.append(lst_pr[i - 1] + step_pr)
    # Correct answer:
    ans_pr = lst_pr[que_pr]
    lst_pr[que_pr] = '..'
    # Create final Question
    for i in lst_pr:
        str_pr += f'{i} '
    question = f'Question: {str_pr}'
    answer = correct_answer(ans_pr)
    return (question, answer)


def correct_answer(ans_pr):
    """Return True answer."""
    return str(ans_pr)
