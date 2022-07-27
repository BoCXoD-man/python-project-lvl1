#!/usr/bin/env python3

"""Brain calc game."""

from brain_games.engine import run
from brain_games.games import brain_calc


def main():
    """Start even game."""
    run(brain_calc)


if __name__ == '__main__':
    main()
