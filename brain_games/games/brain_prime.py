from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    """Generate question."""
    number = randint(1, 100)
    question = f'Question: {number}'
    answer = correct_answer(number)
    return (question, answer)


def is_prime(number):
    """Prime number or no prime"""
    counter = 3
    if number <= 3:
        return True
    if not number % 2:
        return False
    while counter <= number // 2:
        if not number % counter:
            return False
        counter += 2
    return True


def correct_answer(num):
    """Return True answer."""
    return 'yes' if is_prime(num) else 'no'
