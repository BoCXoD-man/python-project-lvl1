#!/usr/bin/env python3

"""Brain even game."""

from brain_games.engine import engine
from brain_games.games import brain_even


def main():
    """Start even game."""
    engine(brain_even)


if __name__ == '__main__':
    main()
