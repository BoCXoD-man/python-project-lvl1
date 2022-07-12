from brain_games.engine import generate_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    """Generate question."""
    num = generate_number()
    question = f'Question: {num}'
    answer = correct_answer(num)
    return (question, answer)


def is_prime(num):
    """Prime number or no prime"""
    counter = 3
    if num <= 3:
        return True
    if not num % 2:
        return False
    while counter <= num // 2:
        if not num % counter:
            return False
        counter += 2
    return True


def correct_answer(num):
    """Return True answer."""
    return 'yes' if is_prime(num) else 'no'

