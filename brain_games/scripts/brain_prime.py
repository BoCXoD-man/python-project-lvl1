#!/usr/bin/env python3

"""Brain Prime game."""

from brain_games.engine import engine
from brain_games.games import brain_prime


def main():
    """Start Prime game."""
    engine(brain_prime)


if __name__ == '__main__':
    main()
