#!/usr/bin/env python3

"""Brain even game."""

from brain_games.engine import run
from brain_games.games import brain_even


def main():
    """Start even game."""
    run(brain_even)


if __name__ == '__main__':
    main()
