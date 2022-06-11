#!/usr/bin/env python

from brain_games.engine import launch_game

from brain_games.games import prime


def main():
    """Starts the 'prime number' game"""

    launch_game(prime)


if __name__ == '__main__':
    main()
