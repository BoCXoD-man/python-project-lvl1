#!/usr/bin/env python3

"""Brain Progression game."""

from brain_games.engine import start
from brain_games.games import brain_progression


def main():
    """Start Br.Progression game."""
    start(brain_progression)


if __name__ == '__main__':
    main()
