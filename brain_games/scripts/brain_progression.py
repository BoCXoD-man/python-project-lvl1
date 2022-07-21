#!/usr/bin/env python3

"""Brain Progression game."""

from brain_games.engine import engine
from brain_games.games import brain_progression


def main():
    """Start Br.Progression game."""
    engine(brain_progression)


if __name__ == '__main__':
    main()
