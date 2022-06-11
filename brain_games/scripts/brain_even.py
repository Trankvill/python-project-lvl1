#!/usr/bin/env python

from brain_games.engine import launch_game
from brain_games.games import even


def main():
    """Starts the 'Even nubmer' game"""

    launch_game(even)


if __name__ == '__main__':
    main()
