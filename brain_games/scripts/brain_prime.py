#!/usr/bin/env python3

"""Brain Prime game."""

from brain_games.engine import start
from brain_games.games import brain_prime


def main():
    """Start Prime game."""
    start(brain_prime)


if __name__ == '__main__':
    main()
