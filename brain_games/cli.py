"""CLI functions."""

import prompt


def get_user_name():
    """Get username."""
    return prompt.string('May I have your name? ')


def get_user_answer():
    """Get user answer."""
    return prompt.string('Your answer: ')