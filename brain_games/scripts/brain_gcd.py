#!/usr/bin/env python3

"""Brain GCD game."""

from brain_games.engine import engine
from brain_games.games import brain_gcd


def main():
    """Start GCD game."""
    engine(brain_gcd)


if __name__ == '__main__':
    main()
