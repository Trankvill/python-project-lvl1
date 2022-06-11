#!/usr/bin/env python

from brain_games.engine import launch_game

from brain_games.games import gcd


def main():
    """Starts the 'Greatest common divisor' game"""

    launch_game(gcd)


if __name__ == '__main__':
    main()
