from brain_games.engine import generate_number

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question():
    """Generate question."""
    num1, num2 = generate_number(), generate_number()
    question = f'Question: {num1} {num2}'
    answer = correct_answer(num1, num2)
    return (question, answer)


def correct_answer(num1, num2):
    """Return True answer."""
    num1, num2 = min(num1, num2), max(num1, num2)
    list_com_div = []  # list_common_divisor
    for i in range(1, num2 + 1):
        if num1 % i == 0 and num2 % i == 0:
            list_com_div.append(i)
    return max(list_com_div)
